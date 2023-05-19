from flask import Flask, render_template
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

myApp = Flask(__name__)

# Define path to aibo's photo folder (source) and static folder 
source_folder = os.path.join(myApp.root_path, 'output_pics')
static_folder = os.path.join(myApp.root_path, 'static')
print(os.path.abspath(source_folder))
print(os.path.abspath(static_folder))
print(myApp.root_path)

@myApp.route('/')
def home():
    return render_template('home.html') 

@myApp.route('/check_for_new_image')
def check_for_new_image():
    print(os.listdir(source_folder))
    latest_image = max(os.listdir(source_folder), key=os.path.getctime)
    return {'latest_image': latest_image}


# -------------------------------------Get blended images and display on the WebApp---------------------------------------------#
# Image handler class
class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        filename = os.path.basename(event.src_path)
        if filename.endswith('.jpg') or filename.endswith('.png'):
            source_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(static_folder, filename)
            shutil.copy(source_path, dest_path)
            time.sleep(1) # Add a delay of 1 second
            print(f'Copied {filename} to static folder')

# Define the observer and event handler
event_handler = ImageHandler()
observer = Observer()
observer.schedule(event_handler, source_folder, recursive=True)

# Start the observer when the WebApp starts
# @myApp.before_app_first_request
# def start_observer():
#     observer.start()
#     print(f'Watching {source_folder} for new image files...')

with myApp.app_context():
    observer.start()
    print(f'Watching {source_folder} for new image files...')

# Stop the observer when the WebApp stops
@myApp.teardown_appcontext
def stop_observer(exception):
    observer.stop()
    observer.join()

if __name__ == '__main__':
    myApp.run()

import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

 #from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
 #to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"
 
from_dir = "C:/Users/Ashish Antony/Downloads"
to_dir = "C:/Users/Ashish Antony/Desktop/Downloaded_Files"

dir_tree = {
   
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
 
}

# Event Handler Class

class FileMovementHandler(FileSystemEventHandler):

    #Student Activity1

    

    def on_created(self, event):
        name,extension=os.path.splitext(event.src_path)
        for key,value in dir_tree.items():
            if extension in value:
                file_name=os.path.basename(event.source_path)
                print("Downloaded " + file_name) 
                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name 
                if os.path.exists(path2):
                    print("directory_exist")
                    shutil.move(path1,path3)
                else: os.makedirs(path2)
                print("moving.."+file_name)
                shutil.move(path1,path3)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

#Student Activity2
while True:
    time.sleep(2)
    print("running...")

    
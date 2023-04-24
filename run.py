from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler

class Sort(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folger_trash):
            ext = filename.split(".")
            if len(ext) > 1 and (ext[1].lower() == 'jpg' or ext[1].lower() == 'png' or ext[1].lower() == 'svg' or ext[1].lower() == 'jpeg'):
                file = folger_trash + "/" + filename
                new_path = folger_image + "/" + filename
                os.rename(file, new_path)

            elif len(ext) > 1 and (ext[1].lower() == 'mp4' or ext[1].lower() == 'wmv'):
                file = folger_trash + "/" + filename
                new_path = folger_video + "/" + filename
                os.rename(file, new_path)

            elif len(ext) > 1 and (ext[1].lower() == 'mp3' or ext[1].lower() == 'wav'):
                file = folger_trash + "/" + filename
                new_path = folger_music + "/" + filename
                os.rename(file, new_path)

            else:
                file = folger_trash + "/" + filename
                new_path = folger_other + "/" + filename
                os.rename(file, new_path)

folger_trash = "trash"

folger_image = "sorted/image"
folger_video = "sorted/video"
folger_music = "sorted/music"
folger_other = "sorted/other"

sort = Sort()
observer = Observer()
observer.schedule(sort, folger_trash, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()




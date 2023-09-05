import os
import shutil
import time

path = input("enter the directory which you want to clean")
ctime = os.stat(path).st_ctime
days = int (input("please enter the number of days"))
seconds = time.time() - (days * 24 * 60 * 60) 
name,ext = os.path.splitext()
ext = ext[1:]

if os.path.exists(path):
    for root_folder, folders, files in os.walk(path):
        folder_path = os.path.join(root_folder, folders)
        if ctime > seconds :
            if ext == '' :
                shutil.rmtree()
            else:
                os.remove(path)
else:
    print("path not found")    

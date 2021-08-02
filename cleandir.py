import os
import shutil


EXT_AUDIO = ['.wav', '.mp3', '.raw', '.aac', '.wav', '.aif', '.cda', '.mpa', '.wpl']
EXT_VIDEO = ['.mp4', '.mia', '.m4v', '.f4vv', '.f4a', '.m4b', '.m4r', '.avi', '.wma', '.flv']
EXT_IMAGES = ['.jpeg', '.png', '.svg', '.gif', '.bmp', '.nef', '.jpg']
EXT_DOCUMENTS = ['.txt', '.pdf', '.doc', '.docx', '.odt', '.html']
EXT_PPT = ['.ppt', '.pptx', '.pps']
EXT_EXCEL = ['.xlsx', '.xls']
EXT_ZIP = ['.zip', '.rar']
EXT_INSTALL = ['.exe', '.iso', '.bin']

print('DOWNLOADS FOLDER CLEANUP')
os.chdir('C:\\Users\\ronma\\Downloads')
print('Current directory: {}' .format(os.getcwd()))

# Show you all the files in the directory
files = os.listdir()

# Create directories if they don't exist
DIRS = ['Audio', 'Video', 'Images', 'Documents', 'Installation', 'Folders', 'PowerPoint', 'Excel', 'Other', 'Zip']
if not os.path.isdir('./Audio'):
    for d in DIRS:
        os.mkdir('./{}'.format(d))

    print('Directories created successfully')

# Run main script
for f in files:
    if f != 'desktop.ini':
        name, extension = os.path.splitext(f)

        if extension in EXT_IMAGES:
            shutil.move(f, './images/{}'.format(f))
        elif extension in EXT_AUDIO:
            shutil.move(f, './audio/{}'.format(f))
        elif extension in EXT_PPT:
            shutil.move(f, './powerpoint/{}'.format(f))
        elif extension in EXT_EXCEL:
            shutil.move(f, './excel/{}'.format(f))
        elif extension in EXT_ZIP:
            shutil.move(f, './zip/{}'.format(f))
        elif extension in EXT_VIDEO:
            shutil.move(f, './video/{}'.format(f))
        elif extension in EXT_DOCUMENTS:
            shutil.move(f, './documents/{}'.format(f))
        elif extension in EXT_INSTALL:
            shutil.move(f, './Installation/{}'.format(f))
        else:
            if os.path.isdir(name):
                if name not in DIRS:
                    shutil.move(f, './folders/{}'.format(f))
            else:
                shutil.move(f, './other/{}'.format(f))

print('CLEANUP COMPLETED')


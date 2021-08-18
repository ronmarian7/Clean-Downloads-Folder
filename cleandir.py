import os
import shutil
import extantions


#def insert_file_to_destination_dir(file, downloads_dir):
#    dest_path = os.path.join(downloads_dir, file)
#    if os.path.isdir(dest_path):


print('DOWNLOADS FOLDER CLEANUP')
downloads_dir = 'C:\\Users\\ronma\\Downloads'
os.chdir(downloads_dir)
print(f'Current directory: {os.getcwd()}')

# List all the files in the downloads directory
files = os.listdir()

# Create directories if they don't exist
DIRS = ['Audio', 'Video', 'Images', 'Documents', 'Installation', 'Folders', 'PowerPoint', 'Excel', 'Other', 'Zip']
if not os.path.isdir('./Audio'):
    for d in DIRS:
        os.mkdir(f'./{d}')

    print('Directories created successfully')

# Run main script
for f in files:
    if f != 'desktop.ini':
        name, extension = os.path.splitext(f)


        if extension in extantions.EXT_IMAGES:
            shutil.move(f, f'./images/{f}')
        elif extension in extantions.EXT_AUDIO:
            shutil.move(f, f'./audio/{f}')
        elif extension in extantions.EXT_PPT:
            shutil.move(f, f'./powerpoint/{f}')
        elif extension in extantions.EXT_EXCEL:
            shutil.move(f, f'./excel/{f}')
        elif extension in extantions.EXT_ZIP:
            shutil.move(f, f'./zip/{f}')
        elif extension in extantions.EXT_VIDEO:
            shutil.move(f, f'./video/{f}')
        elif extension in extantions.EXT_DOCUMENTS:
            shutil.move(f, f'./documents/{f}')
        elif extension in extantions.EXT_INSTALL:
            shutil.move(f, f'./Installation/{f}')
        else:
            if os.path.isdir(name):
                if name not in DIRS:
                    shutil.move(f, f'./folders/{f}')
            else:
                shutil.move(f, f'./other/{f}')

print('CLEANUP COMPLETED')


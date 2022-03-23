import os
import shutil

# known file extensions with folder names
# TODO: read from a config file
known_extensions = {"doc": "Documents", "xls": "Documents", "ppt": "Documents", "pdf": "Documents", "txt": "Documents", "docx" : "Documents", "xlsx": "Documents",
                    "jpg": "Pictures", "jpeg": "Pictures", "png": "Pictures", "gif": "Pictures",
                    "mp3": "Music", "mp4": "Music", "wav": "Music", "m4a": "Music", "m4v": "Music",
                    "avi": "Videos", "mpg": "Videos", "mpeg": "Videos", "mkv": "Videos", "mov": "Videos",
                    "zip": "Archives", "rar": "Archives", "7z": "Archives", "tar": "Archives", "gz": "Archives",
                    "bz2": "Archives", "tgz": "Archives", "bak": "Backups", "old": "Backups", "tmp": "Temporary", 
                    "lnk" : "Links", "url" : "Web Links", "exe" : "Tools"}


# TODO: Check for OS and set path accordingly, right now assuming Windows
home = os.environ['USERPROFILE']

# there is a public desktop folder which will not be effected yet
desktop = os.path.join(home, 'Desktop')

# for testing use a temp directory

desktop = r"C:\test"

# Ask user for confirmation
shoud_i_ask = False

dir_to_scan = os.scandir(desktop) # python 3.5+

for entry in dir_to_scan:
    if entry.is_file():
        
        # get the file extension
        ext  = os.path.splitext(entry.name)[1].strip('.')

        # check if the extension is known if not use extension as target folder
        try:
            targetfolder = known_extensions[ext]        
        except KeyError:
            targetfolder = ext 

        # create the target folder if it does not exist
        target = os.path.join(desktop, targetfolder)
        os.makedirs(target, exist_ok=True)

        do_it = True

        
        if shoud_i_ask:
            do_it = input("Move {} to {}. Do you want to move it? (y/n)".format(entry.name, targetfolder)) == "y"
        
        if do_it:
            # move the file to the target folder
            shutil.move(os.path.join(desktop, entry.name), target)
            print("Moved {} to {}\n".format(entry.name, targetfolder))

        
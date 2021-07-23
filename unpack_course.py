import sys
import subprocess
from pathlib import Path
import time
import shutil
import os

tempdir = "temp/"

def clean_temp():
    path_to_folder = tempdir
    list_dir = os.listdir(path_to_folder)
    for filename in list_dir:
        file_path = os.path.join(path_to_folder, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

def main():
    clean_temp()
    url = input("Please copy-paste the course download link here: ")
    wget_command = f"wget {url} -P {tempdir}"
    print("Downloading Course Materials...")
    p1 = subprocess.Popen(wget_command.split(), stdout=subprocess.PIPE)
    p1.wait()

    target_zip = url.split('/')[-1]
    unzip_command = f"unzip -d {tempdir} {tempdir}{target_zip}"
    print("Unzipping Materials")
    p2 = subprocess.Popen(unzip_command.split(), stdout=subprocess.PIPE)
    time.sleep(1.5)
    target_dir = target_zip.split('.')[0]
    directory_in_str = f"{tempdir}{target_dir}"

    pathlist = list(Path(directory_in_str).rglob('*.py'))
    for path in pathlist:
         # because path is object not string
         cwd = os.getcwd()
         path_in_str = str(path)
         subpath = Path(path_in_str.split(tempdir)[1])
         newpath = Path(cwd, subpath.parent)
         if not newpath.is_dir():
             os.makedirs(newpath)
         shutil.move(path, f"{cwd}/{subpath}")

if __name__ == "__main__":
    try:
        main()
    except:
        sys.exit(1)
    finally:
        clean_temp()
    sys.exit(0)

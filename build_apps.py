import os
import sys
import shutil

def build():
    root = os.path.dirname(__file__)
    target = os.path.join(root, "dist")
    if os.path.isdir(target):
        shutil.rmtree(target)
    
    os.mkdir(target)
    apps_dir_path = os.path.join(root, "src/apps")
    apps_dirs = os.listdir(apps_dir_path)
    
    for dir in apps_dirs:
        copy_target = os.path.join(target, dir)
        shutil.copytree(os.path.abspath(os.path.join(apps_dir_path, dir)), os.path.abspath(copy_target))

def copy_requirements():
    root = os.path.dirname(__file__)
    apps_dir_path = os.path.abspath(os.path.join(root, "dist"))
    apps_dirs = os.listdir(apps_dir_path)

    file_name = "requirements.txt"
    with open(os.path.abspath(os.path.join(root, file_name)), "r") as copy_source:
        for dir in apps_dirs:
            with open(os.path.abspath(os.path.join(apps_dir_path, dir, file_name)), "a") as target_file:
                target_file.write("\n")
                target_file.writelines(copy_source)

if __name__ == "__main__":
    build()
    copy_requirements()
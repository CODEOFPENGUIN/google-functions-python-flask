import os
import sys
import shutil

before_arrow = ">>>>>>>>> "

def create_new_app():
    print("\r")
    new_file_list = ["__init__ .py", "main.py", "requirements.txt"]
    gcloud_ignore_list = [".gcloudignore\n", "# Python pycache:\n", "__pycache__/"]
    app_name = input("Enter app name: ")
    print("\r")
    print(before_arrow + "App name is : " + app_name)
    root = os.path.dirname(__file__)
    apps_dir = os.path.join(root, 'src/apps')
    target_dir = os.path.abspath(os.path.join(apps_dir, app_name))
    if os.path.exists(target_dir):
        print("!!!!!!!Already Exists!!!!!!!!!")
        print(before_arrow + "Exit")
    else:
        os.mkdir(target_dir)
        for file_name in new_file_list:
            with open(os.path.join(target_dir, file_name), 'w'):
                print(before_arrow + file_name + " created.")
        with open(os.path.join(target_dir, ".gcloudignore"), "w") as gcloudignore:
            gcloudignore.writelines(gcloud_ignore_list)
            print(before_arrow + ".gcloudignore created.")
    print("\r")

if __name__ == "__main__":
    create_new_app()
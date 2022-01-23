import os, sys

YES = "--assume-yes"
DOWNLD_LINK = "something"
FOLDER_PATH = "something"


def main():
    os.system("sudo apt-get update")
    os.system(f"sudo apt-get {YES} install git ")
    os.system(f"git clone {DOWNLD_LINK}")
    os.system(f"cd {FOLDER_PATH}")
    os.system(f"sudo apt-get {YES} install python3-pip")
    os.system("pip3 install -r requirements.txt")
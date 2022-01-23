import os, sys

YES = "--assume-yes"
DOWNLD_LINK = "https://github.com/huzmgod/CDPSp2.git"
FOLDER_PATH = "CDPSp2/bookinfo/src/productpage/"
CUSTOM_PORT = 4000

def main():
    os.system("sudo apt-get update")
    os.system(f"sudo apt-get {YES} install git ")
    os.system(f"git clone {DOWNLD_LINK}")
    os.system(f"cd {FOLDER_PATH}")
    os.system(f"sudo apt-get {YES} install python3-pip")
    os.system("pip3 install -r requirements.txt")
    os.system("export GROUP_NUMBER=46")
    os.system(f"python3 productpage_monolithic {CUSTOM_PORT}")

if __name__ == "__main__":
    main()
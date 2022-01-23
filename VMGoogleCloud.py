import os, sys

YES = "--assume-yes"
DOWNLD_LINK = "https://github.com/huzmgod/CDPSp2.git"
FOLDER_PATH = "CDPSp2/bookinfo/src/productpage"
CUSTOM_PORT = 4000

def main():
    os.system("sudo apt-get update")
    print("\n Installing git dependencies... \n")
    os.system(f"sudo apt-get {YES} install git ")
    print("\n Cloning files into virtual machine... \n")
    os.system(f"git clone {DOWNLD_LINK}")
    print("\n Installing pip... \n")
    os.system(f"sudo apt-get {YES} install python3-pip")
    print("\n Installing app requirements... \n")
    os.system(f"pip3 install -r {FOLDER_PATH}/requirements.txt")
    print("\n Creating GROUP_NUMBER as a environment variable \n")
    # TODO: Export no funciona desde aquí y no sé por qué
    os.system("export GROUP_NUMBER=46")
    print("\n Configuring firewall to allow http connections with port 4000... \n")
    os.system(f"sudo gcloud compute --project=strong-augury-338916 \
               firewall-rules create allow-http-{CUSTOM_PORT} --direction=INGRESS \
               --priority=1000 --network=default --action=ALLOW --rules=tcp:{CUSTOM_PORT} \
               --source-ranges=0.0.0.0/0 --target-tags=http-server")
    print("\n Starting the app... \n")
    os.system(f"python3 {FOLDER_PATH}/productpage_monolith.py {CUSTOM_PORT}")

if __name__ == "__main__":
    main()
import os
FOLDER_PATH = "CDPSp2/docker-compose/bookinfo/src"


def main():
    print("Building docker images...")
    print("\n Building product page image... \n")
    os.system(f"sudo docker build {FOLDER_PATH}/productpage -t g46/product-page")
    print("\n Building details image...\n ")
    os.system(f"sudo docker build {FOLDER_PATH}/details -t g46/details")
    print("\n Building ratings image ...\n ")
    os.system(f"sudo docker build {FOLDER_PATH}/ratings -t g46/ratings")
    print("\n Compiling gradle...\n ")
    os.system(f'sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')
    print("\n Building revies image...\n ")
    os.system(f"sudo docker build {FOLDER_PATH}/reviews/reviews-wlpcfg -t g46/reviews")

if __name__ == '__main__':
    main()
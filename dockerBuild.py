import os
FOLDER_PATH = "CDPSp2/docker-compose/bookinfo/src"


def main():
    print("Building docker images...")
    os.system(f"sudo docker build {FOLDER_PATH}/productpage -t g46/product-page")
    os.system(f"sudo docker build {FOLDER_PATH}/details -t g46/details")
    os.system(f"sudo docker build {FOLDER_PATH}/ratings -t g46/ratings")
    os.system(f'sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')
    os.system(f"sudo docker build {FOLDER_PATH}/reviews-wlpcfg -t g46/reviews")
    os.system(f"sudo docker build {FOLDER_PATH}/productpage -t g46/product-page")

if __name__ == '__main__':
    main()
import os


def main():
    os.chdir("k8s/")
    os.system("sudo kubectl apply -f g46-product-page-deployment.yaml,g46-reviews-deployment.yaml,g46-details-deployment.yaml,g46-ratings-deployment.yaml")
    os.system('sudo kubectl expose deployment g46-product-page --type="LoadBalancer"')

    os.system("sudo kubectl apply -f g46-reviews-service.yaml,g46-details-service.yaml,g46-ratings-service.yaml")
    
if __name__ == '__main__':
    main()
    

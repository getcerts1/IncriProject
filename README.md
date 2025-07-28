# IncriProject 🚀

Overview

IncriProject is a Flask web app that counts page visits using a Redis backend. The application is designed for cloud-native deployments, with persistent storage, configurable environment variables, and scalable containerized deployments.

![](Screen%20Recording%202025-07-27%20at%2019.55.41.gif)

Tech Stack

Backend: Flask
Database: Redis
Containerization: Docker
Orchestration: Kubernetes
CI/CD: GitHub Actions (soon)
Cloud: Azure AKS + ACR


Requirements 

Python 3.9+ \
Docker & Docker Compose \
Redis (via Docker)  
Azure Subscription




```bash
    #To test the app locally 
    docker-compose --version
    git clone git@github.com:getcerts1/IncriProject.git
    cd IncriProject/
    docker-compose up --build


# Docker Network Example

## Project Setup Instructions

### Prerequisites
- Python 3.10.12 installed
- Flask 3.0.3 installed (already added in requirements.txt)

### Step-by-Step Guide

1. **Clone the Repository**:
   ```bash
   git clone 
   cd docker-network-example

2. **Copy .env.example File to Create .env File**:
    ```bash
    cp .env.example .env

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   

5. **Run the Development Server**:
   ```bash
   python main.py

6. **Access the Application**:
   Open a browser and go to: `http://127.0.0.1:5000`


## Docker Network and Docker containers

### Prerequisites
- Docker installed

### Step-by-Step Guide

1. **Build Application Docker Image from Dockerfile**:
    ```bash
    docker build -t image-name:tag-name .    //replace your flask-app-image-name and tag name

2. **Create Docker Network**:
    ```bash
    docker network ls  // to list all the networks in docker
    docker network create flask-app-network     //create new network
   
3. **Run PostgreSQL DB Container**:
    ```bash
    docker run --rm -d \
    --name db \
    --env-file .env \
    -p 5433:5432 \
    --network flask-app-network \
    postgres:13

4. **Run pgAdmin Container**:
    ```bash
    docker run --rm -d \
    --name pgadmin \
    -e PGADMIN_DEFAULT_EMAIL=admin@admin.com \
    -e PGADMIN_DEFAULT_PASSWORD=admin \
    -p 8080:80 \
    --network flask-app-network \
    dpage/pgadmin4:latest

5. **Create Redis Container**:
    ```bash
    docker run --rm -d \
    --name redis \
    --network flask-app-network \
    redis:latest

6. **Create Flask App Container**:
    ```bash
    docker run --rm -d \
    --name flask-app \
    --env-file .env \
    -p 5000:5000 \
    --network flask-app-network \
    image-name:tag-name  //replace your flask-app-image-name and tag name

## Accessing Application:
1. Before Accessing the Application, Access pgAdmin in `http://localhost:8080`.
2. Login using the credential passed during container creation.
3. On right top, right click `Servers`, Click `Create->Server Group` and Save.
4. Right Click on recently created Server, Click `Register->Server-> Connection Tab`, Add Postgres Credentials and Connect. If Connection is successful, the docker network is working.
***Note***: For host section in Connection tab, add the db container name and other credentials passed via env files.
5. Look for mydb inside Server and add `users table` with some data.
6. Now, Access the Flask Application in `http://localhost:5000`
7. To make sure it is correctly connected with db:
Check URL: `http://localhost:5000/users`, a list of users will retun.
8. To check whether, it is correctly connected with redis cache server,
Check URL: `http://localhost:5000/cache`, it will return a message: `Cache Hit: b'Hello from Redis Cache!'`

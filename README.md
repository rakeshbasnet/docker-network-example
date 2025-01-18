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

2. **Copy .env.example file to create .env file**:
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
1. **Create Docker Network**:
    ```bash
    sudo docker ls  
   
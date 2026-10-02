# VS Code Server POC

Simple FastAPI application.

## Run without Docker

Install packages:

pip install -r requirements.txt

Run:

uvicorn app:app --host 0.0.0.0 --port 8080

Open:

http://localhost:8080

## Docker Build

docker build -t vscode-server-poc .

## Docker Run

docker run -p 8080:8080 vscode-server-poc

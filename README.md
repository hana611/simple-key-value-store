# Simple Key-Value Store

This project is a simple in-memory key-value store built with Python and Flask.  
It allows storing and retrieving key-value pairs via REST API.  
Docker is used to containerize the application.

## Endpoints
- POST /set : store a key-value pair
- GET /get/<key> : retrieve value by key
- GET /health : check server health

## Run Locally
```bash
pip install -r requirements.txt
python app.py

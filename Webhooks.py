import requests

def send_to_server(url: str, message: str):
    data = {
    "content": message
    }
    requests.post(url, json=data)

import requests

print(requests.post("http://127.0.0.1:5000/robot_status?id=1", json={"id": 1}).text)

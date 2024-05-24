import requests
from threading import Thread

def make_request():
    response = requests.post("http://127.0.0.1:5000/generate", json={"input_text": "Hello,good morning?"})
    print(response.json())

threads = []
for i in range(30):
    t = Thread(target=make_request)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

import requests

r = requests.get(url='http://127.0.0.1:5000/')
s = requests.post(url='http://127.0.0.1:5000/', data="test2")
print(s.text)

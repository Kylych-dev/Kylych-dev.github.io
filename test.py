import requests

BASE = 'http://localhost:5000/'

# response = requests.get(BASE + 'hello')


response = requests.get(f'{BASE}hello/tim/')
# response = requests.get(f'{BASE}/hello/bob/15/')
response2 = requests.post(f'{BASE}/he/post', json={'hello': 'world'})
# response2 = requests.post(f'{BASE}/hello', json={'hello': 'world'})

# response3 = requests.put(f'{BASE}/video', {'likes': 10})

# print('raw response: ', response2.text)
print(response.json())
print(response2.json())
# print(response3.json())

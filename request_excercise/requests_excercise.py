import requests

url = 'https://api.douban.com/v2/movie/top250'
req = requests.get(url)
print(req)
print(req.status_code)
data = req.json()
print(data)
print(type(data))
print(data['title'])
if req.status_code == requests.codes.ok:
    print("success")
import urllib.request
import urllib.parse

word = input('search:\n')
word = urllib.parse.quote(word)
url = 'http://www.baidu.com/s?wd=%s'%word
print(url)
req = urllib.request.urlopen(url)
data = req.read().decode('utf8')
with open('search.html','w',encoding='utf8') as f:
    f.write(data)

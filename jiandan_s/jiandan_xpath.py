import requests
from lxml import etree

url = 'http://jandan.net/duan'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Host': 'jandan.net'
    }
data_all = ''
for i in range(3):
    print(url)
    req = requests.get(url,headers=headers)
    html = req.text
    print(html)

    tree = etree.HTML(html)
    result = tree.xpath('//li//div[@class="text"]')

    for div in result:
        author = div.xpath('../div[@class="author"]/strong/text()')
        data_all += (author[0] + ':\n')
        content = div.xpath('p/text()')
        for p in content:
            data_all += p
        data_all += '\n\n'

    current_page = tree.xpath('//span[@class="current-comment-page"]/text()')
    print(current_page)
    next_page = int(current_page[0].strip('[]')) - 1

    url = 'http://jandan.net/duan/page-%d' % next_page

# print(data_all)
with open('jokes.txt', 'w', encoding='utf8') as f:
    f.write(data_all)

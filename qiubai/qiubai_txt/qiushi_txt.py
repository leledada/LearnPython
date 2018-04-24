# -*- coding: utf-8 -*-

import requests
from lxml import etree


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                  Chrome/65.0.3325.181 Safari/537.36"
}


def my_request(url):
    req = requests.get(url, headers=header)
    data = req.text
    return data


def parse_html(data):
    tree = etree.HTML(data)
    # xpath_div = tree.xpath('//div[@class="article block untagged mb15"]')
    xpath_div = tree.xpath('//div[contains(@class,"article block untagged mb15")]')
    print(xpath_div)

    data = ''
    for div in xpath_div:
        author = div.xpath('.//h2/text()')
        content = div.xpath('.//div[@class="content"]/span/text()')
        funny_count = div.xpath('.//span[@class="stats-vote"]/i/text()')
        repost_count = div.xpath('.//span[@class="stats-comments"]/a/i/text()')

        head = author[0] + '\t好笑数:' + funny_count[0] + '\t回复数:' + repost_count[0]
        content = head + '\n' + ''.join(content) + '\n'

        data += content
        print(data)

    return data


def my_save(data):
    with open('qsbk.txt', 'a+', encoding='utf-8') as f:
        f.write(data)


def main():
    url = 'https://www.qiushibaike.com/8hr/page/{}/'
    # 逐页 请求-解析-保存
    for i in range(1, 4):
        qurl = url.format(i)
        req_data = my_request(qurl)
        parse_data = parse_html(req_data)
        my_save(parse_data)
        print(qurl,'保存完毕')

if __name__ == '__main__':
    main()
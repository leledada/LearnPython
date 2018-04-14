# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import hashlib
import re
import base64
import os
import threading
import time


def _md5(value):
    '''md5加密'''
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()


def _base64_decode(data):
    '''bash64解码，要注意原字符串长度报错问题'''
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    return base64.b64decode(data)


def get_imgurl(m, r='', d=0):
    '''解密获取图片链接'''
    e = "DECODE"
    q = 4
    r = _md5(r)
    o = _md5(r[0:0 + 16])
    n = _md5(r[16:16 + 16])
    l = m[0:q]
    c = o + _md5(o + l)
    m = m[q:]
    k = _base64_decode(m)
    h = list(range(256))
    b = [ord(c[g % len(c)]) for g in range(256)]

    f = 0
    for g in range(0, 256):
        f = (f + h[g] + b[g]) % 256
        tmp = h[g]
        h[g] = h[f]
        h[f] = tmp

    t = ""
    p, f = 0, 0
    for g in range(0, len(k)):
        p = (p + 1) % 256
        f = (f + h[p]) % 256
        tmp = h[p]
        h[p] = h[f]
        h[f] = tmp
        t += chr(k[g] ^ (h[(h[p] + h[f]) % 256]))
    t = t[26:]
    return t


def get_r(js_url):
    '''获取关键字符串'''
    js = requests.get(js_url).text
    # print(js)
    _r = re.findall(r'c=[\w\d]+\(e,"(.*?)"\)', js)[0]
    # print(_r)
    return _r


def get_urls(url):
    '''获取一个页面的所有图片的链接'''
    url_list = []
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Host': 'jandan.net'
    }
    html = requests.get(url, headers=headers).text
    js_url = 'http:' + re.findall('<script src="(//cdn.jandan.net/static/min/[\w\d]+\.\d+\.js)"></script>', html)[-1]
    # print(js_url)
    _r = get_r(js_url)
    soup = BeautifulSoup(html, 'lxml')
    tags = soup.select('.img-hash')
    for tag in tags:
        img_hash = tag.text
        img_url = get_imgurl(img_hash, _r)
        # print(img_url)
        url_list.append(img_url[2:])
    return url_list


def download_pic(path, img_list):
    for i in img_list:
        pic_url = 'http://%s' % i
        # print(pic_url)
        resp = requests.get(pic_url)
        with open(path + pic_url[-36:], 'wb')as f:
            f.write(resp.content)
            print(pic_url[-36:], '下载完毕。')


def get_input_page():
    while True:
        try:
            st_num = int(input('请输入起始(非0)页码: \n'))
        except:
            pass
        if type(st_num) == int and st_num != 0:
            break

    while True:
        try:
            end_num = int(input('请输入结束页码: \n'))
        except:
            pass
        if type(end_num) == int and st_num <= end_num:
            break

    return st_num, end_num


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)
        print(path, ' 创建成功')
        return True
    else:
        print(path + ' 目录已存在')


if __name__ == '__main__':
    s_time = time.time()
    st, end = get_input_page()
    pic_list = []
    print('下载开始---请等待：')
    for pn in range(st, end + 1):
        url = 'http://jandan.net/ooxx/page-%d' % pn
        pic_list += get_urls(url)
    print(pic_list)
    my_path = "jdpics/"
    mkdir(my_path)
    download_pic(my_path, pic_list)
    # t1 = threading.Thread(target=download_pic, args=(my_path,pic_list,))
    # t2 = threading.Thread(target=download_pic, args=(my_path,pic_list,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    print('执行完毕')
    e_time = time.time()
    print('haoshi', e_time - s_time)

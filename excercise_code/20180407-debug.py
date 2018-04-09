# -*- coding: utf-8 -*-

import urllib.request

url1 = 'http://m.weather.com.cn/data3/city.xml'
content1 = urllib.request.urlopen(url1).read().decode('utf8')
provinces = content1.split(',')
result = 'city = {\n'
url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
    p_code = p.split('|')[0]
    url2 = url % p_code
    # content2 = urllib.request.urlopen(url2).read().decode('utf8')
    r = urllib.request.urlopen(url2)
    # print('r->', r)
    d = r.read()
    # print('d-->', d)
    content2 = d.decode('utf8')
    # print('content2--->', content2)
    cities = content2.split(',')
    # print('cities---->', cities)
    for c in cities:
        c_code = c.split('|')[0]
        url3 = url % c_code
        content3 = urllib.request.urlopen(url3).read().decode('utf8')
        districts = content3.split(',')
        for d in districts:
            d_pair = d.split('|')
            # print('d_pair',d_pair,len(d_pair))
            d_code = d_pair[0]
            name = d_pair[1]
            url4 = url % d_code
            content4 = urllib.request.urlopen(url4).read().decode('utf8')
            # print('content4------->', content4)
            code = content4.split('|')[1]
            line = "    '%s': '%s',\n" % (name, code)
            result += line
            print(name + ':' + code)
result += '}'
f = open('city.py', 'w', encoding='utf8')
f.write(result)
f.close()

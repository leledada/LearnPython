#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
import gzip

from city import city

cityname = input('你想查哪个城市的天气？\n')

citycode = city.get(cityname)
print(citycode)

if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    print('url:', url)
    data = requests.get(url)
    data.encoding='utf8'
    print('data---:',data)
    print(data.text)
    print(type(data.text))
    # data1 = gzip.decompress(data)
    # data1.decode('utf8')
    # print('data1---:',data1)
    # result = data['weatherinfo']

    # str_temp = ('%s\n%s ~ %s') % (result['weather'],
    #
    #                               result['temp1'],
    #
    #                               result['temp2'])

# print(str_temp)

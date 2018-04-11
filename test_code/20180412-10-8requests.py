#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

while True:
    city_name = input('您要查询那个城市的天气？')
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s' % city_name

    req = requests.get(url)
    # print(req)
    # print(req.text)
    # print(type(req.text))
    result = req.json()
    # print(result)
    # print(type(result))

    result_data = result.get('data')
    if result_data:
        print('当前温度：', result_data.get('wendu'), '℃')
        print('空气质量：', result_data.get('aqi'))
        print(result_data.get('ganmao'))
        print('5日天气预报：')
        forecast = result_data.get('forecast')
        # 预告数组里面包含字典
        for fc in forecast:
            print(fc.get('date'), '：', fc.get('type'), '，', fc.get('low'), '，', fc.get('high'))
    else:
        print('未能获取此城市的天气情况。')

    flag = input('q退出，其他任意按键继续查询')
    if flag == 'q':
        break

        # {'data': {'yesterday':
        # {'high': '高温 30℃', 'date': '10日星期二', 'type': '晴', 'low': '低温 15℃', 'fx': '南风', 'fl': '<![CDATA[<3级]]>'},
        # 'city': '慈利',
        # 'forecast':
        # [{'fengli': '<![CDATA[<3级]]>', 'high': '高温 28℃', 'date': '11日星期三', 'type': '阵雨', 'low': '低温 19℃', 'fengxiang': '东北风'},
        # {'fengli': '<![CDATA[<3级]]>', 'high': '高温 22℃', 'date': '12日星期四', 'type': '小雨', 'low': '低温 14℃', 'fengxiang': '南风'},
        # {'fengli': '<![CDATA[3-4级]]>', 'high': '高温 19℃', 'date': '13日星期五', 'type': '中雨', 'low': '低温 12℃', 'fengxiang': '北风'},
        # {'fengli': '<![CDATA[3-4级]]>', 'high': '高温 17℃', 'date': '14日星期六', 'type': '小雨', 'low': '低温 12℃', 'fengxiang': '北风'},
        # {'fengli': '<![CDATA[<3级]]>', 'high': '高温 18℃', 'date': '15日星期天', 'type': '多云', 'low': '低温 12℃', 'fengxiang': '东北风'}],
        # 'ganmao': '相对于今天将会出现大幅度降温，空气湿度较大，易发生感冒，请注意适当增加衣服。', 'wendu': '21'}, 'status': 1000, 'desc': 'OK'}

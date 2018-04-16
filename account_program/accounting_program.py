#!/usr/bin/python3
# -*- coding: utf-8 -*-

# with open('account.txt','w',encoding='utf8') as f:
#     f.write('结算日期	资产/w	负债/w	净资产/w')
#
# with open('recording.txt','w',encoding='utf8') as f:
#     f.write('交易对象	收入/w	支出/w	应收账款/w	应出账款/w	交易日期')

import datetime

today = datetime.date.today()


def input_d(prompt):
    while True:
        d = input(prompt)
        if d.isdigit():
            return d
        else:
            print('输入有误，请输入数字.')


def input_s(prompt):
    while True:
        d = input(prompt)
        if d.isalnum():
            return d
        else:
            print('输入有误，请输入数字或字母.')


def select_assets():
    day, asset, liability, net_asset = '0', '0', '0', '0'
    with open('account.txt', 'r', encoding='utf8') as f_1:
        lines = f_1.readlines()
        if len(lines) > 1:
            new_assets = lines[len(lines) - 1]
            assets_list = new_assets.split()
            day = assets_list[0]
            asset = assets_list[1]
            liability = assets_list[2]
            net_asset = assets_list[3]

    return day, asset, liability, net_asset


def show_assets():
    day, asset, liability, net_asset = select_assets()
    print('最新资产：%s 万\n最新负债：%s 万\n最新净资产：%s 万\n最后更新日期：%s\n'
          % (asset, liability, net_asset, day))


def recording():
    day, assets, liability, net_asset = select_assets()
    deal_op = input_s("交易对象：")
    income_n = input_d("收入/万：")
    expend_n = input_d("支出/万：")
    receivable_n = input_d("应收账款/万:")
    payable_n = input_d("应出账款/万：")
    assets = int(assets) + int(income_n) - int(expend_n)  # 资产=资产+收入-支出
    liability = int(liability) + int(payable_n) - int(receivable_n)  # 负债=负债+应出账款-应收账款
    net_asset = assets - liability
    records = '\n' + deal_op + '\t' + income_n + '\t' + expend_n + '\t' + receivable_n + '\t' + payable_n + '\t' + str(
        today)
    accounts = '\n' + str(today) + '\t' + str(assets) + '\t' + str(liability) + '\t' + str(net_asset)
    with open('recording.txt', 'a', encoding='utf8') as f_w:
        f_w.write(records)
    with open('account.txt', 'a', encoding='utf8') as f_w1:
        f_w1.write(accounts)
    print('记账成功！')
    show_assets()


# 最近10条交易记录
def last_ten():
    result = []
    with open('recording.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()
        lines_len = len(lines)
        # print(lines[1:lines_len])
        if 1 < lines_len < 11:
            result = lines[1:lines_len]
            print('总记录不满十条...')
        elif lines_len >= 11:
            result = lines[-10:]
        else:
            print('----查询无记录-----')
            return
    print('交易对象	收入	支出	应收账款	应出账款	交易日期')
    for i in result:
        print(i.replace('\n', ''))


def read_all_records():
    with open('recording.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()
    return lines


# 与某公司的交易往来
def deal_with_key(key):
    key_result = []
    all_records = read_all_records()
    for i in all_records:
        if i.find(key) >= 0:
            key_result.append(i)
    if len(key_result) == 0:
        print('----查询无记录----')
        return
    print('交易对象	收入	支出	应收账款	应出账款	交易日期')
    for i in key_result:
        print(i.replace('\n', ''))


def sub_select(flag):
    if flag_2 == '1':
        key = input_s("请输入公司名称：")
        deal_with_key(key)
    elif flag_2 == '2':
        last_ten()
    else:
        show_assets()


def go_or_stop():
    if input('按任意键继续，按Q结束').lower() == 'q':
        print('谢谢使用！再见')
        return False
    else:
        print('欢迎继续使用')
        return True


go_flag = True
while go_flag:
    print("1.查账；2.记账")
    flag_1 = input_d("请选择服务：")
    if flag_1 == '2':
        recording()
        go_flag = go_or_stop()
    else:
        print('1.查询与某公司的贸易往来\n2.查询最近十笔交易记录\n3.查询最新资产负债情况')
        flag_2 = input_d("请选择：")
        sub_select(flag_2)
        go_flag = go_or_stop()

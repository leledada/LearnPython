#!/usr/bin/python3
# -*- coding: utf-8 -*-

# with open('from.txt','w',encoding='utf8') as f:
#     f.write('Hello Mr.张，welcome you to 南京。\nA B C 565$% 的撒旦')
import re

str_list = []
# reg = r'[A-Za-z]+'
reg = r'[A-z]+'  # 找出所有从A-Za-z的连续字符

# 读取文件，多行
with open('from.txt', 'r', encoding='utf8') as f_r:
    lines = f_r.readlines()

# findall找出所有从A-Za-z的连续字符
for line in lines:
    str_list += (re.findall(reg, line))

# print('\n'.join(sorted(str_list)))
# 结果写入文件
with open('to.txt', 'w', encoding='utf8') as f_W:
    f_W.write('\n'.join(sorted(str_list)))

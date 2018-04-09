#!/usr/bin/python3
# -*- coding: utf-8 -*-

import chardet

import sys

print('当前环境的编码方式：', sys.getdefaultencoding())

str = "乐大"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))
try:
    print("对 UTF-8 解码 -->GBK 解码 ：", str_utf8.decode('GBK', 'strict'))
    print("对GBK 编码--->UTF-8 解码 ：", str_gbk.decode('UTF-8', 'strict'))
except Exception as e1:
    print(e1)

try:
    print('str_utf8-->', chardet.detect(str_utf8))
    print('str_gbk-->', chardet.detect(str_gbk))
    print("(b'0xc0')-->", chardet.detect(b'0xc0'))
    print(chardet.detect(str))
except Exception as e:
    print(e)

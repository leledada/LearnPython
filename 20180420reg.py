# -*- coding: utf-8 -*-
import re

aaa = 'Hi,I am Shirley Hilton. I am his wife.'
# 懒惰匹配
print(re.findall(r'I.*e', aaa))
# 贪婪匹配
print(re.findall(r'I.*?e', aaa))

# 从下面一段文本中，匹配出所有s开头，e结尾的单词。
bbb = 'site sea sue sweet see case sse ssee loses'
print(re.findall(r'\bs.*?e\b', bbb))  # . 会匹配到空格， 需要用\S
print(re.findall(r'\bs\S*?e\b', bbb))
print(re.findall(r'\bs\S*e\b', bbb))

ccc = '123aaa28029293895bbb de18012345678 12 8901223    cc 18029293895 汉子'
print(re.findall(r'\d*', ccc))  # * 任意长度包括0
print(re.findall(r'\d+', ccc))  # + 1个或更长
print(re.findall(r'[0-9]+', ccc))  # + 1个或更长
print(re.findall(r'\d{11}', ccc))
print(re.findall(r'\b1\d{10}', ccc))
print(re.findall(r'1\d{10}', ccc))
print(re.findall(r'\w+', ccc))  # \w 匹配字母或数字或下划线或汉字
print(re.findall(r'\s+', ccc))  # \s  匹配空白符
print(re.findall(r'\s*', ccc))  # \s  匹配空白符
print(re.findall(r'^\d+', ccc))  # ^  匹配字符串的开始
print(re.findall(r'.\w+$', ccc))  # $  匹配字符串的结束

# \S  其实就是\s的反义，任意不是空白符的字符。同理，还有：
# \W  匹配任意不是字母，数字，下划线，汉字的字符
# \D  匹配任意非数字的字符
# \B  匹配不是单词开头或结束的位置

# ? - 重复零次或一次
# {n,} - 重复n次或更多次
# {n,m} - 重复n到m次
print(re.findall(r'\d{2,3}', ccc))
print(re.findall(r'\d{2,}', ccc))
print(re.findall(r'[2,3]{2,3}', ccc))

ddd = '''
(021)88776543 010-55667890 02584453362 0571 66345673  (02188776543  106612345556
'''
print(re.findall('\(?0\d{2,3}[) -]?\d{7,8}',  ddd))  # 如(02188776543这样的数据也是符合条件的
print(re.findall('0\d{2,3}[ -]?\d{7,8}',  ddd))   # 分解1
print(re.findall('\(0\d{2,3}\)\d{7,8}',  ddd))    # 分解2
print(re.findall('\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}',  ddd))  # 通过 |  or合起来 ,无法判断1开头
print(re.findall('\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}|\d+',  ddd))    # 最末尾加上|\d+    √√√√√
print(re.findall('\d+|\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}',  ddd))    # 对比开头加上|\d+
print()


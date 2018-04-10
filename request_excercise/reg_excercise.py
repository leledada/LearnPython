import re

string = 'Hi there this hi'

pattern = re.compile(r'\b[Hh]i')

result = pattern.findall(string)

print(result)

string2 = '12312 dddd 中文 122 hi'
result2 = re.findall(r'\d*', string2)
print(result2)
print(re.findall(r'\d?', string2))
print(re.findall(r'\d+', string2))
print(re.findall(r'.3', string2))
print(re.findall(r'.*', string2))
print(re.findall(r'\w+', string2))
print(re.findall(r'\W+', string2))

text = "Hi, I am Shirley Hilton 123. I am his wife. 456"

# 取出 text 中所有的数字
regex = r'\d+'
m = re.findall(regex, text)
print(m)

# 取出 text 中所有的单词（不包括数字）
regex = r'[a-zA-Z]+'
n = re.findall(regex, text)
print(n)

# 匹配出所有s开头，e结尾的单词。
# \b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。

text = 'site sea sue sweet see case sse ssee loses'
regex = r'\bs\S*e\b'  # \S，它表示的是不是空白符的任意字符。注意是大写字符S。
regex1 = r"\bs.*?e\b"  # “.” 在正则表达式中表示除换行符以外的任意字符
regex2 = r"\bs.?e\b"  # 会用“?”表示任意一个字符，
regex3 = r"\bs.?.*e\b"  # “*”表示任意数量连续字符
regex4 = r'\bs+e+\b'  # 一个与*类似的符号+，表示的则是1个或更长。

print(re.findall(regex, text))
print(re.findall(regex1, text))
print(re.findall(regex2, text))
print(re.findall(regex3, text))
print(re.findall(regex4, text))

# 写一个正则表达式，能匹配出多种格式的电话号码，包括
# (021)88776543
# 010-55667890
# 02584453362
# 0571 66345673

# ?表示这个括号是可有可无的。
# 要匹配字符"("，需要用"\("
# 0\d{2,3} 区号，0xx或者0xxx
# [) -]? 在区号之后跟着的可能是")"、" "、"-"，也可能什么也没有。
# \d{7,8} 7或8位的数字 电话号码
# | 相当于or
regex5 = r'\(?0\d{2,3}[) -]?\d{7,8}'
regex6 = '\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}|\d+'
regex7 = '\d+|\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}'
# 注意\d+ 的位置；使用“|”时，匹配时，会按照从左往右的顺序，一旦匹配成功就停止验证后面的规则。
# 比如010-55667890 在regex7中会匹配成两段，而regex6则不会。
number = '''
# (021)88776543  0abc123456
# 010-55667890   111-222333
# 02584453362    (02188776543
# 0571 66345673
'''
print(re.findall(regex5, number))
print(re.findall(regex6, number))
print(re.findall(regex7, number))

import re

string = 'Hi there this hi'

pattern = re.compile(r'\b[Hh]i')

result = pattern.findall(string)

print(result)


string2 = '12312 dddd 中文 122 hi'
result2 = re.findall(r'\d*',string2)
print(result2)
print(re.findall(r'\d?',string2))
print(re.findall(r'\d+',string2))
print(re.findall(r'.3',string2))
print(re.findall(r'.*',string2))
print(re.findall(r'\w+',string2))
print(re.findall(r'\W+',string2))


text = "Hi, I am Shirley Hilton 123. I am his wife. 456"

# 取出 text 中所有的数字
regex = r'\d+'
m = re.findall(regex, text)
print(m)

# 取出 text 中所有的单词（不包括数字）
regex =r'[a-zA-Z]+'
n = re.findall(regex, text)
print(n)

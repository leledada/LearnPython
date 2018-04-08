# 单引号
b = 'best'
print(b)
# 双引号
a = "python"
print(a)
# 混用
c = 'I\'m the "best"'
print(c)
# 三引号
d = '''
i
am
the
best
'''
print(d)
e = """
i
am
god
"""
print(e)
print(d + e)
# 链接字符串和数字，用+号会报错
print("123", "abc", 20)
# 强制转换
print(str(123) + "23")
print(int("123") + 23)
print(float("123.3") + 23)
# 用+号会报错
# print("abc"+123)

print("answer is %d" % 20)
print("i am %s" % "zhanggs")
print("length is %f" % 16.6)
print("length is %.2f" % 16.6)
print("i am %s, age is %d, jj is %.2f" % ("zhanggs", 18, 16.6))
print(bool(0.0), bool(""), bool([]), bool(None), bool(123), bool("123"), bool('False'))

# 判斷空字符的寫法
t = '123'
if t:   # if bool(t)
    print("it's true")

num1 = '3.3'
num2 = 2.5
# 将 num1 转换为浮点数
num1 = float(num1)
# 再和 num2 相加后输出
print(num1 + num2)

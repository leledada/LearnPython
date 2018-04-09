# 想一下以下变量分别是什么。输出结果，看看是否符合你的判断。
# a = 'hello,world'  字符串 hello,world
# b = 1.414          浮点型 1.414
# c = (1 != 2)       布尔型 True
# d = (True and False)    布尔型 False
# e = (True or False)     布尔型 True

a = 'hello,world'
b = 1.414
c = (1 != 2)
d = (True and False)
e = (True or False)
print(a,b,c,d,e)
print("a = 'hello,world'","a-->\n",type(a))
print("b = 1.414","b-->\n",type(b))
print("c = (1 != 2)","c-->\n",type(c))
print("d = (True and False)","d-->\n",type(d))
print("e = (True or False)","e-->\n",type(e))


# 通过字符串格式化在同一行输出 a，b，c，d，e，其中浮点数要求只保留两位小数。输出示例：
# a:hello,world; b:1.41; c:True; d:False; e:True

print("a: %s; b: %.2f; c: %s; d: %s; e: %s; "%("hello,world",1.4111,str(bool(1)),str(bool(0)),"True"))
print("a: %s; b: %.2f; c: %s; d: %s; e: %s; "%(a,b,c,d,e))

# 定义一个字符串，使其输出结果如下
# 'hello world'
# \"hello world"

a = '''
\'hello world\'
\\"hello world"
'''
print(a)
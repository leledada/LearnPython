# 字典 无序，没有索引，通过key访问,键值必须唯一 ，因此，也没有序号index、切片和排序sort：
dict_b = {1: 'aa', 3.14: 'pi'}
print(dict_b)
print(dict_b.get(1))
print(dict_b.keys())
dict_a = {'a': 1, 'b': 2}
print(dict_a)

# 添加字典元素
dict_a['cc'] = 3
print(dict_a)

# 删除字典的元素
del (dict_a['a'])
print(dict_a)

print(dict_a['cc'])
# 官方文档推荐用 key in dict 的语法，因为它更短更通俗易懂。has_key是老旧遗留的api，为了支持2.2之前的代码留下的。Python3已经删除了该函数。
# print(dict_a.has_key('cc'))

# 判断key是否在字典中
print('cc' in dict_a)
# 类似列表中也有该方法
print(1 in [1, 2, 3, 4])
# for 遍历字典
for i in dict_a:
    print(i, dict_a[i])

# 元组，元素创建之后不能修改
a = ()
b = ('a',)  # 一个元素的元组，需要逗号，否则会当初普通的括号运算符
c = (1, 2, 3)
d = c[1:2]
print(a)  # ()
print(b)  # ('a',)
print(c)  # (1, 2, 3)
print(d)  # (2,)
print(' %d, and %s' % (1, 'ss'))  # 元组用于格式化
print(1 in c)
print(1 not in a)


# 元组当返回值
def size():
    w = 1024
    h = 768
    return (w, h)


width, height = size()
print(width)
print(height)

w_h = size()
print(w_h)

# 集合 (确定的无序的一组数据)
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # 并集
# {1, 2, 3, 4, 5}

print(set1 & set2)  # 交集
# {3}

print(set1 ^ set2)  # 交集在并集中的补集
# {1, 2, 4, 5}

print(set1 - set2)  # 交集在set1中的补集

print('-----------------')  # 找出十组样本中，都有的序号
data = [[1, 3, 6, 2], [1, 2, 5, 9, 10], [2, 11, 15, 10], [1, 2, 3, 4], [2, 3, 4, 5], [2, 5, 8, 9], [2, 14], [2, 13],
        [2, 12], [2, 11]]
set_1 = [set(i) for i in data]
# print(d[0])
a = set(set_1[0])
# print(a)
for i in range(len(set_1)):
    a = set_1[i] & a
print(a)

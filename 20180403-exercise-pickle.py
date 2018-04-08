#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@version: python3
@author:
@contact:
@file:
@time:
@software: PyCharm
"""
import _pickle as pickle

obj = 123, "abcdedf", ["ac", 123], {"key": "value", "key1": "value1"}
print(obj)
# 输出：(123, 'abcdedf', ['ac', 123], {'key1': 'value1', 'key': 'value'})



# 序列化到文件
with open("a.txt") as f:
    pickle.dump(obj, f)

with open('a.txt') as f:
    print(pickle.load(f))
# 输出：(123, 'abcdedf', ['ac', 123], {'key1': 'value1', 'key': 'value'})

# 序列化到内存（字符串格式保存），然后对象可以以任何方式处理如通过网络传输
obj1 = pickle.dumps(obj)
print(type(obj1))
# 输出：<type 'str'>
print(obj1)
# 输出：python专用的存储格式

obj2 = pickle.loads(obj1)
print(type(obj2))
# 输出：<type 'tuple'>
print(obj2)
# 输出：(123, 'abcdedf', ['ac', 123], {'key1': 'value1', 'key': 'value'})

# 列表
print(range(5))
# python3的range不直接产生list
# 相当于py2的 xrange，产生的是一个迭代器。这样可以节省空间
# print([]+range(5))   # TypeError: can only concatenate list (not "range") to list
print(list(range(5)))

a = [1, 2]
print(a + [x for x in range(5)])
print(a)

b = [1, "hello", 2.5, True, {1, 2, 3}]
print(b)
for i in b:
    print(i)

c = ["您好", 1, a]
print(c)
print(c[-3])

print('##########l4#########')
l4 = [1,['a',[True,[0.1,0.2]], [False],'a'],2,3]
for l in l4:
    print(l)
print(len(l4))

print('###############')
l4.remove(1)
print(l4)
l4.pop(1)
print(l4)

print('#############slice')

l5=[1,2,4,5,6,7,8,[1,2,3]]
print('l5 ',l5)
l6=l5[:]
print('l6 ',l6)
l7=l5[5:]
print('l7 ',l7)
l8=l5[1:3]
print('l8 ',l8)
l9= l5[-1:]
print('l9',l9)

lst = [365, 'everyday', 0.618, True, 2, 5]

# 取出 lst 的第二个位置至倒数第二个位置的子串
# 创建为一个新列表 lst2
lst2 = lst[1:-1]
print(lst2)

print('#############list comprehension')
arr = [1,2,3,4,5,6,[1,23]]
print('arr',arr)
arr1 = arr[:]
print('arr1',arr1)
arr2 = [i for i in arr if type(i)==int and i >3]
print('arr2',arr2)


# 执行语句 b.remove(2)，内存中的列表被删除元素 2。
# 又因为列表 a、b 指向的是同一个列表，所以，此时 a 列表也相当于被删除了元素 2.
a = [1,2,3,4]
b = a
b.remove(2)
print(a)
print(b)


a = [1,2,3,4]
b = a[:]
b.remove(2)
print(a)
print(b)

print('############sort')
l = [1,3,4,2,4,6]
l2 = sorted(l)
l3 = l.sort()
l4 = sorted(l,reverse=True)
l5 = l.sort(reverse=True)
print(l,'\n',l2,'\n',l3,'\n',l4,'\n',l5)

# sort() 该方法没有返回值，但是会对列表中的元素进行排序。 sorted()返回重新排序的列表。 sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# python3 中没有cmp方法，sorted也少了cmp参数

l = [[1, '学'], [3, '使'], [5, '快'], [2, '习'], [4, '我'], [6, '乐']]
l2 = sorted(l, key=lambda x: x[0])  # 按每项第一个元素排序
print(l)
print(l2)

#lambda表达式
func = lambda x, y: x + y
print(func(1, 2))

def func(x,y):
    return(x+y)
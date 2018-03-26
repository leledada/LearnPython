import random

num = random.randint(1, 100)  # random.randint(a, b)可以生成一个a到b间的随机整数，包括a和b。
print(num)

print(random.random())  # 生成一个0到1之间的随机浮点数，包括0但不包括1，也就是[0.0, 1.0)。

print(random.uniform(1.5, 3))  # 生成a、b之间的随机浮点数。不过与randint不同的是，a、b无需是整数，也不用考虑大小
print(random.uniform(1.5, 1.5))
print(random.uniform(3, 1.5))

# random.choice(seq)
# 从序列中随机选取一个元素。seq需要是一个序列，比如list、元组、字符串。
print(random.choice([1, 2, 3, 5, 8, 13]))  # list
print(random.choice('hello'))  # 字符串
print(random.choice(['hello', 'world']))  # 字符串组成的list
print(random.choice((1, 2, 3)))  # 元组

# random.randrange(start, stop, step)
# 生成一个从start到stop（不包括stop），间隔为step的一个随机数。start、stop、step都要为整数，且start<stop。
# 比如：
# random.randrange(1, 9, 2)
# 就是从[1, 3, 5, 7]中随机选取一个。
# start和step都可以不提供参数，默认是从0开始，间隔为1。但如果需要指定step，则必须指定start。
# random.randrange(4) #[0, 1, 2, 3]
# random.randrange(1, 4) #[1, 2, 3]
# random.randrange(start, stop, step)其实在效果上等同于
# random.choice(range(start, stop, step))

print(random.randrange(4))

print(random.randrange(1, 4, 2))

print("range(start, stop, step)")
for i in range(0, 10, 2):
    print(i)

num = 0
while (num < 5):
    random.seed(5)
    print(random.random())
    num += 1
print("----")
num = 0
random.seed(5)
while (num < 5):
    print(random.random())
    num += 1

    # seed( ) 用于指定随机数生成时所用算法开始的整数值。
    # 1.如果使用相同的seed( )值，则每次生成的随即数都相同；
    # 2.如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。
    # 3.设置的seed()值仅一次有效

import math

print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(math.degrees(1.57))
print(math.radians(90))

print(math.sin(math.radians(90)))  # sin90
print(math.sin(math.radians(30)))  # sin30

import time

print(time.time())  # epoch 1970-01-01 00:00:00 UTC。从epoch到当前的秒数（不考虑闰秒）。这个值被称为unix时间戳

starttime = time.time()
print('start:%f' % starttime)
for i in range(10):
    print(i)
endtime = time.time()
print('end:%f' % endtime)
print('total time:%f' % (endtime - starttime))

print(1)
time.sleep(3)
print(2)



age = 10
print(age)


def sayHello():
    global age  # 全局变量
    age += 1
    print("age", age)


sayHello()

print(age)

height = 10


def sayHi(height):
    height += 1  # 局部变量，不影响外部变量大小
    print(height)
    return height


sayHi(11)
print(height)
print("调用函数sayHi", sayHi(12))


def func(x):
    print("neibu", x)
    return x + 1


x = 2
print("waibu", func(x))


# def func():
#     x = x +1
#     print(x)
#
# x = 1
# func()
# UnboundLocalError: local variable 'x' referenced before assignment

def func(x):
    return x * 2


p = func(20)
print(p)


# 函数 hello 有一个参数 name
# 如果没有提供 name 参数的值，默认使用 'world'

def hello(name="world"):
    print('hello ' + name)


hello()
hello('python')

# 通过函数重写猜数字
import random


def guess(num):
    ans = int(input("猜猜是几？ "))
    flag = False
    if ans > num:
        print("big")
    elif ans < num:
        print("small")
    else:
        print("bingo")
        flag = True
    # print("guess函数执行，返回值", flag)
    return flag


def play(num=0):
    if num == 0:
        num = random.randint(1, 10)
    while not guess(num):
        pass


while True:
    choice = input("输入[s]开始游戏，[e]结束游戏")
    if choice == 's':
        play()
    elif choice == 'e':
        print("老板下次再来哟~~么么哒")
        break
    else:
        print("请输入正确的指令~~么么哒")


# 接受任意数量的参数，放在有序的 tuple（元组）对象中
def printAll(*args):
    for i in args:
        print(i)


printAll(1, 2, 3)
printAll([1, 2, 3], [1])
printAll(3, 2, 1)


def calcSum(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


# calcSum([1, 2, 3],1) #unsupported operand type(s) for +=: 'int' and 'list'

calcSum(123, 456)

calcSum()


def func(x, y=5, *a, **b):
    print(x, y, a, b)

func(1)   # 1 5 () {}
func(1, 2)
func(1, 2, 3)  # 1 2 (3,) {}
func(1, 2, 3, 4) # 1 2 (3, 4) {}
func(x=1)
func(x=1, y=1)
func(x=1, y=1, a=1)
func(x=1, y=1, a=1, b=1)
func(1, y=1)
func(1, 2, 3, 4, a=1)
func(1, 2, 3, 4, k=1, t=2, o=3)  # 1 2 (3, 4) {'t': 2, 'o': 3, 'k': 1}
func(1, 2, 3, 4, 5, s=1) #1 2 (3, 4, 5) {'s': 1}


# 在混合使用时，首先要注意函数的写法，必须遵守：
# 带有默认值的形参(arg=)须在无默认值的形参(arg)之后；
# 元组参数(*args)须在带有默认值的形参(arg=)之后；
# 字典参数(**kargs)须在元组参数(*args)之后。

# 可以省略某种类型的参数，但仍需保证此顺序规则。

# 调用时也需要遵守：
# 指定参数名称的参数要在无指定参数名称的参数之后；
# 不可以重复传递，即按顺序提供某参数之后，又指定名称传递。

# 而在函数被调用时，参数的传递过程为：
# 1.按顺序把无指定参数的实参赋值给形参；
# 2.把指定参数名称(arg=v)的实参赋值给对应的形参；
# 3.将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
# 4.将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**kargs)。
# 打印自己的英文昵称
print("zhanggs")

# 打印一个含有加减乘除的数学表达式
print(1+2-3+8/2*2)

# 使用两次 print 语句，但只显示一行

# 打小抄
# python2中输出默认是换行的，为了抑制换行，是这么做的:
# print x,
# 到了python3中，print变成一个函数，这种语法便行不通了。用2to3工具转换了下，变成这样了：
print("zhanggs", end=' ')
print("is the best！！")

# 使用一次 print 语句，但显示在两行中
print("zhanggs\nis the best！！")

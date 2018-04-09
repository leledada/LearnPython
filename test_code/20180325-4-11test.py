# 1,2,3,4 四个数字，能组成多少个互不相同且无重复数字的三位数？分别是多少？
# 要求：输出 1,2,3,4 组合出的所有无重复数字的三位数。

for i in [1,2,3,4]:
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and j!=k and i!=k):
                print(i*100+j*10+k);

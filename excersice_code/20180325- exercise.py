money = 88
# 当 money 的值大于 100 时，输出 "rich"
# 否则，输出 "poor"
if money > 100:
    print("rich")
else:
    print("poor")

num = 10
while True:
    ans = int(input('input: '))
    if ans > num:
        print(ans, ' > ', num)
    elif ans < num:
        print(ans, ' < ', num)
    else:
        print('they are same, over')
        break

# 输出 1 到 10
count = 1
while count <= 10:
    print(count)
    count += 1

count = 1
while True:
    print(count)
    count += 1
    if count > 10:
        break

for count in range(10):
    print(count+1)

nums = [23, 45, 8, 13, 50, 43, 21]
# 把 nums 里的值从前向后累加
# 当总和超过 100 时则不再继续累加
sum = 0
for n in nums:
    # 累加
    sum += n
    if sum > 100:
        # 满足条件时跳出循环
        break
print(sum)

print("99乘法表")
for i in range(1, 10):
    for j in range(9):
        print('%d x %d = %d' % (i, j+1, i * (j+1)))

print("99乘法表")
for i in range(1, 10):
    for j in range(1,10):
        print ('%d x %d = %d' % (i,j,i*j))


for i in [1,2]:
    print("dasd",i);
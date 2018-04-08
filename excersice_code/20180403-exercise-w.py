# 从data中读取成绩计算总分
results = []
with open('data.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    # print(f.readlines())
    for line in lines:
        print(line)
        data = line.split()

        sum = 0
        for score in data[1:]:
            sum += int(score)
        result = '%s \t: %d \n'%(data[0],sum)

        results.append(result)

with open('result.txt', 'a',encoding='utf8') as f_r:
    f_r.writelines(results)




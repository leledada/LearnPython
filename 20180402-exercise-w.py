# 从一个文件读，写入另一个文件
with open('data.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    print(f.readlines())
    for line in lines:
        print(line)
        with open("out_data.txt", 'a', encoding='utf8') as f_out:
            f_out.write(line)

# 异常处理
try:
    with open('data.txt', encoding='utf8') as f:
        print(f.readlines())
except:
    print('error')
else:
    print('ok')
finally:
    print('at last')

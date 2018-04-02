# 法一，在字符串引号前加 r 使 反斜杠不转义
file_address = r'd:\test\temporary\python.txt'
print(file_address)

# 法二，使用双反斜杠 \\ 对转义符转义
file_address = 'd:\\test\\temporary\\python.txt'
print(file_address)

# 法三，Windows支持斜杠符 / 分割，系统会自动转为反斜杠
file_address = 'd:/test/temporary/python.txt'
print(file_address)

multi_lines_file = open('data.txt')
# read 函数一次性读取整个文件的内容
print(multi_lines_file.read())


# readline 函数一次只读一行内容
# multi_lines_file = open('data.txt')
multi_lines_file.seek(0)   # 将文件指针（可以想象成光标）移动至文件开头
print('第1行', multi_lines_file.readline())
print('第2行', multi_lines_file.readline())
print('第3行', multi_lines_file.readline())

# readlines 函数一次读完整个文件，且每行作为一个元素存入列表中
multi_lines_file.seek(0)
print(multi_lines_file.readlines())
multi_lines_file.close()


print('###使用with open')
with open('data.txt') as f:
    print(f.read())
    f.seek(0)
    print(f.readlines())
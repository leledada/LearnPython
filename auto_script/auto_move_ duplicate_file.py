import os
import shutil

# 有重复文件的当前文件夹，按照实际情况修改
current_dir = r'E:/test'

# 在当前文件夹，创建存放重复文件的 cf 文件夹
duplicate_dir = current_dir + '/' + 'cf'

# 存放检测重复文件包含的字段，比如 20180101 - 副本.PNG 中的副本
check_words = ['(1)', '副本', '(2)']

# 创建存放重复文件的文件夹创建成功
if not os.path.exists(duplicate_dir):
    os.mkdir(duplicate_dir)
    print('存放重复文件的文件夹创建成功', duplicate_dir)


# 判断是否存在带有‘重复列表’中字样的文件
def is_exists(in_file):
    e_flag = False
    for cw in check_words:
        if cw in in_file:
            e_flag = True
    return e_flag


# 将current_dir文件夹中的 重复的的文件，移动到duplicate_dir文件夹中
for i in os.listdir(current_dir):
    if is_exists(i):
        shutil.move(current_dir + '/' + i, duplicate_dir + '/' + i)
        print('文件：', i, ' 移动到--> ', duplicate_dir)
    else:
        print('文件：', i, ' 未移动。')

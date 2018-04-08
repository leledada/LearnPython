# -*- coding: utf-8 -*-
import os


def findfile(key, inputdir='.'):
    found_list = []
    # os.walk 获取指定目录下的所有深度的文件、子目录的列表
    for rt, dir_names, file_names in os.walk(inputdir):
        print('searching', rt, '...')
        for name in file_names:
            full_name = rt + '/' + name
            if key in name:  # 如果文件名中有关键字
                found_list.append(full_name)
                # print('key in name ', found_list)
                # 查找文件内容
            with open(full_name, 'r', encoding='utf8') as f:
                for l in f.readlines():
                    if key in l:  # 如果当前行中有关键字
                        found_list.append(full_name + ' : ' + l)
    return found_list


# 输入搜索关键字和路径
keyword = input('search:')
path = input('in:')
if not path.strip():
    path = '.'

result = findfile(keyword, path)
# print('result', result)

print('========== Search result ===========\n')
for r in result:
    print(r)



# 要求：输入关键字，列出指定文件夹中的所有文件名中含有此关键字的文件，以及文件内容中含有此关键字的文件。
# 任务分解：
# 1.输入关键字
# 2.文件夹的遍历
# 3.循环文件名中是否包含关键字
# 4.读文件夹的文件内容是否包含关键字
# os.walk返回一个三元组.其中dir_names是所有文件夹名字(不包含路径),file_names是所有文件的名字(不包含路径).parent表示父目录.

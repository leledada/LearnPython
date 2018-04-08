# coding:utf-8
import os


# 在in_file文档的顶部增加call...
def write_top_line(in_file, add_text):
    # 先把in_file文件里的内容都出来放到old_txt
    f = open(in_file, 'r', encoding='utf8')
    old_txt = (f.readlines())
    f.close()
    add_all_list = list([])
    # 把要追加的内容放在list中
    add_all_list.append(add_text + '\n')
    # 把要原来的内容extend在list中
    add_all_list.extend(old_txt)
    # 写入文件
    f = open(in_file, 'w', encoding='utf8')
    for i in add_all_list:
        f.write(i)
    f.close()


my_dir = "C:\\Users\\zhanggs\\Desktop\\deployIc\\sql\\table\\sql"


def is_has_call(in_file):
    with open(in_file, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            line_lower = line.lower()
            if 'call' in line_lower:
                return True
            else:
                return False


count = 0
# 循环路径下的每个文件, 对每个文件的顶部加上一句call...
for i in (os.listdir(my_dir)):
    in_file = my_dir + '\\' + i
    if not is_has_call(in_file):
        write_top_line(in_file, "call P_DROP_TABLE('%s');" % (i.split(".")[0]))
        print(in_file, '完成了添加')
        count += 1
        # print(my_dir + '\\' + i, "call P_DROP_TABLE('%s');" % (i.split(".")[0]))
        # write_top_line(my_dir + '\\' + i, "call P_DROP_TABLE('%s');" % (i.split(".")[0]))

if count == 0:
    print("没有文件需要添加")
else:
    print('添加了%d个文件' % count)

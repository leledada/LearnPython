import os


# 如: path 路径下 将12150003_queryPage.txt 改成 88888888_queryPage.txt,
# 则调用 rename('12150003', '88888888')

def rename(old_str, new_str):
    path = r"C:\Users\zhanggs\Desktop\test"
    file_list = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in file_list:  # 遍历所有文件
        old_dir = os.path.join(path, files)  # 原来的文件路径
        if os.path.isdir(old_dir):  # 如果是文件夹则跳过
            continue
        filename = os.path.splitext(files)[0]  # 文件名
        filename_list = filename.split('_')
        sub_filename = filename_list[0]
        file_type = os.path.splitext(files)[1]  # 文件扩展名
        if sub_filename == old_str:
            sub_filename = new_str
            new_name = sub_filename + '_' + filename_list[1]
            new_dir = os.path.join(path, new_name + file_type)
            os.rename(old_dir, new_dir)  # 重命名
            print('重命名完成：', new_dir)


rename('12150003', '88888888')

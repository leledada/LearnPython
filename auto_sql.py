import os

my_dir = "C:\\Users\\"

results = []
# 遍历指定文件夹my_dir下所有的SQL脚本，拼装成plsql命令窗口识别的字符串，如：
# @C:\Users\xxx.sql;
for i in (os.listdir(my_dir)):
    results.append('@' + my_dir + '\\' + i + ";" + '\n')

# 将上面拼装的字符串，写入auto_sql.txt
with open('auto_sql.txt', 'w', encoding='utf8') as f:
    f.writelines(results)

print('done')

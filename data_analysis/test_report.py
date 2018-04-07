#!/usr/bin/python3
# -*- coding: utf-8 -*-

o_list = []  # 存放读取出来的原始list
results = []  # 存放处理后的结果
avg_result = ['0', '平均']  # 存放第一行的平均分


# 求每人的总分
def get_peer_sum(in_list):
    return sum([int(i) for i in in_list[1:]])


# 求每人的平均分
def get_peer_avg(in_list):
    return '%0.1f' % (sum([int(i) for i in in_list[1:]]) / len(in_list[1:]))


# 将小于60分的替换成‘不及格’
def replace_failed_points(in_list):
    out_list = in_list[0:2]
    for i in in_list[2:]:
        if float(i) < 60.0:
            i = '不及格'
            out_list.append(i)
        else:
            out_list.append(i)
    return out_list


# 将行列转置用来求每列的平均分
def get_column_avg(in_list):
    col_len = len(in_list[0])  # 列数
    for i_col in range(col_len - 1):  # 排除第一列姓名不用计算
        column_result = []  # 存放行列转置后的结果
        for p_result in in_list:
            column_result.append(float(p_result[i_col + 1]))
        # print(column_result,sum(column_result)/len(column_result))
        avg_result.append('%0.1f ' % (sum(column_result) / len(column_result)))
    avg_result.append('\n')


# 读取 report.txt 文件中的成绩；
with open('report.txt', 'r', encoding='utf8') as f:
    o_list = f.readlines()  # 读取所有记录

# 循环原始list，添加总分，平均分，排序
for o in o_list:
    s_list = o.split()  # 原始每人的数据list
    copy_s_list = s_list[:]  # 复制一份上述list用于append总分和平均分,避免干扰
    # print(s_list[0], s_list[1:])
    copy_s_list.append(str(get_peer_sum(s_list)))  # 总分，加到list末尾
    copy_s_list.append(str(get_peer_avg(s_list)))  # 平均分，加到list末尾
    results.append(copy_s_list)
    results = sorted(results, key=lambda x: x[11], reverse=True)

get_column_avg(results)  # 求列的平均分

# 将序号插入到每行行首
i = 1
for peer in results:
    peer.insert(0, i)
    i += 1

results_replace = []  # 存放替换完成后的list
# 替换不及格
for result in results:
    result = replace_failed_points(result)
    s_str = ' '.join([str(i) for i in result]) + '\n'
    results_replace.append(s_str)

# print('--replace-->', results_replace)

with open('report_result.txt', 'a', encoding='utf8') as f_w:
    f_w.write('名次 姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分' + '\n')
    f_w.writelines(avg_result)
    f_w.writelines(results_replace)

print('Completion of data processing ~~')






# 统计每名学生总成绩、计算平均并从高到低重新排名；
# 汇总每一科目的平均分和总平均分（见下表第一行）；
# 添加名次，替换60分以下的成绩为“不及格”；
# 将处理后的成绩另存为一个新文件。

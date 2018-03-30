#有这样一个成绩列表 score：

# score=[['张三', 89, 78, 91], ['李四', 99, 87], ['王五', 49, 55, 78]]
# 列表中的元素为嵌套着的多元列表，便于区别，我们姑且叫它子列表。每个子列表的第一项是学生的名字，后面几项是学生的语数英考试成绩，但是由于有同学因病缺考，可能考试成绩没有三项（比如李四只有两项成绩）。
# 问，如何才能在一行代码中实现：
# 1. 重新建立一个列表，用来统计完成全部三门考试的学生的成绩；
# 2. 新列表中每一项均为一个二元列表，同样，我们称作新子列表；
# 3. 新子列表中第一项仍为学生名字，第二项则为该学生的平均分；
# 4. 对新子列表按平均分从大到小排序；
# （请先行自主思考，答案在之后的教程给出）
score=[['张三', 89, 78, 91], ['李四', 99, 87], ['王五', 49, 55, 78]]
score3 = sorted([[a[0],(a[1]+a[2]+a[3])/3] for a in score if len(a)==4],key=lambda x:x[1],reverse=True)
# 根据高人指点，进一步用sum简化
score4 = sorted([[a[0],sum(a[1:])/3] for a in score if len(a)==4],key=lambda x:x[1],reverse=True)


# 以下为辅助理解推导过程
a=['张三', 89, 78, 91]
b=[]
b.append(a[0])
b.append((a[1]+a[2]+a[3])/3)
print(type(a))
print(b)

score=[['张三', 89, 78, 91], ['李四', 99, 87], ['王五', 49, 55, 78]]
score1 = [[a[0],(a[1]+a[2]+a[3])/3] for a in score if len(a)==4]
score2 = sorted(score1,key=lambda x:x[1],reverse=True)
print(score1)
print(score2)
print(score3)
print(score4)


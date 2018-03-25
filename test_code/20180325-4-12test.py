# BMI 指数（即身体质量指数，简称体质指数又称体重，英文为Body Mass Index，简称BMI），是用体重公斤数除以身高米数平方得出的数字
# BMI < 18.5 体重偏轻
# 18.5 <= BMI < 24 体重正常
#  BMI >= 24 体重偏重
# 设计一个BMI计算器吧，看看自己体重是否正常。
# 输入：身高、体重值
# 输出：BMI 指数、是否正常

# height = eval(input("pls input your height: (M)"))
height = float(input("pls input your height: (M)"))
weight = float(input("pls input your weight: (KG)"))
bmi = weight/(height**2)
# print("BMI",bmi)
# if bmi < 18.5:
#     print("体重偏轻")
# if (18.5 < bmi <24):
#     print("体重正常")
# if bmi >= 24 :
#     print("体重偏重")

print('BMI:%.2f' % bmi)
if bmi < 18.5:
    print('体重偏轻')
elif bmi > 24.5:
    print('体重偏重')
else:
    print('体重正常')

# 捕获异常
#  Flag = True
# while Flag:
#     try:
#         height = float(input('what is your height:'))
#         weight = float(input('what is your weight: '))
#         BMI = weight / (height * height)
#     except:
#         print('please enter number.')
#     else:
#         if 1:
#             if BMI < 18.5:
#                 print('you are slim.')
#
#             elif BMI > 24:
#                 print('you are over weight.')
#
#             else:
#                 print('you are OK.')
#         Flag = bool(input("谢谢使用BMI测试\n输入任意键+回车继续测试，直接回车退出"))

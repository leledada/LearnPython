# 【问题描述】
# 很多付费应用的开发者，会设计一些优惠券来吸引用户来使用新开发的应用，以达到一定的广告效应。
#
# 现在，请你帮他们设计并生成200个优惠券号码：
#
# 优惠码的字符由26个英文字符（大小写）组成
# 每个优惠码有8位


import random
import string

# l = [1,2,3]
# print(string.ascii_letters) 获取26个大小写字母
# print(l)
# random.shuffle(l)   将序列的所有元素随机排序。
# random.sample(l,2)
# print(l)

for i in range(200):
    l = list(string.ascii_letters)
    # b = ''.join(random.sample(l, 8))
    # print(b)

    random.shuffle(l)
    a = ''.join(l[:8])
    print(a)
    # c = ''
    # for j in range(8):
    #     c += ''.join(random.choice(l))
    # print(c)

# 方法四：
# 英文字母的大小写字符都有一个相对应的ASCII码，而chr()函数可以将一个数字转变成该ASCII码对应的字符，
# 而ord()函数可以得到单个字符的ASCII码。因此我们可以将这道题转化为生成随机数并将该数字转化为字符的做法。
# 先生成一个随机数，之后通过chr函数将其转化为字符
result_list = []


# 生成单张优惠券
def gen_code():
    ll = []
    for x in range(4):
        ll.append(chr(random.randint(65, 90)))
        ll.append(chr(random.randint(97, 122)))
    # print(''.join(ll))
    return ''.join(ll)


# 判断优惠券是否在结果list中
def is_in_list(s_str, l_list):
    if s_str in l_list:
        return True
    else:
        return False


# 打印优惠券
def print_code(list1):
    for i in range(len(list1)):
        print('优惠券', i + 1, '：', list1[i])


# 入口main方法
def code_main():
    while True:
        code = gen_code()
        if not is_in_list(code, result_list):
            result_list.append(code)
        if len(result_list) == 200:
            print_code(result_list)
            break

code_main()
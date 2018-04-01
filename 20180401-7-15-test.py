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
# print(l)

for i in range(200):
    l = list(string.ascii_letters)
    random.shuffle(l)
    print(''.join(l[:8]))

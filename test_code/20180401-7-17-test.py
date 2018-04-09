# 三人斗地主手牌规则：
# 一副牌54张（4种花色各13张，大小王），一人17张，留3张做底牌。
#
# 要求：
# 将一副牌随机打乱（洗牌）后分配给3位玩家（发牌），输出每个人的手牌和剩余底牌。


import random

# S表示黑桃;H表示红桃;D表示方块;C表示草花。

p_color = ['S', 'H', 'D', 'C']
p_number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
p_king = ['Red-Joker', 'Black-Joker']
p_all = []


# 生成54张扑克牌
def gen_poker():
    for i in p_color:
        for j in p_number:
            p_all.append(i + j)
    p_all.extend(p_king)
    return p_all


# 发牌并将发出的牌从列表中删除
def deal_poker(num, in_list):
    out_list = []
    x = ''
    for i in range(num):
        x = random.choice(in_list)
        out_list.append(x)
        in_list.remove(x)
    return out_list


# 生成手牌
list1 = gen_poker()

# 洗牌
random.shuffle(list1)

# 发牌
player1 = deal_poker(17, list1)
player2 = deal_poker(17, list1)
player3 = deal_poker(17, list1)
not_deal = list1

# 打印到后台
print('玩家1：', player1, '共%d张牌' % (len(player1)))
print('玩家2：', player2, '共%d张牌' % (len(player3)))
print('玩家3：', player3, '共%d张牌' % (len(player3)))
print('底牌：', not_deal, '共%d张牌' % (len(not_deal)))

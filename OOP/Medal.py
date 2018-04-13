#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Medal:
    def __init__(self, sn='China', gm=0, sm=0, bm=0):
        self.name = sn
        self.gold = gm
        self.silver = sm
        self.bronze = bm

    # def get_place(self, place):
    #     if place == 1:
    #         self.gold += 1
    #     elif place == 2:
    #         self.silver += 1
    #     elif place == 3:
    #         self.bronze += 1

    def add_gold(self, num):
        self.gold += num

    def add_silver(self, num):
        self.silver += num

    def add_bronze(self, num):
        self.bronze += num

    # 总奖牌数
    @property
    def count_medal(self):
        return self.gold + self.silver + self.bronze

    def show_medal(self):
        print("目前拥有奖牌：金牌 %d 枚，银牌 %d 枚，铜牌 %d 枚" % (self.gold_medal, self.silver_medal, self.bronze_medal))

        # 对象的字符串表示，被print时显示

    def __str__(self):
        return '%s: 金 %d, 银 %d, 铜 %d, 总 %d' % (
            self.name, self.gold, self.silver, self.bronze, self.count_medal
        )


# m1 = Medal()
# m1.add_gold(1)
# m1.add_bronze(2)
# m1.add_silver(3)
# print('拥有总奖牌数量：', m1.count_medal())
# m1.show_medal()

print(__name__)

if __name__ == '__main__':
    china = Medal('中国', 26, 18, 26)
    us = Medal('美国', 10, 10, 70)
    uk = Medal('英国', 8, 8, 8)
    print(china)
    print(us)
    print(uk)
    print(uk.bronze)
    # uk.gold(100)
    print("中国获得一个亚军：")
    china.add_silver(1)
    print(china)
    medal_list = [us, uk, china]
    # print(type(medal_list),medal_list[1])
    print("按金牌数排序：")
    order_by_gold = sorted(medal_list,key=lambda x:x.gold,reverse=True)
    for o in order_by_gold:
        print(o)
    print("按总数排序：")
    order_by_gold = sorted(medal_list, key=lambda x: x.count_medal, reverse=True)
    for o in order_by_gold:
        print(o)



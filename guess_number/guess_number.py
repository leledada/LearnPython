#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

print("___游戏开始___")
name = input("请输入您的姓名： ")
print('欢迎回来，%s，祝您玩得愉快！' % name)


def user_input():
    while True:
        try:
            user_num = int(input())
            if 0 < user_num < 100:
                return user_num
            else:
                print("请输入100以内的整数数字: ")
        except Exception:
            print("请输入100以内的整数数字: ")


# 展示结果和记录成绩
def show_and_record():
    result = ''
    lines = []
    # 从game.txt中读取成绩计算总分
    try:
        with open('game.txt', 'r', encoding='utf8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        with open('game.txt', 'w', encoding='utf8') as f_n:
            f_n.write('')
    scores = {}
    for l in lines:
        s = l.split()
        scores[s[0]] = s[1:]
    score = scores.get(name)
    if score is None:
        score = [0, 0, 0]
    # 游戏次数
    game_times = int(score[0])
    # 最小猜中轮数
    min_times = int(score[1])
    # 共猜中轮数
    total_times = int(score[2])
    if game_times == 0 or times < min_times:
        min_times = times
    total_times += times
    game_times += 1

    if game_times > 0:
        avg_times = float(total_times) / game_times
    else:
        avg_times = 0

    print('游戏记录：你猜中答案一共用了 %d 次机会\n你已经玩了 %d 次\n最好成绩是：最少 %d 轮猜出答案\n你平均%.2f轮猜出答案'
          % (times, game_times, min_times, avg_times))

    scores[name] = [str(game_times), str(min_times), str(total_times)]

    for score in scores:
        line = score + ' ' + ' '.join(scores[score]) + '\n'
        # print('--->', line)
        result += line

    with open('game.txt', 'w', encoding='utf8') as f_w:
        f_w.write(result)


def go_or_stop():
    go_flag = input('输入 go 再玩一次，否则退出游戏\n')
    if go_flag.lower() == 'go':
        print('新一轮游戏~~')
        return False
    else:
        print('ByeBye,欢迎客官下次再来~~')
        return True


num = random.randint(1, 100)
print("请输入100以内的整数数字: ")
times = 0
bingo = False
while not bingo:
    times += 1
    print('第 %d 次：' % times)
    answer = user_input()
    if answer < num:
        print("太小了")
    elif answer > num:
        print("太大了")
    else:
        print("猜对了，答案就是 %d " % num)
        show_and_record()
        bingo = go_or_stop()  # 用户选择是否继续
        times = 0  # 用户继续新游戏，计数器清零

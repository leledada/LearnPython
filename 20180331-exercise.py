# get_after 函数的输入是一个整数
# 返回值是这个数的后面 相邻的 两个数
# 提示：使用元组作为函数的返回值


def get_after(n):
    return n + 1, n + 2  # 不打括号也是返回的元组


# 调用 get_after
after = get_after(10)
print(after)

# 输出 after 的第二项值
print(after[1])

# 参考输出：
# 12


# 左中右三个方向，用字符串来表示。射门或者扑救的时候，直接输入方向;脑随机挑选方向，如果用数字表示，就用randint来随机。
# 用random的另一个方法：choice。它的作用是从一个list中随机挑选一个元素
# 循环5次，并且记录下各自得分
# from random import choice
#
# score_you = 0
# score_com = 0
# direction = ['left', 'center', 'right']
#
#
# def kick(player1, player2):
#     print('Choose one side to shoot:')
#     print('left, center, right')
#     p1 = input()
#     print(player1 + ' kicked ' + p1)
#
#     p2 = choice(direction)
#     print(player2 + ' saved ' + p2)
#
#     if p1 != p2:
#         print('Goal!')
#         return True
#     else:
#         print('Oops...')
#         return False
#
#
# for i in range(5):
#     print('==== Round %d - You Kick! ====' % (i + 1))
#     rounda = kick('you','com')
#     if rounda:
#         score_you += 1
#     roundb = kick('com','you')
#     if roundb:
#         score_com += 1
#     print('Score: %d(you) - %d(com)\n' % (score_you, score_com))
#
from random import choice

score = [0, 0]

direction = ['left', 'center', 'right']


def you_input():
    print('left, center, right')
    while True:
        you = input()
        if you in direction:
            return you
        else:
            print("err input,pls check and input again:")


def kick():
    print('==== You Kick! ====')
    print('Choose one side to shoot:')
    # print('left, center, right')
    you = you_input()
    print('You kicked ' + you)
    com = choice(direction)
    print('Computer saved ' + com)
    if you != com:
        print('Goal!')
        score[0] += 1
    else:
        print('Oops...')
    print('Score: %d(you) - %d(com)\n' % (score[0], score[1]))
    print('==== You Save! ====')
    print('Choose one side to save:')
    # print('left, center, right')
    you = you_input()
    print('You saved ' + you)
    com = choice(direction)
    print('Computer kicked ' + com)
    if you == com:
        print('Saved!')
    else:
        print('Oops...')
        score[1] += 1
    print('Score: %d(you) - %d(com)\n' % (score[0], score[1]))


for i in range(5):
    print('==== Round %d ====' % (i+1))
    kick()

while score[0] == score[1]:
    i += 1
    print('==== Round %d ====' % (i+1))
    kick()


if score[0] > score[1]:
    print('You Win!')
else:
    print('You Lose.')
import random

print("___START---GAME___")
name = input("Pls input your name ")

# 从game.txt中读取成绩计算总分
with open('game.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()

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

if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0

print('%s 你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (name, game_times, min_times, avg_times))

num = random.randint(1, 100)
print("GUESS A NUMBER(1,100):")
times = 0
bingo = False
while not bingo:
    times += 1
    answer = int(input())
    if answer < num:
        print("too SMALL")
    elif answer > num:
        print("too Big")
    else:
        print("BINGO")
        bingo = True

if game_times == 0 or times < min_times:
    min_times = times
total_times += times
game_times += 1
scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''
for score in scores:
    line = score + ' ' + ' '.join(scores[score]) + '\n'
    result += line

with open('game.txt', 'w', encoding='utf8') as f_w:
    f_w.write(result)

# 测试将dict转换成str
# name = {1: ['1', '2', '3'], 2: 'aa'}
# for n in name:
#     print(n, '||'.join((name[n])))

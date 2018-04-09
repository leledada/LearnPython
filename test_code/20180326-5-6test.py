# 程序随机一个结果，用户通过命令行输入去猜。程序会告诉你猜大了还是小了，直到猜中为止。
# 1.游戏可以反复进行，猜中了之后可以重新开始
# 2.统计用户猜了几轮，平均几次猜中
# 3.限制每轮猜的次数，判定输赢
import random

rounds = 0  # 记录游戏轮数
num = 0  # 记录猜的总次数
numPerRound = 0  # 记录每轮猜的次数，猜中后清零
bingo = 0  # 记录猜中的次数
Flag = True
while Flag:
    selected = input("请输入\n【1】开始游戏\n【0】结束游戏")
    if (str(selected) == '1'):
        rounds += 1  # 游戏轮数+1
        target = random.randint(1, 100)
        while True:
            guess = int(input("猜大小，请输入1-100的整数: "))
            num += 1  # 猜的次数+1
            numPerRound += 1
            if numPerRound > 9:
                Flag = False
                print("您一轮猜了10次还没猜中，还是算了吧。")
                break
            if guess > target:
                print("猜的数大了一点")
            elif guess < target:
                print("猜的数小了一点")
            else:
                print("BINGO！")
                bingo += 1
                numPerRound = 0
                break
                # Flag = bool(input("输入任意键+回车继续测试，直接回车退出"))
                # target = random.randint(1, 100)
                # # print("随机数已重置",target)
    elif str(selected) == '0':
        Flag = False
    if rounds > 0 and bingo > 0:  # 防止除0错误
        # 输出结果
        print("共猜了 %d 次，猜中 %d 次，平均 %.1f 次猜中\n" % (rounds, bingo, float(num) / rounds))
print("THANKS GAME OVER")

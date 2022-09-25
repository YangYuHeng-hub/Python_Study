'''
掷骰子
两个：1-6
1.玩游戏要有金币，否则不能玩
2.玩游戏赠金币一枚，充值获取金币
3.10的倍数，20枚金币
4.玩游戏消耗五枚金币
5.猜大小，猜对  鼓励两枚金币  猜错  没有奖励  超出6点为大，否则为小
6.游戏结束：1.主动退出  2.没有金币退出
7.只要退出则打印金币数，一共完了几局
'''

import random

coin = 0
charge = input("游戏开始，是否充值？y/n")
if charge == 'y':
    money = int(input("请输入您充值的金额：(10元的倍数)"))
    if money % 10 == 0:
        coin += money
        print("充值成功，您的金币数为%d,开始游戏" % coin)
        count = 0
        while True:
            coin -= 4
            count += 1
            n1 = random.randint(1, 6)
            n2 = random.randint(1, 6)
            guess = input("请您猜大小：")
            if (n1 + n2 > 6 and guess == '大') or (n1 + n2 <= 6 and guess == '小'):
                print("结果为%d+%d=%d  恭喜您猜对了！奖励两枚金币" % (n1, n2, n1 + n2))
                coin += 2
            else:
                print("结果为%d+%d=%d  很遗憾，您猜错了" % (n1, n2, n1 + n2))
            if coin < 5:
                print("您的金币数已不足，游戏结束")
                print("您的剩余金币为:%d，一共完了%d局" % (coin, count))
                break
            else:
                play = input("您现在的金币:%d,是否继续?(y/n)" % coin)
                if play == 'n':
                    print("您的剩余金币为:%d，一共完了%d局" % (coin, count))
                    break
    else:
        print("充值失败，游戏结束")
else:
    print("金币不足，无法开始游戏")

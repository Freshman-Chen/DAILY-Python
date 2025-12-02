''' 用Python设计第一个游戏'''
''' 改进：答案是随机生成 '''

import random

answer = random.randint(1,10)
count = 3
while count > 0:  
    temp = input('不妨猜一下小甲鱼现在心里想的是哪个数字：')
    guess = int(temp)
    if guess == answer:
        print("你是小甲鱼心里的蛔虫嘛？！")
        print('哼，猜中了也没有奖！')
        break
    else:
        if guess < answer:
            print('小了~')
        else:
            print('大了~')
        count = count - 1
print('游戏结束，不玩了^_^')

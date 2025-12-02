''' 随机生成10个数，求平均值 '''

import random

list1 = []
for i in range(0,10):
    list1.append(random.randint(60,100))
print('生成的十个数是：',list1)
print('平均值是：', (sum(list1))/10)
n = sum(1 for num in list1 if num > sum(list1)/10)
print('大于平均值的数有：{}个'.format(n))

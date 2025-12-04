''' 字符串str 查找 '''

x = '上海自来水来自海上'
# count(sub[, start[, end]])    #查找指定子字符串在字符串中出现的次数
                                #可以指定查找的起始位置和终止位置
print(x.count('海'))         #输出：2
print(x.count('海', 0, 5))   #输出：1   查找范围是：上海自来水


# find(sub[, start[, end]])      #(从左往右找)定位子字符串在字符串中的索引下标值
print(x.find('海'))          #输出：1   找不到对应子字符串返回 -1

# rfind(sub[, start[, end]])     #(从右往左找)定位子字符串在字符串中的索引下标值
print(x.rfind('海'))         #输出：7   找不到对应的字符串返回 -1

# index(sub[,start[, end]])      #和 find() 用法一样
print(x.index("海"))         #输出：1   找不到对应字符串抛出异常

# rindex(sub[, start[, end]])   #用法和 rfind() 一样
print(x.rindex('海'))        #输出：7   找不到抛出异常

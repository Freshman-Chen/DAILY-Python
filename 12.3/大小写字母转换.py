''' 字符串str 大小字母转换 '''
x = 'I love FishC'
#   capitalize() #返回首字母变成大写的新字符串
print(x.capitalize())   #输出：I love fishc

#   casefold()  #返回都是小写的新字符串（还可以处理其他语言）
print(x.casefold())     #输出：i love fishc

#   title()     #将字符串中，所有的单词转换成首字母大写
print(x.title())        #输出：I Love Fishc

#   swapcase()  #将原来字符串中的大小字母翻转
print(x.swapcase())     #输出：i LOVE fISHc

#   upper()     #输出都是大写的新字符串
print(x.upper())        #输出：I LOVE FISHC

#   lower()     #输出都是小写的新字符串
print(x.lower())        #输出：i love fishc

#原字符串并不会改变
print(x)                #输出：I love FishC

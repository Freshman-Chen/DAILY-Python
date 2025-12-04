''' 字符串str 左中右对齐 '''

x = '有内鬼，停止交易！'
### width(小于或等于源字符串长度,会直接输出源字符串)

# center(width, fillchar = ' ') #居中对齐，默认用空格填充
print(x.center(20))     #输出："     有内鬼，停止交易！      "

# ljust(width, fillchar = ' ')  #左对齐，默认用空格填充
print(x.ljust(20))      #输出："有内鬼，停止交易！           "

# rjust(width, fillchar = ' ')  #右对齐，默认用空格填充
print(x.rjust(20))      #输出："           有内鬼，停止交易！"

# zfill(width)   #右对齐，默认用 0 填充，并且负数也可以
print(x.zfill(20))      #输出："00000000000有内鬼，停止交易！"

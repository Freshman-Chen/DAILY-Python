''' 字符串str 替换 '''

x = '''
\tprint('I love FishC!')
    '''
# expandtabs([tabsize = 8])     #将字符串中的 Tab（\t） 转换成 空格(' ')
print(x.expandtabs(4))          #输出：    print('I love FishC!')

# replace(old, new, count = -1) #将 old 替换成 new ,count 默认为替换所有
print(x.replace('FishC', '陈雨琴'))           #输出：print('I love 陈雨琴!')

# translate(table)          #按照 表格(table) 替换相应字符串
s = "I love you!123ABC"
table = str.maketrans('ABCDEFG', '1234567') #制表：两个字符串一一对应
print(s.translate(table))   #输出：I love you!123123
 

''' 字符串str 拆分和拼接 '''

x = 'www.ilovefishc.com'

# partition(sep)    #从左往右找分割符
# rpartition(sep)   #从右往左找分割符
#           找到分割符，将字符串切割，返回一个三元组
print(x.partition('.'))     #输出：('www', '.', 'ilovefishc.com')

# split(sep = None, maxsplit = -1)      #从左往右找分割符
# rsplit(sep = None, maxsplit = -1)     #从右往左找分割符
#       根据选定的分割符来分割字符串，分割成列表
#       maxsplit 为你想要分割的次数（默认为 -1 ,会分割所有）
s = "苟日新，日日新，又日新"
print(s.split('，'))    #输出：['苟日新', '日日新', '又日新']

# splitlines(keepends = False)
#   将指定字符串按行分割，以列表形式返回
    # keepends = True/False 返回列表的字符串是否包含换行
print('苟日新\n日日新\r\n又日新\n'.splitlines())   #输出：['苟日新', '日日新', '又日新']


# join(iterable) 拼接 (比普通的字符串相加（ + ）更快)

print('.'.join(['www', 'ilovefishc', 'com']))   #输出：www.ilovefishc.com
print('.'.join(('www', 'ilovefishc', 'com')))   #列表或者元组都可以

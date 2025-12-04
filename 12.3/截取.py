''' 字符串str 截取 '''

# ‘去除空白’ 左（右）可选，或者去除全部空白
#   参数可以是具体的字符串，他会按字符查找
#   直到字符不是参数里任一字符为止 (单个字符匹配)

# strip(chars = None)    #从左往右并且从右往左
# lstrip(chars = None)   #从左往右
# rstrip(chars = None)   #从右往左

x = 'www.ilovefishc.com'
print(x.strip('wcom.'))   #输出：ilovefish
print(x.lstrip('wcom.'))  #输出：ilovefishc.com
print(x.rstrip('wcom.'))  #输出：www.ilovefish

#  删除指定的前缀/后缀   （整个字符串匹配）
# removeprefix(prefix)
# removesuffix(suffix)
print(x.removeprefix('www.'))   #输出：ilovefishc.com
print(x.removesuffix('.com'))   #输出：www.ilovefishc




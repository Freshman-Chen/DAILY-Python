'''论语：输出字数和标点符号数 '''

#方法一
s = "有朋自远方来，不亦说乎？"
a = 0
b = 0
for c in s:
    if c.isalpha():
        a += 1
    elif c in '，。！？':
        b += 1
print("字数是：",a)
print("符号数是：",b)

#方法二
# 使用列表推导式
word_count = sum(1 for c in s if c.isalpha())
punct_count = sum(1 for c in s if c in '，。？！')

print(f"字数是：{word_count}")
print(f"符号数是：{punct_count}")

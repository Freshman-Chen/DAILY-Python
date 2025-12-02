''' 将字符串中的数字转换成 * '''
#方法一
s1 = input('请输入字符串：')
char_list = list(s1)
for i in range(len(char_list)):
    if char_list[i].isnumeric():
        char_list[i] = '*'
result = ''.join(char_list)
print(result)

#方法二
s1 = input('请输入字符串：')
result = "".join('*' if char.isdigit() else char for char in s1)
print("处理结果:", result)

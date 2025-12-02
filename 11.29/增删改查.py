''' 列表的增删改查 '''

heros = ["钢铁侠", "绿巨人"]
##增
heros.append("黑寡妇")#在列表末尾添加一个元素
print(heros)#['钢铁侠', '绿巨人', '黑寡妇']

heros.extend(["蜘蛛侠", "雷神"])#在末尾添加多个元素
print(heros)#['钢铁侠', '绿巨人', '黑寡妇', '蜘蛛侠', '雷神']

heros[4:] = ["黑豹", "鹰眼"]#在后面加上元素(或者替换)
print(heros)#['钢铁侠', '绿巨人', '黑寡妇', '蜘蛛侠', '黑豹', '鹰眼']

heros.insert(0, "灭霸")#插入一个元素，在第一个元素位置插入
print(heros)#['灭霸', '钢铁侠', '绿巨人', '黑寡妇', '蜘蛛侠', '黑豹', '鹰眼']

##删
heros.remove("灭霸")#删除对应的一个元素(多个时，删前面的)(不存在会报错)
print(heros)#['钢铁侠', '绿巨人', '黑寡妇', '蜘蛛侠', '黑豹', '鹰眼']

heros.pop(5)#删除对应下标的一个元素,并将它返回
print(heros)#['钢铁侠', '绿巨人', '黑寡妇', '蜘蛛侠', '黑豹']
'''
heros.clear()#清空列表
print(heros)#[]
'''
##改
heros[2] = "鹰眼"#替换对应下标的元素
print(heros)#['钢铁侠', '绿巨人', '鹰眼', '蜘蛛侠', '黑豹']

heros[3:] = ["武松", "林冲" , "李逵"]#从下标为3的元素开始替换
print(heros)#['钢铁侠', '绿巨人', '鹰眼', '武松', '林冲', '李逵']

#排序
nums = [3, 5, 4, 8, 4, 3, 3, 1]
nums.sort()#从小到大排序
print(nums)#[1, 3, 3, 3, 4, 4, 5, 8]
'''
nums.sort(reverse = True)#从大到小排序
print(nums)#[8, 5, 4, 4, 3, 3, 3, 1]
'''
nums.reverse()#	原地反转列表中的元素（第一个与最后一个互换，第二个与倒数第二个互换，第三个与倒数第三个互换，...）
print(nums)#[8, 5, 4, 4, 3, 3, 3, 1]

##查
i = nums.count(3)#查找nums列表中 3 出现的次数
print(i)#3

i = heros.index("绿巨人")#查找"绿巨人"的下标,没有该元素则报错
print(i)#1

i = nums.index(1, 3, 8)#查找 1 从下标为3开始到第8个元素
print(i)#7

i = nums.index(4)#多个则返回出现的第一个的下标
print(i)#2

heros[heros.index("绿巨人")] = "钢铁侠"#将绿巨人替换成钢铁侠
print(heros)#['钢铁侠', '钢铁侠', '鹰眼', '武松', '林冲', '李逵']

#浅拷贝（引用，相当于地址的传递）
nums_copy1 = nums.copy()#浅拷贝
nums_copy2 = nums[:]#浅拷贝
print(nums_copy1)#[8, 5, 4, 4, 3, 3, 3, 1]
print(nums_copy2)#[8, 5, 4, 4, 3, 3, 3, 1]

import copy
nums_copy3 = copy.copy(nums)#浅拷贝
nums_copy4 = copy.deepcopy(nums)#深拷贝(只有在包含嵌套可变对象时，深拷贝和浅拷贝才有明显区别)
nums.reverse()
print(nums)#[1, 3, 3, 3, 4, 4, 5, 8]
print(nums_copy3)#[8, 5, 4, 4, 3, 3, 3, 1]
print(nums_copy4)#[8, 5, 4, 4, 3, 3, 3, 1]

# " + "
wo = ['w', 'o']
ai = ['a', 'i']
ni = ['n', 'i']
print(wo + ai + ni)#['w', 'o', 'a', 'i', 'n', 'i']
# " * "
num = [1, 2, 3]
print(num * 3)#[1, 2, 3, 1, 2, 3, 1, 2, 3]


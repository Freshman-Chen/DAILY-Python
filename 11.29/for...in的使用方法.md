# for ... in ...

### 1.循环语句

```
for 变量 in 可迭代对象:
    # 循环体
    执行语句
```

### 2.遍历各种数据类型

```python
'''遍历列表(List)'''
matrix = [1, 2, 3, 4, 5, 6]
for i in matrix:
	print(i,end = " ")
#输出：1 2 3 4 5 6

'''遍历字符串(String)'''
str1 = "Hello!"
for i in str1:
    print(i, end = " ")
#输出：H e l l o !

'''遍历元组(Tuple)'''
heros = ('钢铁侠', '蜘蛛侠', '灭霸')
for man in heros:
    print(man, end = " ")
#输出：钢铁侠 蜘蛛侠 灭霸 

'''遍历字典'''
student = {'name' : '陈占军', 'age' : 25}
# 遍历键
for key in student:
    print(key, end = " ")	#输出：name age 
# 遍历值
for value in student.values():
    print(value,end = " ")	#输出：陈占军 25 
# 遍历键值对
for key, value in student.items():
    print(f"{key}: {value}", end = " ")#输出：name: 陈占军 age: 25 
```

### 3.结合 range() 函数

```python
# 生成数字序列
for i in range(5):           # 0,1,2,3,4
    print(i)

for i in range(1, 6):        # 1,2,3,4,5
    print(i)

for i in range(0, 10, 2):    # 0,2,4,6,8
    print(i)

for i in range(5, 0, -1):    # 5,4,3,2,1
    print(i)
```

### 4.遍历嵌套结构

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
#遍历行
for row in matrix:
    print(row, end = ' ')#输出：[1, 2, 3] [4, 5, 6] [7, 8, 9] 
#遍历每个元素
for row in matrix:
    for element in row:
        print(element, end = " ")
    print()
'''
输出：
1 2 3 
4 5 6 
7 8 9 
'''
```

### 5.使用 enumerate() 获取索引

```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f" 索引 {index}: {fruit}", end = "\r")
# 输出: 索引 0: apple 索引 1: banana 索引 2: cherry

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f" 第{index}个: {fruit}", end = "\r")
# 输出：第1个: apple 第2个: banana 第3个: cherry
```

### 6.使用 zip() 遍历多个序列

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old",end = ", ")
#输出：Alice is 25 years old, Bob is 30 years old, Charlie is 35 years old, 
```

### 7.循环控制语句

```python
#break - 退出循环
for i in range(10):
    if i == 5:
        break
    print(i, end = ",")  # 输出: 0,1,2,3,4,
    
##continue - 跳过本次循环
for i in range(5):
    if i == 2:
        continue
    print(i, end = ",")  # 输出: 0,1,3,4,

###else - 循环正常结束执行
for i in range(3):
    print(i,end = ",")
else:
    print("循环完成",end = ",")#输出：0,1,2,循环完成,
```

### 8.遍历文件内容 *

```python
# 遍历文件的每一行
with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

### 9.遍历自定义对象 *

```python
# 只要对象是可迭代的，就可以用 for...in
class MyRange:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return iter(range(self.n))

for i in MyRange(3):
    print(i)  # 输出: 0,1,2
```

## 重要特点总结

1. **自动迭代**：不需要手动管理索引
2. **适用于任何可迭代对象**
3. **简洁易读**
4. **支持嵌套和复杂逻辑**
5. **可与其他函数配合使用**（enumerate, zip等）

# ...for...in...

### 1.列表推导式 (List Comprehension)

```python
# 基本格式
[表达式 for 变量 in 可迭代对象]

# 示例
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# 带条件过滤
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

### 2.生成器表达式 (Generator Expression)

```python
# 基本格式 - 使用圆括号
(表达式 for 变量 in 可迭代对象)

# 示例 - 惰性计算，节省内存
squares_gen = (x**2 for x in range(5))
print(list(squares_gen))  # [0, 1, 4, 9, 16]

# 直接用在函数中
total = sum(x**2 for x in range(5))
print(total)  # 30
```

### 3.集合推导式 (Set Comprehension)

```python
# 基本格式 - 使用花括号
{表达式 for 变量 in 可迭代对象}

# 示例 - 自动去重
unique_squares = {x**2 for x in [1, 2, 2, 3, 3, 3]}
print(unique_squares)  # {1, 4, 9}
```

### 4. 字典推导式 (Dictionary Comprehension)

```python
# 基本格式
{键: 值 for 变量 in 可迭代对象}

# 示例
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 键值对转换
fruits = ['apple', 'banana', 'cherry']
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths)  # {'apple': 5, 'banana': 6, 'cherry': 6}
```

### 5.嵌套的 `...for...in...`

```python
# 多重循环
matrix = [[1, 2], [3, 4], [5, 6]]

# 展平二维列表
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6]

# 创建坐标对
coordinates = [(x, y) for x in range(3) for y in range(2)]
print(coordinates)  # [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1)]
```

### 6.带条件的复杂推导式

```python
numbers = range(10)

# 多个条件
result = [x for x in numbers if x % 2 == 0 if x > 5]
print(result)  # [6, 8]

# 条件表达式（三元运算）
labels = ['偶数' if x % 2 == 0 else '奇数' for x in range(5)]
print(labels)  # ['偶数', '奇数', '偶数', '奇数', '偶数']
```

### 7.在函数参数中使用

```python
# 直接作为函数参数
numbers = [1, 2, 3, 4, 5]

# 求平方和
total = sum(x**2 for x in numbers)
print(total)  # 55

# 找最大值
max_even = max(x for x in numbers if x % 2 == 0)
print(max_even)  # 4
```

### 8. 与 if-else 结合

```python
numbers = [1, 2, 3, 4, 5]

# 使用三元表达式
result = [x if x % 2 == 0 else -x for x in numbers]
print(result)  # [-1, 2, -3, 4, -5]

# 复杂条件
grades = [85, 92, 78, 60, 45]
passed = ["及格" if score >= 60 else "不及格" for score in grades]
print(passed)  # ['及格', '及格', '及格', '及格', '不及格']
```

### 9. 性能对比

```python
import time

# 传统 for 循环
start = time.time()
result1 = []
for i in range(1000000):
    if i % 2 == 0:
        result1.append(i**2)
time1 = time.time() - start

# 列表推导式
start = time.time()
result2 = [i**2 for i in range(1000000) if i % 2 == 0]
time2 = time.time() - start

print(f"传统循环: {time1:.4f}秒")
print(f"列表推导式: {time2:.4f}秒")
# 通常列表推导式更快！
```

## 总结 `...for...in...` 的特点：

1. **简洁性**：一行代码完成多行循环的功能
2. **可读性**：逻辑清晰，意图明确
3. **性能**：通常比传统循环执行更快
4. **灵活性**：支持条件过滤、嵌套循环、复杂表达式
5. **多样性**：可用于列表、集合、字典、生成器

**语法模式：**

```
[表达式 for 变量 in 可迭代对象]                    # 列表推导式
{表达式 for 变量 in 可迭代对象}                    # 集合推导式  
{键: 值 for 变量 in 可迭代对象}                   # 字典推导式
(表达式 for 变量 in 可迭代对象)                    # 生成器表达式
```


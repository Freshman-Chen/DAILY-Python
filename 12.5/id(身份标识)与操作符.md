# id		身份标识

​	变量创建之后有3个基本属性：类型（**type**）身份标识（**id**）值（**value**）.

***

​	**id**可以理解为这个对象占用的内存地址，id(object)函数可以返回对象object的身份标识，也就是系统为这个对象分配的内存的首地址，用一个整数表示。

​	对象创建后，其身份标识**id**绝对不会变改变。

```python
x = 'FishC'
y = 'FishC'
id(x)	#输出：3295540979120
id(y)	#输出：3295540979120
#x和y是'FishC'的两种标签，id最终是指'FishC'的身份标识
```

***

### **is** 与 **is not**

***

操作符可以比较两个对象的身份标识（**id**值）是否相同，返回 **True** / **False**

```python
x = 'FishC'
y = 'FishC'
print(x is y)		#输出：True
print(x is not y)	#输出：False
```

***

### in 和 not in

***

判断**序列**是否存在**包含**关系，返回 **True** / **False**

```python
x = '小满'
y = '姬小满'
print(x in y)		#输出：True
print(x not in y)	#输出：False
```

***

### del语句

a.删除一个或多个指定的对象

b.删除可变序列中的指定元素

***

```python
x = [1,2,3,4,5,6,7]
del x[1:4]
print(x)		#输出：[1, 5, 6, 7]
del x[:]
print(x)		#输出：[]
del x
print(x)		#输出：报错，x未定义

#切片也能实现
y = [1,2,3,4,5,6,7]
y[1:4] = []		#将切片区域变成空
print(y)		#输出：[1, 5, 6, 7]
```
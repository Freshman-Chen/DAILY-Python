''' 嵌套列表（矩阵） '''
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix)#输出：[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#循环索引
for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()
'''
1 2 3 
4 5 6 
7 8 9
'''
print(matrix[0])#索引第一行
print(matrix[2][2])#输出：9

##初始化一个矩阵

#1.使用循环嵌套创建
A = [0] * 3
for i in range(3):
    A[i] = [0] * 3
print(A)
#输出：[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#2.使用列表推导式
S = [[0] * 3 for i in range(3)]
print(S)
#输出：[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

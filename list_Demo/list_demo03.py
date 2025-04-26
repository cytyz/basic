# 创建嵌套列表
s = [1, 2, 3]
t = [4, 5, 6]
print(s+t)
# [1, 2, 3, 4, 5, 6]
print(s*2)
# [1, 2, 3, 1, 2, 3]

# 嵌套列表， 多维列表
# 二维列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# 遍历数组
for i in matrix:
    print(i)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
for i in matrix:
    for j in i:
        print(j, end=" ")
# 1 2 3 4 5 6 7 8 9
print()
print(matrix[0])
# [1, 2, 3]
print(matrix[0][0])
# 1

# 创建只有0的二维列表
A = [0] * 3
print(A)
# [0, 0, 0]
for i in range(3):
    A[i] = [0] * 3
print(A)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(A[0] is A[1], A[1] is A[2])
# False False

# 错误的二维列表创建方式
B = [[0] * 3] * 3
print(B)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(B[0] is B[1], B[1] is B[2])
# True True 复制了对同一个列表的引用，三个列表实际上指向的是同一个列表，同一个地址

a = 250
b = 250
print(a is b)
# True

a = 1000
b = 1000
print(a is b)
# True  交互模式下为False
# Python 的缓存机制，所以在 IDE 环境或者脚本模式下同一个整数被多个变量引用不会开辟新的内存空间

# 三维数组
C = [0] * 3
for i in range(3):
    C[i] = [0] * 3
    for j in range(3):
        C[i][j] = [0] * 3
print(C)

# 从空数组开始创建
d = []
for i in range(3):
    d.append([])
    for j in range(3):
        d[i].append([])
        for k in range(3):
            d[i][j].append(0)
print(d)

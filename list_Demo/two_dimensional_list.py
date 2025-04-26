# 创建一个 88 x 88 的随机整数矩阵（二维列表），然后匹配用户输入的整数是否与其中某元素相等，如果相等则打印其行号和列号。
# 要求1：随机整数取值范围 0~1024
# 要求2：需找出所有匹配的元素来
import random
list1 = [0] * 88
for i in range(88):
    list1[i] = [random.randint(0, 1025)]
    for j in range(87):
        list1[i].append(random.randint(0, 1025))
        # list1[i] += [random.randint(0, 1025)]
num = int(input("请输入一个待匹配的整数："))
for i in range(88):
    for j in range(88):
        if list1[i][j] == num:
            print(i, j)

import random

# 创建并初始化二维列表
matrix = []
for i in range(88):
    matrix.append([])
    for j in range(88):
        matrix[i].append(random.randint(0, 1024))

target = int(input("请输入一个代匹配的整数："))

# 匹配用户输入的整数
for i in range(88):
    for j in range(88):
        if matrix[i][j] == target:
            print(i, j)

# 假设给定一个 m * n 的矩阵（矩阵中数值的取值范围是 0~1024，且各不相同），如果某一个元素的值在同一行的所有元素中最小，并且在同一列的所有元素中最大，那么该元素便是幸运数字
matrix = [[10, 36, 52],
          [33, 24, 88],
          [66, 76, 99]]
# 找出每一行最小和每一列最大，再一一比对
m = len(matrix)
n = len(matrix[0])
min_row = [1024] * m
max_col = [0] * n
for i in range(m):
    for j in range(n):
        min_row[i] = min(matrix[i][j], min_row[i])
        max_col[j] = max(matrix[i][j], max_col[j])

for i in range(m):
    for j in range(n):
        if matrix[i][j] == min_row[i] and matrix[i][j] == max_col[j]:
            print(matrix[i][j])
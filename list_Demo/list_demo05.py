# 列表推导式
x = [i for i in range(10)]
print(x)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [i + 1 for i in range(10)]
print(x)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 对于字符串
y = [c * 2 for c in "FishC"]
print(y)
# ['FF', 'ii', 'ss', 'hh', 'CC']
z = []
for c in "FishC":
    z.append(c * 2)
print(z)
# ['FF', 'ii', 'ss', 'hh', 'CC']

# ord()转换成ASCII编码
code = [ord(c) for c in "FishC"]
print(code)
# [70, 105, 115, 104, 67]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
flatten = [col for row in matrix for col in row]
print(flatten)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
re_flatten = [col for row in matrix for col in row]
re_flatten.reverse()
print(re_flatten)
# [9, 8, 7, 6, 5, 4, 3, 2, 1]


col2 = [row[1] for row in matrix]
print(col2)
# [2, 5, 8]
diag = [matrix[i][i] for i in range(len(matrix))]
print(diag)
# [1, 5, 9]
diag2 = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
print(diag2)
# [3, 5, 7]
diag3 = [i * matrix[i][i] for i in range(len(matrix))]
print(diag3)
# [0, 5, 18]


# 创建二维列表
d = [[i, i + 2] for i in range(6)]
print(d)
# [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]

# 列表推导式添加 if 条件
even = [i for i in range(10) if i % 2 == 0]
print(even)
# [0, 2, 4, 6, 8]

# 找出首字母为F的单词
words = ["Great", "FishC", "Brilliant", "Excellent", "Fantastic"]
for i in words:
    if i[0] == "F":
        print(i)
# FishC
# Fantastic
words1 = [i for i in words if i[0] == "F"]
print(words1)
# ['FishC', 'Fantastic']

# 笛卡尔乘积
w = [x + y for x in "fishc" for y in "FISHC"]
print(w)
# ['fF', 'fI', 'fS', 'fH', 'fC', 'iF', 'iI', 'iS', 'iH', 'iC', 'sF', 'sI', 'sS', 'sH',
# 'sC', 'hF', 'hI', 'hS', 'hH', 'hC', 'cF', 'cI', 'cS', 'cH', 'cC']

# _ 可用于临时变量，无关紧要的变量
_ = []
w2 = [[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 3 == 0]
print(w2)
# [[0, 0], [0, 3], [0, 6], [0, 9], [2, 0], [2, 3], [2, 6], [2, 9], [4, 0], [4, 3], [4, 6],
# [4, 9], [6, 0], [6, 3], [6, 6], [6, 9], [8, 0], [8, 3], [8, 6], [8, 9]]
_ = []
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 3 == 0:
                _.append([x, y])
print(_)
# [[0, 0], [0, 3], [0, 6], [0, 9], [2, 0], [2, 3], [2, 6], [2, 9], [4, 0], [4, 3], [4, 6],
# [4, 9], [6, 0], [6, 3], [6, 6], [6, 9], [8, 0], [8, 3], [8, 6], [8, 9]]

w3 = [[x, y] for x in range(10) for y in range(10) if x % 2 == 0 if y % 3 == 0]
print(w3)
# [[0, 0], [0, 3], [0, 6], [0, 9], [2, 0], [2, 3], [2, 6], [2, 9], [4, 0], [4, 3], [4, 6],
# [4, 9], [6, 0], [6, 3], [6, 6], [6, 9], [8, 0], [8, 3], [8, 6], [8, 9]]

# 三维列表
d = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
print(d)
# [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
# 使用列表推导式创建一个 4 * 5 的二维列表，并将每个元素初始化为数字 8
d = [[8 for _ in range(5)] for _ in range(4)]
print(d)
# [[8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8]]
d = [[8] * 5 for _ in range(4)]
print(d)
# [[8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8]]

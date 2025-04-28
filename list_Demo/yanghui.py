# 杨辉三角形
tri = []
for i in range(10):
    tri.append([])
    for j in range(10):
        if i == 0:
            tri[i].append(1)
            break
        elif j == 0:
            tri[i].append(1)
        elif j == i:
            tri[i].append(1)
            break
        else:
            tri[i].append(tri[i-1][j-1]+tri[i-1][j])
for i in tri:
    # 去掉[]和， :列表转字符串，并以空格连接起来
    tri1 = " ".join(str(j) for j in i)
    print(tri1)
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
# 1 8 28 56 70 56 28 8 1
# 1 9 36 84 126 126 84 36 9 1

for i in tri:
    # 去掉[]和， :列表转字符串，并以空格连接起来
    # int的 j 转换成str后可计算长度
    # 将字符串和  6 - 1 - len(str(j))  个空格以空格连接起来，其中 -1 的空格是以空格连接的空格
    tri2 = " ".join(str(j) + " " * (6 - 1 - len(str(j))) for j in i)
    print(" " * 3 * (len(tri)-len(i)), tri2)
#                            1
#                         1     1
#                      1     2     1
#                   1     3     3     1
#                1     4     6     4     1
#             1     5     10    10    5     1
#          1     6     15    20    15    6     1
#       1     7     21    35    35    21    7     1
#    1     8     28    56    70    56    28    8     1
# 1     9     36    84    126   126   84    36    9     1

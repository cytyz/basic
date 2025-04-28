# 顺时针输出
# 按照顺时针螺旋顺序输出矩阵中的所有元素
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
# 四个方向的长度
top = 0
bottom = len(matrix)
left = 0
right = len(matrix[0])
result = []
# 每输出一圈少2行
for i in range(len(matrix) // 2 + 1):
    # 从头到尾依次输出
    for j in range(left, right):
        result.append(matrix[top][j])
    top += 1
    if top >= bottom:
        break
    for k in range(top, bottom):
        result.append(matrix[k][right-1])
    right -= 1
    if left >= right:
        break
    # 倒着生成range
    for l in range(right-1, left-1, -1):
        result.append(matrix[bottom-1][l])
    bottom -= 1
    if top >= bottom:
        break
    for m in range(bottom-1, top-1, -1):
        result.append(matrix[m][left])
    left += 1
    if left >= right:
        break
print(result)

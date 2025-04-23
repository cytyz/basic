# 水仙花数
# 求解 100~999 之间的所有水仙花数
# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
hundred = 0
ten = 0
piece = 0
for i in range(100, 1000):
    hundred = i // 100
    ten = i // 10 % 10
    piece = i % 10
    if pow(hundred, 3) + pow(ten, 3) + pow(piece, 3) == i:
        print(i)

# ************************************
# 重点学习思路
for i in range(100, 1000):
    sum = 0
    temp = i

    while temp >= 1:
        sum = sum + (temp % 10) ** 3
        temp //= 10

    if sum == i:
        print(i)

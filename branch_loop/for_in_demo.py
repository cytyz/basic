for each in "FishC":
    print(each)
# F
# i
# s
# h
# C
print("————————————————————————")
# 用while实现
i = 0
while i < len("FishC"):
    print("FishC"[i])
    i += 1
# F
# i
# s
# h
# C
print("————————————————————————")
# range(10) 从0到10（不包括10）的整数序列
# range(0, 10)
# range(0, 10, 2)
for each in range(10):
    print(each)

# 求1~10之间的素数
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "=", n // x, "*", x)
            break
    else:
        print(n, "是一个素数")

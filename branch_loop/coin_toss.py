# 抛硬币实验
# 如果抛硬币的次数小于 100，则打印每次的结果，否则不打印
# 统计最终正面和反面的次数
# 分别统计正反面最多出现连续的次数
import random

counts = int(input("请输入抛硬币的次数："))
i = 0
positive = 0
opposite = 0
temp = 0
positive_continuous = 0
PC_sum = 0
opposite_continuous = 0
OC_sum = 0
print("开始抛硬币实验：")
while i < counts:
    num = random.randint(1, 10)
    if num % 2:
        if counts < 100:
            print("正面", end=" ")
        positive += 1
        if temp != 1:
            positive_continuous = 1
            temp = 1
        else:
            positive_continuous += 1
        if PC_sum < positive_continuous:
            PC_sum = positive_continuous
    else:
        if counts < 100:
            print("反面", end=" ")
        opposite += 1
        if temp != 2:
            opposite_continuous = 1
            temp = 2
        else:
            opposite_continuous += 1
        if OC_sum < opposite_continuous:
            OC_sum = opposite_continuous
    i += 1
    if ((i % 20 == 0) and (counts < 100)) or ((i == counts) and (counts < 100)):
        print()
print("一共模拟了", counts, "次抛硬币，结果如下:")
print("正面", positive, "次")
print("反面", opposite, "次")
print("最多连续正面", PC_sum, "次")
print("最多连续反面", OC_sum, "次")

# 请输入抛硬币的次数：88
# 开始抛硬币实验：
# 反面 反面 正面 正面 正面 反面 正面 反面 正面 正面 正面 反面 正面 反面 正面 正面 正面 反面 反面 正面
# 正面 正面 反面 反面 反面 反面 正面 正面 反面 正面 正面 正面 反面 正面 反面 正面 反面 正面 正面 反面
# 正面 反面 正面 反面 反面 正面 正面 反面 正面 反面 反面 反面 正面 正面 反面 反面 正面 正面 正面 反面
# 反面 反面 正面 反面 正面 正面 反面 正面 反面 反面 反面 正面 反面 反面 反面 正面 反面 反面 正面 正面
# 反面 反面 正面 反面 反面 反面 正面 正面
# 一共模拟了 88 次抛硬币，结果如下:
# 正面 44 次
# 反面 44 次
# 最多连续正面 3 次
# 最多连续反面 4 次

# 请输入抛硬币的次数：10000
# 开始抛硬币实验：
# 一共模拟了 10000 次抛硬币，结果如下:
# 正面 5050 次
# 反面 4950 次
# 最多连续正面 12 次
# 最多连续反面 12 次

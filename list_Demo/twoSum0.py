# 两数之和
# 让用户自己来录入 整数列表nums 和 目标值target 的数据，在该数组中找出和为目标值的两个元素，并将它们的数组下标值打印出来
nums = []
while True:
    num = input("请录入一个整数（输入STOP结束）：")
    if num == "STOP":
        break
    try:
        nums.append(int(num))
    except ValueError:
        print("输入无效，请输入整数！")
target = int(input("请录入目标整数："))
n = len(nums)
# 获取 nums 的长度，并将结果存放到 n 变量中 #
for i in range(n):
    for j in range(i + 1, n):
        if (nums[i] + nums[j]) == target:
            print("[", i, ",", j, "]")
            break
        # 将找到的两个元素下标值以列表的形式打印出来 #
# 请录入一个整数（输入STOP结束）：22
# 请录入一个整数（输入STOP结束）：33
# 请录入一个整数（输入STOP结束）：45
# 请录入一个整数（输入STOP结束）：18
# 请录入一个整数（输入STOP结束）：62
# 请录入一个整数（输入STOP结束）：88
# 请录入一个整数（输入STOP结束）：93
# 请录入一个整数（输入STOP结束）：72
# 请录入一个整数（输入STOP结束）：67
# 请录入一个整数（输入STOP结束）：19
# 请录入一个整数（输入STOP结束）：STOP
# 请录入目标整数：100
# [ 1 , 8 ]

# 用random 模块，生成一个由 10000 个整数（范围是 1 ~ 65535）构成的随机列表
import random
nums = []
for i in range(10000):
    num = random.randint(1, 65535)
    nums.append(num)
target = int(input("请录入目标整数："))
n = len(nums)
# 获取 nums 的长度，并将结果存放到 n 变量中 #
for i in range(n):
    for j in range(i + 1, n):
        if (nums[i] + nums[j]) == target:
            print("[", i, ",", j, "]")
        # 将找到的两个元素下标值以列表的形式打印出来 #
# 请录入目标整数：12345
# [ 52 , 8499 ]
# [ 60 , 6637 ]
# [ 104 , 618 ]
# [ 108 , 882 ]
# [ 134 , 6948 ]
# [ 135 , 5853 ]
# [ 136 , 4694 ]
# [ 156 , 1470 ]
# .........

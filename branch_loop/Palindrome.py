# 判断一个整数是否为回文数
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
num = int(input("请输入一个正整数："))
# 使用切片
# print("是回文数") if num == num[::-1] else print("不是回文数")

num_temp = num
if num < 0 or num % 10 == 0:
    print("不是回文数")
else:
    temp = 0
    while num_temp >= 1:
        temp = temp * 10 + num_temp % 10
        num_temp = num_temp // 10
    if num == temp:
        print("是回文数")
    else:
        print("不是回文数")

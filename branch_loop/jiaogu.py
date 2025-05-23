# 验证角谷猜想
# 角谷猜想的内容是：任意给定一个正整数，若它为偶数则除以 2，若它为奇数则乘以 3 再加 1，得到一个新的自然数，按照这样的方法计算下去，最终的结果必将是 1。
# 比如给定的自然数是 5，则 5 * 3 + 1 = 16 -> 16 / 2 = 8 -> 8 / 2 = 4 -> 4 / 2 = 2 -> 2 / 2 = 1。
# 现在要求大家编写一个验证角谷猜想的程序。
n = int(input("请输入一个正整数："))

while n > 0:
    # 判断 n 是否可以被 2 整除 #
    if n % 2 == 0:
        print(n, " / 2 = ", n // 2)
        n = n // 2
    else:
        print(n, " * 3 + 1 == ", n * 3 + 1)
        n = n * 3 + 1
    if n == 1:
        break
# 请输入一个正整数：5
# 5  * 3 + 1 ==  16
# 16  / 2 =  8
# 8  / 2 =  4
# 4  / 2 =  2
# 2  / 2 =  1

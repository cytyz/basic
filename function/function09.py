# 递归
# 函数调用自身， 必须有一个结束条件
def func(i):
    if i > 0:
        print("qwer")
        i -= 1
        func(i)
func(4)
# qwer
# qwer
# qwer
# qwer

# ————————————————————————————————————————————
# 例子：阶乘
def factIter(n):
    value = 1
    for i in range(1, n + 1):
        value *= i
    return value
print(factIter(4))
# 24

def factRecur(n):
    if n == 1:
        return 1
    return factRecur(n - 1) * n
print(factRecur(4))
# 24

# ————————————————————————————————————————————
# 例子：斐波那契数列
def fibIter(n):
    a = 1
    b = 1
    c = 1
    while n > 2:
        c = a + b
        a, b = b, c
        n = n - 1
    return c
print(fibIter(12))
# 144

def fibRecur(n):
    if n == 1 or n == 2:
        return 1
    return fibRecur(n - 1) + fibRecur(n - 2)
print(fibRecur(12))
# 144
# 时间优化
def fibRecur_new(n, a, b):
    if n == 1 or n == 2:
        return b
    return fibRecur_new(n - 1, b, a + b)
print(fibRecur_new(12, 1, 1))
# 144
import timeit
# 这个耗时会比较久（因为默认是重复测试 5 次），请大家耐心等待
FR = timeit.timeit("fibRecur(12)", setup="from __main__ import fibRecur")
print(f"普通递归耗时：{FR:.2f}秒。")
# 普通递归耗时：10.17秒。
TFR = timeit.timeit("fibRecur_new(12, 1, 1)", setup="from __main__ import fibRecur_new")
print(f"优化递归耗时：{TFR:.2f}秒。")
# 优化递归耗时：0.46秒。
FI = timeit.timeit("fibIter(12)", setup="from __main__ import fibIter")
print(f"普通迭代耗时：{FI:.2f}秒。")
# 普通迭代耗时：0.30秒。

# ————————————————————————————————————————————
# 例子：汉诺塔
# 一次只能移动一个圆盘，小的圆盘只能在大的圆盘上面
def hanoi(n):
    if n == 1:
        return 1
    return hanoi(n - 1) * 2 + hanoi(1)
print(hanoi(5))
# 31
def hanoi_fact(n, x, y, z):
    if n == 1:
        print(x, "-->", z)
    else:
        hanoi_fact(n - 1, x, z, y)
#         将x的 n - 1 个圆盘移动到y
        print(x, "-->", z)
        hanoi_fact(n - 1, y, x, z)
#         将y的 n - 1 个圆盘移动到z
hanoi_fact(5,"A","B","C")
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
# A --> B
# C --> B
# C --> A
# B --> A
# C --> B
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
# B --> A
# C --> B
# C --> A
# B --> A
# B --> C
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C

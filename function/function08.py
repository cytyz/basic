# 生成器
# yield 代替return， 拥有yield的函数被成为生成器，它是一种特殊的迭代器，支持next函数
# 生成器对象无法使用下标索引
# 每次调用yield 只会提供一个数据，并记住当时的状态
def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1
        print("yes")
print(counter())
# <generator object counter at 0x000002F571FA5A80>
for i in counter():
    print(i)
# 0
# yes
# 1
# yes
# 2
# yes
# 3
# yes
# 4
# yes
# 5
# yes

print("________________________________-")
c = counter()
print(next(c))
print("____")
print(next(c))
print("____")
print(next(c))
# 0
# ____
# yes
# 1
# ____
# yes
# 2


# 斐波那契数列
def fib():
    back1, back2 = 0, 1
    while True:
        yield back1
        back1, back2 = back2, back1 + back2
f = fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
# 0
# 1
# 1
# 2
# 3

# 生成器表达式（元组推导式）  与列表不同的是列表推导式会一次性生成出来，生成器表达式需要一次次调用
print((i ** 2 for i in range(10)))
# <generator object <genexpr> at 0x0000015BB9DFAB50>
t = ((i ** 2) for i in range(10))
print(next(t))
print(next(t))
print(next(t))
# 0
# 1
# 4

# 生成器会记住当时的状态，所以后面会接着上次的生成
for i in t:
    print(i)
# 9
# 16
# 25
# 36
# 49
# 64
# 81

print(list(map(abs, (-1, 2, -3, 4, -5))))
# [1, 2, 3, 4, 5]
# 转换成生成器表达式
print(list((abs(x) for x in (-1, 2, -3, 4, -5))))
# [1, 2, 3, 4, 5]

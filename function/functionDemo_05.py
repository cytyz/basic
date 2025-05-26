# 闭包嵌套求平均值 与 返回斐波那契数列
def make_avg():
    x = 0
    i = 0
    def inner(y):
        nonlocal x, i
        x += y
        i += 1
        return x / i
    return inner
avg = make_avg()
print(avg(5))
# 5.0
print(avg(3))
# 4.0
print(avg(7))
# 5.0
print(avg(19))
# 8.5

# 闭包嵌套返回一个斐波那契数列
def fib():
    a, b = 0, 1
    def inner():
        nonlocal a, b
        a, b = b, a + b
        return b - a
    return inner
f = fib()
print(f(), f(), f(), f(), f(), f(), f(), f(), f())
# 0 1 1 2 3 4 5 8 13 21
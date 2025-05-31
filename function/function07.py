# lambda 表达式（匿名函数）
# lambda arg1, arg2, ... argN : expression
# 可以存在于函数无法存在的地方，如列表，但不建议这么写
def squarex(x):
    return x * x

print(squarex(3))
# 9

squareY = lambda y : y * y
print(squareY(3))
# 9

# 可以存在于 整个函数的定义过程  无法存在的地方，如列表
y = [lambda x : x * x, 2, 3]
print(y[0](y[1]))
# 4

mapped = map(lambda x : ord(x) + 10, "FishC")
print(list(mapped))
# [80, 115, 125, 114, 77]

def boring(x):
    return ord(x) + 10
print(list(map(boring, "FishC")))
# [80, 115, 125, 114, 77]

print(list(filter(lambda x : x % 2, range(10))))
# [1, 3, 5, 7, 9]


# ——————————————————————————————————————————————————————
# 闭包转换成 lambda 表达式
def power(exp):
    def exp_of(base):
        return base ** exp
    return exp_of
square = power(2)
square(2)
# 4
# 转换成lambda表达式
f = lambda exp : lambda base : base ** exp
square = f(2)
square(2)
# 4

# 装饰器转换成 lambda 表达式
def add(func):
    def inner():
        x = func()
        return x + 1
    return inner
@add
def test():
    return 2
print(test())
# 3
# 转换成lambda表达式
@lambda func : lambda : func() + 1
def test1():
    return 2
print(test1())
# 3
# ———————————————————————————————————————————————————————

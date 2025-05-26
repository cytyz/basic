# 装饰器
# 一种设计模式    在目标函数前添加@函数  将目标函数作为实际参数传入到装饰器函数中
# 函数可以添加多个装饰器
# 运行程序一般都是从上到下，添加装饰器后运行到装饰器函数时，添加装饰器函数，然后定位到装饰器，将目标函数传入装饰器函数，再返回装饰器函数，正常往下进行

# ()相当于在调用函数
def myfunc():
    print("正在调用myfunc------")
def report(func):
    print("开始调用函数")
    func()
    print("调用函数结束")
report(myfunc)
# 开始调用函数
# 正在调用myfunc------
# 调用函数结束

import time
def time_master(func):
    print("开始运行程序")
    start = time.time()
    func()
    print("结束运行程序")
    end = time.time()
    print(f"一共耗费了{(end - start):.5f}秒")
def myfunc():
    time.sleep(2)
    print("Hello, FishC")
time_master(myfunc)
# 开始运行程序
# Hello, FishC
# 结束运行程序
# 一共耗费了2.00034秒

def time_master(func):
    print("开始运行程序")
    start = time.time()
    func()
    print("结束运行程序")
    end = time.time()
    print(f"一共耗费了{(end - start):.5f}秒")

def myfunc():
    time.sleep(2)
    print("Hello, FishC")
time_master(myfunc)
# 开始运行程序
# Hello, FishC
# 结束运行程序
# 一共耗费了2.00036秒

def time_master(func):
    def call_func():
        print("开始运行程序")
        start = time.time()
        func()
        print("结束运行程序")
        end = time.time()
        print(f"一共耗费了{(end - start):.5f}秒")
    return call_func

# 装饰器 将函数作为实际参数传入到装饰器函数中
# 相当于myfunc = time_master(myfunc)  此时返回call_func  后面再myfunc()来屌用
@time_master
def myfunc():
    time.sleep(2)
    print("Hello, FishC")
myfunc()
# 开始运行程序
# Hello, FishC
# 结束运行程序
# 一共耗费了2.00040秒

# 函数可以添加多个装饰器
def add(func):
    def inner():
        x = func()
        return x + 1
    return inner
def cube(func):
    def inner():
        x = func()
        return x * x * x
    return inner
def square(func):
    def inner():
        x = func()
        return x * x
    return inner
@add
@cube
@square
def test():
    return 2
print(test())
# 65   add(cube(square(test)))

# 给装饰器传递参数
def logger(msg):
    def time_master(func):
        def call_func():
            print("开始运行程序")
            start = time.time()
            func()
            print("结束运行程序")
            end = time.time()
            print(f"{msg}一共耗费了{(end - start):.5f}秒")
        return call_func
    return time_master
# 相当于funA() = logger(msg="A")(func)
@logger(msg="A")
def funA():
    time.sleep(1)
    print("正在调用函数A")
@logger(msg="B")
def funB():
    time.sleep(1)
    print("正在调用函数B")
funA()
# 开始运行程序
# 正在调用函数A
# 结束运行程序
# A一共耗费了1.00018秒
funB()
# 开始运行程序
# 正在调用函数B
# 结束运行程序
# B一共耗费了1.00064秒

# 目标函数需要参数时
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("在原函数之前执行")
        func(*args, **kwargs)
        print("在原函数之后执行")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# 在原函数之前执行
# Hello, Alice!
# 在原函数之后执行

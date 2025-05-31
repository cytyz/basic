# 高阶函数
# 一个调用其他函数作为参数时，这个函数被称为高阶函数
# functools 包括许多高阶函数的模块
# reduce, 将可迭代的元素依次放入函数中, 依次进行，前一次计算的结果会作为前一次的参数传入
import functools
def add(x, y):
    return x + y
print(functools.reduce(add, [1, 2, 3, 4, 5]))    # 15
print(add(add(add(add(1,2),3),4),5))    # 15

# 阶乘
print(functools.reduce(lambda x, y: x*y, range(1, 11)))    # 3628800


# 偏函数
# partial 对指定的函数进行二次包装，将所需参数预先绑定一部分，剩下的才是需要输入的
square = functools.partial(pow, 2)
print(square(3))    # 9
cube = functools.partial(pow, 3)
print(cube(3))    # 27


# @wraps装饰器
# 可以使得被装饰函数在查询 __name__ 时查到自己的函数名
import time
def time_master(func):
    def call_func():
        print("开始运行程序")
        start = time.time()
        func()
        print("结束运行程序")
        end = time.time()
        print(f"一共耗费了{(end - start):.5f}秒")
    return call_func

@time_master
def myfunc():
    time.sleep(2)
    print("Hello, FishC")
# myfunc()
print(myfunc.__name__)
# call_func

def time_master(func):
    @functools.wraps(func)
    def call_func():
        print("开始运行程序")
        start = time.time()
        func()
        print("结束运行程序")
        end = time.time()
        print(f"一共耗费了{(end - start):.5f}秒")
    return call_func

@time_master
def myfunc():
    time.sleep(2)
    print("Hello, FishC")
# myfunc()
print(myfunc.__name__)
# myfunc

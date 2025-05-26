# 装饰器函数的创建与参数
import time

# 添加装饰器函数
def delay(func):
    def sleep_func():
        time.sleep(1)
        func()
    return sleep_func

def fib():
    back1, back2 = 0, 1
    # 添加装饰器
    @delay
    def func():
        nonlocal back1, back2
        back1, back2 = back2, back1 + back2
        print(back1, end=' ')

    return func

def get_fib(n):
    f = fib()
    for i in range(n):
        f()

n = int(input("请输入需要获取的斐波那契数："))
get_fib(n)
print()
# 题目要求：
# 请在此处补充装饰器 type_check() 的代码
def type_check(correct_type):
    def type_func(func):
        def inner(*args):
            if type(*args) == correct_type:
                return func(*args)
            else:
                return "参数类型错误！"
        return inner
    return type_func


print("<<<--- 测试整数 --->>>")

@type_check(int)
def double(x):
    return x * 2

print(double(2))      # 这里打印结果应该是 4
print(double("2"))    # 这里打印结果应该是 “参数类型错误”


print("\n<<<--- 测试字符串 --->>>")

@type_check(str)
def upper(s):
    return s.upper()

print(upper('I love FishC.'))   # 这里打印结果应该是 I LOVE FISHC
print(upper(250))               # 这里打印结果应该是 “参数类型错误”

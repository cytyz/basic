# 函数
# 创建和调用
def myfunc():
    # pass 空语句，作为占位符使用，在规划功能时占位
    pass
myfunc()
def myfunc():
    for i in range(3):
        print("I Love FishC")
myfunc()
# I Love FishC
# I Love FishC
# I Love FishC

# 函数的参数
# 形式参数与实际参数    函数定义时用的是形式参数，函数调用时用的是实际参数
def myfunc(name, times):
    for i in range(times):
        print(f"I Love {name}.")
myfunc("Python", 3)
# I Love Python.
# I Love Python.
# I Love Python.

# 函数的返回值 return    执行return时结尾，不会再运行后面的语句
# BIF 指内置函数 build-in function
# 函数在执行完所有语句后会默认隐式地返回一个 none 值
def div(x, y):
    z = x // y
    return z
print(div(4, 2))
# 2
def div(x, y):
    return x // y
print(div(4, 2))
# 2
def div(x, y):
    if y == 0:
        return "除数不能为0！"
    else:
        return x // y
print(div(4, 2))
# 2
print(div(4, 0))
# 除数不能为0！

def div(x, y):
    if y == 0:
        return "除数不能为0！"
    return x // y
print(div(4, 2))
# 2
print(div(4, 0))
# 除数不能为0！
def myfunc():
    # pass 空语句，作为占位符使用，在规划功能时占位
    pass
print(myfunc())
# None

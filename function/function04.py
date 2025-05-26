# 作用域
# 作用域指一个变量可以被访问的范围
# 局部作用域    函数内创建的变量
# 全局作用域    函数外创建的变量
# 当存在全局变量时，若在函数内创建同名局部变量，则在函数中创建一个同名的局部变量进行覆盖
# global x  在函数内使用，创建全局变量

# 嵌套函数 函数中创建一个内部函数
# 内部函数无法在外部被直接调用，需要在其对应的外部函数中调用
def funA():
    x = 520
    def funB():
        x = 880
        print(f"In funB, x={x}")
    funB()
    print(f"In funA, x={x}")

funA()
# In funB, x=880
# In funA, x=520

# nonlocal  可以在内部函数修改上一层外部函数的变量
def funA():
    x = 520
    def funB():
        nonlocal x
        x = 880
        print(f"In funB, x={x}")
    funB()
    print(f"In funA, x={x}")

funA()
# In funB, x=880
# In funA, x=880

# LEGB规则
# Local 局部作用域  Enclosed 嵌套函数的外层函数作用域  Global 全局作用域  Build-In 内置作用域
# 小则优先 范围小



x = [1, 2, 3]
def invert(x):
    x = x[::-1]
invert(x)
print(x)
# [1, 2, 3]

x = [1, 2, 3]
def invert(x):
    x[:] = x[::-1]
invert(x)
print(x)
# [3, 2, 1]


x = 100
def funA():
    global x
    x = 250
    def funB():
        # nonlocal x  此时funA的 x 为全局变量， 无局部变量 x 此时 nonlocal会报错
        x = 520
    funB()

funA()
print(x)
# 250

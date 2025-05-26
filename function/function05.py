# 闭包  如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包
# 闭包的核心特征是内部函数能够访问外部函数的变量，即使外部函数已经执行完毕

# 闭包是由函数及其相关的引用环境组合而成的实体(即：闭包=函数+引用环境)
# (想想Erlang的外层函数传入一个参数a, 内层函数依旧传入一个参数b, 内层函数使用a和b, 最后返回内层函数)
# x()() 通过x调用下一层内部函数
# 每次调用外部函数后都将生成并保存一个新的局部变量。其实这里外部函数返回的就是闭包

# 1、当闭包执行完后，仍然能够保持住当前的运行环境
# 2、闭包可以根据外部作用域的局部变量来得到不同的结果
def funA():
    x = 888
    def funB():
        print(x)
    return funB
print(funA())
# <function funA.<locals>.funB at 0x000001CEAD9B8540>    得到funB的引用
funA()()
# 888

# 不直接通过funA调用funB
funny = funA()
funny()
# 888

# 嵌套函数的外层函数作用域  赋值给变量时  能保留
# 嵌套函数调用，  类似二维数组
def power(exp):
    def exp_of(base):
        return base ** exp
    return exp_of
square = power(2)
cube = power(3)
print(square(5))
# 25
print(cube(5))
# 125
print(power(2)(3))
# 9

def outer():
    x = 0
    y = 0
    def inner(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f"现在，x = {x}, y = {y}")
    return inner
move = outer()
move(1, 2)
# 现在，x = 1, y = 2
move(-2, 2)
# 现在，x = -1, y = 4

# 当闭包执行完后，仍然能够保持住当前的运行环境
# 移动小游戏
origin = (0, 0)
legal_x = [-100, 100]
legal_y = [-100, 100]

def create(pos_x=0, pos_y=0):
    def moving(direction, step):
        nonlocal pos_x, pos_y
        new_x = pos_x + direction[0] * step
        new_y = pos_y + direction[1] * step

        if new_x < legal_x[0]:
            pos_x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            pos_x = legal_x[1] - (new_x - legal_x[1])
        else:
            pos_x = new_x

        if new_y < legal_y[0]:
            pos_y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > origin[1]:
            pos_y = legal_y[1] - (new_y - legal_y[1])
        else:
            pos_y = new_y
        return pos_x, pos_y
    return moving

move = create()
print("向右移动20步后，位置是：", move([1, 0], 20))
# 向右移动20步后，位置是： (20, 0)
print("向上移动120步后，位置是：", move([0, 1], 120))
# 向上移动120步后，位置是： (20, 80)
print("向右下角移动88步后，位置是：", move([1, -1], 88))
# 向右下角移动88步后，位置是： (92, -8)



# ----------------------------------------------------
def addx(x):
    def adder(y): return x + y
    return adder
c =  addx(8)
print(type(c))
# <type 'function'>
print(c.__name__)
# adder
print(c(10))
# 18
# ----------------------------------------------------

flist = []
for i in range(3):
    def foo(x): print(x + i)
    flist.append(foo)
for f in flist:
    f(2)
# 4
# 4
# 4
# 先执行完第一个for循环，列表中添加的都是foo(x): print(x + i),此时i = 2 ，执行第二个for循环，结果均为4

flist = []
for i in range(3):
    def foo(x, y = i): print(x + y)
    flist.append(foo)
for f in flist:
    f(2)
# 2
# 3
# 4
# 先执行完第一个for循环，列表中添加的为foo(x): print(x + 0/1/2),，执行第二个for循环，结果为2/3/4


def outter():
    def innerA():
        x = 100

    def innerB():
        nonlocal x
        x = 250

    def innerC():
        global x
        x = 520

    x = 880

    innerA()
    print(f"调用完 innerA() 函数之后，x = {x}")

    innerB()
    print(f"调用完 innerB() 函数之后，x = {x}")

    innerC()
    print(f"调用完 innerC() 函数之后，x = {x}")
outter()
print(f"此时此刻，全局变量 x = {x}")
# 调用完 innerA() 函数之后，x = 880
# 调用完 innerB() 函数之后，x = 250
# 调用完 innerC() 函数之后，x = 250
# 此时此刻，全局变量 x = 520

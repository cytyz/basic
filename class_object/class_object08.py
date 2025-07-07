# 内置默认方法基础
# __new__(cls[, ...]) 创建对象时第一个调用，返回 self  cls:类  作用于不可变量
class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return super().__new__(cls, string)
cs = CapStr("FishC")
print(cs)    # FISHC
print(cs.lower())    # fishc
print(cs.capitalize())    # Fishc

# ———————————————————————————————————————————
# __del__(self):    当类最后一个引用销毁时触发
class C:
    def __init__(self):
        print("我来了~")
    def __del__(self):
        print("我走了~")
c = C()
# 我来了~
print("1") # 1
del c
# 我走了~ 销毁时触发
print("2") # 2

c = C()
# 我来了~
d = c
del c # 最后一个引用销毁时触发
print("3") #3
# 我走了~    若程序中未销毁，程序运行结束时销毁，垃圾回收机制

# ———————————————————————————————————————————
# del方法可以通过创建一个该实例的新引用来推迟其销毁（对象的重生）（不建议，上下文环境改变，无法正常工作）
class D:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        # 一般不要使用全局变量，会污染命名空间
        global x
        x = self
d = D("tyz")
print(d, d.name) # <__main__.D object at 0x000001F2DED76F90> tyz
del d
print(x, x.name) # <__main__.D object at 0x0000028BF9DB6F90> tyz

class E:
    def __init__(self, name, func):
        self.name = name
        self.func = func
    def __del__(self):
        self.func(self)
# 闭包
def outer():
    x = 0
    def inner(y=None):
        nonlocal x
        if y:
            x = y
        else:
            return x
    return inner
f = outer()
e = E("tyz", f)
del e
# 销毁时给 func() f=inner(self)赋值，将 self 保存在 x 中，g=f()时调用
g = f()
print(g, g.name) # <__main__.E object at 0x00000219DDDF70E0> tyz

# ———————————————————————————————————————————
# 绕过类的构造函数，创建出它的实例对象
class C:
    def __init__(self, x):
        self.x = x
c = C.__new__(C)
print(isinstance(c, C)) # True
# c.x 不存在，仅创建了实例对象，未初始化

# type()函数
# type() 检测类型，返回对应的类型
# 检测对象类型更适合用 isinstance() 它会考虑到子类的情况

print(type(250)) # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type("fishc")) # <class 'str'>

print(int) # <class 'int'>
print(type(250) is int) # True

# 把 type() 作为类型转换来用
print(type(250)('520'), int('520')) # 520 520

# 返回对象的类
class C:
    def __init__(self, x):
        self.x = x
c = C(250)
print(c) # <__main__.C object at 0x00000163F1AE6F90>
print(type(c)) # <class '__main__.C'>
d = type(c)(520)
print(d) # <__main__.C object at 0x00000159945B4E10>

# ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
print(type(C), type(type)) # <class 'type'> <class 'type'>
# python 万物皆对象，而类自身也是对象，是由 type 生成的对象， type 是type的对象


# ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# type(name, base, dict, **kwds) 根据传入的三个参数，返回一个新的 type
# name:指定将要创造的类的名字
# bases:指定将要创造的类的父类
# dict:指定将要创造的类的属性和方法
# kwds:（可选）收集参数(可以设置多个)，当且仅当需要时，该收集参数将被传递给适当的元类机制（通常为 __init__subclass()：类方法，作用：加强父类对子类的管理）

class C:
    pass
# 等价于
C = type('C', (), {}) # () 元组，此时无指定父类，{} 字典，此时无指定属性方法
c = C()
print(c.__class__) # <class '__main__.C'> 查看对象所属的类
print(C.__bases__) # (<class 'object'>,) 查看类的父类

D = type('D', (C,), {}) # 父类为C，元组，后面加,
print(D.__bases__) # (<class '__main__.C'>,)

E = type('E', (), dict(x=250, y=520))
print(E.x, E.y) # 250 520

# 在外部创建函数，在字典中调用
def funC(self, name='FishC'):
    print("hello", name)
F = type('F', (), dict(say_hi=funC))
f = F()
f.say_hi() # hello FishC

class C:
    def __init_subclass__(cls):
        print("父爱如山")
        cls.x = 520
class D(C):
    x = 250
# 父爱如山
print(D.x) # 520

class C:
    def __init_subclass__(cls, value):
        print("父爱如山")
        cls.x = value
class D(C, value=520):
    x = 250
# 父爱如山
print(D.x) # 520
# 等价于
D = type('D', (C, ), dict(x=250), value=520)
# 父爱如山
print(D.x) # 520

class C:
    def __init_subclass__(cls, value1, value2):
        print("父爱如山")
        cls.x = value1
        cls.y = value2
D = type('D', (C, ), dict(x=250), value1=520, value2=250)
# 父爱如山
print(D.x, D.y) # 520 250

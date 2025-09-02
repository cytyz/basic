# 元类（metaclass)
# 元类：创造类的模板，type本身就是元类，且是所有元类的父类，所以它能创造类
# 元类，这里是类和 type 间的桥梁
class MetaC(type):
    pass
class C(metaclass=MetaC):
    pass
c = C()
print(type(c)) # <class '__main__.C'>
print(type(C)) # <class '__main__.MetaC'>
print(type(MetaC)) # <class 'type'>


class MetaC(type):
    def __new__(mcls, name, bases, attrs): # 元类，类名，父类，属性和方法
        print("__new__() in MetaC")
        print(f'mcls={mcls}, name={name}, bases={bases}, attrs={attrs}')
        return type.__new__(mcls, name, bases, attrs)
    def __init__(cls, name, bases, attrs): # 类
        print("__init__ in MetaC")
        print(f'cls={cls}, name={name}, bases={bases}, attrs={attrs}')
        type.__init__(cls, name, bases, attrs)
# 创建完成之后调用
# __new__() in MetaC
# mcls=<class '__main__.MetaC'>, name=C, bases=(), attrs={'__module__': '__main__', '__qualname__': 'C', '__firstlineno__': 23, '__new__': <function C.__new__ at 0x000002063F2D87C0>, '__init__': <function C.__init__ at 0x000002063F2D8CC0>, '__static_attributes__': (), '__classcell__': <cell at 0x000002063F2E4A90: empty>}
# __init__ in MetaC
# cls=<class '__main__.C'>, name=C, bases=(), attrs={'__module__': '__main__', '__qualname__': 'C', '__firstlineno__': 23, '__new__': <function C.__new__ at 0x000002063F2D87C0>, '__init__': <function C.__init__ at 0x000002063F2D8CC0>, '__static_attributes__': (), '__classcell__': <cell at 0x000002063F2E4A90: MetaC object at 0x000002063F3A2DE0>}
class C(metaclass=MetaC):
    def __new__(cls):
        print("__new__() in C")
        return super().__new__(cls) # object 的 new 所有类的父类
    def __init__(self):
        print("__init__ in C")
c = C()
# __new__() in C
# __init__ in C

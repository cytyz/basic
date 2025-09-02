# 元类的应用

# ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 1.给所有的类添加 作者 属性
class MetaC(type):
    def __new__(mcls, name, bases, attrs):
        attrs["auther"] = "FishC"
        return type.__new__(mcls, name, bases, attrs)
class C(metaclass=MetaC):
    pass
class D(metaclass=MetaC):
    pass
c = C()
d = D()
print(c.auther) # FishC
print(d.auther) # FishC

class MetaC(type):
    def __init__(cls, name, bases, attrs):
        cls.auther = "FishC"
        type.__init__(cls, name, bases, attrs)
class C(metaclass=MetaC):
    pass
class D(metaclass=MetaC):
    pass
c = C()
d = D()
print(c.auther) # FishC
print(d.auther) # FishC

# ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 2.对类名的定义规范做限制
# 例如：让类的名字只支持大写字母开头
class MetaC(type):
    def __init__(cls, name, bases, attrs):
        if not name.istitle():
            raise TypeError("类名必须是大写字母开头")
        type.__init__(cls, name, bases, attrs)
# class mycls(metaclass=MetaC):
#     pass

# ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 3.修改对象的属性值
# 例如：让对象的所有属性值大写
class MetaC(type):
    # call 允许实例对象像函数一样被调用
    def __call__(cls, *args, **kwargs):
        new_args = [each.upper() for each in args if isinstance(each, str)]
        return type.__call__(cls, *new_args, **kwargs)
class C(metaclass=MetaC):
    def __init__(self, name):
        self.name = name
c = C('FishC')
print(c.name) # FISHC

# ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 4.限制类实例化时的传参方式
# 例如：让类在对象实例化时仅能传入 关键字参数
class MetaC(type):
    def __call__(cls, *args, **kwargs):
        if args:
            raise TypeError("仅支持关键字参数")
        return type.__call__(cls, *args, **kwargs)
class C(metaclass=MetaC):
    def __init__(self, name):
        self.name = name
# c = C('FishC') 报错
c = C(name='FishC')

# ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 5.禁止一个类被实例化
# 静态方法 类方法 直接通过类访问 是允许的
class NoInstances(type):
    # call 实例化时触发
    def __call__(cls, *args, **kwargs):
        raise TypeError("该类不允许直接实例化对象")
class C(metaclass=NoInstances):
    pass
# c = C() 报错
class C(metaclass=NoInstances):
    @staticmethod
    def static_ok():
        print("静态方法直接访问是允许的")
C.static_ok() # 静态方法直接访问是允许的
# c = C() 报错
class C(metaclass=NoInstances):
    @classmethod
    def class_ok(cls):
        print(f"静态方法直接访问是允许的 {cls.__name__}")
C.class_ok() # 静态方法直接访问是允许的 C

# ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 6.只允许实例化一个对象（实例出来的都是同一个对象）
# instance 指一个类的实例
class SimpleInstance(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        type.__init__(cls, *args, **kwargs)
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None: # 判断是否存在实例
            cls.__instance = type.__call__(cls, *args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance
class C(metaclass=SimpleInstance):
    pass
c1 = C()
c2 = C()
print(c1 is c2) # True
print(dir(C))
# ['_SimpleInstance__instance', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__']

# 类方法/静态方法
# 类方法： 用于绑定类的方法 使用 @classmethod 装饰器来实现
# 类方法可以帮助统计对象的数量，或通过创建列表来维护一个类对应的所有对象
# 静态方法： 在类里面定义一个不需要绑定的方法
class C:
    # 绑定实例对象
    def funA(self):
        print(self)
    # 绑定类
    @classmethod
    def funB(cls):
        print(cls)
c = C()
c.funA() # <__main__.C object at 0x000001B173056F90>
c.funB() # <class '__main__.C'>

# 统计对象的数量
class C:
    count = 0
    def __init__(self):
        # 类属性的 count +1
        C.count += 1
    @classmethod
    def get_count(cls):
        print(f"该类一共实例化了{cls.count}个对象")
c1 = C()
c2 = C()
c3 = C()
c3.get_count() # 该类一共实例化了3个对象


# 实例属性不会覆盖类属性
c3.count = 1
print(c3.count) # 1
c3.get_count() # 该类一共实例化了3个对象


# ————————————————————————————————————————————————————
# 静态方法
class C:
    @staticmethod
    def funC(): # 不需要任何参数进行绑定
        print("I Love FishC")
c = C()
c.funC() # I Love FishC
C.funC() # I Love FishC

class D:
    count = 0
    def __init__(self):
        # 类属性的 count +1
        D.count += 1
    @staticmethod
    def get_count():
        print(f"该类一共实例化了{D.count}个对象")
d1 = D()
d2 = D()
d3 = D()
d3.get_count() # 该类一共实例化了3个对象


# ——————————————————————————————————————————————————————————————————
class C:
    count = 0
    # 在涉及继承时可以自动将对应的类传进去
    @classmethod
    def add(cls):
        cls.count += 1
    def __init__(self):
        self.add()
    @classmethod
    def get_count(cls):
        print(f"该类一共实例化了{cls.count}个对象")

class D(C):
    count = 0

class E(C):
    count = 0

c1 = C()
d1, d2 = D(), D()
e1, e2, e3 = E(), E(), E()
c1.get_count() # 该类一共实例化了1个对象
d1.get_count() # 该类一共实例化了2个对象
e1.get_count() # 该类一共实例化了3个对象


# ————————————————————————————————————————————————————————————————————
class C:
    def funA(self):
        return self

    @classmethod
    def funB(cls):
        return cls
c = C()
print(isinstance(c.funA(), c.funB())) # True
# isinstance() 函数用于判断一个对象是否属于某个类。
# c.funA() 返回 self 对象，即对象 c；c.funB() 则返回类方法的参数，即类 C

# ————————————————————————————————————————————————————————————————————
# 类方法和静态方法区别
class Settings:
    config = {"theme": "dark", "language": "en"}

    @classmethod
    def update_config(cls, key, value):
        cls.config[key] = value

    @staticmethod
    def reset_config():
        Settings.config = {}


# 更新配置
Settings.update_config("theme", "light")
print(Settings.config)

# 重置配置
Settings.reset_config()
print(Settings.config)
# update_config() 定义为类方法，因为它需要访问并修改类属性 config，使用 cls.config 使其在继承时具有多态性。
# reset_config() 定义为静态方法，因为它不依赖于类或实例的状态，直接操作 Settings.config，无需通过 cls 参数，表示该操作与类的关联较弱，仅仅是对配置进行重置

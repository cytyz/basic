# 私有变量
# __x  name mangling 设置"私有变量"
# 在类实例化时，名字会被改变， 需要通过 c._C__x 获取该“私有变量“
# 方法名同理 d._D__func() 调用方法
# 不建议使用
class C:
    def __init__(self, x):
        self.__x = x
    def set_x(self, x):
        self.__x = x
    def get_x(self):
        return self.__x

c = C(250)
# print(c.__x)  “私有变量”无法获取到值
print(c.get_x())  # 250
c.set_x(1)
print(c.get_x())  # 1
print(c.__dict__)  # {'_C__x': 1}
print(c._C__x)  # 1 通过 _C__x 获取“私有变量”

class D:
    def __func(self):
        print("hello world")
d = D()
# d.__func() 无法直接调用该方法
d._D__func() # hello world

# 动态添加“私有变量”，但动态添加的名字并不会改变，依旧是 c.__y
c.__y = 250
print(c.__dict__) # {'_C__x': 1, '__y': 250}

# _单个下横线开头或结尾的变量  都是内部变量，最好不要去访问它


c.x = 1
# 通过动态添加键值对添加属性
c.__dict__["z"] = 2
print(c.__dict__) # {'_C__x': 1, '__y': 250, 'x': 1, 'z': 2}


# 类 实际上 字典
# 字典会消耗大量空间，当遇到固定空间的对象时可以使用 __slots__属性

class C:
    # 该类的对象仅有 x,y两个属性可用
    __slots__ = ['x', 'y']
    def __init__(self, x):
        self.x = x
c = C(250)
print(c.x) # 250
c.y = 520
print(c.y) # 520

# 当继承该类时，不会在子类生效，仍可以添加额外属性，放置于__dict__属性
class E(C):
    pass
e = E(250)
e.x = 1
e.y = 2
e.z = 3
print(e.__slots__) # ['x', 'y']
print(e.__dict__) # {'z': 3}

# 想要 __slots__ 属性真正发挥功效，要求必须在整个继承链条中，每个父类和子类均做出一致的实现
class C:
    # __slots__ = ["x", "y"] 当父类和子类同时限制时生效
    pass
class D(C):
    __slots__ = ["x", "y"]
    def __init__(self, x, y):
        self.x = x
        self.y = y
d = D(3, 4)
d.z = 5
print(d.__dict__) # {'z': 5}

# 构造函数
# __init__() 构造函数，在类中定义以个性化对象
class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def mul(self):
        return self.x * self.y
c = C(2, 3)
print(c.add()) # 5
print(c.mul()) # 6
print(c.__dict__) # {'x': 2, 'y': 3}


# 重写
# 子类重写父类的方法来覆盖为自己的方法
class A:
    def __init__(self):
        print("A")

class B1(A):
    def __init__(self):
        A.__init__(self)
        print("B1")

class B2(A):
    def __init__(self):
        A.__init__(self)
        print("B2")

class C(B1, B2):
    def __init__(self):
        B1.__init__(self)
        B2.__init__(self)
        print("C")
c = C()
# A
# B1
# A
# B2
# C
# A重复调用了

# super 父类，在多重继承时可以避免重复调用
# 自动根据 MRO 顺序查找， Method Resolution Order 方法解析顺序
class A:
    def __init__(self):
        print("A")

class B1(A):
    def __init__(self):
        super().__init__()
        print("B1")

class B2(A):
    def __init__(self):
        super().__init__()
        print("B2")

class C(B1, B2):
    def __init__(self):
        super().__init__()
        print("C")
c = C()
# A
# B2
# B1
# C

# 查看mro    mro() 或 __mro__
print(C.mro())
# [<class '__main__.C'>, <class '__main__.B1'>, <class '__main__.B2'>, <class '__main__.A'>, <class 'object'>]
print(B1.mro())
# [<class '__main__.B1'>, <class '__main__.A'>, <class 'object'>]

# property 类中的方法转换为属性，使得对属性的访问、赋值和删除操作可以通过调用相应的方法来执行
# class property(fget=None, fset=None, fdel=None, doc=None)
class C:
    def __init__(self):
        self._x = 250
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    # 创建一个属性对象，并将 getx、setx 和 delx 方法分别作为获取、设置和删除属性的操作
    # x 为 _x 的托管属性
    x = property(getx, setx, delx)

c = C()
print(c.x) # 250
c.x = 520
print(c.__dict__) # {'_x': 520}
del c.x
print(c.__dict__) # {}

class D:
    def __init__(self):
        self._x = 250
    def __getattr__(self, name):
        if name == "x":
            return self._x
        else:
            super().__getattr__(name)
    def __setattr__(self, name, value):
        if name == "x":
            super().__setattr__('_x', value)
        else:
            super().__setattr__(name, value)
    def __delattr__(self, name):
        if name == "x":
            super().__delattr__('_x')
        else:
            super().__delattr__(name)

d = D()
print(d.x) # 250
d.x = 520
print(d.__dict__) # {'_x': 520}
del d.x
print(d.__dict__) # {}

class E:
    def __init__(self):
        self._x = 250
    # 这里只有获取属性的方法，即只读，无法写入或删除
    @property
    def x(self):
        return self._x
e = E()
print(e.x) # 250

class E:
    def __init__(self):
        self._x = 250
    @property # 相当于 x = property(x)
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x
e = E()
print(e.x) # 250
e.x = 520
print(e.__dict__) # {'_x': 520}
del e.x
print(e.__dict__) # {}

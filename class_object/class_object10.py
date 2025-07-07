# 内置属性方法
# hasattr(ob, str) 是否有 str 这个属性
# getattr(ob, str) 获取 str 这个属性  __getattribute__()
# __getattr__() 当获取不存在的属性时触发
# setattr(ob, str) 给 str 这个属性赋值 __setattr__()
# delattr(ob, str) 删除 str这个属性 __delattr__()
class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # __age 私有变量

c = C("小甲鱼", 18)
print(hasattr(c, "name")) # True
print(getattr(c, "name")) # 小甲鱼
print(getattr(c, "_C__age")) # 18
setattr(c, "_C__age", 19)
print(getattr(c, "_C__age")) # 19
delattr(c, "_C__age")
print(hasattr(c, "_C__age")) # False

# ——————————————————————————————————————————————————————
# __getattribute__()
class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __getattribute__(self, attrname):
        print("截取")
        return super().__getattribute__(attrname)

c = C("小甲鱼", 18)
print(getattr(c, "name"))
# 截取
# 小甲鱼

# ——————————————————————————————————————————————————————
# __getattr__() 当获取对象不存在时触发
class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __getattribute__(self, attrname):
        print("截取")
        return super().__getattribute__(attrname)

    def __getattr__(self, attrname):
        if attrname == "FishC":
            print("I love FishC")
        else:
            raise AttributeError(attrname)
c = C("小甲鱼", 18)
print(c.FishC)
# 截取
# I love FishC
# None
print(c.name)
# 截取
# 小甲鱼

# ——————————————————————————————————————————————————————
# __setattr__()
class D:
    def __setattr__(self, name, value):
        self.__dict__[name] = value
d = D()
d.name = "小甲鱼"
print(d.name) # 小甲鱼

class D:
    def __setattr__(self, name, value):
        return super().__setattr__(name, value)
d = D()
d.name = "小甲鱼"
print(d.name) # 小甲鱼

# ——————————————————————————————————————————————————————
# __delattr__()
class D:
    def __setattr__(self, name, value):
        self.__dict__[name] = value
    def __delattr__(self, name):
        del self.__dict__[name]
d = D()
d.name = "小甲鱼"
del d.name
print(d.__dict__) # {}

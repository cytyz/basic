# 绑定
# self 将实例对象和类进行绑定
class C:
    y = 200
    def get_self(self):
        print(self)

c = C()
c.x = 100
# c.__dict__ 查看对象私有属性，公有属性不会显示
print(c.__dict__) # {'x': 100}
c.y = 300
print(c.__dict__) # {'x': 100, 'y': 300}


# 在类中给实例化对象赋予私有属性
class C:
    def set_x(self, x):
        self.x = x
c = C()
print(c.__dict__) # {}
# 在方法中传入参数
c.set_x(100)
print(c.x) # 100
print(c.__dict__) # {'x': 100}


# __init__ 初始化参数
class C:
    def __init__(self, x):
        self.x = x
# 直接在创建对象时传入参数
c = C(10)
print(c.x)  # 10

# 类还可以作为字典来使用，通过对象来作为字典使用更好
class F:
    pass
f = F()
f.x = 1
f.y = "FishC"
f.z = [1, 2, 3]
print(f.x, f.y, f.z) # 1 FishC [1, 2, 3]


# 字典
d = {}
d["x"] = 1
d["y"]= "FishC"
d["z"]= [1, 2, 3]
print(d["x"], d["y"], d["z"]) # 1 FishC [1, 2, 3]


x = 123
class C:
    x = 100
    def get_x(self):
        print(f"x = {x}")
        print(f"self.x = {self.x}")
c = C()
c.get_x()
# x = 123
# self.x = 100
c.x = 250
c.get_x()
# x = 123
# self.x = 250

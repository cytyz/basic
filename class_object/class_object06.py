# 多态
# 指函数可以根据不同的对象执行不同的操作
# 类的继承与重写方法：类与对象中实现多态的一种方式
class Shape: # 形状
    def __init__(self, name):
        self.name = name
    def area(self):
        pass

class Square(Shape): # 正方形
    def __init__(self, length):
        super().__init__('正方形')
        self.length = length
    def area(self):
        return self.length * self.length

class Circle(Shape): # 圆形
    def __init__(self, radius): # 半径
        super().__init__('圆形')
        self.radius = radius
    def area(self):
        return self.radius * self.radius * 3.14

class Triangle(Shape): # 三角形
    def __init__(self, base, height): # 底和高
        super().__init__('三角形')
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height / 2

s = Square(5)
c = Circle(6)
t = Triangle(3, 4)
print(s.name, s.area()) # 正方形 25
print(c.name, c.area()) # 圆形 113.04
print(t.name, t.area()) # 三角形 6.0

# —————————————————————————————————————————————————————————
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"我是一只猫咪，我叫{self.name}，今年{self.age}岁")
    def say(self):
        print("喵~")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"我是一只修狗，我叫{self.name}，今年{self.age}岁")
    def say(self):
        print("汪~")

class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"我是一只猪，我叫{self.name}，今年{self.age}岁")
    def say(self):
        print("oink~")

c = Cat("web", 4)
d = Dog("布布", 7)
p = Pig("大肠", 5)

# 给函数传递不同的对象
# 鸭子类型 不需要关注传入的是什么类型，只要它符合这里面的 intro 和 say 方法， 它就属于这个类型
def animal(x):
    x.intro()
    x.say()

animal(c)
# 我是一只猫咪，我叫web，今年4岁
# 喵~
animal(d)
# 我是一只修狗，我叫布布，今年7岁
# 汪~
animal(p)
# 我是一只猪，我叫大肠，今年5岁
# oink~

class Bicycle:
    def intro(self):
        print("走过多远的路")
    def say(self):
        print("继续走")
b = Bicycle()
animal(b)
# 走过多远的路
# 继续走

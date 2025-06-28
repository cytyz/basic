# Mixin Mix-in 混入，临时加入 一种设计模式
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f"我叫{self.name}，今年{self.age}岁")

# 临时想给 pig 添加一个飞行的技能
class FlyMixin:
    def fly(self):
        print("我也会飞了")

# 多继承
class Pig(FlyMixin, Animal):
    def special(self):
        print("我的技能是拱白菜")

p = Pig("大肠", 5)
p.say() # 我叫大肠，今年5岁
p.special() # 我的技能是拱白菜
p.fly() # 我也会飞了


# ————————————————————————————————————————————————————————————
# super 与 MRO顺序
# 当 super 无直接父类时： 会根据对象直接对应的类的 MRO顺序 来找寻其“父类”
# self 也取决于当前对象
class Displayer:
    def display(self, message):
        print(message)

class LoggerMixin:
    def log(self, message, filename="logfile.txt"):
        with open(filename, "w") as f:
            f.write(message)

    def display(self, message):
        super().display(message)
        self.log(message)

class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, "subclasslog.txt")

subclass = MySubClass()
subclass.display("This is a test")

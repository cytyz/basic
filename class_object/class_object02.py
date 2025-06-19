# 继承
# 在类中定义类属性，并不会被类方法直接通过变量名访问到，需要通过 self.属性 来访问
class A:
    x = 520
    def hello(self):
        print("hello,我是A")

# class B(A) B类 继承 A类
class B(A):
    pass

b = B()
b.hello() # hello,我是A

class C(A):
    x = 888
    def hello(self):
        print("hello,我是C")
c = C()
print(c.x) # 888
c.hello() # hello,我是C

# isinstance() 判断对象是否属于某个类
print(isinstance(c, C)) # True
print(isinstance(c, A)) # True

# issubclass() 判断一个类是否为某个类的子类
print(issubclass(C, A)) # True

class B:
    x = 888
    y = 666
    def hello(self):
        print("hello,<UNK>B")

# 同时继承两个类，访问顺序从左到右
class C(A, B): pass
c = C()
print(c.x) # 520
print(c.y) # 666
c.hello() # hello,我是A


# 组合
# 将多个类的实例放到一个类中
class Turtle:
    def say(self):
        print("乌龟")

class Cat:
    def say(self):
        print("喵")

class Dog:
    def say(self):
        print("汪")

# 将多个类的实例化对象放到一个类中
class Garden:
    t = Turtle()
    cat = Cat()
    dog = Dog()
    def say(self):
        self.t.say()
        self.cat.say()
        self.dog.say()

g = Garden()
g.say()
# 乌龟
# 喵
# 汪

# 可以在子类中修改父类的属性
class D(B):
    B.y = 111
print(B.y) # 111

# 对象
# 对象 = 属性 + 方法
# 封装 创建对象之前将相关的属性和方法通过类打包到一起
# 创建对象需要先创建一个类class，再创建对象
# 创建类
class Turtle: # 类命名以大写字母开头
    head = 1
    eyes = 2
    legs = 4
    shell = True # 壳

    # self 实例对象本身，调用时通过self传递对象信息
    # self 在对象访问方法时自动进行传递，不需要显式传递
    def crawl(self): # 爬
        print("爬")

    def run(self):
        print("跑")

    def bite(self):
        print("咬")

    def eat(self):
        print("吃")

    def sleep(self):
        print("睡觉")

# 创建对象
t1 = Turtle()
# 调用类的属性，方法
print(t1.head) # 1
t1.eat() # 吃


t2 = Turtle()
# 改变或创建对象特有属性和方法
t2.legs = 3
print(t2.legs) # 3
t2.mouth = 1
print(t2.mouth) # 1


# dir(t)查看属性
print(dir(t1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'bite', 'crawl', 'eat', 'eyes', 'head', 'legs', 'run', 'shell', 'sleep']
print(dir(t2))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'bite', 'crawl', 'eat', 'eyes', 'head', 'legs', 'mouth', 'run', 'shell', 'sleep']


# 基于统一个类的两个对象，但它们并不相同，也并不相等。但它们所拥有的属性，确都是来自于同一个类的

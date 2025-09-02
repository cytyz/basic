# 抽象基类

# 元类可以 只允许实例化一个对象（实例出来的都是同一个对象）
# 符合的如：抽象基类，Mixin（非抽象基类） 为子类提供一些额外功能的实现（不希望被直接实例化）

# 抽象基类：1.不能被直接实例化，只能被继承使用；2.子类必须实现抽象基类中定义的抽象方法
# 如水果类，这种类就不能直接实现，需要作为抽象类
# 抽象基类，使用abc模块--AbstractBaseClass, 主要使用 ABCMeta 和 abstractmethod
# 规范子类，保证子类有相同方法，相同属性，及时检测出问题
from abc import ABCMeta, abstractmethod
class Fruit(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def good_for_health(self):
        pass
class Banana(Fruit):
    def good_for_health(self):
        print("只要吃香蕉，人就会变得开心")
banana = Banana("香蕉")
banana.good_for_health() # 只要吃香蕉，人就会变得开心

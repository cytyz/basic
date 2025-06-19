# 创建类
# 设计一个 Person 类，该类有 name 和 age 两个属性（分别用于指定对象的姓名和年龄），该类还有 set_name()、set_age()、get_name() 和 get_age() 四个方法（分别用于设置、获取对象的姓名和年龄）
class Person:
    name = None
    age = None
    def set_name(self):
        self.name = input("请输入名字：")

    def set_age(self):
        self.age = input("请输入年龄：")

    def get_name(self):
        if self.name:
            return self.name
        else:
            print("名字未设置")

    def get_age(self):
        if self.age:
            return self.age
        else:
            print("年龄未设置")

# 设计一个 Rectangle 类，该类有 length 和 width 两个属性（分别用于指定长方形的长度和宽度），该类还有 set_length()、set_width()、get_ perimeter() 和 get_area() 四个方法（分别用于设置长方形的长和宽，以及获取长方形的周长和面积）
class Rectangle:
    length = None
    width = None

    def set_length(self):
        self.length = input("请输入矩形的长度：")

    def set_width(self):
        self.width = input("请输入矩形的宽度：")

    def get_perimeter(self):
        if not self.length:
            self.set_length()

        if not self.width:
            self.set_width()

        return (self.length + self.width) * 2

    def get_area(self):
        if not self.length:
            self.set_length()

        if not self.width:
            self.set_width()

        return self.length * self.width

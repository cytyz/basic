# __call__(self[,args...] 可以像调用函数那样调用对象调用对象
class C:
    def __call__(self):
        print("嗨~")
c = C()
c() # 嗨~
class C:
    def __call__(self, *args, **kwargs):
        print(f"位置参数 -> {args}\n关键字参数 -> {kwargs}")
c = C()
c(1, 2, 3, x = 250, y = 520)

class Power:
    def __init__(self, exp):
        self.exp = exp
    def __call__(self, base):
        return base ** self.exp
square = Power(2)
print(square(3)) # 9

cube = Power(3)
print(cube(3)) # 27


# ——————————————————————————————————————————————————————
# __str__(self) 将参数转换为字符串对象
# __repr__(self) 将对象转换为程序可执行的字符串，可以作为 str() 的代偿
# eval 将参数去引号后执行
print(str("FishC")) # FishC
print(repr("FishC")) # 'FishC'
print(eval('1 + 2')) # 3

class C:
    def __repr__(self):
        return "I Love FishC"
c = C()
print(repr(c)) # I Love FishC
print(str(c)) # I Love FishC
cs = [C(), C(), C()]
for each in cs:
    print(each)
# I Love FishC
# I Love FishC
# I Love FishC
print(cs) # [I Love FishC, I Love FishC, I Love FishC]

class C:
    def __str__(self):
        return "I Love FishC"
cs = [C(), C(), C()]
for each in cs:
    print(each)
# I Love FishC
# I Love FishC
# I Love FishC
print(cs) # [<__main__.C object at 0x000001F4203F70E0>, <__main__.C object at 0x000001F4205D51D0>, <__main__.C object at 0x000001F4205D5310>]
class C:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return f"data = {self.data}"
    def __repr__(self):
        return f"C({self.data})"
    def __add__(self, other):
        self.data += other
c = C(250)
print(c) # data = 250
c + 250
print(c)  # data = 500

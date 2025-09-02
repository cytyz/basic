# 代偿
# 该部分无法工作，其他部分代替它来工作
# __contains__(self, item) 实现成员关系的检测 对应运算符：in/not in
class C:
    def __init__(self, data):
        self.data = data
    def __contains__(self, item):
        print("嗨~", end=" ")
        return item in self.data
c = C([1, 2, 3, 4, 5])
print(3 in c) # 嗨~ True
print(6 in c) # 嗨~ False

# ————————————————————————————————————————————————————————————
# 使用in/not in时，会调用__contains__(self, item)，若无则找__iter__和__next__，若仍无则找__getitem__()
class C:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        print("iter", end="->")
        self.i = 0
        return self
    def __next__(self):
        print("next", end="->")
        if self.i == len(self.data):
            raise StopIteration
        item = self.data[self.i]
        self.i += 1
        return item
c = C([1, 2, 3, 4, 5])
print(3 in c) # iter->next->next->next->True
print(6 in c) # iter->next->next->next->next->next->next->False

# ————————————————————————————————————————————————————————————
class C:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        print("getitem", end="->")
        return self.data[index]
c = C([1, 2, 3, 4, 5])
print(3 in c) # getitem->getitem->getitem->True
print(6 in c) # getitem->getitem->getitem->getitem->getitem->getitem->False

# ————————————————————————————————————————————————————————————
# 布尔测试
# 遇到bool() 会先找 __bool__() ，若无则找 __len__()(返回值不为0，则为True)
class D:
    def __bool__(self):
        print("Bool", end="->")
        return True
d = D()
print(bool(d)) # Bool->True

class D:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        print("len", end="->")
        return len(self.data)
d = D("FishC")
print(bool(d)) # len->True

# ————————————————————————————————————————————————————————————
# 比较方法魔法方法（magic method）
# < __lt__(self, other)
# <= __le__(self, other)
# > __gt__(self, other)
# >= __ge__(self, other)
# == __eq__(self, other)
# != __ne__(self, other)
class S(str):
    def __lt__(self, other):
        return len(self) < len(other)
    def __gt__(self, other):
        return len(self) > len(other)
    def __eq__(self, other):
        return len(self) == len(other)
s1 = S("FishC")
s2 = S("fishc")
print(s1 < s2) # False
print(s1 > s2) # False
print(s1 == s2) # True

# ————————————————————————————————————————————————————————————
# 希望某个方法魔法方法不生效时，设置为None
class S(str):
    def __lt__(self, other):
        return len(self) < len(other)
    def __gt__(self, other):
        return len(self) > len(other)
    def __eq__(self, other):
        return len(self) == len(other)
    __le__ = None
    __ge__ = None
    __ne__ = None
s1 = S("FishC")
s2 = S("fishc")
# print(s1 <= s2) # 报错

class C:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        print("iter", end="->")
        self.i = 0
        return self
    def __next__(self):
        print("next", end="->")
        if self.i == len(self.data):
            raise StopIteration
        item = self.data[self.i]
        self.i += 1
        return item
    __contains__ = None
c = C([1, 2, 3, 4, 5])
# print(3 in c) # 阻止了__contains__后明确不希望检测成员关系，直接报错，不会再继续往后寻找代偿方法

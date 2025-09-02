# 索引，切片，迭代协议
# 索引：当被索引时，调用 __getitem__(self, index) 支持单下标，还支持切片     相关的获取操作都会被拦截
# 为索引或切片赋值时，调用 __setitem__(self, index， value)
# ——————————————————————————————————————————————————————————
# __getitem__(self, index)
class C:
    def __getitem__(self, index):
        print(index)
c = C()
c[2] # 2
c[2:8] # slice(2, 8, None) slice内置BIF，切片调用

s = "I love FishC"
print(s[2:6]) # love
print(s[slice(2, 6)]) # love
print(s[7:]) # FishC
print(s[slice(7, None)]) # FishC
print(s[::4]) # Ivi
print(s[slice(None, None, 4)]) # Ivi

# ——————————————————————————————————————————————————————————
# __setitem__(self, index， value)
class D():
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index] = value
d = D([1, 2, 3, 4, 5])
print(d[1]) # 2
d[1] = 1
print(d[1]) # 1
d[2:4] = [2, 3]
print(d[:]) # [1, 1, 2, 3, 5]

# ——————————————————————————————————————————————————————————
# __getitem__也能拦截for语句
class D():
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index] * 2
d = D([1, 2, 3, 4, 5])
for i in d:
    print(i, end=" ") # 2 4 6 8 10
print()

# ——————————————————————————————————————————————————————————
# for 语句真正的拦截语句：__iter__(self) __next__(self)
# 可迭代对象都有__iter__()方法，调用它会变成迭代器，可以使用 next 方法
# for 语句做的第一步操作，是将对象传入内置函数 iter() 中，并由此拿到一个相应的迭代器。
# 因为只有拿到这个迭代器，才能拥有所需的 __next__() 方法。
# 第二步就是利用 __next__() 方法进行真正的迭代操作
x = [1, 2, 3, 4, 5]
for i in x:
    print(i, end=" ") # 1 2 3 4 5
print()
# 相当于：
_ = iter(x)
while True:
    try:
        i = _.__next__()
    except StopIteration:
        break
    print(i, end=" ") # 1 2 3 4 5
print()

# ——————————————————————————————————————————————————————————
# 迭代器类
class Double:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value * 2
d = Double(1, 5)
for i in d:
    print(i, end=" ") # 2 4 6 8 10
print()

matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

# 创建两个 slice 对象
rows = slice(1, 4) # 空白一：对应于切片操作 [1:4]
cols = slice(2, None) # 空白二：对应于切片操作 [2:]

# 使用切片操作获取子矩阵
sub_matrix1 = [row[cols] for row in matrix[rows]]
# 使用 slice 对象获取子矩阵
sub_matrix2 = [row.__getitem__(cols) for row in matrix.__getitem__(rows)]

print(sub_matrix1)
print(sub_matrix2)

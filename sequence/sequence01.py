# 序列
x = "FishC"
y = [1, 2, 3]
# 删除 x, y这个变量，使其不再指向任何对象
del x, y
x = [1, 2, 3, 4, 5]
del x[1:4]
print(x)
# [1, 5]
y = [1, 2, 3, 4 ,5]
y[1:4] = []
print(y)
# [1, 5]
x = [1, 2, 3, 4, 5]
del x[::2]
print(x)
# [2, 4]

# max, min 按Ascii值对字母进行排序
print(max("FiShC"))
# i
s = []
# default 当调用函数时，如果没有提供该参数的值，将使用默认值
print(min(s, default="啥都没有"))
# 啥都没有

# len读取的长度不能超过pow(2,63) - 1

s = [1, 2, 3, 0, 6]
print(sum(s))
# 12
print(sum(s, start=100))
# 112

# sorted 排序但不改变，并给出返回值
# .sort 排序且改变，但不给出返回值
print(sorted(s), s)
# [0, 1, 2, 3, 6] [1, 2, 3, 0, 6]
s.sort()
print(s)
# [0, 1, 2, 3, 6]
# key  关键值，作为根据 如排序依据
t = ["FishC", "Apple", "Book", "Banana", "Pen"]
print(sorted(t))
# ['Apple', 'Banana', 'Book', 'FishC', 'Pen']
print(sorted(t, key=len))
# ['Pen', 'Book', 'FishC', 'Apple', 'Banana']

# reversed 返回的是一个迭代器对象，需要list进行转换才能正常使用
print(reversed(t))
# <list_reverseiterator object at 0x000001D1AEC65CC0>
print(list(reversed(t)))
# ['Pen', 'Banana', 'Book', 'Apple', 'FishC']

print(list(reversed(sorted("FishC520"))))
# ['s', 'i', 'h', 'F', 'C', '5', '2', '0']

# all() 判断是否全部为真 any() 是否存在某个元素的值为真
x = [1, 1, 0]
y = [1, 1, 9]
print(all(x), all(y), any(x), any(y))
# False True True True

# ————————————————————————————————————————————
# enumerate() 用于返回一i个枚举对象，它的功能就是将可迭代对象中的每个元素及从0开始的序号共同构成一个二元组的列表
print(list(enumerate(x)))
# [(0, 1), (1, 1), (2, 0)]
print(list(enumerate(x, start=10)))
# [(10, 1), (11, 1), (12, 0)]

# zip() 用于创建一个聚合多个可迭代对象的迭代器
# 它会将作为参数传入的每个可迭代对象依次组合成元组，即第i个元组包含来自每个参数的第i个元素
# zip 当长度不一时，以最短的为准，长的会舍弃掉
# 若要保留长的部分，需要调用itertools
print(list(zip(x, y)))
z = [1, 4, 5]
print(list(zip(x, y, z)))
# [(1, 1, 1), (1, 1, 4), (0, 9, 5)]
z = "FishC"
print(list(zip(x, y, z)))
# [(1, 1, 'F'), (1, 1, 'i'), (0, 9, 's')] 舍弃了hC
import itertools
zipped = itertools.zip_longest(x, y, z)
print(list(zipped))
# [(1, 1, 'F'), (1, 1, 'i'), (0, 9, 's'), (None, None, 'h'), (None, None, 'C')]

# map() 它会根据提供的函数对指定的可迭代对象的每个元素进行运算，并将 返回运算结果 的迭代器
# 和zip一样，以最短的为准
mapped = map(ord, "FishC")
print(list(mapped))
# [70, 105, 115, 104, 67]
mapped = map(pow, [2, 3, 10], [5, 2, 3])
print(list(mapped))
# [32, 9, 1000]
mapped = map(max, [1, 3, 5], [2, 2, 2], [0, 3, 9, 8])
print(list(mapped))
# [2, 3, 9] 舍弃了8

# filter() 它会根据提供的函数对指定的可迭代对象的每个元素进行运算，并将 运算结果为真的元素 以迭代器的形式返回
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))
# [2, 4]
print(list(filter(str.islower, "FishC")))
# ['i', 's', 'h']

# 迭代器与可迭代对象
# 迭代器一定是一个可迭代对象，可迭代对象可以重复使用，而迭代器是一次性的，临时存储
mapped = map(ord, "FishC")
print(list(mapped))
# [70, 105, 115, 104, 67]
print(list(mapped))
# []
# iter 将可迭代对象转换成一次性的迭代器， 所有的可迭代对象都可以转换成一次性的迭代器
# next 逐个将迭代器中的元素提取出来，使用一次提取一个
x = [1, 2, 3]
y = iter(x)
print(type(x), type(y))
# <class 'list'> <class 'list_iterator'>
print(next(y, "元素提取完毕"))
# 1
print(next(y, "元素提取完毕"))
# 2
print(next(y, "元素提取完毕"))
# 3
print(next(y, "元素提取完毕"))
# 元素提取完毕

matrix = [[1, 3, 2],
          [5, 4, 6],
          [8, 7, 9]]
mapped = map(sorted, matrix)
print(list(mapped))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list(filter(str.islower, "FishC")))
# ['i', 's', 'h']
print([i for i in "FishC" if i.islower()])
# ['i', 's', 'h']

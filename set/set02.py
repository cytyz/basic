# 可变集合的增删查改
# 可变与不可变集合
# 可变 set()
# 不可变 frozenset() 可哈希， 状态不会改变，线程安全
x = frozenset("FishC")
print(x)
# frozenset({'F', 'i', 'h', 'C', 's'})

# 仅适用于 可变集合 set 的方法
# 改 update中的，迭代获取其中的每一个字符
# s.update(*others)  (union_update) 将others更新到s中 无返回值  others:支持多个参数 other:仅支持一个参数
# s.intersection_update(*others) 将交集更新到s中
# s.difference_update(*others) 将差集更新到s中
# s.symmetric_difference_update(*others) 将对称差集更新到s中
s = set("FishC")
s.update([1, 1], "23")
print(s)
# {'F', 'h', 1, '2', 'C', '3', 'i', 's'}
s.intersection_update("FishC")
print(s)
# {'h', 'F', 's', 'C', 'i'}
s.difference_update("Php", "Python")
print(s)
# {'F', 'C', 'i', 's'}
s.symmetric_difference_update("Python")
print(s)
# {'C', 'o', 't', 'h', 'F', 'P', 'i', 'n', 's', 'y'}

# 增
# add(elem) add中的  将改元素直接添加到集合中
s.add("45")
print(s)
# {'F', 'y', 'i', 'P', 'o', 't', 'n', '45', 'C', 'h', 's'}

# 删
# remove(elem) 删除的元素不存在则抛出异常
# discard(elem) 删除的元素不存在静默处理
# pop() 随机删除并返回集合中的一个元素
s.remove("45")
print(s)
# {'s', 'o', 'y', 'P', 'h', 'i', 'n', 't', 'C', 'F'}
s.discard("F")
print(s)
# {'s', 'o', 'y', 'P', 'h', 'i', 'n', 't', 'C'}
s.pop()
print(s)
# {'o', 'y', 'P', 'h', 'i', 'n', 't', 'C'}

# 清空
# clear()
s.clear()
print(s)
# set()


# 字典的键和集合的元素：可哈希 哈希值在它的生命周期不变
# python中大部分不可变的对象都是可哈希的（字符串，元组，不可变的集合（frozenset）），可变的都是不可哈希的(列表， 字典，可变的集合（set）)
# 故字典的键和集合的元素可以是：字符串，元组，不可变的集合（frozenset）
# hash(object) 获取对象的哈希值
# 对一个整数求哈希值，这个值等于它本身
# 两个对象值相等，哈希值相同
print(hash(1))
# 1
print(hash(1.0))
# 1
print(hash(1.001))
# 2305843009213441
print(hash("FishC"))
# 3210646892617875685
print(hash((1, 2, 3)))
# 529344067295497451
# 嵌套的集合
x = frozenset((1, 2 ,3))
print(x)
# frozenset({1, 2, 3})
y = {x, 4, 5}
print(y)
# {frozenset({1, 2, 3}), 4, 5}

s1 = set([1, 1, 2, 3, 5])
s2 = frozenset([1, 1, 2, 3, 5])
print(s1 == s2)
# True

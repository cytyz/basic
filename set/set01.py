# 集合
# 不重复，无序，无法用下标访问 集合可以被看作是一个只有键没有值的字典
# 创建
x = {"FishC", "Python"}
print(x)
# {'Python', 'FishC'}
x = {i for i in "FishC"}
print(x)
# {'C', 'F', 'h', 's', 'i'}
x = set("FishC")
print(x)
# {'F', 's', 'i', 'C', 'h'}

print("C" in x)
# True

# x.isdisjoint(b) x和b是否没有交集
# x.issubset(b)  x是否是b的子集
# x.issuperset(b)  x是否是b的超集（A包含B，B是A的子集，A是B的超集）
print(x.isdisjoint(set("Python")))
# False
print(x.issubset("FishC.com.cn"))
# True
print(x.issuperset("Fish"))
# True

# x.union(b) 生成x和b的并集
# x.intersection(b) 生成x和b的交集
# x.difference(b) 生成x和b的差集（属于x但不属于b的部分）
# x.symmetric_difference(b) 生成x和b的对称差集（并集 - 交集）
print(x.union({"Fishc", 1, 2, 3}, "Fishc.com"))
# {'C', 1, 2, 3, 's', 'c', 'm', 'F', 'o', 'Fishc', '.', 'i', 'h'}
print(x.intersection("fishc"))
# {'s', 'i', 'h'}
print(x.difference("fishc"))
# {'F', 'C'}
print(x.symmetric_difference("fishc"))
# {'c', 'f', 'C', 'F'}

# x <= b x是否是b的子集    x < b x是否是b的真子集
# x >= b x是否是b的超集（A包含B，B是A的子集，A是B的超集）    x > b x是否是b的真超集
# x | b  生成 x和b 的并集
# x & b  生成 x和b 的交集
# x - b  生成 x和b 的差集（属于x但不属于b的部分）
# x ^ b  生成x和b的对称差集（并集 - 交集）
print(x <= set("FishC.com.cn"))
# True
print(x >= set("Fish"))
# True
print(x | {1, 2, 3} | set("Python"))
# {'C', 1, 2, 3, 'y', 'h', 'F', 'i', 's', 'o', 't', 'P', 'n'}
print(x & set("Fish"))
# {'i', 's', 'h', 'F'}
print(x & {"Fishc"})
# set()    {'F', 's', 'i', 'C', 'h'} 和 {"Fishc"} 交集为空集
print(x - set("Fish"))
# {'C'}
print(x ^ set("Fishc"))
# {'c', 'C'}

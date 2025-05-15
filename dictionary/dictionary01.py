# 字典{“key”:"value"}
y = {"吕布":"口口布", "关羽":"关习习"}
print(y["吕布"])
# 口口布

y["刘备"] = "刘baby"
print(y)
# {'吕布': '口口布', '关羽': '关习习', '刘备': '刘baby'}

# 创建字典的6种方法
# 1 直接赋值
a = {"吕布":"口口布", "关羽":"关习习", "刘备":"刘Baby"}
# 2 dict
b = dict(吕布="口口布", 关羽="关习习", 刘备="刘Baby")
# 3 dict中列表元素一一对应，类似zip
c = dict([("吕布", "口口布"), ("关羽", "关习习"), ("刘备", "刘Baby")])
# 4 dict + 直接赋值
d = dict({"吕布":"口口布", "关羽":"关习习", "刘备":"刘Baby"})
# 5 4+2混合
e = dict({"吕布":"口口布", "关羽":"关习习"}, 刘备="刘Baby")
# 6 dict +zip
f = dict(zip(["吕布","关羽","刘备"], ["口口布", "关习习", "刘Baby"]))
print(a == b == c == d == e == f)
# True

# 增删查改
# fromkeys(iterable[, value])
# 删 pop(key[, default]), 有返回值
# popitem 删除最后一个元素 有返回值
# 改 update
# 查 get(key[, default])
# setdefault(key, value) 查找key，若找到则返回值，找不到则将 key:value 加入字典中

# 快速初始化字典
x = dict.fromkeys("Fish", 250)
print(x)
# {'F': 250, 'i': 250, 's': 250, 'h': 250}
x["F"] = 70
print(x)
# {'F': 70, 'i': 250, 's': 250, 'h': 250}
x["C"] = 67
print(x)
# {'F': 70, 'i': 250, 's': 250, 'h': 250, 'C': 67}

# 删 pop(key[, default]), 有返回值
x.pop("C","不存在该值")
print(x)
# {'F': 70, 'i': 250, 's': 250, 'h': 250}
# popitem 删除最后一个元素 有返回值
x.popitem()
print(x)
# {'F': 70, 'i': 250, 's': 250}
del x["i"]
print(x)
# {'F': 70, 's': 250}

x.clear()
print(x)
# {}

z = dict()
z["a"] = 1, 2, 3, 4, 5
print(z, z["a"], z["a"][1])
# {'a': (1, 2, 3, 4, 5)} (1, 2, 3, 4, 5) 2

d = {}.fromkeys("吕布", 999)
print(d)
# {'吕': 999, '布': 999}

a = {"小甲鱼":"You are my super star."}
b = a
a.clear()
print(b)
# {}

d = dict.fromkeys("FishC")
print(d)
# {'F': None, 'i': None, 's': None, 'h': None, 'C': None}
d["s"] = 115
print(d)
# {'F': None, 'i': None, 's': 115, 'h': None, 'C': None}

# update 改
d.update({"i":105, "h":104})
print(d)
# {'F': None, 'i': 105, 's': 115, 'h': 104, 'C': None}
d.update(F=70, C=67)
print(d)
# {'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67}

# get(key[, default]) 查
# setdefault(key, value) 查找key，若找到则返回值，找不到则将 key:value 加入字典中
print(d.get("c", "这里没有c"), d.get("C"))
# 这里没有c 67
print(d["C"]) if "C" in d else print("这里没有c")
# 67

# setdefault(key, value) 查找key，若找到则返回值，找不到则将 key:value 加入字典中
print(d.setdefault("c", "code"))
# code
print(d)
# {'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67, 'c': 'code'}

# items(), keys(), value() 键值对，键和值三者的视图对象，随字典数据变化而变化
items = d.items()
keys = d.keys()
values = d.values()
print(items, keys, values)
# dict_items([('F', 70), ('i', 105), ('s', 115), ('h', 104), ('C', 67), ('c', 'code')]) dict_keys(['F', 'i', 's', 'h', 'C', 'c']) dict_values([70, 105, 115, 104, 67, 'code'])

e = d.copy()
print(e)
# {'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67, 'c': 'code'}
print(len(d))
# 6

print("C" in d, "c" not in d)
# True False
print(list(d))
# ['F', 'i', 's', 'h', 'C', 'c'] 输出所有的键构成的列表
print(list(d.values()))
# [70, 105, 115, 104, 67, 'code'] 输出所有的值构成的列表

# iter, next 迭代器
e = iter(d)
print(next(e))
# F
print(next(e))
# i

# reversed python3.8
print(list(reversed(d)))
# ['c', 'C', 'h', 's', 'i', 'F']

# 字典嵌套
d = {"吕布":{"语文":60, "数学":70, "英语":80}, "关羽":{"语文":70, "数学":70, "英语":60}}
print(d)
# {'吕布': {'语文': 60, '数学': 70, '英语': 80}, '关羽': {'语文': 70, '数学': 70, '英语': 60}}
print(d["吕布"]["数学"])
# 70
d = {"吕布":[60, 70, 80], "关羽":[70, 80, 90]}
print(d["吕布"][1])
# 70

# 字典推导式
d = {"F":70, "i":105, "s":115, "h":104, "C":67}
b = {v:k for k, v in d.items()}
print(b)
# {70: 'F', 105: 'i', 115: 's', 104: 'h', 67: 'C'}

d = {x:y for x in [1, 3, 5] for y in [2, 4,  6]}
print(d)
# {1: 6, 3: 6, 5: 6} 每循环一次，值替换一次

d = {"小甲鱼":"千年王八，万年龟。"}
e = d.copy()
d["小甲鱼"] = "666"
print(d, e)
# {'小甲鱼': '666'} {'小甲鱼': '千年王八，万年龟。'} 字符串不可变

d = {"小甲鱼":{"数学":99, "英语":88, "语文":101}}
e = d.copy()
d["小甲鱼"]["语文"] = 100
print(d, e)
# {'小甲鱼': {'数学': 99, '英语': 88, '语文': 100}} {'小甲鱼': {'数学': 99, '英语': 88, '语文': 100}}

d = {}
d[1] = "千年王八"
d[1.0] = "万年龟"
print(d)
# {1: '万年龟'}

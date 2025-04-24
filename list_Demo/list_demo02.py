# 列表的增删改查等方法
# append 在该列表后面增加一个元素（包括列表）
heroes = ["钢铁侠", '绿巨人']
heroes.append("黑寡妇")
print(heroes)
# ['钢铁侠', '绿巨人', '黑寡妇']


# extend 将一个列表中的元素添加到该列表的后面
heroes.extend(["鹰眼", "灭霸", "雷神"])
print(heroes)
# ['钢铁侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神']
# 以切片来添加列表中的元素，相当于extend
heroes[len(heroes):] = [6, 7]
print(heroes)
# ['钢铁侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神', 6, 7]

# insert 在某个位置插入一个元素（包括列表）
heroes.insert(1, 1)
print(heroes)
# ['钢铁侠', 1, '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神', 6, 7]
heroes.insert(2, [2, 3])
print(heroes)
# ['钢铁侠', 1, [2, 3], '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神', 6, 7]
heroes.insert(len(heroes), 8)
print(heroes)
# ['钢铁侠', 1, [2, 3], '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神', 6, 7, 8]

# remove 删除指定元素
heroes.remove("灭霸")
print(heroes)
# ['钢铁侠', 1, [2, 3], '绿巨人', '黑寡妇', '鹰眼', '雷神', 6, 7, 8]

# pop 删除指定位置的元素，  有返回值！！！
heroes.pop(4)
print(heroes)
# ['钢铁侠', 1, [2, 3], '绿巨人', '鹰眼', '雷神', 6, 7, 8]

# clear 清空列表中的所有元素
heroes.clear()
print(heroes)
# []

# 改
s = [1, 2, 3, 4, 5]
s[len(s)-2:] = [2, 1]
print(s)
# [1, 2, 3, 2, 1]

w = [3, 2, 3, 4, 8, 6]
w[4] = 7
print(w)
# [3, 2, 3, 4, 7, 6]

# sort 列表从小到大排序
w.sort()
print(w)
# [2, 3, 3, 4, 6, 7]

# reverse 反转列表，原地反转列表中的元素顺序
w.reverse()
print(w)
# [7, 6, 4, 3, 3, 2]
w = w[:: -1]
print(w)
# [2, 3, 3, 4, 6, 7]

# sort(reverse=True) 列表从大到小排序
w = [3, 2, 3, 4, 8, 6]
w.sort(reverse=True)
print(w)
# [8, 6, 4, 3, 3, 2]

# count 查找某个元素的数量
print(w.count(3))
# 2

# index 查找某个元素第一次出现的的索引值
print(w.index(6))
# 1
# 替换元素但未知某个元素的索引值时
w[w.index(6)] = 9
print(w)
# [8, 9, 4, 3, 3, 2]

print(w.index(3))
# 3
# 查找指定区间某个元素第一次出现的索引值
print(w.index(3, 4, 5))
# 4

# copy 拷贝列表 浅拷贝 copy函数创建的新列表与原始列表不是同一个内存空间，不同享数据变更
# 二次赋值的变量与原始变量享有相同内存空间
# a = [1,2,3]
# b = a 给b列表中添加或删除元素，a列表也会受到相同的影响
w_copy1 = w.copy()
print(w_copy1)
# [8, 9, 4, 3, 3, 2]
w_copy2 = w[:]
print(w_copy2)
# [8, 9, 4, 3, 3, 2]

s = [1, 2, 3, 4, 5]
s[:] = "FishC"
print(s)
# ['F', 'i', 's', 'h', 'C']

# 元组
# 元组只需要  ,   隔开
# 元组是不可变的， 元组小括号可以省略
rhyme = (1, 2, 3, 4, 5, "上山打老虎")
rhyme = 1, 2, 3, 4, 5, "上山打老虎"

# 切片
print(rhyme[:3])
# (1, 2, 3)
print(rhyme[:])
# (1, 2, 3, 4, 5, '上山打老虎')
print(rhyme[:: 2])
# (1, 3, 5)
print(rhyme[:: -1])
# ('上山打老虎', 5, 4, 3, 2, 1)

# count计算其中某个元素有多少个 index索引第一次出现的位置
nums = (1, 2, 3, 6, 3, 9, 6, 3)
print(nums.count(3))
# 3
print(nums.index(9))
# 5


print(rhyme + nums)
# (1, 2, 3, 4, 5, '上山打老虎', 1, 2, 3, 6, 3, 9, 6, 3)
print(rhyme * 3)
# (1, 2, 3, 4, 5, '上山打老虎', 1, 2, 3, 4, 5, '上山打老虎', 1, 2, 3, 4, 5, '上山打老虎')

# 嵌套元组
w = rhyme, nums
print(w)
# ((1, 2, 3, 4, 5, '上山打老虎'), (1, 2, 3, 6, 3, 9, 6, 3))
for i in w:
    print(i)
# (1, 2, 3, 4, 5, '上山打老虎')
# (1, 2, 3, 6, 3, 9, 6, 3)
for i in w:
    for j in i:
        print(j, end=" ")
print()
# 1 2 3 4 5 上山打老虎 1 2 3 6 3 9 6 3


# 列表推导式，注意：   结果生成为列表
s = (1, 2, 3, 4, 5)
print([i * 2 for i in s])
# [2, 4, 6, 8, 10]

# 生成只有一个元素的元组
x = (343, )
print(x, type(x))
# (343,) <class 'tuple'>

# 打包：生成一个元组  解包：把元组中的元素一次性赋值给三个变量名   (适用于任何序列类型)
t = (123, "FishC", 3.14)
x, y, z = t
print(t, x, y, z)
# (123, 'FishC', 3.14) 123 FishC 3.14

# 列表解包
t = [123, "FishC", 3.14]
x, y, z = t
print(t, x, y, z)
# [123, 'FishC', 3.14] 123 FishC 3.14

# 字符串解包
a, b, c, d, e = y
print(y, a, b, c, d, e, type(y), type(a))
# FishC F i s h C <class 'str'> <class 'str'>
a, b, c, d, e = "FishC"
print(a, b, c, d, e, type(a))
# F i s h C <class 'str'>

# *c   将c作为列表装入剩余字符
a, b, *c = "FishC"
print(a, b, c, type(a), type(b), type(c))
# F i ['s', 'h', 'C'] <class 'str'> <class 'str'> <class 'list'>

x, y = 10, 20
# 实际上：
_ = 10, 20
x, y = _

# 元组中的列表，当元组中的元素为列表时，该列表可以被修改
s = [1, 2, 3]
t = [4, 5, 6]
w = (s, t)
print(w)
# ([1, 2, 3], [4, 5, 6])
w[0][0] = 0
print(w)
# ([0, 2, 3], [4, 5, 6])

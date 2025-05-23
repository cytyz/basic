# 利用 dict() 来实现交集和并集  破解 MD5 哈希加密
# 生成一个随机数列表，一共有 100 个元素，每个元素取 1~100 的随机值，赋值给变量 x
# 生成另一个随机数列表，一共有 100 个元素，每个元素取 50~150 的随机值，赋值给变量 y
# 利用字典的 “键” 不会重复的特点，计算 x 和 y 的交集（就是两者共有的元素）
import random
# 生成一个随机数列表 x，一共有 100 个元素，每个元素取 1~100 的随机值
x = [random.randint(1, 101) for i in range(100)]
# 生成另一个随机数列表 y，一共有 100 个元素，每个元素取 50~150 的随机值
y = [random.randint(50, 151) for j in range(100)]

# 用字典来记录
dict_x = dict(zip(x, [i for i in range(100)]))
dict_y = dict(zip(y, [i for i in range(100)]))

# 计算交集
intersection = [key for key in dict_x.keys() if key in dict_y.keys()]

#计算并集
union = list(dict_x.keys()) + [key for key in dict_y.keys() if key not in dict_x.keys()]

print(x)
# [90, 20, 37, 71, 61, 1, 59, 55, 76, 82, 82, 22, 48, 41, 67, 4, 72, 61, 32, 49, 27, 88, 26, 67, 21, 100, 28, 5, 74, 25, 10, 14, 36, 81, 82, 25, 40, 1, 79, 2, 18, 45, 37, 95, 27, 58, 52, 29, 91, 13, 26, 64, 96, 70, 52, 48, 19, 70, 36, 69, 56, 8, 84, 9, 59, 93, 84, 83, 43, 48, 34, 51, 28, 85, 58, 63, 81, 41, 65, 44, 71, 88, 65, 40, 48, 100, 12, 67, 94, 29, 100, 81, 60, 56, 92, 74, 20, 52, 9, 82]
print(y)
# [55, 107, 110, 87, 77, 73, 104, 121, 76, 142, 93, 110, 72, 70, 86, 143, 72, 76, 81, 62, 82, 108, 141, 116, 103, 77, 103, 71, 135, 50, 142, 103, 95, 97, 107, 134, 108, 117, 143, 85, 97, 90, 120, 144, 105, 62, 73, 126, 141, 89, 51, 136, 56, 56, 93, 59, 122, 118, 65, 93, 61, 62, 129, 137, 105, 146, 104, 128, 57, 63, 89, 99, 120, 126, 58, 147, 52, 128, 142, 106, 91, 116, 146, 91, 66, 114, 73, 124, 84, 146, 64, 118, 115, 90, 69, 129, 121, 107, 82, 65]
print(intersection)
# [90, 71, 61, 59, 55, 76, 82, 72, 81, 95, 58, 52, 91, 64, 70, 69, 56, 84, 93, 51, 85, 63, 65]
print(union)
# [90, 20, 37, 71, 61, 1, 59, 55, 76, 82, 22, 48, 41, 67, 4, 72, 32, 49, 27, 88, 26, 21, 100, 28, 5, 74, 25, 10, 14, 36, 81, 40, 79, 2, 18, 45, 95, 58, 52, 29, 91, 13, 64, 96, 70, 19, 69, 56, 8, 84, 9, 93, 83, 43, 34, 51, 85, 63, 65, 44, 12, 94, 60, 92, 107, 110, 87, 77, 73, 104, 121, 142, 86, 143, 62, 108, 141, 116, 103, 135, 50, 97, 134, 117, 120, 144, 105, 126, 89, 136, 122, 118, 129, 137, 146, 128, 57, 99, 147, 106, 66, 114, 124, 115]

# 破解 MD5 哈希加密
# 生成 0~999999 所有整数组成密码的哈希值
# 将上面生成的哈希值保存为映射类型
# 通过查表的方式，计算下面 3 个哈希值对应的明文密码
hash1 = "021bbc7ee20b71134d53e20206bd6feb"
hash2 = "e10adc3949ba59abbe56e057f20f883e"
hash3 = "655d03ed12927aada3d5bd1f90f06eb7"

import hashlib

hash_list = {}
for i in range(1000000):
    hash_list[i] = hashlib.md5(str(i).encode("utf-8")).hexdigest()
    if hash1 == hash_list[i]:
        print(f"{hash1}: {i}")
    if hash2 == hash_list[i]:
        print(f"{hash2}: {i}")
    if hash3 == hash_list[i]:
        print(f"{hash3}: {i}")
# 021bbc7ee20b71134d53e20206bd6feb: 1024
# e10adc3949ba59abbe56e057f20f883e: 123456
# 655d03ed12927aada3d5bd1f90f06eb7: 960520

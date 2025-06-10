# with 和 pickle模块
# with语句和上下文管理器(上文打开文件，下文关闭文件)
f = open("FishC.txt", "w")
f.write("I love fishc")
f.close()
# 用with代替,不需要再关闭文件，即时保存操作，即使后面报错也能正常关闭文件
with open("FishC.txt", "w") as f:
    f.write("I love fishc")


# pickle模块 永久存储python对象 二进制
import pickle
x, y, z = 1, 2, 3
s = "FishC"
l = ["小甲鱼", 520, 3.14]
d = {"one":1, "two":2}
# 保存到.pkl文件
with open("data.pkl", "wb") as f:
    pickle.dump((x, y, z, s, l, d), f)

# 读取.pkl文件
with open("data.pkl", "rb") as f:
    x, y, z, s, l, b = pickle.load(f)

print(x, y, z, s, l, b, sep="\n")
# 1
# 2
# 3
# FishC
# ['小甲鱼', 520, 3.14]
# {'one': 1, 'two': 2}

# 使用 with 语句管理两个文件的上下文
with open("FishC.txt", "r") as f1, open("FishD.txt", "r") as f2:
    f1.seek(10)
    f2.write(f1.read(5))

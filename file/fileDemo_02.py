# 文件路径处理练习
# 判断当前路径是否为文件夹类型，如果是则在路径末尾追加一个 FishC.txt
from pathlib import Path

p = Path(r"D:\临时\test")
if p.is_dir():
    n = p / "FishC.txt"
    print(n.resolve())


# ————————————————————————————————————————————————————————
# 列举出当前目录下的所有子目录
# 带绝对路径
p = Path.cwd()
n = list(p.glob("./*"))
for i in n:
    if i.is_dir():
        print(i)
        print(i.name)
# D:\Program_Repository\github\basic\file\test
# test
# 不带绝对路径
p = Path(".")
n = list(p.glob("./*"))
for i in n:
    if i.is_dir():
        print(i)
# test

print([x for x in p.iterdir() if x.is_dir()])
# [WindowsPath('test')]


# ————————————————————————————————————————————————————————
# 列举出当前目录下的所有文件的尺寸
for i in p.iterdir():
    print(f"文件名：{i}，文件尺寸：{i.stat().st_size}字节")
# 文件名：file01.py，文件尺寸：1491字节
# 文件名：file02.py，文件尺寸：4581字节
# 文件名：fileDemo_01.py，文件尺寸：813字节
# 文件名：fileDemo_02.py，文件尺寸：750字节
# 文件名：FishD.txt，文件尺寸：5字节
# 文件名：target.zip，文件尺寸：179字节
# 文件名：test，文件尺寸：0字节
# 文件名：test.jpg，文件尺寸：71633字节


# ————————————————————————————————————————————————————————
# 列举出当前目录下的所有文件的修改时间
# time.strftime(format, struct_time) 用于将时间元组或者struct_time对象格式化为字符串
# time.strptime(string, format) 用于解析字符串为时间元组对象
# time.localtime() 根据提供的时间戳来转换为本地时间
from time import strftime,localtime
for i in n:
    print(f"文件名：{i}，修改时间：{strftime('%Y-%m-%d %H-%M-%S', localtime(i.stat().st_mtime))}")
# 文件名：file01.py，修改时间：2025-06-01 17-28-15
# 文件名：file02.py，修改时间：2025-06-05 01-56-27
# 文件名：fileDemo_01.py，修改时间：2025-06-01 17-38-15
# 文件名：fileDemo_02.py，修改时间：2025-06-05 17-22-00
# 文件名：FishD.txt，修改时间：2025-06-05 01-33-49
# 文件名：target.zip，修改时间：2025-06-01 17-33-13
# 文件名：test，修改时间：2025-06-05 01-26-57
# 文件名：test.jpg，修改时间：2025-06-05 01-33-49


# ————————————————————————————————————————————————————————
# 获取指定路径（文件夹）中所有的文件名，并按文件尺寸按从小到大进行排序
p = Path("..")
file = []
for i in p.iterdir():
    if i.is_dir():
        file.append(i)

file.sort(key=lambda x: x.stat().st_size)
for i in file:
    print(f"文件名：{i}，尺寸大小：{i.stat().st_size}字节")
# 文件名：..\assets，尺寸大小：0字节
# 文件名：..\dictionary，尺寸大小：0字节
# 文件名：..\FristGame，尺寸大小：0字节
# 文件名：..\number，尺寸大小：0字节
# 文件名：..\sequence，尺寸大小：0字节
# 文件名：..\set，尺寸大小：0字节
# 文件名：..\tuple，尺寸大小：0字节
# 文件名：..\Variables_Strings，尺寸大小：0字节
# 文件名：..\.git，尺寸大小：4096字节
# 文件名：..\.idea，尺寸大小：4096字节
# 文件名：..\branch_loop，尺寸大小：4096字节
# 文件名：..\file，尺寸大小：4096字节
# 文件名：..\function，尺寸大小：4096字节
# 文件名：..\list_Demo，尺寸大小：4096字节
# 文件名：..\strings，尺寸大小：4096字节

# 一行流
print("\n".join(f"文件名：{i}，尺寸大小：{i.stat().st_size}字节" for i in sorted((j for j in Path("..").iterdir() if j.is_dir()), key=lambda x:x.stat().st_size)))


# ————————————————————————————————————————————————————————
# 找出指定路径（文件夹）中最后被修改的文件
from time import strftime,localtime
p = Path("..")
file = []
for i in p.iterdir():
    if i.is_file():
        file.append(i)
n = max(file, key=lambda x: x.stat().st_mtime)
print(f"文件名:{n}，修改时间：{strftime('%Y-%m-%d %H-%M-%S', localtime(n.stat().st_mtime))}")
# 文件名:..\PythonBasic.md，修改时间：2025-06-01 00-24-04

# 一行流
# f"{a := b}" 表示a = b
# max([a, b]) 多个列表时，默认对列表中第一个元素进行比较，但返回的是整个列表，这也意味着后面的元素可以放置想要打印的东西
print(f"文件名:{(file := max([j for j in Path("..").iterdir() if j.is_file()], key=lambda x:x.stat().st_mtime)).name}，修改时间：{strftime('%Y-%m-%d %H-%M-%S', localtime(file.stat().st_mtime))}")
# 文件名:PythonBasic.md，修改时间：2025-06-01 00-24-04
print(max([(strftime("修改时间 -> %Y-%m-%d %H:%M:%S", localtime(f.stat().st_mtime)), f"文件名 -> {f.name}") for f in Path("..").iterdir() if f.is_file()]))

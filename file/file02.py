# 路径处理
# pathlib 模块
# Path.cwd() 获取当前目录的路径
# Path() 打开指定路径
# a / b 拼接路径
# __file__ 当前脚本的绝对路径
from os import rename
from pathlib import Path

print(Path.cwd())   # D:\Program_Repository\github\basic\file
p = Path(r"D:\Program_Repository\github\basic\file\test")
print(p)    # D:\Program_Repository\github\basic\file\test
q = p / "FishC.txt"
print(q)    # D:\Program_Repository\github\basic\file\test\FishC.txt


# is_dir() 路径是否为文件夹    is_file() 路径是否为文件
# exists() 路径是否存在
# name 获取路径的最后一个部分
# stem 获取文件名    suffix 获取文件后缀
# parent 获取其父级目录
# parents 获取逻辑祖先路径构成的序列
# parts 将路径拆分成元组
# stat() 查看当前状态
print(p.is_dir(), p.is_file())    # True False
print(p.exists())    # True
print(p.name)    # file
print(q.stem, q.suffix)    # FishC .txt
print(p.parent)    # D:\Program_Repository\github\basic\file

ps = p.parents
for each in ps:
    print(each)
# D:\Program_Repository\github\basic\file
# D:\Program_Repository\github\basic
# D:\Program_Repository\github
# D:\Program_Repository
# D:\
print(ps[0], ps[1])    # D:\Program_Repository\github\basic\file D:\Program_Repository\github\basic

print(p.parts)    # ('D:\\', 'Program_Repository', 'github', 'basic', 'file', 'test')
print(p.stat())    # os.stat_result(st_mode=16895, st_ino=2533274790466088, st_dev=17911000550101998974, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1749058015, st_mtime=1749058009, st_ctime=1749058009)

# stat().st_size 文件或文件夹大小(单位字节)
print(p.stat().st_size)    # 0


# 绝对路径/相对路径
# . 当前所在目录    .. 上一级目录
# resolve() 转换成绝对路径
# iterdir() 获取当前路径下所有的子文件和子文件夹
print(Path("./FishD.txt"))    # FishD.txt
print(Path("../assets"))    # ..\assets
print(Path("./FishD.txt").resolve())    # D:\Program_Repository\github\basic\file\FishD.txt
m = Path(r"D:\Program_Repository\github\basic\file")
for i in m.iterdir():
    print(i)
# D:\Program_Repository\github\basic\file\file01.py
# D:\Program_Repository\github\basic\file\file02.py
# D:\Program_Repository\github\basic\file\fileDemo_01.py
# D:\Program_Repository\github\basic\file\FishD.txt
# D:\Program_Repository\github\basic\file\target.zip
# D:\Program_Repository\github\basic\file\test
# D:\Program_Repository\github\basic\file\test.jpg

print([i for i in m.iterdir() if i.is_file()])
# [WindowsPath('D:/Program_Repository/github/basic/file/file01.py'), WindowsPath('D:/Program_Repository/github/basic/file/file02.py'), WindowsPath('D:/Program_Repository/github/basic/file/fileDemo_01.py'), WindowsPath('D:/Program_Repository/github/basic/file/FishD.txt'), WindowsPath('D:/Program_Repository/github/basic/file/target.zip'), WindowsPath('D:/Program_Repository/github/basic/file/test.jpg')]

# 路径修改
# mkdir() 创建文件夹
n = p / "FishC"
# 若文件夹存在会报错,需要设置 exist_ok=True
n.mkdir(exist_ok=True)
# 若路径中有多个不存在的文件夹会报错，需要设置 parents=True
n = p / "FishC/A/B/C"
n.mkdir(parents=True, exist_ok=True)
# open() 打开该路径
n = n / "FishC.txt"
f = n.open("w")
f.write("I love FishC")
f.close()

import os
# rename() 修改文件或文件夹名字, 无指定路径时默认当前文件夹
# replace() 替换指定的文件或文件夹，将文件剪切并替换掉
# rmdir() unlink() 删除文件夹（文件夹非空时会报错）；删除文件
# glob() 查找    迭代器，需要用list
# help(os.rename)
# os.rename(r"D:\Program_Repository\github\basic\file\test\FishC\A\B\C\FishC.txt", r"D:\Program_Repository\github\basic\file\test\FishC\A\B\C\NewFishC.txt")
m = Path("FishC.txt")
# m.replace(n) # 无替换文件时会报错

# n.unlink()
# n.parent.rmdir()

p = Path(".") # 当前目录
print(p.resolve())
# D:\Program_Repository\github\basic\file
p1 = list(p.glob("*.txt"))
for each in p1:
    print(each)
# FishD.txt

p = Path("..") # 上一级目录
print(p.resolve())
# D:\Program_Repository\github\basic
p2 = list(p.glob("file/*.py")) # 下一级目录
for each in p2:
    print(each)
# ..\file\file01.py
# ..\file\file02.py
# ..\file\fileDemo_01.py

p = Path(".")
p3 = list(p.glob("**/*.py")) # 当前目录及下一级目录
for each in p3:
    print(each)
# file01.py
# file02.py
# fileDemo_01.py
p4 = list(p.glob("*/*.py")) # 下一级目录
print(p4) # []

# 收集参数
# 定义函数时不限制用户输入个数，
# 形参前加*， 通过*将多个参数打包为元组， **将多个参数打包为字典
# 定义时多个参数则置于函数最后位置，若不置于最后位置，则在收集参数后的参数只能是关键字参数（在使用时指定形参对应的实参）
# *  斜杠右侧必须传入关键字参数， 这就是一个匿名的收集参数
# 打包为元组
def myfunc(start, *args):
    print(f"有{len(args)}个无限制参数")
    print(f"第二个参数是{args[1]}")
myfunc(1, "tge", 35, [1, 3, "werf"])
# 有3个无限制参数
# 第二个参数是35

# python在返回多个值时利用元组进行打包
def myfunc(*args):
    print(args)
myfunc(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)  以元组形式打包返回
def myfunc():
    return 1, 2, 4
print(myfunc())
# (1, 2, 4)  以元组形式打包返回
# 可以进行元组解包
x, y, z = myfunc()
print(x, y, z)
# 1 2 4

# 打包为字典
def myfunc(**kwargs):
    print(kwargs)
myfunc(a=1, b=2, c=3)
# {'a': 1, 'b': 2, 'c': 3}
# 混合
def myfunc(a, *b, **c):
    print(a, b, c)
myfunc(1, 2, 3, x=1, y=2, z=3)
# 1 (2, 3) {'x': 1, 'y': 2, 'z': 3}

# 解包参数 实参前加* 或** 实现解包，以此给形参赋值
# * 解包成位置参数， **解包成关键字参数
args = (1, 2, 3, 4)
def myfunc(a, b, c ,d):
    print(a, b, c, d)
myfunc(*args)
# 1 2 3 4

kwargs = {"a": 1, "b": 2, "c": 3, "d": 4}
myfunc(**kwargs)
# 1 2 3 4

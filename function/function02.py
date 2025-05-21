# 位置参数 在定义函数时将参数位置固定了下来，而这类参数称之为位置参数
def myfunc(s, vt , o):
    return "".join([o, vt, s])
print(myfunc("我", "打了", "小甲鱼"))
# 小甲鱼打了我

# 关键字参数 更适用鱼参数多的函数
print(myfunc(o="我", vt="打了", s="小甲鱼"))
# 我打了小甲鱼
# 混用，位置参数要在关键字参数之前
print(myfunc("小甲鱼", o="我", vt="打了"))
# 我打了小甲鱼

# 默认参数 函数在定义时指定默认的参数值    默认参数要放在最后
def myfunc(s, vt, o="小甲鱼"):
    return "".join((o, vt, s))
print(myfunc("香蕉","吃"))
# 小甲鱼吃香蕉
def myfunc(vt, s="苹果", o="小甲鱼"):
    return "".join((o, vt, s))
print(myfunc("吃"))
# 小甲鱼吃苹果

# /  斜杠左侧必须传入位置参数
# *  斜杠右侧必须传入关键字参数， 这就是一个匿名的收集参数
print(help(abs), help(sum))
# 如abs(x, /)    sun(iterable, /, start=0)
print(abs(-1.5))
# 1.5   abs(x=-1.5)则会报错
print(sum([1, 2, 3], 4))
# 10
print(sum([1, 2, 3], start=4))
# 10
def abc(a, /, b, c):
    print(a, b, c)
abc(1, b=2, c=3)
# 1 2 3
def abc(a, *, b, c):
    print(a, b, c)
abc(1, b=2, c=3)
# 1 2 3
abc(a=1, b=2, c=3)
# # 1 2 3

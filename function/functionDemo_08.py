# 利用生成器定义一个支持浮点数的 frange() 函数，其功能与 range() 函数相仿。
# round(number, ndigits=None)    ndigits 指定精度
# round() 函数用于返回一个指定精度（四舍五入）的结果。
def frange(start, stop=None, step=0.1):
    s = str(step)
    len1 = len(s) - 2
    start += 0.0
    if stop is None:
        stop = start + 0.0
        start = 0.0
    while start < stop:
        yield round(start, len1)
        start += step

for i in frange(1):
    print(i)

for i in frange(1, 2):
    print(i)

for i in frange(5, 10, 0.5):
    print(i)

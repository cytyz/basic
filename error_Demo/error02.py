# 异常
# try-except-else    try-except-finally
# raise语句 直接抛出异常，主动引发异常
# raise ValueError("值不正确") # 报错ValueError
# assert语句 断言 只能引发AssertionError异常    常用于调试    类似于if语句
s = "FishC"
assert s == "FishC" # 为真，什么都不发生
# assert s != "FishC" # 为假，报错AssertionError

# 用异常来实现goto语句（勿用）
try:
    while True:
        while True:
            for i in range(10):
                if i > 3:
                    # 可以无指定异常，但会爆红，抛出异常后，except捕获异常，直接跳出循环
                    raise
                    # raise 如果不带任何参数，抛出的异常为RuntimeError，
                    # 当检测到一个不归属于任何其他类别的错误时，就会引发 RuntimeError 异常，关联的值是一个指示问题原因的字符串，
                    # 由于我们是直接 raise 引发，所以它这个字符串 No active exception to reraise 的意思大概就是说这个异常属于 “无中生有”。
                print(i)
            print("break")
        print("break")
    print("break")
except:
    print("到这里来了")

# 实现在捕获异常之后，打印一句 “出错啦”，再重新抛出相对应的异常（注意，这里我们说的异常并不特指具体的哪一类，而是泛指所有的异常）。
# 利用不带参数的 raise 语句即可实现
try:
    1 / 0
except:
    print("出错啦~")
    raise

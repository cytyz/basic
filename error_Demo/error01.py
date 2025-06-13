# 异常捕获
# try-except 捕获异常
# 异常后加as 可以打印出异常来
# e 指向对应的异常类，比如这里是 TypeError，那么它就是 <class 'TypeError'>
try:
    1 / 0
except ZeroDivisionError as e:
    print(e) # division by zero

# 有时候没把握出现的会是哪个异常,，可以把可能出现的异常放到元组中
try:
    520 + "FishC"
    1 / 0 # 上一行异常，这行未运行
except (ZeroDivisionError, TypeError, ValueError) as e:
    print(e) #unsupported operand type(s) for +: 'int' and 'str'

try:
    1 / 0
    520 + "FishC" # 上一行异常，这行未运行
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("值不正确")
except TypeError:
    print("类型不正确")
# 除数不能为0

# locals(); 查看当前所有变量
# 测试是否定义过一个值 f in locals();
# 可以检测是否关闭文件

# assert：断言；当这个关键字后边的条件为假的时候，程序自动崩溃并抛出AssertionError的异常。 可以用 assert **Error 来自定断言异常类型

# 如果试图引用一个未曾定义过的变量，Python 会抛出NameError异常
# 如果试图访问一个对象中不存在的属性，Python 会抛出AttributeError异常

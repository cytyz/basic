# 函数文档、类型注释、内省
# help 查看函数文档
help(print)
# Help on built-in function print in module builtins:
#
# print(*args, sep=' ', end='\n', file=None, flush=False)
#     Prints the values to a stream, or to sys.stdout by default.
#
#     sep
#       string inserted between values, default a space.
#     end
#       string appended after the last value, default a newline.
#     file
#       a file-like object (stream); defaults to the current sys.stdout.
#     flush
#       whether to forcibly flush the stream.

def exchange(dollar, rate=7.18):
    """
    功能：汇率转换，美元 -> 人名币
    参数：
    - dollar 美元数量
    - rate 汇率，默认值是7.18(2025-05-29
    返回值：
    - 人民币的数量
    """
    return dollar * rate
help(exchange)
# Help on function exchange in module __main__:
#
# exchange(dollar, rate=7.18)
#     功能：汇率转换，美元 -> 人名币
#     参数：
#     - dollar 美元数量
#     - rate 汇率，默认值是7.18(2025-05-29
#     返回值：
#     - 人民币的数量

# ————————————————————————————————————————————————————————————
# 类型注释
# 告知希望传入参数类型及返回值
def times(s:str, n:int) ->str:
    return s * n
print(times(5,5))
# 25

def times(s:str = "FishC", n:int = 3) ->str:
    return s * n
print(times())
# FishCFishCFishC

# 希望是列表
def times(s:list, n:int = 3) ->list:
    return s * n
print(times([1, 2, 3]))
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 希望是整数列表
def times(s:list[int], n:int = 3) ->list:
    return s * n

# 希望是字典
def times(s:dict[str,int], n:int = 3) ->list:
    return list(s.keys()) * n


# 内省
print(times.__name__)
# times
# annotations 注释
print(times.__annotations__)
# {'s': dict[str, int], 'n': <class 'int'>, 'return': <class 'list'>}
# 查看函数文档
print(exchange.__doc__)
# 功能：汇率转换，美元 -> 人名币
# 参数：
# - dollar 美元数量
# - rate 汇率，默认值是7.18(2025-05-29
# 返回值：
# - 人民币的数量

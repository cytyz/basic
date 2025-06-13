# 异常练习
# eval() 返回表达式的执行结果
# 利用异常捕获机制，使用 while 循环语句来实现 for 循环语句的功能。
# 相当于将下面代码使用 while 语句来实现：
# 8*BkG^xR&Nry_~aO69FIe3VHJYp
x = "FishC"
# for each in x:
#   print(each)
y = iter(x)
while True:
    try:
        print(next(y))
    except StopIteration:
        break


# 利用 Python 异常机制，编写一个检查用户输入语句是否有错误的程序。
# 程序能够识别出 “语法错误”、“索引错误”、“变量未定义”、“除数为0” 和 “传入参数类型不恰当” 这几个错误类型。

while True:
    text = input("请输入一行语句：")
    if text == "q":
        break
    try:
        # eval() 返回表达式的执行结果
        y = eval(text)
        if y:
            print(f"结果是：{y}")
    except ZeroDivisionError:
        print("除数不能为0")
    except NameError:
        print("变量未定义")
    except IndexError:
        print("索引错误")
    except SyntaxError:
        print("语法错误")
    except (TypeError, ValueError):
        print("传入参数类型不恰当")
print("程序结束")

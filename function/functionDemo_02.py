# 回文字符串拼音版 与 模拟栈
# 提示一：放宽要求后，只要文字的发音构成前后回文，即认定为符合要求。
# 提示二：将汉字转换为对应拼音的方法 -> https://fishc.com.cn/thread-213439-1-1.html
# 提示三：请将各个独立的功能封装为函数。
from xpinyin import Pinyin
def input_text():
    text = input("请输入一段话：")
    while len(text) <= 1:
        text = input("字数太少，请重新输入：")
    return text

def changepy(text):
# 转换成拼音
    text1 = Pinyin().get_pinyin(text, ",")
    text1 = text1.split(",")
    return text1

def judge(text, text1):
    temp = []
    i = 0
    if len(text1) % 2 == 0:
        while i < len(text1) - 1:
            if i <= len(text1) // 2 - 1:
                temp.append(text1[i])
                i += 1
            else:
                if temp.pop() != text1[i]:
                    print(f"{text}不是回文")
                    break
                else:
                    i += 1
    else:
        while i < len(text1):
            if i == len(text1) // 2:
                i += 1
                continue
            elif i <= len(text1) // 2 - 1:
                temp.append(text1[i])
                i += 1
            else:
                if temp.pop() != text1[i]:
                    print(f"{text}不是回文")
                    break
                else:
                    i += 1
    if i >= len(text1):
        print(f"{text}是回文")

text = input_text()
text1 = changepy(text)
judge(text1, text1)
# 请输入一段话：前任只认钱
# ['qian', 'ren', 'zhi', 'ren', 'qian']是回文

# 利用函数模拟创建【栈】的数据结构操作
stack_like = []
def input_text1():
    while True:
        command = input("请输入指令（push/pop/top/exit）：")
        if command == "push":
            stack_push()
        elif command == "pop":
            stack_pop()
        elif command == "top":
            stack_top()
        elif command == "exit":
            break
        else:
            print("请输入正确的指令：")

def stack_push():
    num = input("请输入将要压入栈中的值：")
    stack_like.append(num)
    temp = [i for i in reversed(stack_like)]
    print("栈:")
    for j in range(len(stack_like)):
        print(temp[j])

def stack_pop():
    if len(stack_like) == 0:
        print("栈已空")
        return 0
    print(stack_like.pop())
    temp = [i for i in reversed(stack_like)]
    print("栈:")
    for j in range(len(stack_like)):
        print(temp[j])


def stack_top():
    if len(stack_like) == 0:
        print("栈已空")
        return 0
    temp = [i for i in reversed(stack_like)]
    print(temp[0])

input_text1()

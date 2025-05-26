# 罗马数字与数字的互转
# 罗马数字包含 I、V、X、L、C、D、M 七种字符，分别表示数值 1、5、10、50、100、500、1000。
# 编写一个函数，将指定的罗马字符转换为数字的形式。
# 增加检测非法字符的功能
# 简化版
# enumerate 枚举
# # 定义一个包含一些水果名称的列表
# fruits = ['apple', 'banana', 'cherry']
#
# # 使用 enumerate 函数遍历列表
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")
# 在这个例子中，enumerate(fruits) 返回一个枚举对象，其中包含了列表中每个元素的索引和值
R2N = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def rome_num2(rome):
    num = 0
    len2 = len(rome)
    for i, j in enumerate(rome):
        v = R2N[j]
        if i < len2 - 1 and  v < R2N[rome[i + 1]]:
            num -= v
        else:
            num += v
    return num
def input_rome2():
    rome = input("请输入一个罗马字符：")
    num = rome_num2(rome)
    print(f"转换后的结果是：{num}")
# input_rome2()

# 数字转罗马数字
N2R = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

def num2roman(num):
    r = []
    for v, s in N2R:
        while num >= v:
            num -= v
            r.append(s)
        if num == 0:
            break

    return "".join(r)

n = input("请输入一个整数：")
r = num2roman(int(n))
print(f"转换后的结果是：{r}")
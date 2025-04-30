# 大小写转换与对齐
# 字符串不可变，改变字符串时实际上是生成一个新的字符串

# capitalize 将整个字符串首字母大写其余变小写
# casefold 将整个字符串变小写（与lower不一样的是它可以处理英文之外的字母）
# title 将字符串中每个单词的首字母大写
# swapcase 将整个字符串所有字母大小写翻转
# upper 将整个字符串变大写
# lower 将整个字符串变小写
x = "I Love FishC"
print(x.capitalize())
# I love fishc
print(x.casefold())
# i love fishc
print(x.title())
# I Love Fishc
print(x.swapcase())
# i lOVE fISHc
print(x.upper())
# I LOVE FISHC
print(x.lower())
# i love fishc

# 左中右对齐
# center(width, fillchar='") 居中对齐，默认空格填充
# ljust(width, fillchar='") 左对齐，默认空格填充
# rjust(width, fillchar='") 右对齐，默认空格填充
# zfill(width) 用0填充左侧
x = "有内鬼，停止交易"
print(x.center(15))
#    有内鬼，停止交易
print(x.ljust(15))
# 有内鬼，停止交易
print(x.rjust(15))
#        有内鬼，停止交易
print(x.zfill(15))
# 0000000有内鬼，停止交易

print("-520".zfill(10))
# -000000520
print("-520".rjust(10, "0"))
# 000000-520
print("I love FishC".swapcase()[::-1])
# cHSIf EVOL i

# 判断回文数
num = ["123", "33211", "12321", "13531", "112233"]
pr = [i for i in num if i == i[::-1]]
print(pr)
# ['12321', '13531']

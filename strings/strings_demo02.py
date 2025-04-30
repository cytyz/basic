# 查找与替换
# 查找
# count(sub[,start[,end]]) 查找指定的子字符串出现的次数
# find(sub[,start[,end]]) 从左往右找指定的子字符串， 找不到返回-1
# rfind(sub[,start[,end]]) 从右往左找指定的字符串， 找不到返回-1
# index(sub[,start[,end]]) 从左往右找指定的子字符串， 找不到抛出异常
# rindex(sub[,start[,end]]) 从右往左找指定的字符串， 找不到抛出异常
x = "上海自来水来自海上"
print(x.count("海"))
# 2
print(x.count("海", 2, 8))
# 1
print(x.find("海"))
# 1
print(x.rfind("海"))
# 7
print(x.find("龟"))
# -1
# print(x.index("龟"))
# Traceback (most recent call last):
#   File "D:\Program Repository\github\basic\strings\strings_demo02.py", line 18, in <module>
#     print(x.index("龟"))
# ValueError: substring not found

# 替换
# expandtabs([tabsize]) 使用来替换tab制表符，并返回一个新的字符串
# replace(old, new, count=-1) 将旧字符串替换为新字符串，count 替换的次数，默认-1
# 尽量用空格代替tab
code = """
    print("I Love FishC")
    print("I Love My Wife")"""
new_code = code.expandtabs(4)
print(new_code)
#
#     print("I Love FishC")
#     print("I Love My Wife")
w = "在吗！我在你家楼下，快点下来！！！"
print(w.replace("在吗", "想你"))
# 想你！我在你家楼下，快点下来！！！

# str.maketrans[x[,y[,z]]] 制定转换规则的表格，x 替换成y 忽略z中包含的字母
# translate(table) 将字符串以表格中的规则替换
table = str.maketrans("ABCDEFG", "1234567")
q = "I Love FishC"
print(q.translate(table))
# I Love 6ish3
print("I Love FishC".translate(str.maketrans("ABCDEFG", "1234567")))
# I Love 6ish3
print("veol Love FishC".translate(str.maketrans("ABCDEFG", "1234567", "love")))
# I  6ish3  z中包含l o v e, 故veol ove都被忽略

x = "上海自来水来自海上"
print(x.rindex("来水来"))
# 3

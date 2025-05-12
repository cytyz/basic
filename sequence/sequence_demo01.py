# 判断子序列与 查找最大奇数
# 给定字符串 s 和 t ，请编程判断 s 是否为 t 的子序列。
# 字符串的子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串（例如，"ace" 是 "abcde" 的子序列，而 "aec" 则不是）。
s = "FishC"
# t = "FiiisjjhkkCBA"
t = "FijkhsC"
# s = input("请输入字符串s：")
# t = input("请输入字符串t：")
temp = 0
j = 0
while j < len(s):
    index = t.find(s[j])
    while index != -1:
        j += 1
        if j < len(s):
            index = t.find(s[j], index)
        else:
            break
    else:
        break
if j == len(s):
    print("字符串 s 是字符串 t 的子序列")
else:
    print("字符串 s 不是字符串 t 的子序列")

# 给定一个字符串 s，请编程求出该字符串中的最大奇数。
# s1 = "43383"
# 输出：43383
# s1 = "5926"
# 输出：59
# s1 = "966"
# 输出：9
s1 = "64062"
# 输出：0
s2 = []
for i in range(len(s1) - 1, -1, -1):
    if int(s1[i]) % 2 != 0:
        for j in range(i + 1):
            s2.append(s1[j])
        break
if len(s2) == 0:
    print("0")
else:
    print("".join(s2))

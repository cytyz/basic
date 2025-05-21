# 整理字符串与ASCII转换
# 一个整理好的字符串中，两个相邻字符 s[j] 和 s[j+1]，其中 0 <= j <= s.length - 2，要满足如下条件：
# 若 s[j] 是小写字符，则 s[j+1] 不可以是相同的大写字符
# 若 s[j] 是大写字符，则 s[j+1] 不可以是相同的小写字符
# 如果 s[j] 和 s[j+1] 满足以上两个条件，则将它们一并删除
# s = input("请输入待整理的字符串:")
# # 请输入待整理的字符串:AAAaBbcC
# # 字符串不可变，转换成列表来处理1
# s2 = list(s)
# j = 0
# while j < len(s2) - 1:
#     if s2[j].lower() == s2[j + 1].lower() and s2[j] != s2[j + 1]:
#         # 先去掉了j，j+1变成了j
#         s2.pop(j)
#         s2.pop(j)
#         j = j - 1
#         print(s2)
#         # ['A', 'A', 'B', 'b', 'c', 'C']
#         # ['A', 'A', 'c', 'C']
#     else:
#         j = j + 1
#
# s3 = ''.join(s2)
# print(s3)
# ['A', 'A']

# 方法二：
s = input("请输入一个字符串：")

res = []
for each in s:
    if res and res[-1].lower() == each.lower() and res[-1] != each:
        res.pop()
    else:
        res.append(each)

for each in res:
    print(each, end='')



# 给定的字符串 s 是按照如下规则存放的：它的偶数下标为小写英文字母，奇数下标为正整数。
# 题目要求：编写代码，将奇数下标的数字转换为相对于上一个字母偏移后的字母。
s = "z1a2c3"
# # ord 将字母转换成ASCII， chr 将ASCII转换成字母
# print(ord("A"), ord("Z"), ord("a"), ord("z"))
# # 65 90 97 122
# print(chr(97))
# # a
s1 = list(s)
for i in range(len(s1)-1):
    if s1[i].isalpha() and s1[i + 1].isdigit():
        temp = ord(s1[i])+int(s1[i+1])
        if 97 <= temp <= 122:
            s1[i + 1] = chr(temp)
        elif temp > 122:
            s1[i + 1] = chr(temp - 122 + 97 -1)
        else:
            s1[i + 1] = chr(temp - 122)
s = ''.join(s1)
print(s)

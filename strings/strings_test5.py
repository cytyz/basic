# 格式化练习
# 请编写一个程序，统计字符串中的单词个数（“单词”以空格进行分隔）
# str1 = ""
# 输出：0
# str1 = "Python"
# 输出：1
str1 = "I love FishC"
# 输出：3
words = str1.split()
print(len(words))

# 请编写一个程序，将用户输入的字符串重新格式化，使得字母和数字相互分隔（即一个字母一个数字相互间隔）
# str2 = "FishC1314"
# 输出：F1i3s1h4C
# str2 = "FishC520"
# 输出：字符串中数字和字母的数量不满足重新格式化的条件
str2 = "Python6543210"
# 输出：6P5y4t3h2o1n0
alp = 0
alptemp = []
num = 0
numtemp = []
str_new = []
for word in str2:
    if word.isalpha():
        alp = alp + 1
        alptemp.append(word)
    elif word.isdecimal():
        num = num + 1
        numtemp.append(word)
if alp - num == 1:
    for i in range(len(str2)):
        print(i, i % 2)
        if i % 2 != 0:
            str_new.append(numtemp[i // 2])
        else:
            str_new.append(alptemp[i // 2])
    print("".join(str_new))
elif alp - num == -1:
    for i in range(len(str2)):
        if i % 2 != 0:
            str_new.append(alptemp[i // 2])
        else:
            str_new.append(numtemp[i // 2])
    print("".join(str_new))
else:
    print("字符串中数字和字母的数量不满足重新格式化的条件")

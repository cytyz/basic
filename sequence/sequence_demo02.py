# 奇偶排序 翻转单词顺序
# 给定一个整数列表，请编程来调整该列表中整数的顺序，使得所有奇数排好序后放在数组的前半部分，所有偶数排好序后放在数组的后半部分。
# 比如给定的整数列表是 [1, 8, 7, 3, 6, 5, 4, 2]，那么调整后的结果应该是 [1, 3, 5, 7, 2, 4, 6, 8]。
list1 = [1, 8, 7, 3, 6, 5, 4, 2]
odd = []
even = []
list2 = []
for i in range(len(list1)):
    if list1[i] % 2 == 0:
        even.append(list1[i])
    else:
        odd.append(list1[i])
list2.extend(sorted(odd))
list2.extend(sorted(even))
print(list2)
# [1, 3, 5, 7, 2, 4, 6, 8]

#  翻转单词顺序。
# 用户输入一个英文句子，请编程翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
# 例如输入字符串是 "I love FishC."，则输出 "FishC. love I"。
# 注意1：用户输入的字符串可能会在前面或者后面包含任意数量的空格，但是反转后的结果将会去除这些空格（例如输入字符串是 "   I love FishC.   "，结果依然输出 "FishC. love I"）。
# 注意2：用户输入的字符串中，单词之间可能不止一个空格，但是反转后的结果将统一使用一个空格作为单词之间的间隔（例如输入字符串是 "I   love        FishC."，结果依然输出 "FishC. love I"）
strings1 = "    I   love     FishC."
reverser = list(reversed(strings1.split()))
strings2 = ' '.join(reverser)
print(strings2)
# FishC. love I

# 给定一个字符串 text 和字符串列表 words，返回 words 中每个单词在 text 中的位置（要求最终的位置从小到大进行排序）。
# text = "I love FishC and FishC love me"
# words = "FishC"
# 输出：[[7, 11], [17, 21]]
# text = "I love FishC and FishC love me"
# words = "FishC love"
# # 输出：[[2, 5], [7, 11], [17, 21], [23, 26]]
# text = "FCFCF"
# words = "FCF FC"
# 输出：[[0, 1], [0, 2], [2, 3], [2, 4]]
text = input("请输入text的内容：")
words = input("请输入words的内容：")
position = []
for word in words.split():
    print(word)
    index = text.find(word)
    while index != -1:
        position.append([index, (index + len(word)) - 1])
        index = text.find(word, index + 1)
position.sort()
print(position)


# 编写一个程序，判断输入的字符串是否由多个子字符串重复多次构成。
# word = "FCFC"
# 输出：True
# word = "FishCFish"
# 输出：False
# word = "FCCF"
# 输出：False
# word = "FishCFishc"
# 输出：False
word = input("请输入要判断的字符串：")
length = len(word)
length2 = 0
for i in range(1, length // 2 + 1):
    same = word[:i]
    length2 = len(same)
    index = word.find(same, length2)
    while index != -1:
        length2 += len(same)
        index = word.find(same, length2)
    else:
        if length2 <= length // 2:
            continue
if length2 >= length:
    print("True")
else:
    print("False")

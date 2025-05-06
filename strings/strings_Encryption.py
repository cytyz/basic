# 位移加密（凯撒密码）  同行键盘字符串
# 凯撒密码是一种通过位移加密的方法，对 26 个（大小写）字母进行位移加密，比如下方是正向位移 6 位的字母对比表：
# 明文字母表如下
# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
# 密文字母表如下
# GHIJKLMNOPQRSTUVWXYZABCDEF
# 所以，如果给定加密的明文是：
# I love FishC
# 那么程序 +6 加密后输出的密文便是：
# O rubk LoynI
# text = "I love FishC"
# position = 6
# text = "I love FishC"
# position = -6
# text_encryption : C fipy ZcmbW
text = input("请输入需要加密的明文（只支持英文字母）：")
position = int(input("请输入移动的位数："))
char_encryption = []
for char in text:
    if char == " ":
        char_encryption.append(" ")
    else:
        temp = ord(char) + position
        if 97 <= temp <= 122 or 65 <= temp <= 90:
            char_encryption.extend(chr(temp))
        elif temp > 122:
            char_encryption.extend(chr(temp - 122 + 97 - 1))
        elif 90 < temp < 97 and 65 <= ord(char) <= 90:
            char_encryption.extend(chr(temp - 90 + 65 - 1))
        elif 90 < temp < 97 and 97 <= ord(char) <= 122:
            char_encryption.extend(chr(122 - (97 - temp - 1 )))
        else:
            char_encryption.extend(chr(90 - (65 - temp - 1 )))
    text_encryption = "".join(char_encryption)
print(text_encryption)


# 同行键盘字符串
# 给定一个字符串数组 words，只返回可以使用在美式键盘同一行的字母打印出来的单词
str1 = "qwertyuiop"
str2 = "asdfghjkl"
str3 = "zxcvbnm"
words = ["Twitter", "TOTO", "FishC", "Python", "ASL"]
words_new = []
for word in words:
    i = 1
    if str1.find(word[0].lower()) != -1:
        while i < len(word):
            if str1.find(word[i].lower()) != -1:
                i += 1
            else:
                break
    elif str2.find(word[0].lower()) != -1:
        while i < len(word):
            if str2.find(word[i].lower()) != -1:
                i += 1
            else:
                break
    else:
        while i < len(word):
            if str3.find(word[i].lower()) != -1:
                i += 1
            else:
                break
    if i == len(word):
        words_new.append(word)
print(words_new)
# ['Twitter', 'TOTO', 'ASL']

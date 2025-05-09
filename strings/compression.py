# 压缩与解压
# 利用字符重复出现的次数，编写一个程序，实现基本的字符串压缩功能。比如，字符串 FFiiiisshCCCCCC 压缩后变成 F2i4s2h1C6（15字符 -> 10字符，66% 压缩率）。
# 对于重复次数小于 3 的字符，我们的程序应该选择不对其进行压缩。
string = "FFiiiisshCCCCCC"
# 压缩后：FFi4sshC6
# 压缩率为：60.00%
# string = input("请输入待压缩字符串：")
string_comp = []
temp = 0
char = 0
while char < len(string):
    index = string.find(string[char], char)
    while index != -1:
        temp += 1
        index = string.find(string[char], char + temp)
    else:
        if temp < 3:
            for i in range(temp):
                string_comp.append(string[char])
        else:
            string_comp.append(string[char])
            string_comp.append(str(temp))
    char = char + temp
    temp = 0
string_comp1 = ''.join(string_comp)
print("压缩后的字符串：", string_comp1)
print("压缩率为：", f"{len(string_comp) / len(string):.2%}")

# 解压
string_decomp = []
char = 0
while char < len(string_comp1):
    if string_comp1[char].isalpha():
        string_decomp.append(string_comp1[char])
    elif string_comp1[char].isdigit():
        for i in range(int(string_comp1[char]) - 1):
            string_decomp.append(string_comp1[char - 1])
    char += 1
string_decomp1 = ''.join(string_decomp)
print("解压后的字符串:", string_decomp1)

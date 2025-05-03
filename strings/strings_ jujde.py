# 判断
# startswith(prefix[,start[,end]]) 参数指定的子字符串是否在字符串的起始位置
# endswith(prefix[,start[,end]]) 参数指定的子字符串是否在字符串的末尾位置

# isupper() 是否全都为大写
# islower() 是否全都为小写
# istitle() 是否所有字母都为开头字母大写
# isalpha() 是否全都为字母
# isascii() 是否为ASCII码
# isspace() 是否为空格
# isprintable() 是否可打印
# isdecimal() 是否都为十进制数字
# isdigit() 是否都为数字字符
# isnumeric() 是否都是数值字符（小数不行。小数有点）
# isalnum() 是否只包含字母和数字（数字为isnumeric级）
# isidentifier() 是否为合法的标识符（如：变量名）

# 以“ ”为起始，结尾
x = "I love FishC"
print(x.startswith("I"))
# True
print(x.endswith("FishC"))
# True
print(x.endswith("C"))
# True
print(x.endswith("c"))
# False
print(x.endswith("hC"))
# True
print(x.endswith("Fi", 0, 9))
# True
# 还支持以元组的形式输入，元组中只要有一个成功匹配就返回True
print(x.startswith(("her", "hew", "I")))
# True

# 是否为字母、空格、可打印
print(x.istitle())
# False
print(x.isupper())
# False
print(x.upper().isupper())
# True 强制True  先转换成大写再判断
print(x.islower())
# False
print(x.isalpha())
# False 其中还有空格
print("   \n".isspace())
# True tab,空格,\n都算空格
print("   \n".isprintable())
# False 转义字符不可打印

# 是否为数字
x = "12345"
print(x.isdecimal())
# True
print(x.isdigit())
# True
print(x.isnumeric())
# True

# 使用unicode字符串输出平方符号
x = "2\u00b2"
print(x)
# 2²
print(x.isdecimal())
# False
print(x.isdigit())
# True
print(x.isnumeric())
# True

# 罗马字符
x = "ⅠⅡⅢⅣⅤⅥ"
print(x.isdecimal())
# False
print(x.isdigit())
# False
print(x.isnumeric())
# True
print(x.isalnum())
# True

# 是否为标识符
print("I am a good boy".isidentifier())
# False
print("I_am_a_good_boy".isidentifier())
# True
print("FishC520".isidentifier())
# True
print("520FishC".isidentifier())
# False

# 关键字
import keyword
print(keyword.iskeyword("if"))
# True

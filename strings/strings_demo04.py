# 截取字符串
# 以所给字符串中单个字符串为单位来剔除
# strip(chars=None) 以所给字符串中单个字符串为单位来剔除当前字符串左右字符
# lstrip(chars=None) 以所给字符串中单个字符串为单位来剔除当前字符串左侧字符
# rstrip(chars=None) 以所给字符串中单个字符串为单位来剔除当前字符串右侧字符
# 剔除掉指定的子字符串
# removeprefix(prefix) 剔除掉整个字符串的指定前缀
# removesuffix(psuffix) 剔除掉整个字符串的指定后缀
# 截取掉空白
print("    左侧不要留白".lstrip())
# 左侧不要留白
print("右侧不要留白    ".lstrip())
# 右侧不要留白
print("    左右都不要留白    ".lstrip())
# 左右都不要留白
print("www.ilovefishc.com".lstrip("wcom.lh"))
# ilovefishc.com
print("www.ilovefishc.com".rstrip("wcom.lh"))
# www.ilovefis
print("www.ilovefishc.com".strip("wcom.lh"))
# ilovefis

print("www.ilovefishc.com".removeprefix("www."))
# ilovefishc.com
print("www.ilovefishc.com".removesuffix(".com"))
# www.ilovefishc
print("www.ilovefishc.com".removeprefix("love"))
# www.ilovefishc.com


# 拆分和拼接
# partition(sep) 根据所给字符串从左到右查找来分割当前字符串，并返回相应的三元组
# rpartition(sep) 根据所给字符串从右到左查找来分割当前字符串，并返回相应的三元组
print("www.ilovefishc.com".partition("."))
print("www.ilovefishc.com".rpartition("."))

# split(sep=None,maxsplit=-1) 默认从左到右以空格来切割，不限次数切割，将结果以列表形式返回
# rsplit(sep=None,maxsplit=-1) 默认从右到左以空格来切割，不限次数切割，将结果以列表形式返回
# 换行符：\n,\r
# splitlines(keepends=False) 按行切割，将结果以列表形式返回 keepspends 指定结果是否包含换行符
print("www.ilovefishc.com".split(".", 1))
# ['www', 'ilovefishc.com']
print("www.ilovefishc.com".rsplit(".", 1))
# ['www.ilovefishc', 'com']
print("www\nilovefishc\rcom".splitlines())
# ['www', 'ilovefishc', 'com']
print("www\nilovefishc\rcom".splitlines("True"))
# ['www\n', 'ilovefishc\r', 'com']

# join(iterable) 字符串拼接
print(".".join(["www", "ilovefishc", "com"]))
# www.ilovefishc.com

# split() 方法常常被应用于对数据的解析处理，那么考考大家，如果要从字符串 "https://ilovefishc.com/html5/index.html"
# 中提取出 "ilovefishc.com"，使用 split() 方法应该如何实现呢？
url = "https://ilovefishc.com/html5/index.html"
parsed_url = url.split("https://")[1].split("/")[0]
print(parsed_url)
# ilovefishc.com

print(",\n".join("FishC"))
# F,
# i,
# s,
# h,
# C

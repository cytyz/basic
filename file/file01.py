# 文件永久存储
# 临时：内存，永久：硬盘
# open()    打开一个文件并返回其对应的文件对象
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# r 读取；w 打开文件，若存在则覆盖；a 追加；+ 更新文件（读取和写入）
# b 二进制；t 文本模式；x 如果文件已存在则创建失败
# write(text)    将字符串写入并返回字符个数
# writelines(lines)    可以将多个字符串写入，不会自动换行，无返回值
# EOF    End Of the File，表示文件末尾的位置
f = open("FishC.txt", "w")
print(f.write("Hello, FishC"))
f.writelines(["Hello, FishC\n", "I love FishC"])
f.close()    # 关闭并写入， flush 刷新并写入

f = open("FishC.txt", "r+")
print(f.readable())    #True
print(f.writable())    #True

for each in f:
    print(each)
# Hello, FishCHello, FishC
#
# I love FishC
print(f.read())    # 文件读取会继续读取后面的内容，但此时文件已经读取完毕，故读取内容为空
# tell()    查询现在读取到了第几个字符
# seek()    修改文件指针，0 文件起始位置；1 当前位置；2 文件末尾
print(f.tell())    # 38
f.seek(0)
# readline()    每次读取一行
print(f.readline())    # Hello, FishCHello, FishC
print(f.read())    # I love FishC

f.write("I love my wife")
f.flush()

# truncate 将文件对象截取到指定位置
f.truncate(29)
f.close()

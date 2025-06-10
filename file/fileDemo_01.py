# 文件截取练习
# 对FishC.txt，截取其中第 10~15 个字符，并保存为新文件（FishD.txt）
f1 = open("FishC.txt", "r")
f2 = open("FishD.txt", "w")

f1.seek(10)
f2.write(f1.read(5))

f1.close()
f2.close()

# 对FishC.txt，截取前面 15 个字符，并保存覆盖保存原文件。
f = open("FishC.txt", "r+")
f.truncate(15)
f.close()

# 打开自己的源文件，然后打印出来
f3 = open("fileDemo_01.py", "r", encoding="utf-8")
for line in f3:
    print(line, end="")
f3.close()

# 图片隐写术   在图片中隐藏文件
# 将压缩文件的内容，追加写入到图片文件的尾部，更改后缀名为zip或rar即可查看压缩文件(二进制)
f4 = open("test.jpg", "ab")
f5 = open("target.zip", "rb")

f4.write(f5.read())

f4.close()
f5.close()

print("finished")

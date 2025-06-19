# 文件搜索
# 先打印路径结构
# 然后通过类和对象的方式来存储每一个文件信息（包含文件名、文件尺寸、位置、创建时间、修改时间和访问时间），并定义相应的方法来获取这些文件信息
# 最后编写一个搜索函数，通过提供文件名的方式搜索对应的文件位置和信息
from time import strftime, localtime
from pathlib import Path
class File:
    def __init__(self, name, size, folder, ctime, mtime, atime):
        self.name = name
        self.size = size
        self.folder = folder
        self.ctime = ctime
        self.mtime = mtime
        self.atime = atime

    def get_name(self):
        return self.name

    def get_size(self):
        return f"{self.size}字节"

    def get_folder(self):
        return f"位置：{self.folder}"

    def get_ctime(self):
        return f"创建时间：{strftime("%Y-%m-%d %H:%M:%S", localtime(self.ctime))}"

    def get_mtime(self):
        return f"修改时间：{strftime("%Y-%m-%d %H:%M:%S", localtime(self.mtime))}"

    def get_atime(self):
        return f"访问时间：{strftime("%Y-%m-%d %H:%M:%S", localtime(self.atime))}"

def get_file_msg(path):
    p = Path(path)
    paths = []
    files = []
    for i in p.glob("**/*"):
        paths.append(i)
        if i.is_file():
            name = i.name
            size = i.stat().st_size
            folder = i.parent.resolve()
            ctime = i.stat().st_ctime
            mtime = i.stat().st_mtime
            atime = i.stat().st_atime
            files.append(File(name, size, folder, ctime, mtime, atime))

    print("路径结构如下：")
    for each in paths:
        print(each)

    return files

def sear_file(files):
    count = 0
    filename = input("\n请输入想要搜索的文件名：")
    for each in files:
        if filename in each.name:
            count += 1
            print(f"\n找到相关文件（{count}）-> {each.get_name()}（{each.get_size()}）")
            print(each.get_folder())
            print(each.get_ctime())
            print(each.get_mtime())
            print(each.get_atime())
        else:
            print("找不到相关文件！")

files = get_file_msg("target")
sear_file(files)

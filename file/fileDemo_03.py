# 文件with练习
# 在 pathlib 模块中，Path 对象有一个 glob() 方法，它提供了向下递归搜索的能力（如下），请自己编写一个递归函数，实现相同的搜索功能
from pathlib import Path
p = Path("..")
# print(list(p.glob("**/*.txt")), end="\n")

files = []
def get_file(p, files, target):
    for each in p.iterdir():
        if each.is_file() and each.suffix == target:
            files.append(each)
        if each.is_dir():
            p = each
            get_file(p, files, target)
    return files

print(get_file(p, files, ".txt"))

# 请下载附件（  target.zip (5.56 KB, 下载次数: 597) ），自动统计该文件夹中的 Python 总代码行数。

# A. 其中包含的子文件夹，也需要一并统计入内
# B. 空行不能算
# C. 本题的源代码不统计入内
# 提示1：可以通过 __file__ 得到包含本源代码文件名的路径（字符串类型）
# 提示2：如果是 windows 系统，打开带中文文件，可能会引发编码错误，此时在 open() 函数中使用 errors="ignore" 参数来避免该问题
# 提示3：使用递归搜索反而会更简单一些

def get_files(p, files):
    for each in p.iterdir():
        if str(each) == __file__: # 跳过本文件
            continue
        if each.is_file() and each.suffix == ".py":
            files.append(each)
        if each.is_dir():
            p = each
            get_files(p, files)
    return files

def count_lines(files):
    lines = 0
    for each in files:
        with open(each, "r", errors="ignore") as f1: # 忽略错误编码
            t = f1.readlines()
            lines += len(t) - t.count("\n")
    return lines

p = Path(r".\target1")
files = []

files = get_files(p, files)
print(f"一共有{count_lines(files)}行代码")


# 编写一个源代码文件，其功能就是在当前文件夹下创建 10 个子文件夹，每个子文件夹下又放入自身的 10 个拷贝
def create_files(p, n):
    if n == 0:
        return None
    else:
        # p / f"{n-1}.py" 是拼接源代码的文件名
        with open(__file__, "r", encoding="utf-8") as f1, open(p / f"{n-1}.py", "w", encoding="utf-8") as f2:
            f2.write(f1.read())
        create_files(p, n-1)

def create_dirs(cwd, n):
    if n == 0:
        return None
    else:
        p = cwd / str(n-1) # 拼接新文件夹的路径
        p.mkdir(exist_ok=True) # 确保文件夹已存在也不会报错
        create_files(p, 10) # 创建10个源代码文件拷贝
        create_dirs(cwd, n-1)

# create_dirs(Path.cwd(), 10)

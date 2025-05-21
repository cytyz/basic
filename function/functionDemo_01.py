# 注册与登录模块
# 请编写一个实现【注册】和【登陆】功能的代码，这次要求将不同的功能封装成独立的函数
# 编写 4 个函数分别用于获取用户指令（get_int()）、注册（register()）、登陆（login()）、MD5加密（encrypt()）
# 使用一个 Python 的字典作为数据库。
# 注册时需验证用户名是否已存在于数据库
# 登陆时需验证用户名和密码是否匹配
# 密码保存需使用 MD5 加密
import hashlib
print("欢迎来到鱼C论坛~")
user = dict()
def get_int():
    print("==========================")
    print("1.注册")
    print("2.登录")
    print("3.退出")
    _ = input("请输入指令：")
    return _

def register():
    print("==========================")
    user_name = input("请输入用户名（输入q退出注册）：")
    if user_name == "q":
        return user
    while user_name in user:
        user_name = input("用户名重复，请重新输入用户名（输入q退出注册）：")
        if user_name == "q":
            return user
    user_pwd = input("请输入密码：")
    user[user_name] = encrypt(user_pwd)
    print("恭喜，注册成功~")
    return user

def login():
    print("==========================")
    user_name = input("请输入用户名（输入q退出登录）：")
    if user_name == "q":
        return 0
    while user_name not in user:
        print("用户名不存在。")
        user_name = input("请重新输入用户名（输入q退出登录）：")
        if user_name == "q":
            return 0
    user_pwd = input("请输入密码：")
    if user_pwd == "q":
        return 0
    while encrypt(user_pwd) != user[user_name]:
        print("密码错误！")
        user_pwd = input("请重新输入密码：")
    print("恭喜，登录成功~")
    return 0

def encrypt(pwd):
    pwd = hashlib.md5(str(pwd).encode("utf-8")).hexdigest()
    return pwd

while True:
    select = get_int()
    if select == "1":
        register()
    elif select == "2":
        login()
    elif select == "3" :
        break
    else:
        print("指令错误，请重新输入！")

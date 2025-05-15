# MD5单向加密
# 请按照要求编写一个网站的注册模块
# 我们知道，通常一个网站的用户名都是唯一的，这就要求注册的时候，系统代码可以识别当前输入的用户名是否已经存在？
# 如果存在，则不允许注册！
# 那么现在请大家一起来动手，编写一个网站的注册模块。
# 要求：
# 用户名不允许重复
# 数据库需要保存用户名及密码
# 初始用户及密码（"小甲鱼":"I_love_FishC"，"不二如是":"FishC5201314"）

# ——————————————————————————————————
# 单向加密 MD5 通过密码无法逆向获得明文的加密手段
# hashlib.md5() 的参数是需要一个 b 字符串（即 bytes 类型的对象），这里可以使用 bytes("123", "utf-8") 的方式将 "123" 转换为 b"123"。
import hashlib
user_pwd1 = hashlib.md5(b"I_love_FishC")
user_pwd2 = hashlib.md5(b"FishC5201314")
user_pwd1_md5 = user_pwd1.hexdigest()
user_pwd2_md5 = user_pwd2.hexdigest()
user = {"小甲鱼":user_pwd1_md5, "不二如是":user_pwd2_md5}
user_name = input("请输入用户名：")
while user_name in user.keys():
    print("该用户名已被注册！")
    user_name = input("请重新输入用户名：")
else:
    user_pwd = input("请输入密码：")
    # encode("utf-8") 也能转换成 byte 类型
    user_pwd = hashlib.md5(user_pwd.encode("utf-8")).hexdigest()
user[user_name] = user_pwd
print("-----------------")
print("目前已注册的用户有：")
user1 = iter(user)
for i in range(len(user)):
    user_name1 = next(user1)
    print(user_name1, ":", user[user_name1])

# 存查电影数据
# 编写一个存储电影数据的小程序。
# 需要存放的数据如下：
# 电影名称
# 上映时间
# 导演（可能有多人）
# 主演（通常有多人）
# 电影评分
# 无间道
# 2003-09-05
# 刘伟强 / 麦兆辉
# 刘德华 / 梁朝伟 / 黄秋生 / 曾志伟 / 郑秀文
# 9.3

print("欢迎进入鱼C影评小程序")
print("1.数据录入")
print("2.查询数据")
print("3.退出程序")
movie = dict()

while True:
    start = input("请输入想要的功能(1/2/3)：")
    if start == "1":
        movie_name = input("请输入电影名称：")
        movie_date = input("请输入上映日期：")
        movie_director = input("请输入导演名字（多人请用 / 分隔）：")
        movie_actor = input("请输入演员名字（多人请用 / 分隔）：")
        movie_score = input("请输入电影评分：")
        movie[movie_name] = movie_date, movie_director, movie_actor, movie_score
    elif start == "2":
        movie_search = input("请输入电影名称：")
        if movie_search in movie:
            print("电影名称：", movie_search)
            print("上映时间：", movie[movie_search][0])
            print("导演名单：", movie[movie_search][1])
            print("演员名单：", movie[movie_search][2])
            print("当前评分：", movie[movie_search][3])
            break
        else:
            print("查无此片！")
    else:
        break


# 电话簿
print("欢迎进入鱼C电话簿")
phone_book = {}
while True:
    start = input("请输入命令（I：录入 / C：查询 / D：删除 / P：打印 / E：退出）：")
    if start == "I":
        print("-- 录入模式 --")
        while True:
            name = input("请输入姓名：")
            if name in phone_book:
                print("该姓名已录入，手机号码是：", phone_book[name])
                cont1= input("请问是否修改（Y/N）：")
                if cont1 == "Y":
                    phone_number = input("请输入新的电话号码：")
                    phone_book[name] = phone_number
                elif cont1 == "N":
                    break
            else:
                phone_number = input("请输入电话号码：")
                while not (phone_number.isdigit() and len(phone_number) == 10):
                    phone_number = input("输入不合法，请重新输入：")
                phone_book[name] = phone_number
            cont = input("是否继续录入（Y/N）：")
            if cont == "Y":
                continue
            else:
                break
    elif start == "C":
        print("-- 查询模式 --")
        while True:
            phone_search = input("请输入姓名：")
            if phone_search in phone_book:
                print(phone_search, ":", phone_book[phone_search])
            else:
                print("查询不到该联系人")
            cont2 = input("是否继续查询（Y/N）：")
            if cont2 == "Y":
                continue
            else:
                break
    elif start == "D":
        print("-- 删除模式 --")
        while True:
            phone_del = input("请输入姓名：")
            if phone_del in phone_book:
                del phone_book[phone_del]
            else:
                print("查询不到该联系人")
            cont3 = input("是否继续删除（Y/N）：")
            if cont3 == "Y":
                continue
            else:
                break
    elif start == "P":
        print("-- 打印模式 --")
        print(phone_book)
    else:
        break

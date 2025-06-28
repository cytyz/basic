# 鱼C超市会员管理系统。
# 1. 会员开卡
# 会员开卡自动赋予一个新的卡号（默认从 10000 开始递增）
# 要求输入用户名和密码
# 密码要求长度不低于 6 位

# 2. 修改密码
# 先确认输入卡号是否存在
# 再判断旧密码是否正确
# 新密码长度同样不能低于 6 位
#
# 3. 商品支付
# 先确认输入卡号是否存在
# 再判断密码是否正确
# 根据输入的消费金额增加会员卡积分（比如输入 250 消费金额，那么积分增加 250）
#
# 4. 积分查询
# 先确认输入卡号是否存在
# 再判断密码是否正确
#
# 代码要求：
# 1. 创建一个会员类（Member），包含信息：卡号、用户名、密码（要求密码需要以 MD5 哈希值的形式存储）、积分、注册日期
# 2. 创建一个管理类（Manage），用于实现上方要求的主要程序功能
# 3. 创建一个 Mixin 类（PasswdMixin），用于实现密码相关的功能组件（密码长度检测和将明文密码转换为 MD5 的操作）
# 4. 创建一个 Mixin 类（LoggerMixin），用于实现日志记录相关的功能组件
import hashlib
import time

# 卡号、用户名、密码、积分、注册日期
class Member:
    def __init__(self, cardid, name, password, scores, regdata):
        self.cardid = cardid
        self.name = name
        self.password = password
        self.scores = scores
        self.regdata = regdata

# 密码长度检测和将明文密码转换为 MD5
class PasswdMixin:
    def tooshort(self, password, request=6):
        while len(password) < request:
            password = input(f"会员密码不能小于{request}位，请重新输入")
        return password

    def to_md5(self, password):
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        return password

# 实现日志记录相关的功能
class LoggerMixin:
    def log(self, message, filename="log.txt"):
        with open(filename, "a") as f:
            f.write(message)


# 主要功能
class Manager(PasswdMixin, LoggerMixin):
    def __init__(self):
        self.member = {}
        self.cardid = 10000

    def welcome(self):
        print("欢迎来到超市会员管理系统")
        command = 0
        while command != "5":
            command = input("\n1.创建新卡;2.修改密码;3.商品支付;4.积分查询;5.退出程序：")
            if command == "1":
                self.create_member()
            elif command == "2":
                self.change_password()
            elif command == "3":
                self.pay()
            elif command == "4":
                self.check_scores()
            elif command == "5":
                print("感谢使用超市会员管理系统")

    def create_member(self):
        name = input("请输入姓名：")
        password = input("请输入密码:")
        password = self.tooshort(password)
        password = self.to_md5(password)
        regdata = time.localtime()
        scores = 0
        member = Member(self.cardid, name, password, scores, regdata)
        self.member[self.cardid] = member
        print(f"创建成功，卡号为 {self.cardid}，关联用户 -> {name}")
        self.log(f"开卡成功: {self.cardid} -> {name}, 时间:{time.strftime("%Y-%m-%d %H:%M:%S", regdata)}")
        self.cardid = self.cardid + 1

    def confirm_password(self):
        cardid = int(input("请输入卡号:"))
        while cardid not in self.member:
            cardid = input("该卡号不存在,请重新输入:")

        password = input("请输入密码:")
        password = self.to_md5(password)
        while not self.member[cardid].password == password:
            password = input("密码错误,请重新输入:")
            password = self.to_md5(password)
        return cardid

    def change_password(self):
        cardid = self.confirm_password()
        newpassword = input("请输入新密码:")
        newpassword = self.tooshort(newpassword)
        newpassword = self.to_md5(newpassword)
        self.member[cardid].password = newpassword
        self.log(f"修改密码: 卡号 -> {cardid}, 时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())})")
        print("密码修改成功.")

    def pay(self):
        cardid = self.confirm_password()
        money = input("请输入支付金额:")
        self.member[cardid].scores += money
        self.log(f"积分累计: 卡号 -> {cardid}, +{money}分, 时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")

    def check_scores(self):
        cardid = self.confirm_password()
        print(f"卡号 {cardid} 当前的消费积分为: {self.member[cardid].scores}")

def main():
    m = Manager()
    m.welcome()

if __name__ == '__main__':
    main()

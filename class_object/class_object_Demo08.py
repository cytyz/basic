# 银行账户管理系统
# a. 创建账户
# 需要提供姓名和密码（要求密码需要以 MD5 哈希值的形式存储）
# 银行卡号自动生成
# 支持预存款
#
# b. 删除账户
# 需要验证卡号、姓名和密码
#
# c. 查询余额
# 需要验证卡号和密码
#
# d. 存款
# 需要验证卡号和密码
# 输入金额
#
# e. 取款
# 需要验证卡号和密码
# 输入金额，并检查余额是否足够
#
# f. 转账
# 需验证我方卡号和密码，验证对方卡号是否存在
# 输入金额，并检查我方余额是否足够
#
# 程序输入限制（如用户不按要求输入，必须予以纠正）：
# 密码必须是 6 位数字
# 金额必须是非负数
# 卡号必须是正整数
#
# 相关类的实现可以参考下面结构（当然你也可以按照自己的想法去构造）：
# PasswdMixin（Mixin 类，用于实现与密码相关的功能组件）
# is_valid() -- 检测密码长度
# to_md5() -- 将明文密码转换为 MD5 存储
#
# Account（基本账户类）
# confirm_name() -- 确认姓名是否匹配
# confirm_passwd() -- 确认密码是否匹配
# withdraw() -- 取款
# deposit() -- 存款
# transfer() -- 转账
# get_balance() -- 查询余额
#
# UserManager（账户管理类）
# check_account() -- 检查账户是否存在及密码是否正确
# create_account() -- 创建账户
# delete_account() -- 删除账户
# get_account() -- 获取账户
import hashlib

class PasswdMixin:
    # 检测密码长度
    def is_valid(self, passwd):
        while True:
            if len(passwd) != 6 or not passwd.isdigit():
                passwd = input("密码需为6位数字，请重新输入：")
            else:
                break
        return passwd

    # 密码转换为 md5 存储
    def to_md5(self, passwd):
        passwd = hashlib.md5(passwd.encode("utf-8")).hexdigest()
        return passwd

class Account(PasswdMixin):
    def __init__(self, username, password, cardid, balance):
        self.username = username
        self.password = password
        self.cardid = cardid
        self.balance = balance

    # 确认姓名
    def confirm_name(self, name):
        return name == self.username

    # 确认密码
    def confirm_password(self, password):
        return password == self.password

    # 取款
    def withdraw(self, money):
        if self.balance < money:
            print(f"您的账户不足{money}元，无法取款")
        else:
            self.balance -= money
            print(f"成功取出{money}元。")

    # 存款
    def deposit(self, money):
        self.balance += money
        print(f"成功存入{money}元")

    # 转账
    def transfer(self, account, money):
        if self.balance < money:
            print(f"您的账户不足{money}元，无法转账")
        else:
            self.balance -= money
            account.balance += money
            print(f"成功转账{money}元。")

    # 查询余额
    def get_balance(self):
        return self.balance

class UserManager(PasswdMixin):
    def __init__(self):
        self.accounts = {}
        self.cardid = 88888888

    # 检测账户密码
    def check_account(self, cardid, password):
        if self.accounts.get(cardid):
            account = self.accounts[cardid]
            password = account.to_md5(password)
            if account.confirm_password(password):
                return True
            else:
                print("密码错误，请重新输入：")
                return False
        else:
            print("账户不存在")
            return False

    # 创建账户
    def create_account(self, name, password, money=0):
        password = self.is_valid(password)
        password = self.to_md5(password)
        account = Account(name, password, self.cardid, money)
        self.accounts[self.cardid] = account
        print(f"创建成功，卡号是：{self.cardid}")
        self.cardid += 1

    # 删除账户
    def delete_account(self, cardid, name, password):
        if self.check_account(cardid, password):
            account = self.accounts[cardid]
            if account.confirm_name(name):
                del self.accounts[cardid]
                print(f"卡号为：{cardid}的账号已删除已删除")
            else:
                print(f"用户名：{name}输入错误")

    def get_account(self, cardid, password, nopassword=False):
        if nopassword:
            if self.accounts.get(cardid):
                account = self.accounts[cardid]
                return account
            else:
                print("该账户不存在")
                return None
        else:
            if self.check_account(cardid, password):
                return self.accounts[cardid]
            else:
                return None

def main():
    bank = UserManager()

    # 需要获取那些信息
    def get_msg(cardid=False, name=False, passwd=False):
        msg = {"cardid":None, "name":None, "passwd":None}
        if cardid:
           msg["cardid"] = get_integer_input("请输入卡号：")
        if name:
            msg["name"] = input("请输入姓名：")
        if passwd:
            msg["password"] = input("请输入密码：")
        return msg

    # 获取整数
    def get_integer_input(str):
        while True:
            try:
                num = int(input(str))
                if num < 0:
                    raise ValueError
                break
            except ValueError:
                print("请输入一个有效的整数！")
        return num

    # 获取浮点数
    def get_float_input(str):
        while True:
            try:
                num = float(input(str))
                if num < 0:
                    raise ValueError
                break
            except ValueError:
                print("请输入一个有效的数值！")
        return num

    while True:
        ins = input("1.创建账户/2.删除账户/3.查询余额/4.存款/5.取款/6.转账/7.退出")
        if ins == "1":
            msg = get_msg(cardid=False, name=True, passwd=True)
            money = get_float_input("请输入预存款：")
            bank.create_account(msg["name"], msg["password"], round(money, 2))

        elif ins == "2":
            msg = get_msg(cardid=True, name=True, passwd=True)
            bank.delete_account(msg["cardid"], msg["name"], msg["password"])

        elif ins == "3":
            msg = get_msg(cardid=True, name=False, passwd=True)
            account = bank.get_account(msg["name"], msg["password"])
            if account:
                print(f"您的余额是：{account.get_balance()}")

        elif ins == "4":
            msg = get_msg(cardid=True, name=False, passwd=True)
            account = bank.get_account(msg["name"], msg["password"])
            if account:
                money = get_float_input("请输入金额：")
                account.deposit(round(money, 2))

        elif ins == "5":
            msg = get_msg(cardid=True, name=False, passwd=True)
            account = bank.get_account(msg["name"], msg["password"])
            if account:
                money = get_float_input("请输入金额：")
                account.withdraw(round(money, 2))

        elif ins == "6":
            msg = get_msg(cardid=True, name=False, passwd=True)
            account = bank.get_account(msg["name"], msg["password"])
            if account:
                target_cardid = get_integer_input("请输入卡号：")
                target_account = bank.get_account(target_cardid, None, True)
                if target_account:
                    money = get_float_input("请输入金额：")
                    account.transfer(target_account, round(money, 2))

        elif ins == "7":
            break

        else:
            print("请输入1~7的数字")

if __name__ == '__main__':
    main()

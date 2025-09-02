# 会员订单系统
# 根据不同的会员级别和促销活动计算订单的最终价格
# 创建一个 Discount 类，包含一个类属性 rate，表示折扣率，默认为 0。
# 实现一个类方法 set_rate(cls, rate)，用于设置折扣率。
# 实现一个静态方法 calculate(price)，用于根据当前的折扣率计算最终价格。
# 根据不同的会员级别（如普通会员、黄金会员、白金会员）设置不同的折扣率。
from itertools import product


class Discount:
    rate = 0

    @classmethod
    def set_rate(cls, rate):
        cls.rate = rate

    @staticmethod
    def calculate(price):
        return price * (1 - Discount.rate)


# 设置普通会员折扣率为 5%
Discount.set_rate(0.05)
original_price = 200
final_price = Discount.calculate(original_price)
print(f"原价：{original_price} 鱼币，普通会员折后价：{final_price} 鱼币")

# 设置高级会员折扣率为 10%
Discount.set_rate(0.10)
original_price = 200
final_price = Discount.calculate(original_price)
print(f"原价：{original_price} 鱼币，高级会员折后价：{final_price} 鱼币")

# 设置至尊会员折扣率为 20%
Discount.set_rate(0.20)
original_price = 200
final_price = Discount.calculate(original_price)
print(f"原价：{original_price} 鱼币，至尊会员折后价：{final_price} 鱼币")


# ———————————————————————————————————————————————————————————————————————
print("——————————————————————————————————————————————————————————————")
# 升级版
class Discount:
    price=0
    def __init__(self, rate=0):
        self.rate = rate

    def set_rate(self,rate):
        self.rate = rate

    @classmethod
    def set_price(cls, price):
        cls.price = price

    def calculate(self):
        return Discount.price * (1 - self.rate)

a = Discount()
original_price = 200
a.set_price(original_price)
a.set_rate(0.05)

b = Discount()
b.set_rate(0.10)

c = Discount()
c.set_rate(0.20)

final_price = a.calculate()
print(f"原价：{original_price} 鱼币，普通会员折后价：{final_price} 鱼币")
final_price = b.calculate()
print(f"原价：{original_price} 鱼币，普通会员折后价：{final_price} 鱼币")
final_price = c.calculate()
print(f"原价：{original_price} 鱼币，普通会员折后价：{final_price} 鱼币")


# ———————————————————————————————————————————————————————————————————————
print("————————————————————————————————————————————————————————————————")
# 日志记录器
# 该类包含一个类属性 log_file，表示日志文件的名称，默认为 app.log。
# 实现一个类方法 set_log_file(cls, filename)，用于更改日志文件的名称。
# 实现一个静态方法 log(message)，用于将日志消息写入指定的日志文件。
# 日志消息需要包含时间戳和日志级别（如 INFO、WARNING、ERROR）。
import datetime
class Logger:
    log_file = "app.log"

    # 更改日志文件的名称
    @classmethod
    def set_log_file(cls, filename):
        cls.log_file = filename

    # 写日志
    @staticmethod
    def log(message, level="INFO"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        log_message = f"{timestamp} [{level}]: {message}\n"
        with open(Logger.log_file, 'a') as f:
            f.write(log_message)

# 更改名称
Logger.set_log_file("fishc_app.log")

# 记录不同等级的日志
Logger.log("应用启动", level="INFO")
Logger.log("出现异常", level="ERROR")
Logger.log("用户登入", level="INFO")
Logger.log("内存空间不足", level="WARNING")

# 查看日志
with open(Logger.log_file, 'r') as f:
    content = f.read()
    print(content)


# ———————————————————————————————————————————————————————————————————————
print("————————————————————————————————————————————————————————————————")
# 库存管理系统
# 使用一个类属性 products，为一个列表，存储所有产品的实例。
# 实现一个类方法 add_product(cls, product)，用于将产品添加到 products 列表中。
# 实现一个静态方法 is_valid_product(product_info)，用于在添加产品前验证产品信息的有效性。
# 在产品实例化时，自动将自身添加到 products 列表中，并确保添加前通过验证。
class Product:
    # 类属性 products，存储所有产品的实例
    products = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        product_info = {'name': self.name, 'price': self.price}
        # 添加产品
        if self.is_valid_product(product_info):
            self.add_product(self)
            print(f"产品{self.name} 添加成功")
        else:
            print(f'无效的产品信息，无法添加产品{self.name}')

    @classmethod
    def add_product(cls, product):
        cls.products.append(product)

    # 验证产品
    @staticmethod
    def is_valid_product(product_info):
        if not product_info['name'] or not isinstance(product_info['name'],str):
            print("产品名称无效")
            return False
        if product_info['price'] <= 0:
            print("产品价格需要为正数")
            return False
        return True

# 添加产品信息
product1 = Product('苹果', 5)
product2 = Product('香蕉', 3)
product3 = Product('', 10)
product4 = Product('橙子', -2)

# 输出所有有效产品信息
for product in Product.products:
    print(f'产品名称：{product.name}, 价格：{product.price}')

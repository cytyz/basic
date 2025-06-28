# 汽车租赁系统
# 汽车类
# a. 车型分类：经济车型（EconomyCar）、豪华车（LuxuryCar）、跑车（SportCar）、SUV（SUV）
# b. 车辆通用属性：品牌（brand）、星号（model）、车牌（platenum）、每天租金（dayrent）、车辆编号（carid）
# c. 车辆通用方法：
# get_brand() -- 获取品牌
# get_model() -- 获取型号
# get_platenum() -- 获取车牌
# get_dayrent() -- 获取每天租金
# get_carid() -- 获取车辆编号
# calc_rent() -- 通过租赁天数和折扣计算一共需要多少租金
#
# d. 不同车型的特殊属性和方法：
# 经济车型享有额外的补贴优惠
# 豪华车需要增加保险费用
# 跑车需要增加损耗费用
# SUV 如果租车时间大于 7 天，原有折扣的基础上再打 7 折
#
# 业务类
# a. 属性：
# cars -- 字典类型，用于绑定车辆编号和相应的对象
# stocks -- 字典类型，用于存放每一种车型的库存
#
# b. 方法：
# operate() -- 程序入口，获取并分发指令
# register() -- 录入汽车
# get_stock() -- 获取库存
# rent_car() -- 租车服务
# return_car() -- 还车服务
class Car:
    # 品牌（brand）、星号（model）、车牌（platenum）、每天租金（dayrent）、车辆编号（carid）
    def __init__(self, brand, model, platenum, dayrent, carid):
        self.brand = brand
        self.model = model
        self.platenum = platenum
        self.dayrent = dayrent
        self.carid = carid

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_platenum(self):
        return self.platenum

    def get_dayrent(self):
        return self.dayrent

    def get_carid(self):
        return self.carid

    def calc_rent(self, days, discount=1):
        return self.dayrent * days * discount

# 经济型
class EconomyCar(Car):
    # 补贴
    def __init__(self, brand, model, platenum, dayrent, carid, subsidies):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.subsidies = subsidies

    def get_subsidies(self):
        return self.subsidies

    def calc_rent(self, days, discount=1):
        return super().calc_rent(days, discount) - self.subsidies * days

# 豪华车
class LuxuryCar(Car):
    # 保险
    def __init__(self, brand, model, platenum, dayrent, carid, insurance):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.insurance = insurance

    def get_insurance(self):
        return self.insurance

    def calc_rent(self, days, discount=1):
        return super().calc_rent(days, discount) + self.insurance * days

# 跑车
class SportCar(Car):
    # 损耗
    def __init__(self, brand, model, platenum, dayrent, carid, loss):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.loss = loss

    def get_loss(self):
        return self.loss

    def calc_rent(self, days, discount=1):
        return super().calc_rent(days, discount) + self.loss * days

# SUV
class SUV(Car):
    def calc_rent(self, days, discount=1):
        if days > 7:
            return super().calc_rent(days, discount) * 0.7

class CarOperation:
    # cars -- 字典类型，用于绑定车辆编号和相应的对象
    # stocks -- 字典类型，用于存放每一种车型的库存
    def __init__(self):
        self.cars = {}
        self.stocks = {"Economy":[], "Luxury":[], "Sport":[], "SUV":[]}
        self.carid1 = 10000
        self.carid2 = 20000
        self.carid3 = 30000
        self.carid4 = 40000

    # 指令
    def operate(self):
        print("欢迎使用鱼C汽车租赁程序")
        while True:
            ins = input("1.录入汽车；2.租车服务；3.还车服务；4.退出程序：")
            if ins == "1":
                self.register()
            if ins == "2":
                self.rent_car()
            if ins == "3":
                self.return_car()
            if ins == "4":
                break

    # 录入
    def register(self):
        op = input("\n1.经济车型；2.豪华车；3.跑车；4.SUV：")
        num = int(input("\n请输入需要录入的数量："))
        for i in range(num):
            print(f"\n请录入第{i + 1}量车")
            brand = input("品牌：")
            model = input("型号：")
            platenum = input("车牌：")
            dayrent = input("租金：")

            if op == "1":
                subsidies = input("补贴：")
                c = EconomyCar(brand, model, platenum, dayrent, self.carid1, subsidies)
                self.cars[self.carid1] = c
                self.stocks["Economy"].append(c)
                self.carid1 += 1

            if op == "2":
                insurance = float(input("保险："))
                c = LuxuryCar(brand, model, platenum, dayrent, self.carid2, insurance)
                self.cars[self.carid2] = c
                self.stocks["Luxury"].append(c)
                self.carid2 += 1

            if op == "3":
                loss = float(input("损耗："))
                c = SportCar(brand, model, platenum, dayrent, self.carid3, loss)
                self.cars[self.carid3] = c
                self.stocks["Sport"].append(c)
                self.carid3 += 1

            if op == "4":
                c = SUV(brand, model, platenum, dayrent, self.carid4)
                self.cars[self.carid4] = c
                self.stocks["SUV"].append(c)
                self.carid4 += 1

    # 获取库存
    def get_stock(self):
        print(f"\n1.经济车型（享有补贴），共有{len(self.stocks['Economy'])}")
        if self.stocks["Economy"]:
            for each in self.stocks['Economy']:
                print(f"车辆编号：{each.get_carid()}，品牌：{each.get_brand()}，型号：{each.get_model()}， 日租金：{each.get_dayrent()} - {each.get_subsidies()}（补贴）元")

        print(f"\n2. 豪华车（需额外购买保险），共有 {len(self.stocks['Luxury'])} 辆。")
        if self.stocks["Luxury"]:
            for each in self.stocks['Luxury']:
                print(f"车辆编号：{each.get_carid()}，品牌：{each.get_brand()}，型号：{each.get_model()}， 日租金：{each.get_dayrent()} + {each.get_insurance()}（保险）元")

        print(f"\n3. 跑车（需增加损耗费用），共有 {len(self.stocks['Sport'])} 辆。")
        if self.stocks["Sport"]:
            for each in self.stocks['Sport']:
                print(f"车辆编号：{each.get_carid()}，品牌：{each.get_brand()}，型号：{each.get_model()}， 日租金：{each.get_dayrent()} + {each.get_loss()}（损耗）元")

        print(f"\n4. SUV（租赁超过7天，享有额外折上7折优惠），共有 {len(self.stocks['SUV'])} 辆。")
        if self.stocks["SUV"]:
            for each in self.stocks['SUV']:
                print(f"车辆编号：{each.get_carid()}，品牌：{each.get_brand()}，型号：{each.get_model()}， 日租金：{each.get_dayrent()}元")

    # 租车
    def rent_car(self):
        self.get_stock()
        carid = input("请输入需要租赁的车辆编号：")
        if self.cars.get(carid):
            car = self.cars[carid]
            if carid // 10000 == 1:
                self.stocks["Economy"].remove(car)
            if carid // 10000 == 2:
                self.stocks["Luxury"].remove(car)
            if carid // 10000 == 3:
                self.stocks["Sport"].remove(car)
            if carid // 10000 == 4:
                self.stocks["SUV"].remove(car)

            days = int(input("请输入需要租赁的天数："))
            if days > 5:
                cost = car.calc_rent(days, discount=0.8)
            elif days > 3:
                cost = car.calc_rent(days, discount=0.9)
            else:
                cost = car.calc_rent(days)

            print(f"租赁{days}天，总共需要花费：{cost}元")
            print("恭喜，租赁成功！")

    # 还车
    def return_car(self):
        carid = input("请输入车辆编号：")
        if self.cars.get(carid):
            car = self.cars[carid]
            if carid // 10000 == 1:
                self.stocks["Economy"].append(car)
            if carid // 10000 == 2:
                self.stocks["Luxury"].append(car)
            if carid // 10000 == 3:
                self.stocks["Sport"].append(car)
            if carid // 10000 == 4:
                self.stocks["SUV"].append(car)
            print("恭喜，还车成功!")

def main():
    car_op = CarOperation()
    car_op.operate()

if __name__ == "__main__":
    main()

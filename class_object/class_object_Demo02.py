# 动物园组合
# 定义一个动物园类（Zoo），里面有鸟类如 1 只孔雀（Peacock）、2 只天鹅（Swan）、3 只八哥（Myna），猫科动物类如 4 头狮子（Lion）、5 头老虎（Tiger）、6 头豹子（Leopard），灵长类（Primate）如 7 只猴子（Monkey）、8 只猩猩（Chimpanzee）、9 只狒狒（Baboon），只需要定义类的构成框架就行，内部用 pass 语句填充即可
class Birds:
    pass

class Peacock:
    pass

class Swan:
    pass

class Myna:
    pass


class Cats:
    pass

class Lion:
    pass

class Tiger:
    pass

class Leopard:
    pass


class Primate:
    pass

class Monkey:
    pass

class Chimpanzee:
    pass

class Baboon:
    pass


class zoo:
    peacocks = Peacock()
    swan = [Swan(), Swan()]
    mynas = [Myna(), Myna(), Myna()]
    lions = [Lion() for i in range(4)]
    tigers = [Tiger() for i in range(5)]
    leopards = [Leopard() for i in range(6)]
    monkeys = [Monkey() for i in range(7)]
    chimpanzees = [Chimpanzee() for i in range(8)]
    baboons = [Baboon() for i in range(9)]

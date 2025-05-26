# 洗牌算法 —— Fisher-Yates 与斗地主
# 对于该算法的实现描述如下（假设需要打乱 N 个数）：
# 写下从 1 到 N 的数字
# 获取一个 1 到剩下数字（包括这个数字）的随机数 k
# 从低位开始，取出第 k 个数字（这个数字还没有被取出），把它写在独立的一个列表的最后一位
# 重复前两个步骤，直到所有数据都被取出
import random
def fy_shuffle(data, num=1):
    for i in range(num):
        target = list(data)
        result = []
        while target:
            pop_num = random.randint(0, len(target) - 1)
            result.append(target.pop(pop_num))
        print(f"第{i}次打乱后的结果：{"".join(result)}")
    return "".join(result)

def input_data():
    data = input("请输入需要打乱的序列：")
    num = int(input("请输入需要打乱的次数："))
    print(f"最终的结果是：{"".join(fy_shuffle(data, num))}")

    pass

input_data()

# 斗地主
import random

cards = ["♦1", "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K",
         "♥1", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K",
         "♣1", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K",
         "♠1", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K",
         "☀", "🌙"]


def fy_shuffle(x, n=1):
    for i in range(n):
        target = list(x)
        result = []
        while target:
            r = random.randint(0, len(target) - 1)  # 步骤2
            result.append(target.pop(r))  # 步骤3

    return result


def dealCards():
    a = input("请输入第一位游戏玩家名称：")
    b = input("请输入第二位游戏玩家名称：")
    c = input("请输入第三位游戏玩家名称：")

    r = {}
    r[a], r[b], r[c] = [], [], []

    new_cards = fy_shuffle(cards, 3)

    for i in range(17):
        r[a].append(new_cards.pop())
        r[b].append(new_cards.pop())
        r[c].append(new_cards.pop())

    d = random.sample((a, b, c), 1)[0]
    print(f"\n地主是：{d}\n")
    r[d].extend((new_cards.pop(), new_cards.pop(), new_cards.pop()))

    print(f"[{a}]拿到的牌是：{' '.join(r[a])}\n")
    print(f"[{b}]拿到的牌是：{' '.join(r[b])}\n")
    print(f"[{c}]拿到的牌是：{' '.join(r[c])}")


dealCards()

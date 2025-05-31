# 斗地主打牌版
import random

def show_cards():
    all_cards = ["♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K", "♦1", "♦2",
             "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K", "♥1", "♥2",
             "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K", "♣1", "♣2",
             "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K", "♠1", "♠2",
             "🌙", "☀"]
    for i in range(len(all_cards)):
        print(all_cards[i], end=" ")
        if (i + 1) % 13 == 0 or i == 53:
            print()

# 洗牌
# def fy_shuffle(x, n=1):
#     for i in range(n):
#         target = list(x)
#         result = []
#         while target:
#             r = random.randint(0, len(target) - 1)  # 步骤2
#             result.append(target.pop(r))  # 步骤3
#
#     return result
#
#
# def dealCards():
#     a = input("请输入第一位游戏玩家名称：")
#     b = input("请输入第二位游戏玩家名称：")
#     c = input("请输入第三位游戏玩家名称：")
#
#     r = {}
#     r[a], r[b], r[c] = [], [], []
#
#     new_cards = fy_shuffle(cards, 3)
#
#     for i in range(17):
#         r[a].append(new_cards.pop())
#         r[b].append(new_cards.pop())
#         r[c].append(new_cards.pop())
#
#     d = random.sample((a, b, c), 1)[0]
#     print(f"\n地主是：{d}\n")
#     r[d].extend((new_cards.pop(), new_cards.pop(), new_cards.pop()))
#
#     print(f"[{a}]拿到的牌是：{' '.join(r[a])}\n")
#     print(f"[{b}]拿到的牌是：{' '.join(r[b])}\n")
#     print(f"[{c}]拿到的牌是：{' '.join(r[c])}")
#
#
# dealCards()

# 一对
def is_pair(cards):
    if len(cards) == 2 and cards[0] == cards[1]:
        return True
    else:
        return False

# 火箭
def is_rocket(cards):
    if len(cards) == 2 and 14 in cards and 15 in cards:
        return True
    else:
        return False

# 三张
def is_three(cards):
    if len(cards) == 3 and cards[0] == cards[1] == cards[2]:
        return True
    else:
        return False

# 炸弹
def is_four(cards):
    if len(cards) == 4 and cards[0] == cards[1] == cards[2] == cards[3]:
        return True
    else:
        return False

def get_input():
    input_card = input("请出牌（出牌间隔，退出请输入Q）：")
    if input_card == "Q":
        return 0
    else:
        input_card = input_card.split()
        return input_card

def change_input(cards):
    result = []
    target = {"3":1, "4":2, "5":3, "6":4, "7":5, "8":6, "9":7, "10":8, "J":9, "Q":10, "K":11, "1":12, "2":13}
    for each in cards:
        num = target.get(each[1:])
        if num:
            result.append(num)
        else:
            result.append(14 if each == "🌙" else 15)
    return result


def check_cards(cards):
    if is_pair(cards):
        print("符合规则：对牌")
    elif is_rocket(cards):
        print("符合规则：火箭")
    elif is_three(cards):
        print("符合规则：三张牌相同")
    elif is_four(cards):
        print("符合规则：炸弹")
    else:
        print("不符合规则!")


def play_cards():
    show_cards()
    cards = get_input()
    while cards:
        cards = change_input(cards)
        check_cards(cards)
        cards = get_input()
play_cards()

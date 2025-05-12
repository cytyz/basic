# 密室打卡（打点计时器 zip)
# 假设有一个密室，每次只能放一个人进去，在进去之前和出来之后都要求摁一下门口的打卡机按钮，打卡机会依次将名字和进出时间戳记录为以下的格式：
import decimal
times = [1, 3, 3.5, 6.5, 9.5, 10, 10.8]
names = ["A", "B", "C", "D", "E", "F", "G"]
# 这里表示：
# A 君是从时间戳为 0 的时候进入，从时间戳为 1 的时候出来，总共耗时为 1
# B 君是从时间戳为 1 的时候进入，从时间戳为 3 的时候出来，总共耗时为 2
# C 君是从时间戳为 3 的时候进入，从时间戳为 3.5 的时候出来，总共耗时为 0.5
# ...
# G 君是从时间戳为 10 的时候进入，从时间戳为 10.8 的时候出来，总共耗时为 0.8
# OK，现在要求大家编写代码，统计给定的数据，打印耗时最长和最短的人员名称。
times_use = []
use = 0
for time in range(len(times)):
    if time == 0:
        times_use.append(float(times[time]))
    else:
        use = decimal.Decimal(str(times[time])) - decimal.Decimal(str(times[time - 1]))
        times_use.append(float(use))
zipped = zip(times_use, names)
temp1 = []
temp2 = []
for i in zipped:
    if i[0] == min(times_use):
        temp1.append(i[1])
    if i[0] == max(times_use):
        temp2.append(i[1])
print("速度最快的是：", temp1, "耗费时间是：", min(times_use))
# 速度最快的是： ['C', 'F'] 耗费时间是： 0.5
print("速度最慢的是：", temp2, "耗费时间是：", max(times_use))
# 速度最慢的是： ['D', 'E'] 耗费时间是： 3.0

# 初始化变量 i #
i = 1
# 初始化变量 s #
s = 0
wheats = 0
while i <= 64:
    # 请计算每一个格子的麦子数，并将其赋值给 wheats 变量#
    wheats = pow(2, i-1)
    s = s + wheats
    i = i + 1

print("舍罕王应该给达依尔", s, "粒麦子！")

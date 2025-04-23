# 有一个长阶梯，若每步上 2 阶，最后剩 1 阶；若每步上 3 阶，最后剩 2 阶；若每步上 5 阶，最后剩 4 阶；若每步上 6 阶，最后剩 5 阶；只有每步上 7 阶，最后刚好一阶也不剩。

steps = 7
i = 1
FIND = False

while i < 100:
    if (steps % 2 == 1) and (steps % 3 == 2) and (steps % 5 == 4) and (steps % 6 == 5):
        FIND = True
        break
    else:
        steps += 7
    i = i + 1

if FIND:
    print('阶梯数是：', steps)
else:
    print('在程序限定的范围内找不到答案！')
# 阶梯数是： 119

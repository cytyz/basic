# 1. 杂记

鱼C论坛https://fishc.com.cn/：cytyz	Cytyz831723

Python代码编写规范	PEP8

菜鸟教程Python测验

https://gotomake.scratch3.fun/python/

\#优先级顺序为 NOT、AND、OR

\#2^3表示为2**3

\#模%，商//

__init__.py，初始化包，当包被导入时，这里面的代码会自动执行。可在此文件中定义包级别的操作，例如：

设置全局变量或常量；

配置日志记录（如初始化日志文件）；

加载数据库连接或外部API；

注册插件或功能模块。

__init__.py中存放些什么



# 2. 第一个游戏

game.py

```python
#用Python设计第一个游戏
#input()用于接受用户的输入并返回，如：
#name = input('你叫什么名字？\n')
#print(name)
temp = input("不妨猜一下小甲鱼在心里想的是那个数字。")
guess = int(temp)

if guess == 8:
	print("你是小甲鱼心里的蛔虫吗？！")
	print("哼，猜中了也没奖励！")
else:
	print("猜错了，小甲鱼心里想的是8！")

print("游戏结束，不玩了。")
```

![image-20250421175008322](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250421175008322.png)

# 3. 变量与字符串



```python
#交换变量值
x=3
y=5
x, y = y, x
print(x, y) #5,3

#文本序列需要用''或""或'''   '''包括起来，在''或""其中的''或""前可加转义字符\，使得Python可以正确识别
print("I Love China!") #I Love China!
print('"Life is short, you need Python"') #"Life is short, you need Python"
print('"Life is short, let\'s learn Python."') #"Life is short, let's learn Python."
print('"I love Python, \nI Love FishC"')
#I love Python,
#I Love FishC

#当需要传入路径时，路径中每个层级前都需要添加一个转义字符\，或者在其前添加r表示后面的为原始字符
print("D:\\three\\two\\one\\now") #D:\three\two\one\now
print(r"D:\three\two\one\now") #D:\three\two\one\now
#(IDLE特别注意)\不能放在末尾，每行行末的\是为了可以用回车键转到下一行，如果没有\直接回车，Python会直接运行

#变量值相加相乘
print(520+1314) #1834
print('520'+'1314') #'5201314'   字符串相加->拼接
print("我每天爱你三千遍!"*3000) #我每天爱你三千遍!我每天爱你三千遍!我每天爱你三千遍!……

#字符串转换为数字 int(), float转为int时忽略后面小数
print( int('123') + 256) #379
#数字转化为字符串 str()
print( '123' + str(256)) #123256
```



# 4.数字类型运算与转换

## 数字类型运算与转换

```python
# 使用浮点数进行运算时容易丢失精度
print(0.1 + 0.2)
# 0.30000000000000004
print(0.3 == 0.1 + 0.2)
# false

# 使用 decimal 来精准计算
import decimal

a = decimal.Decimal("0.1")
b = decimal.Decimal("0.2")
c = decimal.Decimal("0.3")
print(a + b)
# 0.3
print(a + b == c)
# True
print("--------------------------------")

# 科学计数法
print(0.00005)
# 5e-05

# 复数
x = 1 + 2j
print(x.real)
# 1
print(x.imag)

# 除
print(3 / 2)
# 1.5

# 地板除（向下取整）
print(3 // 2)
# 1
print(-3 // 2)
# -2

# 模（余数）
print(3 % 2)
# 1
print(4 % 2)
# 0

# 求地板除和余数
print(divmod(3, 2))
#(1,1)

# 绝对值
print(abs(-2323))
# -2323

# 复数的绝对值:复数的模   根号（a + b^2）
print(abs(x))
# 2.23606797749979

# 转为整数
print(int("520"))
# 520
print(int(3.14))
# 3
print(9.99)
# 9

# 转为浮点数
print(float("520"))
# 520.0
print(float(520))
# 520.0
print(float(1E6))
# 1000000.0

print(complex("1+2j"))
# (1+2j)
print(complex(1, 2))

# 幂运算
print(pow(2, 3))
# 8
print(pow(2, 3, 5))
# 3
print(2 ** 3 % 5)
# 3

# 有理数分数形式（约分后）
from fractions import Fraction
print(Fraction(16, -10))
#Fraction(8, -5)
print(Fraction(123))
#Fraction(123, 1)
print(Fraction("-3/7"))
#Frafction(-3, 7)

print("--------------------------------")
#布尔值
print(1 == True)
#True
print(0 == False)
#True
print(5 > 3 and 4)
#4

# 优先级顺序为 NOT、AND、OR
# 短路逻辑核心思路
# 从左到右，只有当第一个操作数的值无法确定逻辑运算的结果时，才对第二个操作数进行求值
print((not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9))
# 4
print(3 and 4)
# 4
print(3 or 4)
# 3
print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)
# 4
print(3 and 5 + True or False)
# 6
print(0 and not 1 or not 2 and 3 or 4 and not 5)
# False

```



![image-20250421152106490](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250421152106490.png)



## 抛硬币实验

```python
# 模拟抛200次硬币
# 导入随机模块 #
import random

# 接收用户输入并将数值赋值给 counts 变量 #
counts = int(input("请输入抛硬币的次数："))
i = 0

print("开始抛硬币实验：")
while i < counts:
    # 生成一个随机数num #
    num = random.randrange(2)

    if num % 2:
        # 打印结果 #
        print("正面", end=" ")
    else:
        # 打印结果 #
        print("反面", end=" ")

    i = i + 1
    if i % 20 == 0:
        print()
# 请输入抛硬币的次数：88
# 开始抛硬币实验：
# 正面 反面 反面 反面 反面 反面 正面 反面 反面 正面 正面 反面 反面 反面 反面 正面 正面 正面 反面 反面 
# 正面 正面 反面 正面 正面 正面 反面 反面 反面 反面 反面 正面 正面 正面 正面 正面 正面 反面 正面 反面 
# 反面 正面 反面 正面 正面 反面 正面 反面 反面 正面 正面 正面 反面 正面 反面 反面 正面 反面 反面 反面 
# 正面 正面 反面 正面 反面 反面 反面 反面 反面 反面 正面 反面 反面 正面 正面 反面 反面 反面 正面 反面 
# 反面 反面 反面 正面 反面 反面 正面 反面 

```



## 偶数和

```python
# 计算 1000000 以内所有偶数的和
i = 0
sum = 0
s = 1000000
while i <= s:
    if i % 2 == 0:
        sum += i
    i = i + 1
print(s, "以内的所有偶数的和是", sum)
# 1000000 以内的所有偶数的和是 250000500000

```



## 国王棋盘麦子

```python
# 相传国际象棋是古印度舍罕王的宰相达依尔发明的。
# 舍罕王十分喜爱国际象棋，便决定让宰相自己选择何种赏赐。这位聪明的宰相指着 8×8 共 64 格的象棋棋盘说：陛下，请您赏给我一些麦子吧。
# 就在棋盘的第 1 格中放 1 粒，第 2 格放 2 粒，第 3 格放 4 粒，以后每一格都比前一格增加一倍，依此放完棋盘上 64 格，我就感激不尽了……
# 舍罕王听了达依尔这个“小小”的要求，便让人扛来一袋麦子，他要兑现许诺。结果，在给达依尔发放麦子时，舍罕王发现他要给达依尔的麦子比自己想象的要多得多，一袋麦子是远远不够的……
# 请编程计算舍罕王应该给达依尔多少粒麦子？
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
# 舍罕王应该给达依尔 18446744073709551615 粒麦子！

```



## 阶梯步数

```python
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

```



# 5.流程图



![image-20250422123702888](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250422123702888.png)



# 6.分支与循环

## if

```python
# 1、if
if condition1:
    statement(s)

# 2、if……else
if condition1:
    statement(s)
else:
    statement(s)

# 3、if……elif……elif
if condition1:
    statement(s)
elif:
    statement(s)
elif:
    statement(s)
elif:
    statement(s)

# 4、if……elif……elif…………else
# 第4种是在第3种的情况下添加一个else，表示上面所有的条件均不成立的情况下，执行某条语句或某个代码块
if condition1:
    statement(s)
elif:
    statement(s)
elif:
    statement(s)
……
else:
    statement(s)
    
```



## ==条件表达式==

```python
# 条件表达式
age = 17
if age < 18:
    print("未成年人禁止进入")
else:
    print('欢迎进入')

print("未成年人禁止进入") if age < 18 else print('欢迎进入')
# 未成年人禁止进入
# 未成年人禁止进入

score = 66
level = ('D' if 0 <= score < 60 else
         'C' if 60 <= score < 80 else
         'B' if 80 <= score < 90 else
         'A' if 90 <= score < 100 else
         'S' if score == 100 else
         "请输入0~100之间的数字")
print(level)
# C

# 其实，大多数 if - else 条件分支还可以使用 and - or 运算符组合的表达式来代替，
# 那么如果将下面代码转变成 and - or 来实现，应该是怎样的呢？
# if "Love":
#     520
# else:
#     404
#
# "Love" and 520 or 404

```



## 角谷猜想

```pytyhon
# 验证角谷猜想
# 角谷猜想的内容是：任意给定一个正整数，若它为偶数则除以 2，若它为奇数则乘以 3 再加 1，得到一个新的自然数，按照这样的方法计算下去，最终的结果必将是 1。
# 比如给定的自然数是 5，则 5 * 3 + 1 = 16 -> 16 / 2 = 8 -> 8 / 2 = 4 -> 4 / 2 = 2 -> 2 / 2 = 1。
# 现在要求大家编写一个验证角谷猜想的程序。
n = int(input("请输入一个正整数："))

while n > 0:
    # 判断 n 是否可以被 2 整除 #
    if n % 2 == 0:
        print(n, " / 2 = ", n // 2)
        n = n // 2
    else:
        print(n, " * 3 + 1 == ", n * 3 + 1)
        n = n * 3 + 1
    if n == 1:
        break
# 请输入一个正整数：5
# 5  * 3 + 1 ==  16
# 16  / 2 =  8
# 8  / 2 =  4
# 4  / 2 =  2
# 2  / 2 =  1

```



## 抛硬币进阶版

```python
# 抛硬币实验
# 如果抛硬币的次数小于 100，则打印每次的结果，否则不打印
# 统计最终正面和反面的次数
# 分别统计正反面最多出现连续的次数
import random

counts = int(input("请输入抛硬币的次数："))
i = 0
positive = 0
opposite = 0
temp = 0
positive_continuous = 0
PC_sum = 0
opposite_continuous = 0
OC_sum = 0
print("开始抛硬币实验：")
while i < counts:
    num = random.randint(1, 10)
    if num % 2:
        if counts < 100:
            print("正面", end=" ")
        positive += 1
        if temp != 1:
            positive_continuous = 1
            temp = 1
        else:
            positive_continuous += 1
        if PC_sum < positive_continuous:
            PC_sum = positive_continuous
    else:
        if counts < 100:
            print("反面", end=" ")
        opposite += 1
        if temp != 2:
            opposite_continuous = 1
            temp = 2
        else:
            opposite_continuous += 1
        if OC_sum < opposite_continuous:
            OC_sum = opposite_continuous
    i += 1
    if ((i % 20 == 0) and (counts < 100)) or ((i == counts) and (counts < 100)):
        print()
print("一共模拟了", counts, "次抛硬币，结果如下:")
print("正面", positive, "次")
print("反面", opposite, "次")
print("最多连续正面", PC_sum, "次")
print("最多连续反面", OC_sum, "次")

# 请输入抛硬币的次数：88
# 开始抛硬币实验：
# 反面 反面 正面 正面 正面 反面 正面 反面 正面 正面 正面 反面 正面 反面 正面 正面 正面 反面 反面 正面 
# 正面 正面 反面 反面 反面 反面 正面 正面 反面 正面 正面 正面 反面 正面 反面 正面 反面 正面 正面 反面 
# 正面 反面 正面 反面 反面 正面 正面 反面 正面 反面 反面 反面 正面 正面 反面 反面 正面 正面 正面 反面 
# 反面 反面 正面 反面 正面 正面 反面 正面 反面 反面 反面 正面 反面 反面 反面 正面 反面 反面 正面 正面 
# 反面 反面 正面 反面 反面 反面 正面 正面 
# 一共模拟了 88 次抛硬币，结果如下:
# 正面 44 次
# 反面 44 次
# 最多连续正面 3 次
# 最多连续反面 4 次

# 请输入抛硬币的次数：10000
# 开始抛硬币实验：
# 一共模拟了 10000 次抛硬币，结果如下:
# 正面 5050 次
# 反面 4950 次
# 最多连续正面 12 次
# 最多连续反面 12 次

```



## continue

```python
# continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
# 1 3 5 7 9

```

![screenshot-01JSERDD2NS32AV0EP23V2ZQQ1](D:\Program Repository\github\basic\assets\screenshot-01JSERDD2NS32AV0EP23V2ZQQ1.png)



## while_else

```python
day = 1
while day <= 7:
    anwer = input("今天有好好学习吗？")
    if anwer != '有':
        break
    day += 1
else:
    print("非常棒，你已经坚持7天了!")
# 今天有好好学习吗？有
# 今天有好好学习吗？有
# 今天有好好学习吗？有
# 今天有好好学习吗？有
# 今天有好好学习吗？有
# 今天有好好学习吗？有
# 今天有好好学习吗？有
# 非常棒，你已经坚持7天了!

```



## 九九乘法表

```python
# 九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(j, "*", i, "=", j * i, end=' ')
        j += 1
    print()
    i += 1
# 1 * 1 = 1 
# 1 * 2 = 2 2 * 2 = 4 
# 1 * 3 = 3 2 * 3 = 6 3 * 3 = 9 
# 1 * 4 = 4 2 * 4 = 8 3 * 4 = 12 4 * 4 = 16 
# 1 * 5 = 5 2 * 5 = 10 3 * 5 = 15 4 * 5 = 20 5 * 5 = 25 
# 1 * 6 = 6 2 * 6 = 12 3 * 6 = 18 4 * 6 = 24 5 * 6 = 30 6 * 6 = 36 
# 1 * 7 = 7 2 * 7 = 14 3 * 7 = 21 4 * 7 = 28 5 * 7 = 35 6 * 7 = 42 7 * 7 = 49 
# 1 * 8 = 8 2 * 8 = 16 3 * 8 = 24 4 * 8 = 32 5 * 8 = 40 6 * 8 = 48 7 * 8 = 56 8 * 8 = 64 
# 1 * 9 = 9 2 * 9 = 18 3 * 9 = 27 4 * 9 = 36 5 * 9 = 45 6 * 9 = 54 7 * 9 = 63 8 * 9 = 72 9 * 9 = 81 

```



## for_in

```python
for each in "FishC":
    print(each)
# F
# i
# s
# h
# C
print("————————————————————————")
# 用while实现
i = 0
while i < len("FishC"):
    print("FishC"[i])
    i += 1
# F
# i
# s
# h
# C
print("————————————————————————")
# range(10) 从0到10（不包括10）的整数序列
# range(0, 10)
# range(0, 10, 2)
for each in range(10):
    print(each)

# 求1~10之间的素数
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "=", n // x, "*", x)
            break
    else:
        print(n, "是一个素数")

```



## ==水仙花数==

```python
# 水仙花数
# 求解 100~999 之间的所有水仙花数
# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
hundred = 0
ten = 0
piece = 0
for i in range(100, 1000):
    hundred = i // 100
    ten = i // 10 % 10
    piece = i % 10
    if pow(hundred, 3) + pow(ten, 3) + pow(piece, 3) == i:
        print(i)

# ************************************
# 重点学习思路
for i in range(100, 1000):
    sum = 0
    temp = i

    while temp >= 1:
        sum = sum + (temp % 10) ** 3
        temp //= 10

    if sum == i:
        print(i)

```



## ==回文数==

```python
# 判断一个整数是否为回文数
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
num = int(input("请输入一个正整数："))
num_temp = num
if num < 0 or num % 10 == 0:
    print("不是回文数")
else:
    temp = 0
    while num_temp >= 1:
        temp = temp * 10 + num_temp % 10
        num_temp = num_temp // 10
    if num == temp:
        print("是回文数")
    else:
        print("不是回文数")

```



# 7.列表

## 列表与切片

```python
rhyme = [1, 2, 3, 4, 5, "上山打老虎"]
print(rhyme)
# [1, 2, 3, 4, 5, '上山打老虎']
for i in rhyme:
    print(i)
# 1
# 2
# 3
# 4
# 5
# 上山打老虎
print(rhyme[1])
# 2
print(rhyme[-1])
# 上山打老虎

# 列表切片
# 获取列表范围的元素列表
print(rhyme[0:3])
# [1, 2, 3]
print(rhyme[:3])
# [1, 2, 3]
print(rhyme[3:])
# [4, 5, '上山打老虎']
print(rhyme[:])
# [1, 2, 3, 4, 5, '上山打老虎']
print(rhyme[0: 6: 2])
# [1, 3, 5]
print(rhyme[:: 2])
# [1, 3, 5]
print(rhyme[:: -1])
# ['上山打老虎', 5, 4, 3, 2, 1]

print([5, "上", 4, "山", 3, "打", 2, "老", 1, "虎"][-2::-2])
# [1, 2, 3, 4, 5]

```



## 两数之和

```python
# 两数之和
# 让用户自己来录入 整数列表nums 和 目标值target 的数据，在该数组中找出和为目标值的两个元素，并将它们的数组下标值打印出来
nums = []
while True:
    num = input("请录入一个整数（输入STOP结束）：")
    if num == "STOP":
        break
    try:
        nums.append(int(num))
    except ValueError:
        print("输入无效，请输入整数！")
target = int(input("请录入目标整数："))
n = len(nums)
# 获取 nums 的长度，并将结果存放到 n 变量中 #
for i in range(n):
    for j in range(i + 1, n):
        if (nums[i] + nums[j]) == target:
            print("[", i, ",", j, "]")
            break
        # 将找到的两个元素下标值以列表的形式打印出来 #
# 请录入一个整数（输入STOP结束）：22
# 请录入一个整数（输入STOP结束）：33
# 请录入一个整数（输入STOP结束）：45
# 请录入一个整数（输入STOP结束）：18
# 请录入一个整数（输入STOP结束）：62
# 请录入一个整数（输入STOP结束）：88
# 请录入一个整数（输入STOP结束）：93
# 请录入一个整数（输入STOP结束）：72
# 请录入一个整数（输入STOP结束）：67
# 请录入一个整数（输入STOP结束）：19
# 请录入一个整数（输入STOP结束）：STOP
# 请录入目标整数：100
# [ 1 , 8 ]

# 用random 模块，生成一个由 10000 个整数（范围是 1 ~ 65535）构成的随机列表
import random
nums = []
for i in range(10000):
    num = random.randint(1, 65535)
    nums.append(num)
target = int(input("请录入目标整数："))
n = len(nums)
# 获取 nums 的长度，并将结果存放到 n 变量中 #
for i in range(n):
    for j in range(i + 1, n):
        if (nums[i] + nums[j]) == target:
            print("[", i, ",", j, "]")
        # 将找到的两个元素下标值以列表的形式打印出来 #
# 请录入目标整数：12345
# [ 52 , 8499 ]
# [ 60 , 6637 ]
# [ 104 , 618 ]
# [ 108 , 882 ]
# [ 134 , 6948 ]
# [ 135 , 5853 ]
# [ 136 , 4694 ]
# [ 156 , 1470 ]
# .........

```



## 列表增删改查方法

```python
# 列表的增删改查等方法
# append 在该列表后面增加一个元素（包括列表）
heroes = ["钢铁侠", '绿巨人']
heroes.append("黑寡妇")
print(heroes)
# ['钢铁侠', '绿巨人', '黑寡妇']


# extend 将一个列表中的元素添加到该列表的后面
heroes.extend(["鹰眼", "灭霸", "雷神"])
print(heroes)
# ['钢铁侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神']
# 以切片来添加列表中的元素，相当于extend
heroes[len(heroes):] = [6, 7]
print(heroes)
# ['钢铁侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神', 6, 7]

# insert 在某个位置插入一个元素（包括列表）
heroes.insert(1, 1)
print(heroes)
# ['钢铁侠', 1, '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神', 6, 7]
heroes.insert(2, [2, 3])
print(heroes)
# ['钢铁侠', 1, [2, 3], '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神', 6, 7]
heroes.insert(len(heroes), 8)
print(heroes)
# ['钢铁侠', 1, [2, 3], '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神', 6, 7, 8]

# remove 删除指定元素
heroes.remove("灭霸")
print(heroes)
# ['钢铁侠', 1, [2, 3], '绿巨人', '黑寡妇', '鹰眼', '雷神', 6, 7, 8]

# pop 删除指定位置的元素，  有返回值！！！
heroes.pop(4)
print(heroes)
# ['钢铁侠', 1, [2, 3], '绿巨人', '鹰眼', '雷神', 6, 7, 8]

# clear 清空列表中的所有元素
heroes.clear()
print(heroes)
# []

# 改
s = [1, 2, 3, 4, 5]
s[len(s)-2:] = [2, 1]
print(s)
# [1, 2, 3, 2, 1]

w = [3, 2, 3, 4, 8, 6]
w[4] = 7
print(w)
# [3, 2, 3, 4, 7, 6]

# sort 列表从小到大排序
w.sort()
print(w)
# [2, 3, 3, 4, 6, 7]

# reverse 反转列表，原地反转列表中的元素顺序
w.reverse()
print(w)
# [7, 6, 4, 3, 3, 2]
w = w[:: -1]
print(w)
# [2, 3, 3, 4, 6, 7]

# sort(reverse=True) 列表从大到小排序
w = [3, 2, 3, 4, 8, 6]
w.sort(reverse=True)
print(w)
# [8, 6, 4, 3, 3, 2]

# count 查找某个元素的数量
print(w.count(3))
# 2

# index 查找某个元素第一次出现的的索引值
print(w.index(6))
# 1
# 替换元素但未知某个元素的索引值时
w[w.index(6)] = 9
print(w)
# [8, 9, 4, 3, 3, 2]

print(w.index(3))
# 3
# 查找指定区间某个元素第一次出现的索引值
print(w.index(3, 4, 5))
# 4

# copy 拷贝列表 浅拷贝 copy函数创建的新列表与原始列表不是同一个内存空间，不同享数据变更
# 二次赋值的变量与原始变量享有相同内存空间
# a = [1,2,3]
# b = a 给b列表中添加或删除元素，a列表也会受到相同的影响
w_copy1 = w.copy()
print(w_copy1)
# [8, 9, 4, 3, 3, 2]
w_copy2 = w[:]
print(w_copy2)
# [8, 9, 4, 3, 3, 2]

s = [1, 2, 3, 4, 5]
s[:] = "FishC"
print(s)
# ['F', 'i', 's', 'h', 'C']

```



## ==合法字符串==



```python
# 合法字符串
# 判断给定的字符串 s 中括号的写法是否合法
s = input("请输入测试字符串：")
temp = []
if len(s) % 2 != 0:
    print("非法")
else:
    for i in s:
        if i == "(" or i == "[" or i == "{":
            temp.append(i)
        else:
            if i == ")" and temp.pop(-1) == "(" or i == "]" and temp.pop(-1) == "[" or i == "}" and temp.pop(-1) == "{":
                continue
            else:
                break
    if len(temp) == 0:
        print("合法")
    else:
        print("非法")

```



## 主要元素

```python
# 主要元素
# 如果有一个列表，其中占比超过一半的元素称之为主要元素，那么如何获取一个列表的主要元素呢？
nums = [2, 2, 4, 2, 3, 6, 2]
nums.sort()
major = nums[len(nums) // 2]
major_num = 0
for i in nums:
    if i == major:
        major_num += 1
if major_num >= (len(nums) // 2):
    print(major, "为主要元素")
else:
    print("不存在主要元素")

```



## 创建嵌套列表

```python
# 创建嵌套列表
s = [1, 2, 3]
t = [4, 5, 6]
print(s+t)
# [1, 2, 3, 4, 5, 6]
print(s*2)
# [1, 2, 3, 1, 2, 3]

# 嵌套列表， 多维列表
# 二维列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# 遍历数组
for i in matrix:
    print(i)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
for i in matrix:
    for j in i:
        print(j, end=" ")
# 1 2 3 4 5 6 7 8 9
print()
print(matrix[0])
# [1, 2, 3]
print(matrix[0][0])
# 1

# 创建只有0的二维列表
A = [0] * 3
print(A)
# [0, 0, 0]
for i in range(3):
    A[i] = [0] * 3
print(A)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(A[0] is A[1], A[1] is A[2])
# False False

# 错误的二维列表创建方式
B = [[0] * 3] * 3
print(B)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(B[0] is B[1], B[1] is B[2])
# True True 复制了对同一个列表的引用，三个列表实际上指向的是同一个列表，同一个地址

a = 250
b = 250
print(a is b)
# True

a = 1000
b = 1000
print(a is b)
# True  交互模式下为False
# Python 的缓存机制，所以在 IDE 环境或者脚本模式下同一个整数被多个变量引用不会开辟新的内存空间

# 三维数组
C = [0] * 3
for i in range(3):
    C[i] = [0] * 3
    for j in range(3):
        C[i][j] = [0] * 3
print(C)

# 从空数组开始创建
d = []
for i in range(3):
    d.append([])
    for j in range(3):
        d[i].append([])
        for k in range(3):
            d[i][j].append(0)
print(d)

```



![image-20250425152659122](D:\Program Repository\github\basic\assets\image-20250425152659122.png)



## ==深浅拷贝、赋值“=”  与 嵌套列表 与  地址==

==深浅拷贝、赋值“=”  与 嵌套列表 与  地址==

==对于不可变对象（数值，字符串，元组），各对象均指向同一地址；因对象不可变，原对象改变时指向新地址，其余复制对象仍指向原地址，不会随之改变==

==对于可变对象（列表，字典）：赋值“=”与原对象指向同一地址，浅拷贝和深拷贝分别创建新的对象，指向了新的地址==

==但浅拷贝、赋值“=”与原对象的子对象均指向同一地址，而深拷贝的子对象则创建了新的对象，指向了新的地址==

==故改变 复杂子对象 的值时，浅拷贝、赋值“=”会随之改变==

==浅拷贝不适用于嵌套列表，对于浅拷贝只能拷贝嵌套列表的外层，而对于内层只是对内层进行引用，当原嵌套列表子对象改变时，浅拷贝对象亦会随之改变==

```python
# 深浅拷贝、赋值“=”  与 嵌套列表 与  地址
# 对于不可变对象（数值，字符串，元组），各对象均指向同一地址；因对象不可变，原对象改变时指向新地址，其余复制对象仍指向原地址，不会随之改变

# 对于可变对象（列表，字典）：赋值“=”与原对象指向同一地址，浅拷贝和深拷贝分别创建新的对象，指向了新的地址
# 但浅拷贝、赋值“=”与原对象的子对象均指向同一地址，而深拷贝的子对象则创建了新的对象，指向了新的地址
# 故改变 复杂子对象 的值时，浅拷贝、赋值“=”会随之改变

# 浅拷贝不适用于嵌套列表，对于浅拷贝只能拷贝嵌套列表的外层，而对于内层只是对内层进行引用，当原嵌套列表子对象改变时，浅拷贝对象亦会随之改变
# copy.copy 浅拷贝: 只拷贝父对象(拷贝顶层)，不会拷贝对象的内部的子对象。
# copy.deepcopy 深拷贝: 拷贝所有对象 包括 子对象
import copy
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 浅拷贝
y = x.copy()
z = copy.copy(x)
# 深拷贝
m = copy.deepcopy(x)

# 对于不可变对象（数值，字符串，元组），各对象均指向同一地址；
# 对象不可变，原对象改变时指向新地址，其余复制对象仍指向原地址，不会随之改变，
# 每次代码运行，地址均会改变
a = 1
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print(id(a))
# 2596863568176
print(id(b))
# 2596863568176
print(id(c))
# 2596863568176
print(id(d))
# 2596863568176
a = 2
print(id(a))
# 2596863568208
print(id(b))
# 2596863568176
print(b)
# 1

# 对于简单可变对象（列表，字典），赋值“=”与原对象指向同一地址，浅拷贝和深拷贝分别创建新的对象，指向了新的地址
# 故不改变 复杂子对象 的值时，仅赋值“=”会随之改变
list1 = [1, 2, 3]
list2 = list1
list3 = copy.copy(list1)
list4 = copy.deepcopy(list1)
print(id(list1))
# 2596869779200
print(id(list2))
# 2596869779200
print(id(list3))
# 2596869779264
print(id(list4))
# 2596869791808
print("——————————————————————————————————")
list1.append(55)
print(id(list1))
# 2596869779200
print(id(list2))
# 2596869779200
print(id(list3))
# 2596869779264
print(id(list4))
# 2596869791808
print(list1)
# [1, 2, 3, 55]
print(list2)
# [1, 2, 3, 55]
print(list3)
# [1, 2, 3]
print(list4)
# [1, 2, 3]

# 对于含复杂子对象的可变对象（列表，字典）：赋值“=”与原对象指向同一地址，浅拷贝和深拷贝分别创建新的对象，指向了新的地址
# 但浅拷贝、赋值“=”与原对象的子对象均指向同一地址，而深拷贝的子对象则创建了新的对象，指向了新的地址
# 故改变 复杂子对象 的值时，浅拷贝、赋值“=”会随之改变
list1 = [1, 2, [1, 2]]
list2 = list1
list3 = copy.copy(list1)
list4 = copy.deepcopy(list1)
print(id(list1[2]))
# 2277450014976
print(id(list2[2]))
# 2277450014976
print(id(list3[2]))
# 2277450014976
print(id(list4[2]))
# 2277450002368
print("——————————————————————————————————")
list1[2][1] = 3
print(id(list1[2]))
# 2277450014976
print(id(list2[2]))
# 2277450014976
print(id(list3[2]))
# 2277450014976
print(id(list4[2]))
# 2277450002368
print(list1)
# [1, 2, [1, 3]]
print(list2)
# [1, 2, [1, 3]]
print(list3)
# [1, 2, [1, 3]]
print(list4)
# [1, 2, [1, 2]]

```



## ==二维列表两个小练习==

```python
# 创建一个 88 x 88 的随机整数矩阵（二维列表），然后匹配用户输入的整数是否与其中某元素相等，如果相等则打印其行号和列号。
# 要求1：随机整数取值范围 0~1024
# 要求2：需找出所有匹配的元素来
import random
list1 = [0] * 88
for i in range(88):
    list1[i] = [random.randint(0, 1025)]
    for j in range(87):
        list1[i].append(random.randint(0, 1025))
        # list1[i] += [random.randint(0, 1025)]
num = int(input("请输入一个待匹配的整数："))
for i in range(88):
    for j in range(88):
        if list1[i][j] == num:
            print(i, j)

import random

# 创建并初始化二维列表
matrix = []
for i in range(88):
    matrix.append([])
    for j in range(88):
        matrix[i].append(random.randint(0, 1024))

target = int(input("请输入一个代匹配的整数："))

# 匹配用户输入的整数
for i in range(88):
    for j in range(88):
        if matrix[i][j] == target:
            print(i, j)

# 假设给定一个 m * n 的矩阵（矩阵中数值的取值范围是 0~1024，且各不相同），如果某一个元素的值在同一行的所有元素中最小，并且在同一列的所有元素中最大，那么该元素便是幸运数字
matrix = [[10, 36, 52],
          [33, 24, 88],
          [66, 76, 99]]
# 找出每一行最小和每一列最大，再一一比对
m = len(matrix)
n = len(matrix[0])
min_row = [1024] * m
max_col = [0] * n
for i in range(m):
    for j in range(n):
        min_row[i] = min(matrix[i][j], min_row[i])
        max_col[j] = max(matrix[i][j], max_col[j])

for i in range(m):
    for j in range(n):
        if matrix[i][j] == min_row[i] and matrix[i][j] == max_col[j]:
            print(matrix[i][j])
# 66

```



## ==列表推导式==

```python
# 列表推导式
x = [i for i in range(10)]
print(x)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [i + 1 for i in range(10)]
print(x)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 对于字符串
y = [c * 2 for c in "FishC"]
print(y)
# ['FF', 'ii', 'ss', 'hh', 'CC']
z = []
for c in "FishC":
    z.append(c * 2)
print(z)
# ['FF', 'ii', 'ss', 'hh', 'CC']

# ord()转换成ASCII编码
code = [ord(c) for c in "FishC"]
print(code)
# [70, 105, 115, 104, 67]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
flatten = [col for row in matrix for col in row]
print(flatten)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
re_flatten = [col for row in matrix for col in row]
re_flatten.reverse()
print(re_flatten)
# [9, 8, 7, 6, 5, 4, 3, 2, 1]


col2 = [row[1] for row in matrix]
print(col2)
# [2, 5, 8]
diag = [matrix[i][i] for i in range(len(matrix))]
print(diag)
# [1, 5, 9]
diag2 = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
print(diag2)
# [3, 5, 7]
diag3 = [i * matrix[i][i] for i in range(len(matrix))]
print(diag3)
# [0, 5, 18]


# 创建二维列表
d = [[i, i + 2] for i in range(6)]
print(d)
# [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]

# 列表推导式添加 if 条件
even = [i for i in range(10) if i % 2 == 0]
print(even)
# [0, 2, 4, 6, 8]

# 找出首字母为F的单词
words = ["Great", "FishC", "Brilliant", "Excellent", "Fantastic"]
for i in words:
    if i[0] == "F":
        print(i)
# FishC
# Fantastic
words1 = [i for i in words if i[0] == "F"]
print(words1)
# ['FishC', 'Fantastic']

# 笛卡尔乘积
w = [x + y for x in "fishc" for y in "FISHC"]
print(w)
# ['fF', 'fI', 'fS', 'fH', 'fC', 'iF', 'iI', 'iS', 'iH', 'iC', 'sF', 'sI', 'sS', 'sH',
# 'sC', 'hF', 'hI', 'hS', 'hH', 'hC', 'cF', 'cI', 'cS', 'cH', 'cC']

# _ 可用于临时变量，无关紧要的变量
_ = []
w2 = [[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 3 == 0]
print(w2)
# [[0, 0], [0, 3], [0, 6], [0, 9], [2, 0], [2, 3], [2, 6], [2, 9], [4, 0], [4, 3], [4, 6],
# [4, 9], [6, 0], [6, 3], [6, 6], [6, 9], [8, 0], [8, 3], [8, 6], [8, 9]]
_ = []
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 3 == 0:
                _.append([x, y])
print(_)
# [[0, 0], [0, 3], [0, 6], [0, 9], [2, 0], [2, 3], [2, 6], [2, 9], [4, 0], [4, 3], [4, 6],
# [4, 9], [6, 0], [6, 3], [6, 6], [6, 9], [8, 0], [8, 3], [8, 6], [8, 9]]

w3 = [[x, y] for x in range(10) for y in range(10) if x % 2 == 0 if y % 3 == 0]
print(w3)
# [[0, 0], [0, 3], [0, 6], [0, 9], [2, 0], [2, 3], [2, 6], [2, 9], [4, 0], [4, 3], [4, 6],
# [4, 9], [6, 0], [6, 3], [6, 6], [6, 9], [8, 0], [8, 3], [8, 6], [8, 9]]

# 三维列表
d = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
print(d)
# [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
# 使用列表推导式创建一个 4 * 5 的二维列表，并将每个元素初始化为数字 8
d = [[8 for _ in range(5)] for _ in range(4)]
print(d)
# [[8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8]]
d = [[8] * 5 for _ in range(4)]
print(d)
# [[8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8]]

```

![image-20250428021557847](D:\Program Repository\github\basic\assets\image-20250428021557847.png)



## ==杨辉三角形==

==去掉[]和， :列表转字符串，并以空格连接起来==
    ==tri1 = " ".join(str(j) for j in i)==

==将字符串和  6 - 1 - len(str(j))  个空格以空格连接起来，其中 -1 的空格是以空格连接的空格==
    ==tri2 = " ".join(str(j) + " " * (6 - 1 - len(str(j))) for j in i)==

```python
# 杨辉三角形
tri = []
for i in range(10):
    tri.append([])
    for j in range(10):
        if i == 0:
            tri[i].append(1)
            break
        elif j == 0:
            tri[i].append(1)
        elif j == i:
            tri[i].append(1)
            break
        else:
            tri[i].append(tri[i-1][j-1]+tri[i-1][j])
for i in tri:
    # 去掉[]和， :列表转字符串，并以空格连接起来
    tri1 = " ".join(str(j) for j in i)
    print(tri1)
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
# 1 8 28 56 70 56 28 8 1
# 1 9 36 84 126 126 84 36 9 1

for i in tri:
    # 去掉[]和， :列表转字符串，并以空格连接起来
    # int的 j 转换成str后可计算长度
    # 将字符串和  6 - 1 - len(str(j))  个空格以空格连接起来，其中 -1 的空格是以空格连接的空格
    tri2 = " ".join(str(j) + " " * (6 - 1 - len(str(j))) for j in i)
    print(" " * 3 * (len(tri)-len(i)), tri2)
#                            1
#                         1     1
#                      1     2     1
#                   1     3     3     1
#                1     4     6     4     1
#             1     5     10    10    5     1
#          1     6     15    20    15    6     1
#       1     7     21    35    35    21    7     1
#    1     8     28    56    70    56    28    8     1
# 1     9     36    84    126   126   84    36    9     1

```



## ==顺时针输出==

```python
# 顺时针输出
# 按照顺时针螺旋顺序输出矩阵中的所有元素
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
# 四个方向的长度
top = 0
bottom = len(matrix)
left = 0
right = len(matrix[0])
result = []
# 每输出一圈少2行
for i in range(len(matrix) // 2 + 1):
    # 从头到尾依次输出
    for j in range(left, right):
        result.append(matrix[top][j])
    top += 1
    if top >= bottom:
        break
    for k in range(top, bottom):
        result.append(matrix[k][right-1])
    right -= 1
    if left >= right:
        break
    # 倒着生成range
    for l in range(right-1, left-1, -1):
        result.append(matrix[bottom-1][l])
    bottom -= 1
    if top >= bottom:
        break
    for m in range(bottom-1, top-1, -1):
        result.append(matrix[m][left])
    left += 1
    if left >= right:
        break
print(result)

```

![image-20250428142930067](D:\Program Repository\github\basic\assets\image-20250428142930067.png)



# 8.元组

rhyme = (1, 2, 3, 4, 5, "上山打老虎")

元组只需要  ,   隔开

元组是不可变的

## 元组

```python
# 元组
# 元组只需要  ,   隔开
# 元组是不可变的， 元组小括号可以省略
rhyme = (1, 2, 3, 4, 5, "上山打老虎")
rhyme = 1, 2, 3, 4, 5, "上山打老虎"

# 切片
print(rhyme[:3])
# (1, 2, 3)
print(rhyme[:])
# (1, 2, 3, 4, 5, '上山打老虎')
print(rhyme[:: 2])
# (1, 3, 5)
print(rhyme[:: -1])
# ('上山打老虎', 5, 4, 3, 2, 1)

# count计算其中某个元素有多少个 index索引第一次出现的位置
nums = (1, 2, 3, 6, 3, 9, 6, 3)
print(nums.count(3))
# 3
print(nums.index(9))
# 5


print(rhyme + nums)
# (1, 2, 3, 4, 5, '上山打老虎', 1, 2, 3, 6, 3, 9, 6, 3)
print(rhyme * 3)
# (1, 2, 3, 4, 5, '上山打老虎', 1, 2, 3, 4, 5, '上山打老虎', 1, 2, 3, 4, 5, '上山打老虎')

# 嵌套元组
w = rhyme, nums
print(w)
# ((1, 2, 3, 4, 5, '上山打老虎'), (1, 2, 3, 6, 3, 9, 6, 3))
for i in w:
    print(i)
# (1, 2, 3, 4, 5, '上山打老虎')
# (1, 2, 3, 6, 3, 9, 6, 3)
for i in w:
    for j in i:
        print(j, end=" ")
print()
# 1 2 3 4 5 上山打老虎 1 2 3 6 3 9 6 3


# 列表推导式，注意：   结果生成为列表
s = (1, 2, 3, 4, 5)
print([i * 2 for i in s])
# [2, 4, 6, 8, 10]

# 生成只有一个元素的元组
x = (343, )
print(x, type(x))
# (343,) <class 'tuple'>

# 打包：生成一个元组  解包：把元组中的元素一次性赋值给三个变量名   (适用于任何序列类型)
t = (123, "FishC", 3.14)
x, y, z = t
print(t, x, y, z)
# (123, 'FishC', 3.14) 123 FishC 3.14

# 列表解包
t = [123, "FishC", 3.14]
x, y, z = t
print(t, x, y, z)
# [123, 'FishC', 3.14] 123 FishC 3.14

# 字符串解包
a, b, c, d, e = y
print(y, a, b, c, d, e, type(y), type(a))
# FishC F i s h C <class 'str'> <class 'str'>
a, b, c, d, e = "FishC"
print(a, b, c, d, e, type(a))
# F i s h C <class 'str'>

# *c   将c作为列表装入剩余字符
a, b, *c = "FishC"
print(a, b, c, type(a), type(b), type(c))
# F i ['s', 'h', 'C'] <class 'str'> <class 'str'> <class 'list'>

x, y = 10, 20
# 实际上：
_ = 10, 20
x, y = _

# 元组中的列表，当元组中的元素为列表时，该列表可以被修改
s = [1, 2, 3]
t = [4, 5, 6]
w = (s, t)
print(w)
# ([1, 2, 3], [4, 5, 6])
w[0][0] = 0
print(w)
# ([0, 2, 3], [4, 5, 6])

```



## 创建元组、列表时间

```python
# 创建元组、列表时间
# 测试一下到底是创建列表的速度快，还是创建元组的速度快？为了得到更精准的数据，请重复测试 100 次，并分别计算出平均时间。
import timeit
# timeit 会默认执行操作1000000次
# timeit.timeit('x = 123', number=10000) 修改次数为10000次
list_time = timeit.repeat("x = [1, 2, 3, 4, 5]", repeat=100)
tuple_time = timeit.repeat("x = (1, 2, 3, 4, 5)", repeat=100)
list_time1 = 0
tuple_time1 = 0
for i in list_time:
    list_time1 += i
list_time1 = list_time1 / 100
print(list_time1)
# 0.04321513000000001
for i in tuple_time:
    tuple_time1 += i
tuple_time1 = tuple_time1 / 100
print(tuple_time1)
# 0.011897149999999997

```



# 9.字符串

## 大小写转换与对齐

```python
# 大小写转换与对齐
# 字符串不可变，改变字符串时实际上是生成一个新的字符串

# capitalize 将整个字符串首字母大写其余变小写
# casefold 将整个字符串变小写（与lower不一样的是它可以处理英文之外的字母）
# title 将字符串中每个单词的首字母大写
# swapcase 将整个字符串所有字母大小写翻转
# upper 将整个字符串变大写
# lower 将整个字符串变小写
x = "I Love FishC"
print(x.capitalize())
# I love fishc
print(x.casefold())
# i love fishc
print(x.title())
# I Love Fishc
print(x.swapcase())
# i lOVE fISHc
print(x.upper())
# I LOVE FISHC
print(x.lower())
# i love fishc

# 左中右对齐
# center(width, fillchar='") 居中对齐，默认空格填充
# ljust(width, fillchar='") 左对齐，默认空格填充
# rjust(width, fillchar='") 右对齐，默认空格填充
# zfill(width) 用0填充左侧
x = "有内鬼，停止交易"
print(x.center(15))
#    有内鬼，停止交易
print(x.ljust(15))
# 有内鬼，停止交易
print(x.rjust(15))
#        有内鬼，停止交易
print(x.zfill(15))
# 0000000有内鬼，停止交易

print("-520".zfill(10))
# -000000520
print("-520".rjust(10, "0"))
# 000000-520
print("I love FishC".swapcase()[::-1])
# cHSIf EVOL i

# 判断回文数
num = ["123", "33211", "12321", "13531", "112233"]
pr = [i for i in num if i == i[::-1]]
print(pr)
# ['12321', '13531']

```



## 整理字符串与ASCII转换

==ord 将字母转换成ASCII， chr 将ASCII转换成字母==

```python
# 整理字符串与ASCII转换
# 一个整理好的字符串中，两个相邻字符 s[j] 和 s[j+1]，其中 0 <= j <= s.length - 2，要满足如下条件：
# 若 s[j] 是小写字符，则 s[j+1] 不可以是相同的大写字符
# 若 s[j] 是大写字符，则 s[j+1] 不可以是相同的小写字符
# 如果 s[j] 和 s[j+1] 满足以上两个条件，则将它们一并删除
s = input("请输入待整理的字符串:")
# 请输入待整理的字符串:AAAaBbcC
# 字符串不可变，转换成列表来处理1
s2 = list(s)
j = 0
while j < len(s2) - 1:
    if s2[j].lower() == s2[j + 1].lower() and s2[j] != s2[j + 1]:
        # 先去掉了j，j+1变成了j
        s2.pop(j)
        s2.pop(j)
        j = j - 1
        print(s2)
        # ['A', 'A', 'B', 'b', 'c', 'C']
        # ['A', 'A', 'c', 'C']
    else:
        j = j + 1

s3 = ''.join(s2)
print(s3)
# ['A', 'A']

# 给定的字符串 s 是按照如下规则存放的：它的偶数下标为小写英文字母，奇数下标为正整数。
# 题目要求：编写代码，将奇数下标的数字转换为相对于上一个字母偏移后的字母。
s = "a1b2c3"
# # ord 将字母转换成ASCII， chr 将ASCII转换成字母
# print(ord("A"), ord("Z"),ord("a"))
# # 97
# print(chr(97))
# # a
# print(ord("z"))
# # 122
s1 = list(s)
for i in range(len(s1)-1):
    if s1[i].isalpha() and s1[i + 1].isdigit():
        s1[i + 1] = chr(ord(s1[i])+int(s1[i+1]))
s = ''.join(s1)
print(s)

```



## 查找与替换

```python
# 查找与替换
# 查找
# count(sub[,start[,end]]) 查找指定的子字符串出现的次数
# find(sub[,start[,end]]) 从左往右找指定的子字符串， 找不到返回-1
# rfind(sub[,start[,end]]) 从右往左找指定的字符串， 找不到返回-1
# index(sub[,start[,end]]) 从左往右找指定的子字符串， 找不到抛出异常
# rindex(sub[,start[,end]]) 从右往左找指定的字符串， 找不到抛出异常
x = "上海自来水来自海上"
print(x.count("海"))
# 2
print(x.count("海", 2, 8))
# 1
print(x.find("海"))
# 1
print(x.rfind("海"))
# 7
print(x.find("龟"))
# -1
# print(x.index("龟"))
# Traceback (most recent call last):
#   File "D:\Program Repository\github\basic\strings\strings_demo02.py", line 18, in <module>
#     print(x.index("龟"))
# ValueError: substring not found

# 替换
# expandtabs([tabsize]) 使用来替换tab制表符，并返回一个新的字符串
# replace(old, new, count=-1) 将旧字符串替换为新字符串，count 替换的次数，默认-1
# 尽量用空格代替tab
code = """
    print("I Love FishC")
    print("I Love My Wife")"""
new_code = code.expandtabs(4)
print(new_code)
#
#     print("I Love FishC")
#     print("I Love My Wife")
w = "在吗！我在你家楼下，快点下来！！！"
print(w.replace("在吗", "想你"))
# 想你！我在你家楼下，快点下来！！！

# str.maketrans[x[,y[,z]]] 制定转换规则的表格，x 替换成y 忽略z中包含的字母
# translate(table) 将字符串以表格中的规则替换
table = str.maketrans("ABCDEFG", "1234567")
q = "I Love FishC"
print(q.translate(table))
# I Love 6ish3
print("I Love FishC".translate(str.maketrans("ABCDEFG", "1234567")))
# I Love 6ish3
print("veol Love FishC".translate(str.maketrans("ABCDEFG", "1234567", "love")))
# I  6ish3  z中包含l o v e, 故veol ove都被忽略

x = "上海自来水来自海上"
print(x.rindex("来水来"))
# 3

```



## 版本号比较与加密（规则替换）

```python
# 版本号比较与加密（规则替换）
# 用户输入两个版本号 v1 和 v2，请编写代码比较它们，找出较新的版本。
# 版本号是由一个或多个修订号组成，各个修订号之间由点号（.）连接，每个修订号由多位数字组成，例如 1.2.33 和 0.0.11 都是有效的版本号。
# 从左到右的顺序依次比较它们的修订号，点号（.）左侧的值要比右侧的权重大，即 0.1 要比 0.0.99 大。
v1 = input("请输入第一个版本号，v1 = ")
v2 = input("请输入第二个版本号，v2 = ")
m, n = len(v1), len(v2)
i, j = 0, 0
x, y = 0, 0
while i < m or j < n:
    x, y = 0, 0
    # 舍弃. 直接用数字进行比较
    while i < m and v1[i] != '.':
        x = x * 10 + int(v1[i])
        i += 1
    i += 1
    while j < n and v2[j] != '.':
        y = y * 10 + int(v2[j])
        j += 1
    j += 1
    if x > y:
        print("v1")
        break
    elif x < y:
        print("v2")
if x == y:
    print("v1 == v2")
# 请输入第一个版本号，v1 = 1.0.0
# 请输入第二个版本号，v2 = 1
# v1 == v2

# 加密
# 编写一个加密程序，其实现原理是通过替换指定的字符进行加密，附加要求是实现密文逆向检测。
s = input("请输入需要加密的明文：")
t1 = input("请输入需要替换的字符：")
t2 = input("请输入将1要替换的字符：")
i = 0
if len(t1) == len(t2):
    table = str.maketrans(t1, t2)
    print("加密后的密文是：", s.translate(table))
    while i < len(t1) - 1:
        if t1[i] == t1[i + 1] or t2[i] == t2[i + 1]:
            print("由于替换字符出现冲突，该密文无法解密！")
            break
        i += 1
else:
    print("需要替换的字符数量必须跟将要替换的字符数量一致！")

```



## 字符串判断

```python
# 判断
# startswith(prefix[,start[,end]]) 参数指定的子字符串是否在字符串的起始位置
# endswith(prefix[,start[,end]]) 参数指定的子字符串是否在字符串的末尾位置

# isupper() 是否全都为大写
# islower() 是否全都为小写
# istitle() 是否所有字母都为开头字母大写
# isalpha() 是否全都为字母
# isascii() 是否为ASCII码
# isspace() 是否为空格
# isprintable() 是否可打印
# isdecimal() 是否都为十进制数字
# isdigit() 是否都为数字字符
# isnumeric() 是否都是数值字符（小数不行。小数有点）
# isalnum() 是否只包含字母和数字（数字为isnumeric级）
# isidentifier() 是否为合法的标识符（如：变量名）

# 以“ ”为起始，结尾
x = "I love FishC"
print(x.startswith("I"))
# True
print(x.endswith("FishC"))
# True
print(x.endswith("C"))
# True
print(x.endswith("c"))
# False
print(x.endswith("hC"))
# True
print(x.endswith("Fi", 0, 9))
# True
# 还支持以元组的形式输入，元组中只要有一个成功匹配就返回True
print(x.startswith(("her", "hew", "I")))
# True

# 是否为字母、空格、可打印
print(x.istitle())
# False
print(x.isupper())
# False
print(x.upper().isupper())
# True 强制True  先转换成大写再判断
print(x.islower())
# False
print(x.isalpha())
# False 其中还有空格
print("   \n".isspace())
# True tab,空格,\n都算空格
print("   \n".isprintable())
# False 转义字符不可打印

# 是否为数字
x = "12345"
print(x.isdecimal())
# True
print(x.isdigit())
# True
print(x.isnumeric())
# True

# 使用unicode字符串输出平方符号
x = "2\u00b2"
print(x)
# 2²
print(x.isdecimal())
# False
print(x.isdigit())
# True
print(x.isnumeric())
# True

# 罗马字符
x = "ⅠⅡⅢⅣⅤⅥ"
print(x.isdecimal())
# False
print(x.isdigit())
# False
print(x.isnumeric())
# True
print(x.isalnum())
# True

# 是否为标识符
print("I am a good boy".isidentifier())
# False
print("I_am_a_good_boy".isidentifier())
# True
print("FishC520".isidentifier())
# True
print("520FishC".isidentifier())
# False

# 关键字
import keyword
print(keyword.iskeyword("if"))
# True

```



## 字符串判断Demo

```python
# 给定一个字符串 text 和字符串列表 words，返回 words 中每个单词在 text 中的位置（要求最终的位置从小到大进行排序）。
# text = "I love FishC and FishC love me"
# words = "FishC"
# 输出：[[7, 11], [17, 21]]
# text = "I love FishC and FishC love me"
# words = "FishC love"
# # 输出：[[2, 5], [7, 11], [17, 21], [23, 26]]
# text = "FCFCF"
# words = "FCF FC"
# 输出：[[0, 1], [0, 2], [2, 3], [2, 4]]
text = input("请输入text的内容：")
words = input("请输入words的内容：")
position = []
for word in words.split():
    print(word)
    index = text.find(word)
    while index != -1:
        position.append([index, (index + len(word)) - 1])
        index = text.find(word, index + 1)
position.sort()
print(position)


# 编写一个程序，判断输入的字符串是否由多个子字符串重复多次构成。
# word = "FCFC"
# 输出：True
# word = "FishCFish"
# 输出：False
# word = "FCCF"
# 输出：False
# word = "FishCFishc"
# 输出：False
word = input("请输入要判断的字符串：")
length = len(word)
length2 = 0
for i in range(1, length // 2 + 1):
    same = word[:i]
    length2 = len(same)
    index = word.find(same, length2)
    while index != -1:
        length2 += len(same)
        index = word.find(same, length2)
    else:
        if length2 <= length // 2:
            continue
if length2 >= length:
    print("True")
else:
    print("False")

```




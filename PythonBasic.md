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



# 7.列表list

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

# 第二种解法：摩尔投票法
# 摩尔投票法分为两个阶段：
# 对抗阶段：分属两个候选人的票数进行两两对抗抵消
# 计数阶段：计算对抗结果中最后留下的候选人票数是否有效
nums = [2, 2, 4, 2, 3, 6, 2]

# 对抗阶段
major = nums[0]
count = 0
for each in nums:
    if count == 0:
        major = each
    if each == major:
        count += 1
    else:
        count -= 1

# 统计阶段
if nums.count(major) > len(nums) / 2:
    print("主要元素是：", major)
else:
    print("不存在主要元素。")
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



# 8.元组tuple

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



# 9.字符串string

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



## ==整理字符串与ASCII转换==

==ord 将字母转换成ASCII， chr 将ASCII转换成字母==

```python
# 整理字符串与ASCII转换
# 一个整理好的字符串中，两个相邻字符 s[j] 和 s[j+1]，其中 0 <= j <= s.length - 2，要满足如下条件：
# 若 s[j] 是小写字符，则 s[j+1] 不可以是相同的大写字符
# 若 s[j] 是大写字符，则 s[j+1] 不可以是相同的小写字符
# 如果 s[j] 和 s[j+1] 满足以上两个条件，则将它们一并删除
# s = input("请输入待整理的字符串:")
# # 请输入待整理的字符串:AAAaBbcC
# # 字符串不可变，转换成列表来处理1
# s2 = list(s)
# j = 0
# while j < len(s2) - 1:
#     if s2[j].lower() == s2[j + 1].lower() and s2[j] != s2[j + 1]:
#         # 先去掉了j，j+1变成了j
#         s2.pop(j)
#         s2.pop(j)
#         j = j - 1
#         print(s2)
#         # ['A', 'A', 'B', 'b', 'c', 'C']
#         # ['A', 'A', 'c', 'C']
#     else:
#         j = j + 1
#
# s3 = ''.join(s2)
# print(s3)
# ['A', 'A']

# 方法二：
s = input("请输入一个字符串：")

res = []
for each in s:
    if res and res[-1].lower() == each.lower() and res[-1] != each:
        res.pop()
    else:
        res.append(each)

for each in res:
    print(each, end='')



# 给定的字符串 s 是按照如下规则存放的：它的偶数下标为小写英文字母，奇数下标为正整数。
# 题目要求：编写代码，将奇数下标的数字转换为相对于上一个字母偏移后的字母。
s = "z1a2c3"
# # ord 将字母转换成ASCII， chr 将ASCII转换成字母
# print(ord("A"), ord("Z"), ord("a"), ord("z"))
# # 65 90 97 122
# print(chr(97))
# # a
s1 = list(s)
for i in range(len(s1)-1):
    if s1[i].isalpha() and s1[i + 1].isdigit():
        temp = ord(s1[i])+int(s1[i+1])
        if 97 <= temp <= 122:
            s1[i + 1] = chr(temp)
        elif temp > 122:
            s1[i + 1] = chr(temp - 122 + 97 -1)
        else:
            s1[i + 1] = chr(temp - 122)
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



## 截取字符串

```python
# 截取字符串
# 以所给字符串中单个字符串为单位来剔除
# strip(chars=None) 以所给字符串中单个字符串为单位来剔除当前字符串左右字符
# lstrip(chars=None) 以所给字符串中单个字符串为单位来剔除当前字符串左侧字符
# rstrip(chars=None) 以所给字符串中单个字符串为单位来剔除当前字符串右侧字符
# 剔除掉指定的子字符串
# removeprefix(prefix) 剔除掉整个字符串的指定前缀
# removesuffix(psuffix) 剔除掉整个字符串的指定后缀
# 截取掉空白
print("    左侧不要留白".lstrip())
# 左侧不要留白
print("右侧不要留白    ".lstrip())
# 右侧不要留白
print("    左右都不要留白    ".lstrip())
# 左右都不要留白
print("www.ilovefishc.com".lstrip("wcom.lh"))
# ilovefishc.com
print("www.ilovefishc.com".rstrip("wcom.lh"))
# www.ilovefis
print("www.ilovefishc.com".strip("wcom.lh"))
# ilovefis

print("www.ilovefishc.com".removeprefix("www."))
# ilovefishc.com
print("www.ilovefishc.com".removesuffix(".com"))
# www.ilovefishc
print("www.ilovefishc.com".removeprefix("love"))
# www.ilovefishc.com


# 拆分和拼接
# partition(sep) 根据所给字符串从左到右查找来分割当前字符串，并返回相应的三元组
# rpartition(sep) 根据所给字符串从右到左查找来分割当前字符串，并返回相应的三元组
print("www.ilovefishc.com".partition("."))
print("www.ilovefishc.com".rpartition("."))

# split(sep=None,maxsplit=-1) 默认从左到右以空格来切割，不限次数切割，将结果以列表形式返回
# rsplit(sep=None,maxsplit=-1) 默认从右到左以空格来切割，不限次数切割，将结果以列表形式返回
# 换行符：\n,\r
# splitlines(keepends=False) 按行切割，将结果以列表形式返回 keepspends 指定结果是否包含换行符
print("www.ilovefishc.com".split(".", 1))
# ['www', 'ilovefishc.com']
print("www.ilovefishc.com".rsplit(".", 1))
# ['www.ilovefishc', 'com']
print("www\nilovefishc\rcom".splitlines())
# ['www', 'ilovefishc', 'com']
print("www\nilovefishc\rcom".splitlines("True"))
# ['www\n', 'ilovefishc\r', 'com']

# join(iterable) 字符串拼接
print(".".join(["www", "ilovefishc", "com"]))
# www.ilovefishc.com

# split() 方法常常被应用于对数据的解析处理，那么考考大家，如果要从字符串 "https://ilovefishc.com/html5/index.html"
# 中提取出 "ilovefishc.com"，使用 split() 方法应该如何实现呢？
url = "https://ilovefishc.com/html5/index.html"
parsed_url = url.split("https://")[1].split("/")[0]
print(parsed_url)
# ilovefishc.com

print(",\n".join("FishC"))
# F,
# i,
# s,
# h,
# C

```



## ==位移加密与同行字符串==

```python
# 位移加密（凯撒密码）  同行键盘字符串
# 凯撒密码是一种通过位移加密的方法，对 26 个（大小写）字母进行位移加密，比如下方是正向位移 6 位的字母对比表：
# 明文字母表如下
# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
# 密文字母表如下
# GHIJKLMNOPQRSTUVWXYZABCDEF
# 所以，如果给定加密的明文是：
# I love FishC
# 那么程序 +6 加密后输出的密文便是：
# O rubk LoynI
# text = "I love FishC"
# position = 6
# text = "I love FishC"
# position = -6
# text_encryption : C fipy ZcmbW
text = input("请输入需要加密的明文（只支持英文字母）：")
position = int(input("请输入移动的位数："))
char_encryption = []
for char in text:
    if char == " ":
        char_encryption.append(" ")
    else:
        temp = ord(char) + position
        if 97 <= temp <= 122 or 65 <= temp <= 90:
            char_encryption.extend(chr(temp))
        elif temp > 122:
            char_encryption.extend(chr(temp - 122 + 97 - 1))
        elif 90 < temp < 97 and 65 <= ord(char) <= 90:
            char_encryption.extend(chr(temp - 90 + 65 - 1))
        elif 90 < temp < 97 and 97 <= ord(char) <= 122:
            char_encryption.extend(chr(122 - (97 - temp - 1 )))
        else:
            char_encryption.extend(chr(90 - (65 - temp - 1 )))
    text_encryption = "".join(char_encryption)
print(text_encryption)


# 同行键盘字符串
# 给定一个字符串数组 words，只返回可以使用在美式键盘同一行的字母打印出来的单词
str1 = "qwertyuiop"
str2 = "asdfghjkl"
str3 = "zxcvbnm"
words = ["Twitter", "TOTO", "FishC", "Python", "ASL"]
words_new = []
for word in words:
    i = 1
    if str1.find(word[0].lower()) != -1:
        while i < len(word):
            if str1.find(word[i].lower()) != -1:
                i += 1
            else:
                break
    elif str2.find(word[0].lower()) != -1:
        while i < len(word):
            if str2.find(word[i].lower()) != -1:
                i += 1
            else:
                break
    else:
        while i < len(word):
            if str3.find(word[i].lower()) != -1:
                i += 1
            else:
                break
    if i == len(word):
        words_new.append(word)
print(words_new)
# ['Twitter', 'TOTO', 'ASL']

```



## ==format 格式化字符串==

```python
# format 格式化字符串
# "{} {}".format(value1, value2) 将变量插入字符串
year = 2025
print("正式开始学习于{}年".format(year))
# 正式开始学习于2025年
print("正式开始{}于{}年".format("学习","2025"))
# 正式开始学习于2025年
print("正式开始{1}于{0}年".format("学习","2025"))
# 正式开始2025于学习年
print("{1}正式开始{1}于{0}年".format("学习","2025"))
# 2025正式开始2025于学习年
print("{year}正式开始{learn}于{year}年".format(learn = "学习",year = "2025"))
# 2025正式开始学习于2025年
print("{name}于{1}开始学习{0}".format("python", "2025", name = "贪影战"))

# 在字符串中输出{}
print("{},{},{}".format(1, "{}", 2))
# 1,{},2
# 两层括号是转义
print("{},{{}},{}".format(1, 2))
# 1,{},2

# format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
# align
# '<'	强制字符串在可用空间内左对齐（默认）
# '>'	强制字符串在可用空间内右对齐
# '='	强制将填充放置在符号（如果有）之后但在数字之前的位置（这适用于以 “+000000120” 的形式打印字符串）
# '^'	强制字符串在可用空间内居中
# 用数字类型（其它类型不支持，会报错）的可感知正负的0填充
print("{:^10}".format(250))
#    250
print("{:=10}".format(250))
#        250
print("{1:>10}{0:<10}".format(520, 250))
#        250520
print("{left:>10}{right:<10}".format(right = 520, left = 250))
#        250520

# 用数字类型（其它类型不支持，会报错）的可感知正负的0填充
print("{:010}".format(-250))
# -000000250
print("{1:%>10}{0:%<10}".format(520, 250))
# 一对{}转义出一个普通的花括号{}
print("{{0}}".format(1))
# {0}
print("{{{0}}}".format(1))
# {1}
print("{{{{0}}}}".format(1))
# {{0}}
print("{{{{{0}}}}}".format(1))
# {{1}}

# sign
# '+'	正数在前面添加正号（+），负数在前面添加负号（-）
# '-'	只有负数在前面添加符号（-），默认行为
# 空格	正数在前面添加一个空格，负数在前面添加负号（-）
# 设置千位分隔符，它有两个值可以选择 —— ',' 或 '_'
print("{:+}{:-}{:-}{: }".format(520, 250, -250, 250))
# +520250-250 250
print("{:,}".format(1234))
print("{:_}".format(1234))

# .precision 适用非整数
# 对于以 'f' 或 'F' 格式化的浮点数值来说，是限定小数点后显示多少个数位
# 对于以 'g' 或 'G' 格式化的浮点数值来说，是限定小数点前后共显示多少个数位
# 对于非数字类型来说，限定最大字段的大小（换句话说就是要使用多少个来自字段内容的字符）
# 对于整数来说，则不允许使用该选项值
print('{} {:.2f}'.format('Pi =', 3.1415))
# Pi = 3.14
print('{} {:.2g}'.format('Pi =', 3.1415))
# Pi = 3.1
print("{:.6}".format("I love Python"))
# I love

# type
# 适用整数
# 'b'	将参数以二进制的形式输出
# 'c'	将参数以 Unicode 字符的形式输出
# 'd'	将参数以十进制的形式输出
# 'o'	将参数以八进制的形式输出
# 'x'	将参数以十六进制的形式输出
# 'X'	将参数以十六进制的形式输出
# 'n'	跟 'd' 类似，不同之处在于它会使用当前语言环境设置的分隔符插入到恰当的位置
# None	跟 'd' 一样
# #     参数以二进制、八进制或十六进制在字符串中输出的时候，会自动追加前缀 "0b"、"0o" 和 "0x"。
print("{:b}".format(80))
# 1010000
print("{:c}".format(80))
# P
print("{:o}".format(80))
# 120
print("{:x}".format(80))
# 50
print("{:#x}".format(80))
# 0x50

# e'	将参数以科学记数法的形式输出（以字母 'e' 来标示指数，默认精度为 6）
# 'E'	将参数以科学记数法的形式输出（以字母 'E' 来标示指数，默认精度为 6）
# 'f'	将参数以定点表示法的形式输出（“不是数” 用 'nan' 标示，无穷用 'inf' 标示，默认精度为 6）
# 'F'	将参数以定点表示法的形式输出（“不是数” 用 'NAN' 标示，无穷用 'INF' 标示，默认精度为 6）
# 'g'	通用格式，小数以 'f' 形式输出，大数以 'e' 的形式输出
# 'G'	通用格式，小数以 'F' 形式输出，大数以 'E' 的形式输出示
# 'n'	跟 'g' 类似，不同之处在于它会使用当前语言环境设置的分隔符插入到恰当的位置
# '%'	以百分比的形式输出（将数字乘以 100 并显示为定点表示法（'f'）的形式，后面附带一个百分号
# None	类似于 'g'，不同之处在于当使用定点表示法时，小数点后将至少显示一位；默认精度与给定值所需的精度一致
print("{:e}".format(3.1415))
# 3.141500e+00
print("{:g}".format(12345678))
# 1.23457e+07
print("{:g}".format(1234.5678))
# 1234.57
print("{:%}".format(0.98))
# 98.000000%
print("{:.2%}".format(0.98))
# 98.00%

print("{:{fill}{align}{width}.{prec}{type}}".format(3.1415, fill="+", align="^", width=10, prec=2, type="g"))
# +++3.1++++


# ——————————————————————————————————————————————————————————
# f-string(python 3.6以后版本)
# 语法糖：指计算机语言中添加的某种语法，这种语法对语言的功能没有影响，但是更方便程序员使用，语法糖让程序更加简洁，有更高的可读性。
year = 2025
print(f"今年是{year}年")
# 今年是2025年
print(f"1+1={1 + 1}，2的平方是{pow(2, 2)}，3的立方是{pow(3, 3)}")
# 1+1=2，2的平方是4，3的立方是27
print(f"{-520:010}")
# -000000520
print(f"{12345678:,}")
# 12,345,678
print(f"{3.1415:.2f}")
# 3.14
print(f"{3.1415:+^10.3g}")
# +++3.14+++
fill = "+"
align = "^"
width = 10
prec = 3
type = "g"
print(f"{3.1415:{fill}{align}{width}.{prec}{type}}")
# +++3.1++++

```



## 格式化练习

```python
# 格式化练习
# 请编写一个程序，统计字符串中的单词个数（“单词”以空格进行分隔）
# str1 = ""
# 输出：0
# str1 = "Python"
# 输出：1
str1 = "I love FishC"
# 输出：3
words = str1.split()
print(len(words))

# 请编写一个程序，将用户输入的字符串重新格式化，使得字母和数字相互分隔（即一个字母一个数字相互间隔）
# str2 = "FishC1314"
# 输出：F1i3s1h4C
# str2 = "FishC520"
# 输出：字符串中数字和字母的数量不满足重新格式化的条件
str2 = "Python6543210"
# 输出：6P5y4t3h2o1n0
alp = 0
alptemp = []
num = 0
numtemp = []
str_new = []
for word in str2:
    if word.isalpha():
        alp = alp + 1
        alptemp.append(word)
    elif word.isdecimal():
        num = num + 1
        numtemp.append(word)
if alp - num == 1:
    for i in range(len(str2)):
        print(i, i % 2)
        if i % 2 != 0:
            str_new.append(numtemp[i // 2])
        else:
            str_new.append(alptemp[i // 2])
    print("".join(str_new))
elif alp - num == -1:
    for i in range(len(str2)):
        if i % 2 != 0:
            str_new.append(alptemp[i // 2])
        else:
            str_new.append(numtemp[i // 2])
    print("".join(str_new))
else:
    print("字符串中数字和字母的数量不满足重新格式化的条件")

```



## 压缩与解压

```python
# 压缩与解压
# 利用字符重复出现的次数，编写一个程序，实现基本的字符串压缩功能。比如，字符串 FFiiiisshCCCCCC 压缩后变成 F2i4s2h1C6（15字符 -> 10字符，66% 压缩率）。
# 对于重复次数小于 3 的字符，我们的程序应该选择不对其进行压缩。
string = "FFiiiisshCCCCCC"
# 压缩后：FFi4sshC6
# 压缩率为：60.00%
# string = input("请输入待压缩字符串：")
string_comp = []
temp = 0
char = 0
while char < len(string):
    index = string.find(string[char], char)
    while index != -1:
        temp += 1
        index = string.find(string[char], char + temp)
    else:
        if temp < 3:
            for i in range(temp):
                string_comp.append(string[char])
        else:
            string_comp.append(string[char])
            string_comp.append(str(temp))
    char = char + temp
    temp = 0
string_comp1 = ''.join(string_comp)
print("压缩后的字符串：", string_comp1)
print("压缩率为：", f"{len(string_comp) / len(string):.2%}")

# 解压
string_decomp = []
char = 0
while char < len(string_comp1):
    if string_comp1[char].isalpha():
        string_decomp.append(string_comp1[char])
    elif string_comp1[char].isdigit():
        for i in range(int(string_comp1[char]) - 1):
            string_decomp.append(string_comp1[char - 1])
    char += 1
string_decomp1 = ''.join(string_decomp)
print("解压后的字符串:", string_decomp1)

```



# 10.序列sequence

## ==序列==

enumerate() 用于返回一i个枚举对象，它的功能就是将可迭代对象中的每个元素及从0开始的序号共同构成一个二元组的列表

zip() 用于创建一个聚合多个可迭代对象的迭代器它会将作为参数传入的每个可迭代对象依次组合成元组，即第i个元组包含来自每个参数的第i个元素
zip 当长度不一时，以最短的为准，长的会舍弃掉若要保留长的部分，需要调用itertools

map() 它会根据提供的函数对指定的可迭代对象的每个元素进行运算，并将 返回运算结果 的迭代
和zip一样，以最短的为准

filter() 它会根据提供的函数对指定的可迭代对象的每个元素进行运算，并将 运算结果为真的元素 以迭代器的形式返回

迭代器与可迭代对象
迭代器一定是一个可迭代对象，可迭代对象可以重复使用，而迭代器是一次性的，临时存储
iter 将可迭代对象转换成一次性的迭代器， 所有的可迭代对象都可以转换成一次性的迭代器
next 逐个将迭代器中的元素提取出来，使用一次提取一个

```python
# 序列
x = "FishC"
y = [1, 2, 3]
# 删除 x, y这个变量，使其不再指向任何对象
del x, y
x = [1, 2, 3, 4, 5]
del x[1:4]
print(x)
# [1, 5]
y = [1, 2, 3, 4 ,5]
y[1:4] = []
print(y)
# [1, 5]
x = [1, 2, 3, 4, 5]
del x[::2]
print(x)
# [2, 4]

# max, min 按Ascii值对字母进行排序
print(max("FiShC"))
# i
s = []
# default 当调用函数时，如果没有提供该参数的值，将使用默认值
print(min(s, default="啥都没有"))
# 啥都没有

# len读取的长度不能超过pow(2,63) - 1

s = [1, 2, 3, 0, 6]
print(sum(s))
# 12
print(sum(s, start=100))
# 112

# sorted 排序但不改变，并给出返回值
# .sort 排序且改变，但不给出返回值
print(sorted(s), s)
# [0, 1, 2, 3, 6] [1, 2, 3, 0, 6]
s.sort()
print(s)
# [0, 1, 2, 3, 6]
# key  关键值，作为根据 如排序依据
t = ["FishC", "Apple", "Book", "Banana", "Pen"]
print(sorted(t))
# ['Apple', 'Banana', 'Book', 'FishC', 'Pen']
print(sorted(t, key=len))
# ['Pen', 'Book', 'FishC', 'Apple', 'Banana']

# reversed 返回的是一个迭代器对象，需要list进行转换才能正常使用
print(reversed(t))
# <list_reverseiterator object at 0x000001D1AEC65CC0>
print(list(reversed(t)))
# ['Pen', 'Banana', 'Book', 'Apple', 'FishC']

print(list(reversed(sorted("FishC520"))))
# ['s', 'i', 'h', 'F', 'C', '5', '2', '0']

# all() 判断是否全部为真 any() 是否存在某个元素的值为真
x = [1, 1, 0]
y = [1, 1, 9]
print(all(x), all(y), any(x), any(y))
# False True True True

# ————————————————————————————————————————————
# enumerate() 用于返回一i个枚举对象，它的功能就是将可迭代对象中的每个元素及从0开始的序号共同构成一个二元组的列表
print(list(enumerate(x)))
# [(0, 1), (1, 1), (2, 0)]
print(list(enumerate(x, start=10)))
# [(10, 1), (11, 1), (12, 0)]

# zip() 用于创建一个聚合多个可迭代对象的迭代器
# 它会将作为参数传入的每个可迭代对象依次组合成元组，即第i个元组包含来自每个参数的第i个元素
# zip 当长度不一时，以最短的为准，长的会舍弃掉
# 若要保留长的部分，需要调用itertools
print(list(zip(x, y)))
z = [1, 4, 5]
print(list(zip(x, y, z)))
# [(1, 1, 1), (1, 1, 4), (0, 9, 5)]
z = "FishC"
print(list(zip(x, y, z)))
# [(1, 1, 'F'), (1, 1, 'i'), (0, 9, 's')] 舍弃了hC
import itertools
zipped = itertools.zip_longest(x, y, z)
print(list(zipped))
# [(1, 1, 'F'), (1, 1, 'i'), (0, 9, 's'), (None, None, 'h'), (None, None, 'C')]

# map() 它会根据提供的函数对指定的可迭代对象的每个元素进行运算，并将 返回运算结果 的迭代器
# 和zip一样，以最短的为准
mapped = map(ord, "FishC")
print(list(mapped))
# [70, 105, 115, 104, 67]
mapped = map(pow, [2, 3, 10], [5, 2, 3])
print(list(mapped))
# [32, 9, 1000]
mapped = map(max, [1, 3, 5], [2, 2, 2], [0, 3, 9, 8])
print(list(mapped))
# [2, 3, 9] 舍弃了8

# filter() 它会根据提供的函数对指定的可迭代对象的每个元素进行运算，并将 运算结果为真的元素 以迭代器的形式返回
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))
# [2, 4]
print(list(filter(str.islower, "FishC")))
# ['i', 's', 'h']

# 迭代器与可迭代对象
# 迭代器一定是一个可迭代对象，可迭代对象可以重复使用，而迭代器是一次性的，临时存储
mapped = map(ord, "FishC")
print(list(mapped))
# [70, 105, 115, 104, 67]
print(list(mapped))
# []
# iter 将可迭代对象转换成一次性的迭代器， 所有的可迭代对象都可以转换成一次性的迭代器
# next 逐个将迭代器中的元素提取出来，使用一次提取一个
x = [1, 2, 3]
y = iter(x)
print(type(x), type(y))
# <class 'list'> <class 'list_iterator'>
print(next(y, "元素提取完毕"))
# 1
print(next(y, "元素提取完毕"))
# 2
print(next(y, "元素提取完毕"))
# 3
print(next(y, "元素提取完毕"))
# 元素提取完毕

matrix = [[1, 3, 2],
          [5, 4, 6],
          [8, 7, 9]]
mapped = map(sorted, matrix)
print(list(mapped))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list(filter(str.islower, "FishC")))
# ['i', 's', 'h']
print([i for i in "FishC" if i.islower()])
# ['i', 's', 'h']

```



## ==判断子序列与 查找最大奇数==

```python
# 判断子序列与 查找最大奇数
# 给定字符串 s 和 t ，请编程判断 s 是否为 t 的子序列。
# 字符串的子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串（例如，"ace" 是 "abcde" 的子序列，而 "aec" 则不是）。
s = "FishC"
# t = "FiiisjjhkkCBA"
t = "FijkhsC"
# s = input("请输入字符串s：")
# t = input("请输入字符串t：")
temp = 0
j = 0
while j < len(s):
    index = t.find(s[j])
    while index != -1:
        j += 1
        if j < len(s):
            index = t.find(s[j], index)
        else:
            break
    else:
        break
if j == len(s):
    print("字符串 s 是字符串 t 的子序列")
else:
    print("字符串 s 不是字符串 t 的子序列")

# 给定一个字符串 s，请编程求出该字符串中的最大奇数。
# s1 = "43383"
# 输出：43383
# s1 = "5926"
# 输出：59
# s1 = "966"
# 输出：9
s1 = "64062"
# 输出：0
s2 = []
for i in range(len(s1) - 1, -1, -1):
    if int(s1[i]) % 2 != 0:
        for j in range(i + 1):
            s2.append(s1[j])
        break
if len(s2) == 0:
    print("0")
else:
    print("".join(s2))

```



## 奇偶排序 翻转单词顺序

```python
# 奇偶排序 翻转单词顺序
# 给定一个整数列表，请编程来调整该列表中整数的顺序，使得所有奇数排好序后放在数组的前半部分，所有偶数排好序后放在数组的后半部分。
# 比如给定的整数列表是 [1, 8, 7, 3, 6, 5, 4, 2]，那么调整后的结果应该是 [1, 3, 5, 7, 2, 4, 6, 8]。
list1 = [1, 8, 7, 3, 6, 5, 4, 2]
odd = []
even = []
list2 = []
for i in range(len(list1)):
    if list1[i] % 2 == 0:
        even.append(list1[i])
    else:
        odd.append(list1[i])
list2.extend(sorted(odd))
list2.extend(sorted(even))
print(list2)
# [1, 3, 5, 7, 2, 4, 6, 8]

#  翻转单词顺序。
# 用户输入一个英文句子，请编程翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
# 例如输入字符串是 "I love FishC."，则输出 "FishC. love I"。
# 注意1：用户输入的字符串可能会在前面或者后面包含任意数量的空格，但是反转后的结果将会去除这些空格（例如输入字符串是 "   I love FishC.   "，结果依然输出 "FishC. love I"）。
# 注意2：用户输入的字符串中，单词之间可能不止一个空格，但是反转后的结果将统一使用一个空格作为单词之间的间隔（例如输入字符串是 "I   love        FishC."，结果依然输出 "FishC. love I"）
strings1 = "    I   love     FishC."
reverser = list(reversed(strings1.split()))
strings2 = ' '.join(reverser)
print(strings2)
# FishC. love I

```



## 密室打卡（打点计时器 zip)

```python
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

```



# 11.字典

字典这个数据结构活跃在所有python程序的背后，即便你的源码里没有直接用到它

字典是python中唯一实现映射关系的内置类型

## ==字典==

```python
# 字典{“key”:"value"}
y = {"吕布":"口口布", "关羽":"关习习"}
print(y["吕布"])
# 口口布

y["刘备"] = "刘baby"
print(y)
# {'吕布': '口口布', '关羽': '关习习', '刘备': '刘baby'}

# 创建字典的6种方法
# 1 直接赋值
a = {"吕布":"口口布", "关羽":"关习习", "刘备":"刘Baby"}
# 2 dict
b = dict(吕布="口口布", 关羽="关习习", 刘备="刘Baby")
# 3 dict中列表元素一一对应，类似zip
c = dict([("吕布", "口口布"), ("关羽", "关习习"), ("刘备", "刘Baby")])
# 4 dict + 直接赋值
d = dict({"吕布":"口口布", "关羽":"关习习", "刘备":"刘Baby"})
# 5 4+2混合
e = dict({"吕布":"口口布", "关羽":"关习习"}, 刘备="刘Baby")
# 6 dict +zip
f = dict(zip(["吕布","关羽","刘备"], ["口口布", "关习习", "刘Baby"]))
print(a == b == c == d == e == f)
# True

# 增删查改
# fromkeys(iterable[, value])
# 删 pop(key[, default]), 有返回值
# popitem 删除最后一个元素 有返回值
# 改 update
# 查 get(key[, default])
# setdefault(key, value) 查找key，若找到则返回值，找不到则将 key:value 加入字典中

# 快速初始化字典
x = dict.fromkeys("Fish", 250)
print(x)
# {'F': 250, 'i': 250, 's': 250, 'h': 250}
x["F"] = 70
print(x)
# {'F': 70, 'i': 250, 's': 250, 'h': 250}
x["C"] = 67
print(x)
# {'F': 70, 'i': 250, 's': 250, 'h': 250, 'C': 67}

# 删 pop(key[, default]), 有返回值
x.pop("C","不存在该值")
print(x)
# {'F': 70, 'i': 250, 's': 250, 'h': 250}
# popitem 删除最后一个元素 有返回值
x.popitem()
print(x)
# {'F': 70, 'i': 250, 's': 250}
del x["i"]
print(x)
# {'F': 70, 's': 250}

x.clear()
print(x)
# {}

z = dict()
z["a"] = 1, 2, 3, 4, 5
print(z, z["a"], z["a"][1])
# {'a': (1, 2, 3, 4, 5)} (1, 2, 3, 4, 5) 2

d = {}.fromkeys("吕布", 999)
print(d)
# {'吕': 999, '布': 999}

a = {"小甲鱼":"You are my super star."}
b = a
a.clear()
print(b)
# {}

d = dict.fromkeys("FishC")
print(d)
# {'F': None, 'i': None, 's': None, 'h': None, 'C': None}
d["s"] = 115
print(d)
# {'F': None, 'i': None, 's': 115, 'h': None, 'C': None}

# update 改
d.update({"i":105, "h":104})
print(d)
# {'F': None, 'i': 105, 's': 115, 'h': 104, 'C': None}
d.update(F=70, C=67)
print(d)
# {'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67}

# get(key[, default]) 查
# setdefault(key, value) 查找key，若找到则返回值，找不到则将 key:value 加入字典中
print(d.get("c", "这里没有c"), d.get("C"))
# 这里没有c 67
print(d["C"]) if "C" in d else print("这里没有c")
# 67

# setdefault(key, value) 查找key，若找到则返回值，找不到则将 key:value 加入字典中
print(d.setdefault("c", "code"))
# code
print(d)
# {'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67, 'c': 'code'}

# items(), keys(), value() 键值对，键和值三者的视图对象，随字典数据变化而变化
items = d.items()
keys = d.keys()
values = d.values()
print(items, keys, values)
# dict_items([('F', 70), ('i', 105), ('s', 115), ('h', 104), ('C', 67), ('c', 'code')]) dict_keys(['F', 'i', 's', 'h', 'C', 'c']) dict_values([70, 105, 115, 104, 67, 'code'])

e = d.copy()
print(e)
# {'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67, 'c': 'code'}
print(len(d))
# 6

print("C" in d, "c" not in d)
# True False
print(list(d))
# ['F', 'i', 's', 'h', 'C', 'c'] 输出所有的键构成的列表
print(list(d.values()))
# [70, 105, 115, 104, 67, 'code'] 输出所有的值构成的列表

# iter, next 迭代器
e = iter(d)
print(next(e))
# F
print(next(e))
# i

# reversed python3.8
print(list(reversed(d)))
# ['c', 'C', 'h', 's', 'i', 'F']

# 字典嵌套
d = {"吕布":{"语文":60, "数学":70, "英语":80}, "关羽":{"语文":70, "数学":70, "英语":60}}
print(d)
# {'吕布': {'语文': 60, '数学': 70, '英语': 80}, '关羽': {'语文': 70, '数学': 70, '英语': 60}}
print(d["吕布"]["数学"])
# 70
d = {"吕布":[60, 70, 80], "关羽":[70, 80, 90]}
print(d["吕布"][1])
# 70

# 字典推导式
d = {"F":70, "i":105, "s":115, "h":104, "C":67}
b = {v:k for k, v in d.items()}
print(b)
# {70: 'F', 105: 'i', 115: 's', 104: 'h', 67: 'C'}

d = {x:y for x in [1, 3, 5] for y in [2, 4,  6]}
print(d)
# {1: 6, 3: 6, 5: 6} 每循环一次，值替换一次

d = {"小甲鱼":"千年王八，万年龟。"}
e = d.copy()
d["小甲鱼"] = "666"
print(d, e)
# {'小甲鱼': '666'} {'小甲鱼': '千年王八，万年龟。'} 字符串不可变

d = {"小甲鱼":{"数学":99, "英语":88, "语文":101}}
e = d.copy()
d["小甲鱼"]["语文"] = 100
print(d, e)
# {'小甲鱼': {'数学': 99, '英语': 88, '语文': 100}} {'小甲鱼': {'数学': 99, '英语': 88, '语文': 100}}

d = {}
d[1] = "千年王八"
d[1.0] = "万年龟"
print(d)
# {1: '万年龟'}

```



## 摩斯密码

```python
# 摩斯密码

c_table = [".-", "-...", "-.-.", "-..", ".", "..-.",
           "--.", "....", "..", ".---", "-.-", ".-..",
           "--", "-.", "---", ".--.", "--.-", ".-.",
           "...", "-", "..-", "...-", ".--", "-..-",
           "-.--", "--.."]
d_table = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
code = input("请输入摩斯密码：")
split_code = code.split(" ")

result = [d_table[c_table.index(each)] for each in split_code]
print(result)
# 请输入摩斯密码：.. --
# ['I', 'M']

# 通过字典
c_table = {".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F",
           "--.":"G", "....":"H", "..":"I", ".---":"J", "-.-":"K", ".-..":"L",
           "--":"M", "-.":"N", "---":"O", ".--.":"P", "--.-":"Q", ".-.":"R",
           "...":"S", "-":"T", "..-":"U", "...-":"V", ".--":"W", "-..-":"X",
           "-.--":"Y", "--..":"Z"}
code = input("请输入摩斯密码：")
split_code = code.split(" ")

result = [c_table[each] for each in split_code]
print(result)
# 请输入摩斯密码：.. --
# ['I', 'M']

```



## ==存查电影数据与电话簿==

```python
# 存查电影数据
# 编写一个存储电影数据的小程序。
# 需要存放的数据如下：
# 电影名称
# 上映时间
# 导演（可能有多人）
# 主演（通常有多人）
# 电影评分
# 无间道
# 2003-09-05
# 刘伟强 / 麦兆辉
# 刘德华 / 梁朝伟 / 黄秋生 / 曾志伟 / 郑秀文
# 9.3

print("欢迎进入鱼C影评小程序")
print("1.数据录入")
print("2.查询数据")
print("3.退出程序")
movie = dict()

while True:
    start = input("请输入想要的功能(1/2/3)：")
    if start == "1":
        movie_name = input("请输入电影名称：")
        movie_date = input("请输入上映日期：")
        movie_director = input("请输入导演名字（多人请用 / 分隔）：")
        movie_actor = input("请输入演员名字（多人请用 / 分隔）：")
        movie_score = input("请输入电影评分：")
        movie[movie_name] = movie_date, movie_director, movie_actor, movie_score
    elif start == "2":
        movie_search = input("请输入电影名称：")
        if movie_search in movie:
            print("电影名称：", movie_search)
            print("上映时间：", movie[movie_search][0])
            print("导演名单：", movie[movie_search][1])
            print("演员名单：", movie[movie_search][2])
            print("当前评分：", movie[movie_search][3])
            break
        else:
            print("查无此片！")
    else:
        break

# 电话簿
print("欢迎进入鱼C电话簿")
phone_book = {}
while True:
    start = input("请输入命令（I：录入 / C：查询 / D：删除 / P：打印 / E：退出）：")
    if start == "I":
        print("-- 录入模式 --")
        while True:
            name = input("请输入姓名：")
            if name in phone_book:
                print("该姓名已录入，手机号码是：", phone_book[name])
                cont1= input("请问是否修改（Y/N）：")
                if cont1 == "Y":
                    phone_number = input("请输入新的电话号码：")
                    phone_book[name] = phone_number
                elif cont1 == "N":
                    break
            else:
                phone_number = input("请输入电话号码：")
                while not (phone_number.isdigit() and len(phone_number) == 10):
                    phone_number = input("输入不合法，请重新输入：")
                phone_book[name] = phone_number
            cont = input("是否继续录入（Y/N）：")
            if cont == "Y":
                continue
            else:
                break
    elif start == "C":
        print("-- 查询模式 --")
        while True:
            phone_search = input("请输入姓名：")
            if phone_search in phone_book:
                print(phone_search, ":", phone_book[phone_search])
            else:
                print("查询不到该联系人")
            cont2 = input("是否继续查询（Y/N）：")
            if cont2 == "Y":
                continue
            else:
                break
    elif start == "D":
        print("-- 删除模式 --")
        while True:
            phone_del = input("请输入姓名：")
            if phone_del in phone_book:
                del phone_book[phone_del]
            else:
                print("查询不到该联系人")
            cont3 = input("是否继续删除（Y/N）：")
            if cont3 == "Y":
                continue
            else:
                break
    elif start == "P":
        print("-- 打印模式 --")
        print(phone_book)
    else:
        break

```



## ==MD5单向加密==

```python
# MD5单向加密
# 请按照要求编写一个网站的注册模块
# 我们知道，通常一个网站的用户名都是唯一的，这就要求注册的时候，系统代码可以识别当前输入的用户名是否已经存在？
# 如果存在，则不允许注册！
# 那么现在请大家一起来动手，编写一个网站的注册模块。
# 要求：
# 用户名不允许重复
# 数据库需要保存用户名及密码
# 初始用户及密码（"小甲鱼":"I_love_FishC"，"不二如是":"FishC5201314"）

# ——————————————————————————————————
# 单向加密 MD5 通过密码无法逆向获得明文的加密手段
# hashlib.md5() 的参数是需要一个 b 字符串（即 bytes 类型的对象），这里可以使用 bytes("123", "utf-8") 的方式将 "123" 转换为 b"123"。
import hashlib
user_pwd1 = hashlib.md5(b"I_love_FishC")
user_pwd2 = hashlib.md5(b"FishC5201314")
user_pwd1_md5 = user_pwd1.hexdigest()
user_pwd2_md5 = user_pwd2.hexdigest()
user = {"小甲鱼":user_pwd1_md5, "不二如是":user_pwd2_md5}
user_name = input("请输入用户名：")
while user_name in user.keys():
    print("该用户名已被注册！")
    user_name = input("请重新输入用户名：")
else:
    user_pwd = input("请输入密码：")
    # encode("utf-8") 也能转换成 byte 类型
    user_pwd = hashlib.md5(user_pwd.encode("utf-8")).hexdigest()
user[user_name] = user_pwd
print("-----------------")
print("目前已注册的用户有：")
user1 = iter(user)
for i in range(len(user)):
    user_name1 = next(user1)
    print(user_name1, ":", user[user_name1])

```



# 12.集合

## ==集合==

```python
# 集合
# 不重复，无序，无法用下标访问 集合可以被看作是一个只有键没有值的字典
# 创建
x = {"FishC", "Python"}
print(x)
# {'Python', 'FishC'}
x = {i for i in "FishC"}
print(x)
# {'C', 'F', 'h', 's', 'i'}
x = set("FishC")
print(x)
# {'F', 's', 'i', 'C', 'h'}

print("C" in x)
# True

# x.isdisjoint(b) x和b是否没有交集
# x.issubset(b)  x是否是b的子集
# x.issuperset(b)  x是否是b的超集（A包含B，B是A的子集，A是B的超集）
print(x.isdisjoint(set("Python")))
# False
print(x.issubset("FishC.com.cn"))
# True
print(x.issuperset("Fish"))
# True

# x.union(b) 生成x和b的并集
# x.intersection(b) 生成x和b的交集
# x.difference(b) 生成x和b的差集（属于x但不属于b的部分）
# x.symmetric_difference(b) 生成x和b的对称差集（并集 - 交集）
print(x.union({"Fishc", 1, 2, 3}, "Fishc.com"))
# {'C', 1, 2, 3, 's', 'c', 'm', 'F', 'o', 'Fishc', '.', 'i', 'h'}
print(x.intersection("fishc"))
# {'s', 'i', 'h'}
print(x.difference("fishc"))
# {'F', 'C'}
print(x.symmetric_difference("fishc"))
# {'c', 'f', 'C', 'F'}

# x <= b x是否是b的子集    x < b x是否是b的真子集
# x >= b x是否是b的超集（A包含B，B是A的子集，A是B的超集）    x > b x是否是b的真超集
# x | b  生成 x和b 的并集
# x & b  生成 x和b 的交集
# x - b  生成 x和b 的差集（属于x但不属于b的部分）
# x ^ b  生成x和b的对称差集（并集 - 交集）
print(x <= set("FishC.com.cn"))
# True
print(x >= set("Fish"))
# True
print(x | {1, 2, 3} | set("Python"))
# {'C', 1, 2, 3, 'y', 'h', 'F', 'i', 's', 'o', 't', 'P', 'n'}
print(x & set("Fish"))
# {'i', 's', 'h', 'F'}
print(x & {"Fishc"})
# set()    {'F', 's', 'i', 'C', 'h'} 和 {"Fishc"} 交集为空集
print(x - set("Fish"))
# {'C'}
print(x ^ set("Fishc"))
# {'c', 'C'}

```



## ==可变集合的增删查改==

```python
# 可变集合的增删查改
# 可变与不可变集合
# 可变 set()
# 不可变 frozenset() 可哈希， 状态不会改变，线程安全
x = frozenset("FishC")
print(x)
# frozenset({'F', 'i', 'h', 'C', 's'})

# 仅适用于 可变集合 set 的方法
# 改 update中的，迭代获取其中的每一个字符
# s.update(*others)  (union_update) 将others更新到s中 无返回值  others:支持多个参数 other:仅支持一个参数
# s.intersection_update(*others) 将交集更新到s中
# s.difference_update(*others) 将差集更新到s中
# s.symmetric_difference_update(*others) 将对称差集更新到s中
s = set("FishC")
s.update([1, 1], "23")
print(s)
# {'F', 'h', 1, '2', 'C', '3', 'i', 's'}
s.intersection_update("FishC")
print(s)
# {'h', 'F', 's', 'C', 'i'}
s.difference_update("Php", "Python")
print(s)
# {'F', 'C', 'i', 's'}
s.symmetric_difference_update("Python")
print(s)
# {'C', 'o', 't', 'h', 'F', 'P', 'i', 'n', 's', 'y'}

# 增
# add(elem) add中的  将改元素直接添加到集合中
s.add("45")
print(s)
# {'F', 'y', 'i', 'P', 'o', 't', 'n', '45', 'C', 'h', 's'}

# 删
# remove(elem) 删除的元素不存在则抛出异常
# discard(elem) 删除的元素不存在静默处理
# pop() 随机删除并返回集合中的一个元素
s.remove("45")
print(s)
# {'s', 'o', 'y', 'P', 'h', 'i', 'n', 't', 'C', 'F'}
s.discard("F")
print(s)
# {'s', 'o', 'y', 'P', 'h', 'i', 'n', 't', 'C'}
s.pop()
print(s)
# {'o', 'y', 'P', 'h', 'i', 'n', 't', 'C'}

# 清空
# clear()
s.clear()
print(s)
# set()


# 字典的键和集合的元素：可哈希 哈希值在它的生命周期不变
# python中大部分不可变的对象都是可哈希的（字符串，元组，不可变的集合（frozenset）），可变的都是不可哈希的(列表， 字典，可变的集合（set）)
# 故字典的键和集合的元素可以是：字符串，元组，不可变的集合（frozenset）
# hash(object) 获取对象的哈希值
# 对一个整数求哈希值，这个值等于它本身
# 两个对象值相等，哈希值相同
print(hash(1))
# 1
print(hash(1.0))
# 1
print(hash(1.001))
# 2305843009213441
print(hash("FishC"))
# 3210646892617875685
print(hash((1, 2, 3)))
# 529344067295497451
# 嵌套的集合
x = frozenset((1, 2 ,3))
print(x)
# frozenset({1, 2, 3})
y = {x, 4, 5}
print(y)
# {frozenset({1, 2, 3}), 4, 5}

s1 = set([1, 1, 2, 3, 5])
s2 = frozenset([1, 1, 2, 3, 5])
print(s1 == s2)
# True

```



## 集合的哈希表效率提升

```python
import random
import timeit

haystack = [random.randint(1, 10000000) for i in range(10000000)]
needles = [random.randint(1, 1000) for i in range(1000)]

# 请在此处添加一行代码，使得查找过程的执行效率提高 10000 倍以上。
haystack = set(haystack)
# 集合有哈希表的支持，速度快，空间换时间

def find():
    found = 0
    for each in needles:
        if each in haystack:
            found += 1

    print(f"一共找到{found}个匹配。")

t = timeit.timeit("find()", setup="from __main__ import find", number=1)
print(f"查找过程一共消耗{t}秒。")

```





## 破解 MD5 哈希加密

```python
# 利用 dict() 来实现交集和并集  破解 MD5 哈希加密
# 生成一个随机数列表，一共有 100 个元素，每个元素取 1~100 的随机值，赋值给变量 x
# 生成另一个随机数列表，一共有 100 个元素，每个元素取 50~150 的随机值，赋值给变量 y
# 利用字典的 “键” 不会重复的特点，计算 x 和 y 的交集（就是两者共有的元素）
import random
# 生成一个随机数列表 x，一共有 100 个元素，每个元素取 1~100 的随机值
x = [random.randint(1, 101) for i in range(100)]
# 生成另一个随机数列表 y，一共有 100 个元素，每个元素取 50~150 的随机值
y = [random.randint(50, 151) for j in range(100)]

# 用字典来记录
dict_x = dict(zip(x, [i for i in range(100)]))
dict_y = dict(zip(y, [i for i in range(100)]))

# 计算交集
intersection = [key for key in dict_x.keys() if key in dict_y.keys()]

#计算并集
union = list(dict_x.keys()) + [key for key in dict_y.keys() if key not in dict_x.keys()]

print(x)
# [90, 20, 37, 71, 61, 1, 59, 55, 76, 82, 82, 22, 48, 41, 67, 4, 72, 61, 32, 49, 27, 88, 26, 67, 21, 100, 28, 5, 74, 25, 10, 14, 36, 81, 82, 25, 40, 1, 79, 2, 18, 45, 37, 95, 27, 58, 52, 29, 91, 13, 26, 64, 96, 70, 52, 48, 19, 70, 36, 69, 56, 8, 84, 9, 59, 93, 84, 83, 43, 48, 34, 51, 28, 85, 58, 63, 81, 41, 65, 44, 71, 88, 65, 40, 48, 100, 12, 67, 94, 29, 100, 81, 60, 56, 92, 74, 20, 52, 9, 82]
print(y)
# [55, 107, 110, 87, 77, 73, 104, 121, 76, 142, 93, 110, 72, 70, 86, 143, 72, 76, 81, 62, 82, 108, 141, 116, 103, 77, 103, 71, 135, 50, 142, 103, 95, 97, 107, 134, 108, 117, 143, 85, 97, 90, 120, 144, 105, 62, 73, 126, 141, 89, 51, 136, 56, 56, 93, 59, 122, 118, 65, 93, 61, 62, 129, 137, 105, 146, 104, 128, 57, 63, 89, 99, 120, 126, 58, 147, 52, 128, 142, 106, 91, 116, 146, 91, 66, 114, 73, 124, 84, 146, 64, 118, 115, 90, 69, 129, 121, 107, 82, 65]
print(intersection)
# [90, 71, 61, 59, 55, 76, 82, 72, 81, 95, 58, 52, 91, 64, 70, 69, 56, 84, 93, 51, 85, 63, 65]
print(union)
# [90, 20, 37, 71, 61, 1, 59, 55, 76, 82, 22, 48, 41, 67, 4, 72, 32, 49, 27, 88, 26, 21, 100, 28, 5, 74, 25, 10, 14, 36, 81, 40, 79, 2, 18, 45, 95, 58, 52, 29, 91, 13, 64, 96, 70, 19, 69, 56, 8, 84, 9, 93, 83, 43, 34, 51, 85, 63, 65, 44, 12, 94, 60, 92, 107, 110, 87, 77, 73, 104, 121, 142, 86, 143, 62, 108, 141, 116, 103, 135, 50, 97, 134, 117, 120, 144, 105, 126, 89, 136, 122, 118, 129, 137, 146, 128, 57, 99, 147, 106, 66, 114, 124, 115]

# 破解 MD5 哈希加密
# 生成 0~999999 所有整数组成密码的哈希值
# 将上面生成的哈希值保存为映射类型
# 通过查表的方式，计算下面 3 个哈希值对应的明文密码
hash1 = "021bbc7ee20b71134d53e20206bd6feb"
hash2 = "e10adc3949ba59abbe56e057f20f883e"
hash3 = "655d03ed12927aada3d5bd1f90f06eb7"

import hashlib

hash_list = {}
for i in range(1000000):
    hash_list[i] = hashlib.md5(str(i).encode("utf-8")).hexdigest()
    if hash1 == hash_list[i]:
        print(f"{hash1}: {i}")
    if hash2 == hash_list[i]:
        print(f"{hash2}: {i}")
    if hash3 == hash_list[i]:
        print(f"{hash3}: {i}")
# 021bbc7ee20b71134d53e20206bd6feb: 1024
# e10adc3949ba59abbe56e057f20f883e: 123456
# 655d03ed12927aada3d5bd1f90f06eb7: 960520

```



# 13.函数

## 函数的创建和调用

```python
# 函数
# 创建和调用
def myfunc():
    # pass 空语句，作为占位符使用，在规划功能时占位
    pass
myfunc()
def myfunc():
    for i in range(3):
        print("I Love FishC")
myfunc()
# I Love FishC
# I Love FishC
# I Love FishC

# 函数的参数
# 形式参数与实际参数    函数定义时用的是形式参数，函数调用时用的是实际参数
def myfunc(name, times):
    for i in range(times):
        print(f"I Love {name}.")
myfunc("Python", 3)
# I Love Python.
# I Love Python.
# I Love Python.

# 函数的返回值 return    执行return时结尾，不会再运行后面的语句
# BIF 指内置函数 build-in function
# 函数在执行完所有语句后会默认隐式地返回一个 none 值
def div(x, y):
    z = x // y
    return z
print(div(4, 2))
# 2
def div(x, y):
    return x // y
print(div(4, 2))
# 2
def div(x, y):
    if y == 0:
        return "除数不能为0！"
    else:
        return x // y
print(div(4, 2))
# 2
print(div(4, 0))
# 除数不能为0！

def div(x, y):
    if y == 0:
        return "除数不能为0！"
    return x // y
print(div(4, 2))
# 2
print(div(4, 0))
# 除数不能为0！
def myfunc():
    # pass 空语句，作为占位符使用，在规划功能时占位
    pass
print(myfunc())
# None

```



## 注册与登录模块

```python
# 注册与登录模块
# 请编写一个实现【注册】和【登陆】功能的代码，这次要求将不同的功能封装成独立的函数
# 编写 4 个函数分别用于获取用户指令（get_int()）、注册（register()）、登陆（login()）、MD5加密（encrypt()）
# 使用一个 Python 的字典作为数据库。
# 注册时需验证用户名是否已存在于数据库
# 登陆时需验证用户名和密码是否匹配
# 密码保存需使用 MD5 加密
import hashlib
print("欢迎来到鱼C论坛~")
user = dict()
def get_int():
    print("==========================")
    print("1.注册")
    print("2.登录")
    print("3.退出")
    _ = input("请输入指令：")
    return _

def register():
    print("==========================")
    user_name = input("请输入用户名（输入q退出注册）：")
    if user_name == "q":
        return user
    while user_name in user:
        user_name = input("用户名重复，请重新输入用户名（输入q退出注册）：")
        if user_name == "q":
            return user
    user_pwd = input("请输入密码：")
    user[user_name] = encrypt(user_pwd)
    print("恭喜，注册成功~")
    return user

def login():
    print("==========================")
    user_name = input("请输入用户名（输入q退出登录）：")
    if user_name == "q":
        return 0
    while user_name not in user:
        print("用户名不存在。")
        user_name = input("请重新输入用户名（输入q退出登录）：")
        if user_name == "q":
            return 0
    user_pwd = input("请输入密码：")
    if user_pwd == "q":
        return 0
    while encrypt(user_pwd) != user[user_name]:
        print("密码错误！")
        user_pwd = input("请重新输入密码：")
    print("恭喜，登录成功~")
    return 0

def encrypt(pwd):
    pwd = hashlib.md5(str(pwd).encode("utf-8")).hexdigest()
    return pwd

while True:
    select = get_int()
    if select == "1":
        register()
    elif select == "2":
        login()
    elif select == "3" :
        break
    else:
        print("指令错误，请重新输入！")

```



## ==函数的参数类型1==

```python
# 位置参数 在定义函数时将参数位置固定了下来，而这类参数称之为位置参数
def myfunc(s, vt , o):
    return "".join([o, vt, s])
print(myfunc("我", "打了", "小甲鱼"))
# 小甲鱼打了我

# 关键字参数 更适用鱼参数多的函数
print(myfunc(o="我", vt="打了", s="小甲鱼"))
# 我打了小甲鱼
# 混用，位置参数要在关键字参数之前
print(myfunc("小甲鱼", o="我", vt="打了"))
# 我打了小甲鱼

# 默认参数 函数在定义时指定默认的参数值    默认参数要放在最后
def myfunc(s, vt, o="小甲鱼"):
    return "".join((o, vt, s))
print(myfunc("香蕉","吃"))
# 小甲鱼吃香蕉
def myfunc(vt, s="苹果", o="小甲鱼"):
    return "".join((o, vt, s))
print(myfunc("吃"))
# 小甲鱼吃苹果

# /  斜杠左侧必须传入位置参数
# *  斜杠右侧必须传入关键字参数， 这就是一个匿名的收集参数
print(help(abs), help(sum))
# 如abs(x, /)    sun(iterable, /, start=0)
print(abs(-1.5))
# 1.5   abs(x=-1.5)则会报错
print(sum([1, 2, 3], 4))
# 10
print(sum([1, 2, 3], start=4))
# 10
def abc(a, /, b, c):
    print(a, b, c)
abc(1, b=2, c=3)
# 1 2 3
def abc(a, *, b, c):
    print(a, b, c)
abc(1, b=2, c=3)
# 1 2 3
abc(a=1, b=2, c=3)
# # 1 2 3

```



## ==回文字符串拼音版 与 模拟栈==

```python
# 回文字符串拼音版
# 提示一：放宽要求后，只要文字的发音构成前后回文，即认定为符合要求。
# 提示二：将汉字转换为对应拼音的方法 -> https://fishc.com.cn/thread-213439-1-1.html
# 提示三：请将各个独立的功能封装为函数。
from xpinyin import Pinyin
def input_text():
    text = input("请输入一段话：")
    while len(text) <= 1:
        text = input("字数太少，请重新输入：")
    return text

def changepy(text):
# 转换成拼音
    text1 = Pinyin().get_pinyin(text, ",")
    text1 = text1.split(",")
    return text1

def judge(text, text1):
    temp = []
    i = 0
    if len(text1) % 2 == 0:
        while i < len(text1) - 1:
            if i <= len(text1) // 2 - 1:
                temp.append(text1[i])
                i += 1
            else:
                if temp.pop() != text1[i]:
                    print(f"{text}不是回文")
                    break
                else:
                    i += 1
    else:
        while i < len(text1):
            if i == len(text1) // 2:
                i += 1
                continue
            elif i <= len(text1) // 2 - 1:
                temp.append(text1[i])
                i += 1
            else:
                if temp.pop() != text1[i]:
                    print(f"{text}不是回文")
                    break
                else:
                    i += 1
    if i >= len(text1):
        print(f"{text}是回文")

text = input_text()
text1 = changepy(text)
judge(text1, text1)
# 请输入一段话：前任只认钱
# ['qian', 'ren', 'zhi', 'ren', 'qian']是回文

# 利用函数模拟创建【栈】的数据结构操作
stack_like = []
def input_text1():
    while True:
        command = input("请输入指令（push/pop/top/exit）：")
        if command == "push":
            stack_push()
        elif command == "pop":
            stack_pop()
        elif command == "top":
            stack_top()
        elif command == "exit":
            break
        else:
            print("请输入正确的指令：")

def stack_push():
    num = input("请输入将要压入栈中的值：")
    stack_like.append(num)
    temp = [i for i in reversed(stack_like)]
    print("栈:")
    for j in range(len(stack_like)):
        print(temp[j])

def stack_pop():
    if len(stack_like) == 0:
        print("栈已空")
        return 0
    print(stack_like.pop())
    temp = [i for i in reversed(stack_like)]
    print("栈:")
    for j in range(len(stack_like)):
        print(temp[j])


def stack_top():
    if len(stack_like) == 0:
        print("栈已空")
        return 0
    temp = [i for i in reversed(stack_like)]
    print(temp[0])

input_text1()

```



## ==函数的参数类型2==

```python
# 收集参数
# 定义函数时不限制用户输入个数，
# 形参前加*， 通过*将多个参数打包为元组， **将多个参数打包为字典
# 定义时多个参数则置于函数最后位置，若不置于最后位置，则在收集参数后的参数只能是关键字参数（在使用时指定形参对应的实参）
# *  斜杠右侧必须传入关键字参数， 这就是一个匿名的收集参数
# 打包为元组
def myfunc(start, *args):
    print(f"有{len(args)}个无限制参数")
    print(f"第二个参数是{args[1]}")
myfunc(1, "tge", 35, [1, 3, "werf"])
# 有3个无限制参数
# 第二个参数是35

# python在返回多个值时利用元组进行打包
def myfunc(*args):
    print(args)
myfunc(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)  以元组形式打包返回
def myfunc():
    return 1, 2, 4
print(myfunc())
# (1, 2, 4)  以元组形式打包返回
# 可以进行元组解包
x, y, z = myfunc()
print(x, y, z)
# 1 2 4

# 打包为字典
def myfunc(**kwargs):
    print(kwargs)
myfunc(a=1, b=2, c=3)
# {'a': 1, 'b': 2, 'c': 3}
# 混合
def myfunc(a, *b, **c):
    print(a, b, c)
myfunc(1, 2, 3, x=1, y=2, z=3)
# 1 (2, 3) {'x': 1, 'y': 2, 'z': 3}

# 解包参数 实参前加* 或** 实现解包，以此给形参赋值
# * 解包成位置参数， **解包成关键字参数
args = (1, 2, 3, 4)
def myfunc(a, b, c ,d):
    print(a, b, c, d)
myfunc(*args)
# 1 2 3 4

kwargs = {"a": 1, "b": 2, "c": 3, "d": 4}
myfunc(**kwargs)
# 1 2 3 4

```



## ==罗马数字与数字的互转==

```python
# 罗马数字与数字的互转
# 罗马数字包含 I、V、X、L、C、D、M 七种字符，分别表示数值 1、5、10、50、100、500、1000。
# 编写一个函数，将指定的罗马字符转换为数字的形式。
# 增加检测非法字符的功能
# 简化版
# enumerate 枚举
# # 定义一个包含一些水果名称的列表
# fruits = ['apple', 'banana', 'cherry']
#
# # 使用 enumerate 函数遍历列表
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")
# 在这个例子中，enumerate(fruits) 返回一个枚举对象，其中包含了列表中每个元素的索引和值
R2N = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def rome_num2(rome):
    num = 0
    len2 = len(rome)
    for i, j in enumerate(rome):
        v = R2N[j]
        if i < len2 - 1 and  v < R2N[rome[i + 1]]:
            num -= v
        else:
            num += v
    return num
def input_rome2():
    rome = input("请输入一个罗马字符：")
    num = rome_num2(rome)
    print(f"转换后的结果是：{num}")
# input_rome2()

# 数字转罗马数字
N2R = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

def num2roman(num):
    r = []
    for v, s in N2R:
        while num >= v:
            num -= v
            r.append(s)
        if num == 0:
            break

    return "".join(r)

n = input("请输入一个整数：")
r = num2roman(int(n))
print(f"转换后的结果是：{r}")

```



## 函数作用域

```python
# 作用域
# 作用域指一个变量可以被访问的范围
# 局部作用域    函数内创建的变量
# 全局作用域    函数外创建的变量
# 当存在全局变量时，若在函数内创建同名局部变量，则在函数中创建一个同名的局部变量进行覆盖
# global x  在函数内使用，创建全局变量

# 嵌套函数 函数中创建一个内部函数
# 内部函数无法在外部被直接调用，需要在其对应的外部函数中调用
def funA():
    x = 520
    def funB():
        x = 880
        print(f"In funB, x={x}")
    funB()
    print(f"In funA, x={x}")

funA()
# In funB, x=880
# In funA, x=520

# nonlocal  可以在内部函数修改上一层外部函数的变量
def funA():
    x = 520
    def funB():
        nonlocal x
        x = 880
        print(f"In funB, x={x}")
    funB()
    print(f"In funA, x={x}")

funA()
# In funB, x=880
# In funA, x=880

# LEGB规则
# Local 局部作用域  Enclosed 嵌套函数的外层函数作用域  Global 全局作用域  Build-In 内置作用域
# 小则优先 范围小



x = [1, 2, 3]
def invert(x):
    x = x[::-1]
invert(x)
print(x)
# [1, 2, 3]

x = [1, 2, 3]
def invert(x):
    x[:] = x[::-1]
invert(x)
print(x)
# [3, 2, 1]


x = 100
def funA():
    global x
    x = 250
    def funB():
        # nonlocal x  此时funA的 x 为全局变量， 无局部变量 x 此时 nonlocal会报错
        x = 520
    funB()

funA()
print(x)
# 250

```



## ==洗牌算法 —— Fisher-Yates 与斗地主==

```python
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

```



## 闭包

```python
# 闭包  如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包
# 闭包的核心特征是内部函数能够访问外部函数的变量，即使外部函数已经执行完毕

# 闭包是由函数及其相关的引用环境组合而成的实体(即：闭包=函数+引用环境)
# (想想Erlang的外层函数传入一个参数a, 内层函数依旧传入一个参数b, 内层函数使用a和b, 最后返回内层函数)
# x()() 通过x调用下一层内部函数
# 每次调用外部函数后都将生成并保存一个新的局部变量。其实这里外部函数返回的就是闭包

# 1、当闭包执行完后，仍然能够保持住当前的运行环境
# 2、闭包可以根据外部作用域的局部变量来得到不同的结果
def funA():
    x = 888
    def funB():
        print(x)
    return funB
print(funA())
# <function funA.<locals>.funB at 0x000001CEAD9B8540>    得到funB的引用
funA()()
# 888

# 不直接通过funA调用funB
funny = funA()
funny()
# 888

# 嵌套函数的外层函数作用域  赋值给变量时  能保留
# 嵌套函数调用，  类似二维数组
def power(exp):
    def exp_of(base):
        return base ** exp
    return exp_of
square = power(2)
cube = power(3)
print(square(5))
# 25
print(cube(5))
# 125
print(power(2)(3))
# 9

def outer():
    x = 0
    y = 0
    def inner(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f"现在，x = {x}, y = {y}")
    return inner
move = outer()
move(1, 2)
# 现在，x = 1, y = 2
move(-2, 2)
# 现在，x = -1, y = 4

# 当闭包执行完后，仍然能够保持住当前的运行环境
# 移动小游戏
origin = (0, 0)
legal_x = [-100, 100]
legal_y = [-100, 100]

def create(pos_x=0, pos_y=0):
    def moving(direction, step):
        nonlocal pos_x, pos_y
        new_x = pos_x + direction[0] * step
        new_y = pos_y + direction[1] * step

        if new_x < legal_x[0]:
            pos_x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            pos_x = legal_x[1] - (new_x - legal_x[1])
        else:
            pos_x = new_x

        if new_y < legal_y[0]:
            pos_y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > origin[1]:
            pos_y = legal_y[1] - (new_y - legal_y[1])
        else:
            pos_y = new_y
        return pos_x, pos_y
    return moving

move = create()
print("向右移动20步后，位置是：", move([1, 0], 20))
# 向右移动20步后，位置是： (20, 0)
print("向上移动120步后，位置是：", move([0, 1], 120))
# 向上移动120步后，位置是： (20, 80)
print("向右下角移动88步后，位置是：", move([1, -1], 88))
# 向右下角移动88步后，位置是： (92, -8)



# ----------------------------------------------------
def addx(x):
    def adder(y): return x + y
    return adder
c =  addx(8)
print(type(c))
# <type 'function'>
print(c.__name__)
# adder
print(c(10))
# 18
# ----------------------------------------------------

flist = []
for i in range(3):
    def foo(x): print(x + i)
    flist.append(foo)
for f in flist:
    f(2)
# 4
# 4
# 4
# 先执行完第一个for循环，列表中添加的都是foo(x): print(x + i),此时i = 2 ，执行第二个for循环，结果均为4

flist = []
for i in range(3):
    def foo(x, y = i): print(x + y)
    flist.append(foo)
for f in flist:
    f(2)
# 2
# 3
# 4
# 先执行完第一个for循环，列表中添加的为foo(x): print(x + 0/1/2),，执行第二个for循环，结果为2/3/4


def outter():
    def innerA():
        x = 100

    def innerB():
        nonlocal x
        x = 250

    def innerC():
        global x
        x = 520

    x = 880

    innerA()
    print(f"调用完 innerA() 函数之后，x = {x}")

    innerB()
    print(f"调用完 innerB() 函数之后，x = {x}")

    innerC()
    print(f"调用完 innerC() 函数之后，x = {x}")
outter()
print(f"此时此刻，全局变量 x = {x}")
# 调用完 innerA() 函数之后，x = 880
# 调用完 innerB() 函数之后，x = 250
# 调用完 innerC() 函数之后，x = 250
# 此时此刻，全局变量 x = 520

```



## ==闭包嵌套求平均值 与 返回斐波那契数列==

```python
# 闭包嵌套求平均值 与 返回斐波那契数列
def make_avg():
    x = 0
    i = 0
    def inner(y):
        nonlocal x, i
        x += y
        i += 1
        return x / i
    return inner
avg = make_avg()
print(avg(5))
# 5.0
print(avg(3))
# 4.0
print(avg(7))
# 5.0
print(avg(19))
# 8.5

# 闭包嵌套返回一个斐波那契数列
def fib():
    a, b = 0, 1
    def inner():
        nonlocal a, b
        a, b = b, a + b
        return b - a
    return inner
f = fib()
print(f(), f(), f(), f(), f(), f(), f(), f(), f())
# 0 1 1 2 3 4 5 8 13 21
```



## 装饰器

```python
# 装饰器
# 一种设计模式    在目标函数前添加@函数  将目标函数作为实际参数传入到装饰器函数中
# 函数可以添加多个装饰器
# 运行程序一般都是从上到下，添加装饰器后运行到装饰器函数时，添加装饰器函数，然后定位到装饰器，将目标函数传入装饰器函数，再返回装饰器函数，正常往下进行

# ()相当于在调用函数
def myfunc():
    print("正在调用myfunc------")
def report(func):
    print("开始调用函数")
    func()
    print("调用函数结束")
report(myfunc)
# 开始调用函数
# 正在调用myfunc------
# 调用函数结束

import time
def time_master(func):
    print("开始运行程序")
    start = time.time()
    func()
    print("结束运行程序")
    end = time.time()
    print(f"一共耗费了{(end - start):.5f}秒")
def myfunc():
    time.sleep(2)
    print("Hello, FishC")
time_master(myfunc)
# 开始运行程序
# Hello, FishC
# 结束运行程序
# 一共耗费了2.00034秒

def time_master(func):
    print("开始运行程序")
    start = time.time()
    func()
    print("结束运行程序")
    end = time.time()
    print(f"一共耗费了{(end - start):.5f}秒")

def myfunc():
    time.sleep(2)
    print("Hello, FishC")
time_master(myfunc)
# 开始运行程序
# Hello, FishC
# 结束运行程序
# 一共耗费了2.00036秒

def time_master(func):
    def call_func():
        print("开始运行程序")
        start = time.time()
        func()
        print("结束运行程序")
        end = time.time()
        print(f"一共耗费了{(end - start):.5f}秒")
    return call_func

# 装饰器 将函数作为实际参数传入到装饰器函数中
# 相当于myfunc = time_master(myfunc)  此时返回call_func  后面再myfunc()来屌用
@time_master
def myfunc():
    time.sleep(2)
    print("Hello, FishC")
myfunc()
# 开始运行程序
# Hello, FishC
# 结束运行程序
# 一共耗费了2.00040秒

# 函数可以添加多个装饰器
def add(func):
    def inner():
        x = func()
        return x + 1
    return inner
def cube(func):
    def inner():
        x = func()
        return x * x * x
    return inner
def square(func):
    def inner():
        x = func()
        return x * x
    return inner
@add
@cube
@square
def test():
    return 2
print(test())
# 65   add(cube(square(test)))

# 给装饰器传递参数
def logger(msg):
    def time_master(func):
        def call_func():
            print("开始运行程序")
            start = time.time()
            func()
            print("结束运行程序")
            end = time.time()
            print(f"{msg}一共耗费了{(end - start):.5f}秒")
        return call_func
    return time_master
# 相当于funA() = logger(msg="A")(func)
@logger(msg="A")
def funA():
    time.sleep(1)
    print("正在调用函数A")
@logger(msg="B")
def funB():
    time.sleep(1)
    print("正在调用函数B")
funA()
# 开始运行程序
# 正在调用函数A
# 结束运行程序
# A一共耗费了1.00018秒
funB()
# 开始运行程序
# 正在调用函数B
# 结束运行程序
# B一共耗费了1.00064秒

# 目标函数需要参数时
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("在原函数之前执行")
        func(*args, **kwargs)
        print("在原函数之后执行")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# 在原函数之前执行
# Hello, Alice!
# 在原函数之后执行

```



## 装饰器函数的创建与参数

```python
# 装饰器函数的创建与参数
import time

# 添加装饰器函数
def delay(func):
    def sleep_func():
        time.sleep(1)
        func()
    return sleep_func

def fib():
    back1, back2 = 0, 1
    # 添加装饰器
    @delay
    def func():
        nonlocal back1, back2
        back1, back2 = back2, back1 + back2
        print(back1, end=' ')

    return func

def get_fib(n):
    f = fib()
    for i in range(n):
        f()

n = int(input("请输入需要获取的斐波那契数："))
get_fib(n)
print()
# 题目要求：
# 请在此处补充装饰器 type_check() 的代码
def type_check(correct_type):
    def type_func(func):
        def inner(*args):
            if type(*args) == correct_type:
                return func(*args)
            else:
                return "参数类型错误！"
        return inner
    return type_func


print("<<<--- 测试整数 --->>>")

@type_check(int)
def double(x):
    return x * 2

print(double(2))      # 这里打印结果应该是 4
print(double("2"))    # 这里打印结果应该是 “参数类型错误”


print("\n<<<--- 测试字符串 --->>>")

@type_check(str)
def upper(s):
    return s.upper()

print(upper('I love FishC.'))   # 这里打印结果应该是 I LOVE FISHC
print(upper(250))               # 这里打印结果应该是 “参数类型错误”

```




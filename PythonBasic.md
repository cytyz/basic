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



### 抛硬币实验

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



### 偶数和

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



### 国王棋盘麦子

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



### 阶梯步数

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



### 角谷猜想

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



### 抛硬币进阶版

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



### 九九乘法表

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



### ==水仙花数==

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



==回文数==

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



### 两数之和

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



### ==合法字符串==

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



### 主要元素

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



### ==二维列表两个小练习==

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



### ==杨辉三角形==

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



==顺时针输出==

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



### 创建元组、列表时间

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



### ==整理字符串与ASCII转换==

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



### 版本号比较与加密（规则替换）

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



### 字符串判断Demo

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



### ==位移加密与同行字符串==

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



### 格式化练习

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



### 压缩与解压

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



### ==判断子序列与 查找最大奇数==

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



### 奇偶排序 翻转单词顺序

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



### 密室打卡（打点计时器 zip)

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



### 摩斯密码

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



==存查电影数据与电话簿==

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



### ==MD5单向加密==

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



### ==可变集合的增删查改==

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



### 集合的哈希表效率提升

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





### 破解 MD5 哈希加密

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



### 注册与登录模块

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



### ==回文字符串拼音版 与 模拟栈==

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



### ==罗马数字与数字的互转==

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



### ==洗牌算法 —— Fisher-Yates 与斗地主==

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



### ==闭包嵌套求平均值 与 返回斐波那契数列==

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



### ==装饰器函数的创建与参数==

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



## ==lambda表达式==

```python
# lambda 表达式（匿名函数）
# lambda arg1, arg2, ... argN : expression
# 可以存在于函数无法存在的地方，如列表，但不建议这么写
def squarex(x):
    return x * x

print(squarex(3))
# 9

squareY = lambda y : y * y
print(squareY(3))
# 9

# 可以存在于 整个函数的定义过程  无法存在的地方，如列表
y = [lambda x : x * x, 2, 3]
print(y[0](y[1]))
# 4

mapped = map(lambda x : ord(x) + 10, "FishC")
print(list(mapped))
# [80, 115, 125, 114, 77]

def boring(x):
    return ord(x) + 10
print(list(map(boring, "FishC")))
# [80, 115, 125, 114, 77]

print(list(filter(lambda x : x % 2, range(10))))
# [1, 3, 5, 7, 9]


# ——————————————————————————————————————————————————————
# 闭包转换成 lambda 表达式
def power(exp):
    def exp_of(base):
        return base ** exp
    return exp_of
square = power(2)
square(2)
# 4
# 转换成lambda表达式
f = lambda exp : lambda base : base ** exp
square = f(2)
square(2)
# 4

# 装饰器转换成 lambda 表达式
def add(func):
    def inner():
        x = func()
        return x + 1
    return inner
@add
def test():
    return 2
print(test())
# 3
# 转换成lambda表达式
@lambda func : lambda : func() + 1
def test1():
    return 2
print(test1())
# 3
# ———————————————————————————————————————————————————————

```



### ==lambda 表达式练习==

```python
# lambda 表达式练习
power = {"吕布": 999, "关羽": 888, "刘备": 666, "张飞": 900, "赵云": 789, "不二如是": 999}

# 请 lambda 表达式和 filter() 函数配合，替换下面的代码
# greater = []
# for k, v in power.items():
#     if v > 800:
#         greater.append((k, v))
# 请 lambda 表达式和 filter() 函数配合，替换下面的代码
# ———————————————————————————————————————————————————————————————————————————————————
greater = list(filter(lambda x : x[1] > 800, power.items()))
# ———————————————————————————————————————————————————————————————————————————————————

print(greater)
# [('吕布', 999), ('关羽', 888), ('张飞', 900), ('不二如是', 999)]


# 字典获取值
# dict.get(key, default=None)
# 返回指定键的值，如果键不在字典中返回 default 设置的默认值
members = {
    "鱼C工作室" : {"小甲鱼":83, "不二如是":89, "二师兄":64, "小师妹":75, "鱼小二":96},
    "复仇者联盟" : {"钢铁侠":85, "绿巨人":39, "黑寡妇":82, "鹰眼":73, "雷神":99},
    "奥特曼家族" : {"迪迦":99, "艾斯":84, "泰罗":63, "佐菲":78, "赛文":78}}

# 请在此处添加一行代码，完成题目要求，并将结果保存在变量 x 中
# ———————————————————————————————————————————————————————————————————————————————————
x = [':'.join((i, min(members[i].items(), key = lambda x:x[1])[0])) for i in members]
# ———————————————————————————————————————————————————————————————————————————————————
# for i in members:
#     i, min(members[i].items(), key = lambda x:x[1])[0]

print(x)
# ['鱼C工作室:二师兄', '复仇者联盟:绿巨人', '奥特曼家族:泰罗']

```



## 生成器

```python
# 生成器
# yield 代替return， 拥有yield的函数被成为生成器，它是一种特殊的迭代器，支持next函数
# 生成器对象无法使用下标索引
# 每次调用yield 只会提供一个数据，并记住当时的状态
def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1
        print("yes")
print(counter())
# <generator object counter at 0x000002F571FA5A80>
for i in counter():
    print(i)
# 0
# yes
# 1
# yes
# 2
# yes
# 3
# yes
# 4
# yes
# 5
# yes

print("________________________________-")
c = counter()
print(next(c))
print("____")
print(next(c))
print("____")
print(next(c))
# 0
# ____
# yes
# 1
# ____
# yes
# 2


# 斐波那契数列
def fib():
    back1, back2 = 0, 1
    while True:
        yield back1
        back1, back2 = back2, back1 + back2
f = fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
# 0
# 1
# 1
# 2
# 3

# 生成器表达式（元组推导式）  与列表不同的是列表推导式会一次性生成出来，生成器表达式需要一次次调用
print((i ** 2 for i in range(10)))
# <generator object <genexpr> at 0x0000015BB9DFAB50>
t = ((i ** 2) for i in range(10))
print(next(t))
print(next(t))
print(next(t))
# 0
# 1
# 4

# 生成器会记住当时的状态，所以后面会接着上次的生成
for i in t:
    print(i)
# 9
# 16
# 25
# 36
# 49
# 64
# 81

print(list(map(abs, (-1, 2, -3, 4, -5))))
# [1, 2, 3, 4, 5]
# 转换成生成器表达式
print(list((abs(x) for x in (-1, 2, -3, 4, -5))))
# [1, 2, 3, 4, 5]

```



### ==利用生成器定义一个支持浮点数的 frange() 函数==

```python
# 利用生成器定义一个支持浮点数的 frange() 函数，其功能与 range() 函数相仿。
# round(number, ndigits=None)    ndigits 指定精度
# round() 函数用于返回一个指定精度（四舍五入）的结果。
def frange(start, stop=None, step=0.1):
    s = str(step)
    len1 = len(s) - 2
    start += 0.0
    if stop is None:
        stop = start + 0.0
        start = 0.0
    while start < stop:
        yield round(start, len1)
        start += step

for i in frange(1):
    print(i)

for i in frange(1, 2):
    print(i)

for i in frange(5, 10, 0.5):
    print(i)

```



## 递归

```python
# 递归
# 函数调用自身， 必须有一个结束条件
def func(i):
    if i > 0:
        print("qwer")
        i -= 1
        func(i)
func(4)
# qwer
# qwer
# qwer
# qwer

# ————————————————————————————————————————————
# 例子：阶乘
def factIter(n):
    value = 1
    for i in range(1, n + 1):
        value *= i
    return value
print(factIter(4))
# 24

def factRecur(n):
    if n == 1:
        return 1
    return factRecur(n - 1) * n
print(factRecur(4))
# 24

# ————————————————————————————————————————————
# 例子：斐波那契数列
def fibIter(n):
    a = 1
    b = 1
    c = 1
    while n > 2:
        c = a + b
        a, b = b, c
        n = n - 1
    return c
print(fibIter(12))
# 144

def fibRecur(n):
    if n == 1 or n == 2:
        return 1
    return fibRecur(n - 1) + fibRecur(n - 2)
print(fibRecur(12))
# 144
# 时间优化
def fibRecur_new(n, a, b):
    if n == 1 or n == 2:
        return b
    return fibRecur_new(n - 1, b, a + b)
print(fibRecur_new(12, 1, 1))
# 144
import timeit
# 这个耗时会比较久（因为默认是重复测试 5 次），请大家耐心等待
FR = timeit.timeit("fibRecur(12)", setup="from __main__ import fibRecur")
print(f"普通递归耗时：{FR:.2f}秒。")
# 普通递归耗时：10.17秒。
TFR = timeit.timeit("fibRecur_new(12, 1, 1)", setup="from __main__ import fibRecur_new")
print(f"优化递归耗时：{TFR:.2f}秒。")
# 优化递归耗时：0.46秒。
FI = timeit.timeit("fibIter(12)", setup="from __main__ import fibIter")
print(f"普通迭代耗时：{FI:.2f}秒。")
# 普通迭代耗时：0.30秒。

# ————————————————————————————————————————————
# 例子：汉诺塔
# 一次只能移动一个圆盘，小的圆盘只能在大的圆盘上面
def hanoi(n):
    if n == 1:
        return 1
    return hanoi(n - 1) * 2 + hanoi(1)
print(hanoi(5))
# 31
def hanoi_fact(n, x, y, z):
    if n == 1:
        print(x, "-->", z)
    else:
        hanoi_fact(n - 1, x, z, y)
#         将x的 n - 1 个圆盘移动到y
        print(x, "-->", z)
        hanoi_fact(n - 1, y, x, z)
#         将y的 n - 1 个圆盘移动到z
hanoi_fact(5,"A","B","C")
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
# A --> B
# C --> B
# C --> A
# B --> A
# C --> B
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
# B --> A
# C --> B
# C --> A
# B --> A
# B --> C
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C

```



### 递归函数练习

```python
# 递归函数练习
# 计算从 1 + 2 + 3 + ... + n 的结果
def get_sum(n):
    if n == 1:
        return 1
    return n + get_sum(n - 1)


# 判断该整数是否为 2 的幂次方。如果是返回 True，否则返回 False
def isPowerOfTwo(n):
    if n == 0:
        return False
    elif str(n).isdigit():
        if n == 1:
            return True
        elif n % 2 != 0:
            return False
        else:
            return isPowerOfTwo(n // 2)
    else:
        return False


# 只使用加号运算符（+）来实现乘法运算的结果
def mul(x,y):
    if y == 0 or x == 0:
        return 0
    if y == 1:
        return x
    if x == 1:
        return y
    if x < y:
        return mul(x-1, y) + y
    else:
        return mul(x, y-1) + x


# 找到列表中最大的元素
def get_max(L):
    max = L[0]
    if not L:
        return None
    if len(L) == 1:
        return max
    if L[1] > max:
        return get_max(L[1:])
    else:
        L.pop(1)
        return get_max(L)
# 小甲鱼版
def get_max(L):
    if len(L) == 2:
        return L[0] if L[0] > L[1] else L[1]
    else:
        sub = get_max(L[1:])
        return L[0] if L[0] > sub else sub

# 假设僧侣每秒钟都能正确地移动一枚金片，请问将 64 枚金片从一根银针移动到另外一根银针上，大概需要使用多少时间？
def hanoi(n):
    if n == 1:
        return 1
    return hanoi(n - 1) * 2 + hanoi(1)

```



## ==函数文档、类型注释、内省==

```python
# 函数文档、类型注释、内省
# help 查看函数文档
help(print)
# Help on built-in function print in module builtins:
#
# print(*args, sep=' ', end='\n', file=None, flush=False)
#     Prints the values to a stream, or to sys.stdout by default.
#
#     sep
#       string inserted between values, default a space.
#     end
#       string appended after the last value, default a newline.
#     file
#       a file-like object (stream); defaults to the current sys.stdout.
#     flush
#       whether to forcibly flush the stream.

def exchange(dollar, rate=7.18):
    """
    功能：汇率转换，美元 -> 人名币
    参数：
    - dollar 美元数量
    - rate 汇率，默认值是7.18(2025-05-29
    返回值：
    - 人民币的数量
    """
    return dollar * rate
help(exchange)
# Help on function exchange in module __main__:
#
# exchange(dollar, rate=7.18)
#     功能：汇率转换，美元 -> 人名币
#     参数：
#     - dollar 美元数量
#     - rate 汇率，默认值是7.18(2025-05-29
#     返回值：
#     - 人民币的数量

# ————————————————————————————————————————————————————————————
# 类型注释
# 告知希望传入参数类型及返回值
def times(s:str, n:int) ->str:
    return s * n
print(times(5,5))
# 25

def times(s:str = "FishC", n:int = 3) ->str:
    return s * n
print(times())
# FishCFishCFishC

# 希望是列表
def times(s:list, n:int = 3) ->list:
    return s * n
print(times([1, 2, 3]))
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 希望是整数列表
def times(s:list[int], n:int = 3) ->list:
    return s * n

# 希望是字典
def times(s:dict[str,int], n:int = 3) ->list:
    return list(s.keys()) * n


# 内省
print(times.__name__)
# times
# annotations 注释
print(times.__annotations__)
# {'s': dict[str, int], 'n': <class 'int'>, 'return': <class 'list'>}
# 查看函数文档
print(exchange.__doc__)
# 功能：汇率转换，美元 -> 人名币
# 参数：
# - dollar 美元数量
# - rate 汇率，默认值是7.18(2025-05-29
# 返回值：
# - 人民币的数量

```



### 斗地主打牌版

```python
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

```



## ==高阶函数==

```python
# 高阶函数
# 一个调用其他函数作为参数时，这个函数被称为高阶函数
# functools 包括许多高阶函数的模块
# reduce, 将可迭代的元素依次放入函数中, 依次进行，前一次计算的结果会作为前一次的参数传入
import functools
def add(x, y):
    return x + y
print(functools.reduce(add, [1, 2, 3, 4, 5]))    # 15
print(add(add(add(add(1,2),3),4),5))    # 15

# 阶乘
print(functools.reduce(lambda x, y: x*y, range(1, 11)))    # 3628800


# 偏函数
# partial 对指定的函数进行二次包装，将所需参数预先绑定一部分，剩下的才是需要输入的
square = functools.partial(pow, 2)
print(square(3))    # 9
cube = functools.partial(pow, 3)
print(cube(3))    # 27


# @wraps装饰器
# 可以使得被装饰函数在查询 __name__ 时查到自己的函数名
import time
def time_master(func):
    def call_func():
        print("开始运行程序")
        start = time.time()
        func()
        print("结束运行程序")
        end = time.time()
        print(f"一共耗费了{(end - start):.5f}秒")
    return call_func

@time_master
def myfunc():
    time.sleep(2)
    print("Hello, FishC")
# myfunc()
print(myfunc.__name__)
# call_func

def time_master(func):
    @functools.wraps(func)
    def call_func():
        print("开始运行程序")
        start = time.time()
        func()
        print("结束运行程序")
        end = time.time()
        print(f"一共耗费了{(end - start):.5f}秒")
    return call_func

@time_master
def myfunc():
    time.sleep(2)
    print("Hello, FishC")
# myfunc()
print(myfunc.__name__)
# myfunc

```



### ==斗地主打牌进阶版==

```python
# 斗地主打牌进阶版
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
    # 用集合判断是否都是同一个数字
    if len(cards) == 2 and len(set(cards)) == 1:
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
    if len(cards) == 3 and len(set(cards)) == 1:
        return True
    else:
        return False

# 炸弹
def is_four(cards):
    if len(cards) == 4 and len(set(cards)) == 1:
        return True
    else:
        return False

# 三带一
def is_three_one(cards):
    if len(cards) == 4:
        for each in cards:
            # 检查给定的牌列表中是否存在一张牌出现了三次
            if cards.count(each) == 3:
                return True
    return False

# 三带二
def is_three_two(cards):
    if len(cards) == 5:
        for each in cards:
            # 检查给定的牌列表中是否存在一张牌出现了三次
            if cards.count(each) == 3 and len(set(cards)) == 2:
                return True
    return False

# 四带二
def is_four_two(cards):
    if len(cards) == 6:
        for each in cards:
            # 检查给定的牌列表中是否存在一张牌出现了四次
            if cards.count(each) == 4 and len(set(cards)) == 2:
                return True
    return False

# 单顺
def is_continue(cards):
    if 2 in cards or 14 in cards or 15 in cards:
        return False
    # 排序
    cards.sort()
    # 判断是否是顺子
    for i in range(len(cards) - 1):
        if cards[i] + 1 != cards[i + 1]:
            return False
    return True

# 双顺
def is_con_pair(cards):
    if len(cards) % 2 != 0:
        return False
    if 2 in cards or 14 in cards or 15 in cards or len(set(cards)) != len(cards) // 2:
        return False
    cards.sort()
    # 判断是否两两成对
    for i in range(0, len(cards) - 1, 2):
        if cards[i] != cards[i + 1]:
            return False
    # 最后判断是否为顺子
    return is_con_pair(cards[::2])

# 三顺
def is_con_three(cards):
    if len(cards) % 3 != 0:
        return False
    if 2 in cards or 14 in cards or 15 in cards or len(set(cards)) != len(cards) // 2:
        return False
    cards.sort()
    for i in range(0, len(cards) - 2, 3):
        if cards[i] != cards[i + 1] or cards[i] != cards[i + 2] or cards[i + 1] != cards[i + 2]:
            return False
    # 最后判断是否为顺子
    return is_con_pair(cards[::3])

# 飞机带翅膀
def is_airplane_wing(cards):
    t1 = []
    t2 = []
    for each in cards:
        if cards.count(each) == 3:
            t1.append(each)
        else:
            t2.append(each)
    if is_con_three(t1) and len(set(t1)) == len(set(t2)):
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

def check_cards(cards):
    if len(cards) == 2:
        if is_pair(cards):
            print("符合规则：对牌")
        elif is_rocket(cards):
            print("符合规则：火箭")
        else:
            print("不符合规则!")

    elif len(cards) == 3:
        if is_three(cards):
            print("符合规则：三张牌相同")
        else:
            print("不符合规则!")

    elif len(cards) == 4:
        if is_four(cards):
            print("符合规则：炸弹")
        elif is_three_one(cards):
            print("符合规则：三带一")
        else:
            print("不符合规则!")

    elif len(cards) >= 5:
        if is_continue(cards):
            print("符合规则：顺子")
        else:
            if len(cards) == 5:
                if is_three_two(cards):
                    print("符合规则：三带二")
                else:
                    print("不符合规则!")

            if len(cards) == 6:
                if is_four_two(cards):
                    print("符合规则：四带二")
                elif is_con_pair(cards):
                    print("符合规则：双顺")
                elif is_con_three(cards):
                    print("符合规则：三顺")
                else:
                    print("不符合规则!")
                    
            if len(cards) == 8:
                if is_airplane_wing(cards):
                    print("符合规则：飞机带翅膀")
                elif is_con_pair(cards):
                    print("符合规则：双顺")
                elif is_con_three(cards):
                    print("符合规则：三顺")
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

```



# 14.文件

## 打开文件

```python
# 文件永久存储
# 临时：内存，永久：硬盘
# open()    打开一个文件并返回其对应的文件对象
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# r 读取；w 打开文件，若存在则覆盖；a 追加；+ 更新文件（读取和写入）
# b 二进制；t 文本模式；x 如果文件已存在则创建失败
# write(text)    将字符串写入并返回字符个数
# writelines(lines)    可以将多个字符串写入，不会自动换行，无返回值
# EOF    End Of the File，表示文件末尾的位置
f = open("FishC.txt", "w")
print(f.write("Hello, FishC"))
f.writelines(["Hello, FishC\n", "I love FishC"])
f.close()    # 关闭并写入， flush 刷新并写入

f = open("FishC.txt", "r+")
print(f.readable())    #True
print(f.writable())    #True

for each in f:
    print(each)
# Hello, FishCHello, FishC
#
# I love FishC
print(f.read())    # 文件读取会继续读取后面的内容，但此时文件已经读取完毕，故读取内容为空
# tell()    查询现在读取到了第几个字符
# seek()    修改文件指针，0 文件起始位置；1 当前位置；2 文件末尾
print(f.tell())    # 38
f.seek(0)
# readline()    每次读取一行
print(f.readline())    # Hello, FishCHello, FishC
print(f.read())    # I love FishC

f.write("I love my wife")
f.flush()

# truncate 将文件对象截取到指定位置
f.truncate(29)
f.close()

```



### 文件截取练习

```python
# 对FishC.txt，截取其中第 10~15 个字符，并保存为新文件（FishD.txt）
f1 = open("FishC.txt", "r")
f2 = open("FishD.txt", "w")

f1.seek(10)
f2.write(f1.read(5))

f1.close()
f2.close()

# 对FishC.txt，截取前面 15 个字符，并保存覆盖保存原文件。
f = open("FishC.txt", "r+")
f.truncate(15)
f.close()

# 打开自己的源文件，然后打印出来
f3 = open("errorDemo_01.py", "r", encoding="utf-8")
for line in f3:
    print(line, end="")
f3.close()

# 图片隐写术   在图片中隐藏文件
# 将压缩文件的内容，追加写入到图片文件的尾部，更改后缀名为zip或rar即可查看压缩文件(二进制)
f4 = open("test.jpg", "ab")
f5 = open("target.zip", "rb")

f4.write(f5.read())

f4.close()
f5.close()

print("finished")

```



## 路径处理

```python
# 路径处理
# pathlib 模块
# Path.cwd() 获取当前目录的路径
# Path() 打开指定路径
# a / b 拼接路径
# __file__ 当前脚本的绝对路径
from os import rename
from pathlib import Path

print(Path.cwd())   # D:\Program_Repository\github\basic\file
p = Path(r"D:\Program_Repository\github\basic\file\test")
print(p)    # D:\Program_Repository\github\basic\file\test
q = p / "FishC.txt"
print(q)    # D:\Program_Repository\github\basic\file\test\FishC.txt


# is_dir() 路径是否为文件夹    is_file() 路径是否为文件
# exists() 路径是否存在
# name 获取路径的最后一个部分
# stem 获取文件名    suffix 获取文件后缀
# parent 获取其父级目录
# parents 获取逻辑祖先路径构成的序列
# parts 将路径拆分成元组
# stat() 查看当前状态
print(p.is_dir(), p.is_file())    # True False
print(p.exists())    # True
print(p.name)    # file
print(q.stem, q.suffix)    # FishC .txt
print(p.parent)    # D:\Program_Repository\github\basic\file

ps = p.parents
for each in ps:
    print(each)
# D:\Program_Repository\github\basic\file
# D:\Program_Repository\github\basic
# D:\Program_Repository\github
# D:\Program_Repository
# D:\
print(ps[0], ps[1])    # D:\Program_Repository\github\basic\file D:\Program_Repository\github\basic

print(p.parts)    # ('D:\\', 'Program_Repository', 'github', 'basic', 'file', 'test')
print(p.stat())    # os.stat_result(st_mode=16895, st_ino=2533274790466088, st_dev=17911000550101998974, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1749058015, st_mtime=1749058009, st_ctime=1749058009)

# stat().st_size 文件或文件夹大小(单位字节)
print(p.stat().st_size)    # 0


# 绝对路径/相对路径
# . 当前所在目录    .. 上一级目录
# resolve() 转换成绝对路径
# iterdir() 获取当前路径下所有的子文件和子文件夹
print(Path("./FishD.txt"))    # FishD.txt
print(Path("../assets"))    # ..\assets
print(Path("./FishD.txt").resolve())    # D:\Program_Repository\github\basic\file\FishD.txt
m = Path(r"D:\Program_Repository\github\basic\file")
for i in m.iterdir():
    print(i)
# D:\Program_Repository\github\basic\file\file01.py
# D:\Program_Repository\github\basic\file\file02.py
# D:\Program_Repository\github\basic\file\errorDemo_01.py
# D:\Program_Repository\github\basic\file\FishD.txt
# D:\Program_Repository\github\basic\file\target.zip
# D:\Program_Repository\github\basic\file\test
# D:\Program_Repository\github\basic\file\test.jpg

print([i for i in m.iterdir() if i.is_file()])
# [WindowsPath('D:/Program_Repository/github/basic/file/file01.py'), WindowsPath('D:/Program_Repository/github/basic/file/file02.py'), WindowsPath('D:/Program_Repository/github/basic/file/errorDemo_01.py'), WindowsPath('D:/Program_Repository/github/basic/file/FishD.txt'), WindowsPath('D:/Program_Repository/github/basic/file/target.zip'), WindowsPath('D:/Program_Repository/github/basic/file/test.jpg')]

# 路径修改
# mkdir() 创建文件夹
n = p / "FishC"
# 若文件夹存在会报错,需要设置 exist_ok=True
n.mkdir(exist_ok=True)
# 若路径中有多个不存在的文件夹会报错，需要设置 parents=True
n = p / "FishC/A/B/C"
n.mkdir(parents=True, exist_ok=True)
# open() 打开该路径
n = n / "FishC.txt"
f = n.open("w")
f.write("I love FishC")
f.close()

import os
# rename() 修改文件或文件夹名字, 无指定路径时默认当前文件夹
# replace() 替换指定的文件或文件夹，将文件剪切并替换掉
# rmdir() unlink() 删除文件夹（文件夹非空时会报错）；删除文件
# glob() 查找    迭代器，需要用list
# help(os.rename)
# os.rename(r"D:\Program_Repository\github\basic\file\test\FishC\A\B\C\FishC.txt", r"D:\Program_Repository\github\basic\file\test\FishC\A\B\C\NewFishC.txt")
m = Path("FishC.txt")
# m.replace(n) # 无替换文件时会报错

# n.unlink()
# n.parent.rmdir()

p = Path(".") # 当前目录
print(p.resolve())
# D:\Program_Repository\github\basic\file
p1 = list(p.glob("*.txt"))
for each in p1:
    print(each)
# FishD.txt

p = Path("..") # 上一级目录
print(p.resolve())
# D:\Program_Repository\github\basic
p2 = list(p.glob("file/*.py")) # 下一级目录
for each in p2:
    print(each)
# ..\file\file01.py
# ..\file\file02.py
# ..\file\errorDemo_01.py

p = Path(".")
p3 = list(p.glob("**/*.py")) # 当前目录及下一级目录
for each in p3:
    print(each)
# file01.py
# file02.py
# errorDemo_01.py
p4 = list(p.glob("*/*.py")) # 下一级目录
print(p4) # []

```



### 文件路径处理练习

```python
# 文件处理练习
# 判断当前路径是否为文件夹类型，如果是则在路径末尾追加一个 FishC.txt
from pathlib import Path

p = Path(r"D:\临时\test")
if p.is_dir():
    n = p / "FishC.txt"
    print(n.resolve())


# ————————————————————————————————————————————————————————
# 列举出当前目录下的所有子目录
# 带绝对路径
p = Path.cwd()
n = list(p.glob("./*"))
for i in n:
    if i.is_dir():
        print(i)
        print(i.name)
# D:\Program_Repository\github\basic\file\test
# test
# 不带绝对路径
p = Path(".")
n = list(p.glob("./*"))
for i in n:
    if i.is_dir():
        print(i)
# test

print([x for x in p.iterdir() if x.is_dir()])
# [WindowsPath('test')]


# ————————————————————————————————————————————————————————
# 列举出当前目录下的所有文件的尺寸
for i in p.iterdir():
    print(f"文件名：{i}，文件尺寸：{i.stat().st_size}字节")
# 文件名：file01.py，文件尺寸：1491字节
# 文件名：file02.py，文件尺寸：4581字节
# 文件名：errorDemo_01.py，文件尺寸：813字节
# 文件名：fileDemo_02.py，文件尺寸：750字节
# 文件名：FishD.txt，文件尺寸：5字节
# 文件名：target.zip，文件尺寸：179字节
# 文件名：test，文件尺寸：0字节
# 文件名：test.jpg，文件尺寸：71633字节


# ————————————————————————————————————————————————————————
# 列举出当前目录下的所有文件的修改时间
# time.strftime(format, struct_time) 用于将时间元组或者struct_time对象格式化为字符串
# time.strptime(string, format) 用于解析字符串为时间元组对象
# time.localtime() 根据提供的时间戳来转换为本地时间
from time import strftime,localtime
for i in n:
    print(f"文件名：{i}，修改时间：{strftime('%Y-%m-%d %H-%M-%S', localtime(i.stat().st_mtime))}")
# 文件名：file01.py，修改时间：2025-06-01 17-28-15
# 文件名：file02.py，修改时间：2025-06-05 01-56-27
# 文件名：errorDemo_01.py，修改时间：2025-06-01 17-38-15
# 文件名：fileDemo_02.py，修改时间：2025-06-05 17-22-00
# 文件名：FishD.txt，修改时间：2025-06-05 01-33-49
# 文件名：target.zip，修改时间：2025-06-01 17-33-13
# 文件名：test，修改时间：2025-06-05 01-26-57
# 文件名：test.jpg，修改时间：2025-06-05 01-33-49


# ————————————————————————————————————————————————————————
# 获取指定路径（文件夹）中所有的文件名，并按文件尺寸按从小到大进行排序
p = Path("..")
file = []
for i in p.iterdir():
    if i.is_dir():
        file.append(i)

file.sort(key=lambda x: x.stat().st_size)
for i in file:
    print(f"文件名：{i}，尺寸大小：{i.stat().st_size}字节")
# 文件名：..\assets，尺寸大小：0字节
# 文件名：..\dictionary，尺寸大小：0字节
# 文件名：..\FristGame，尺寸大小：0字节
# 文件名：..\number，尺寸大小：0字节
# 文件名：..\sequence，尺寸大小：0字节
# 文件名：..\set，尺寸大小：0字节
# 文件名：..\tuple，尺寸大小：0字节
# 文件名：..\Variables_Strings，尺寸大小：0字节
# 文件名：..\.git，尺寸大小：4096字节
# 文件名：..\.idea，尺寸大小：4096字节
# 文件名：..\branch_loop，尺寸大小：4096字节
# 文件名：..\file，尺寸大小：4096字节
# 文件名：..\function，尺寸大小：4096字节
# 文件名：..\list_Demo，尺寸大小：4096字节
# 文件名：..\strings，尺寸大小：4096字节

# 一行流
print("\n".join(f"文件名：{i}，尺寸大小：{i.stat().st_size}字节" for i in sorted((j for j in Path("..").iterdir() if j.is_dir()), key=lambda x:x.stat().st_size)))


# ————————————————————————————————————————————————————————
# 找出指定路径（文件夹）中最后被修改的文件
from time import strftime,localtime
p = Path("..")
file = []
for i in p.iterdir():
    if i.is_file():
        file.append(i)
n = max(file, key=lambda x: x.stat().st_mtime)
print(f"文件名:{n}，修改时间：{strftime('%Y-%m-%d %H-%M-%S', localtime(n.stat().st_mtime))}")
# 文件名:..\PythonBasic.md，修改时间：2025-06-01 00-24-04

# 一行流
# f"{a := b}" 表示a = b
# max([a, b]) 多个列表时，默认对列表中第一个元素进行比较，但返回的是整个列表，这也意味着后面的元素可以放置想要打印的东西
print(f"文件名:{(file := max([j for j in Path("..").iterdir() if j.is_file()], key=lambda x:x.stat().st_mtime)).name}，修改时间：{strftime('%Y-%m-%d %H-%M-%S', localtime(file.stat().st_mtime))}")
# 文件名:PythonBasic.md，修改时间：2025-06-01 00-24-04
print(max([(strftime("修改时间 -> %Y-%m-%d %H:%M:%S", localtime(f.stat().st_mtime)), f"文件名 -> {f.name}") for f in Path("..").iterdir() if f.is_file()]))

```



## with 和 pickle模块

```python
# with 和 pickle模块
# with语句和上下文管理器(上文打开文件，下文关闭文件)
f = open("FishC.txt", "w")
f.write("I love fishc")
f.close()
# 用with代替,不需要再关闭文件，即时保存操作，即使后面报错也能正常关闭文件
with open("FishC.txt", "w") as f:
    f.write("I love fishc")


# pickle模块 永久存储python对象 二进制
import pickle
x, y, z = 1, 2, 3
s = "FishC"
l = ["小甲鱼", 520, 3.14]
d = {"one":1, "two":2}
# 保存到.pkl文件
with open("data.pkl", "wb") as f:
    pickle.dump((x, y, z, s, l, d), f)

# 读取.pkl文件
with open("data.pkl", "rb") as f:
    x, y, z, s, l, b = pickle.load(f)

print(x, y, z, s, l, b, sep="\n")
# 1
# 2
# 3
# FishC
# ['小甲鱼', 520, 3.14]
# {'one': 1, 'two': 2}

# 使用 with 语句管理两个文件的上下文
with open("FishC.txt", "r") as f1, open("FishD.txt", "r") as f2:
    f1.seek(10)
    f2.write(f1.read(5))

```



### 文件with练习

```python
# 文件with练习
# 在 pathlib 模块中，Path 对象有一个 glob() 方法，它提供了向下递归搜索的能力（如下），请自己编写一个递归函数，实现相同的搜索功能
from pathlib import Path
p = Path("..")
# print(list(p.glob("**/*.txt")), end="\n")

files = []
def get_file(p, files, target):
    for each in p.iterdir():
        if each.is_file() and each.suffix == target:
            files.append(each)
        if each.is_dir():
            p = each
            get_file(p, files, target)
    return files

print(get_file(p, files, ".txt"))

# 请下载附件（  target.zip (5.56 KB, 下载次数: 597) ），自动统计该文件夹中的 Python 总代码行数。

# A. 其中包含的子文件夹，也需要一并统计入内
# B. 空行不能算
# C. 本题的源代码不统计入内
# 提示1：可以通过 __file__ 得到包含本源代码文件名的路径（字符串类型）
# 提示2：如果是 windows 系统，打开带中文文件，可能会引发编码错误，此时在 open() 函数中使用 errors="ignore" 参数来避免该问题
# 提示3：使用递归搜索反而会更简单一些

def get_files(p, files):
    for each in p.iterdir():
        if str(each) == __file__: # 跳过本文件
            continue
        if each.is_file() and each.suffix == ".py":
            files.append(each)
        if each.is_dir():
            p = each
            get_files(p, files)
    return files

def count_lines(files):
    lines = 0
    for each in files:
        with open(each, "r", errors="ignore") as f1: # 忽略错误编码
            t = f1.readlines()
            lines += len(t) - t.count("\n")
    return lines

p = Path(r".\target1")
files = []

files = get_files(p, files)
print(f"一共有{count_lines(files)}行代码")


# 编写一个源代码文件，其功能就是在当前文件夹下创建 10 个子文件夹，每个子文件夹下又放入自身的 10 个拷贝
def create_files(p, n):
    if n == 0:
        return None
    else:
        # p / f"{n-1}.py" 是拼接源代码的文件名
        with open(__file__, "r", encoding="utf-8") as f1, open(p / f"{n-1}.py", "w", encoding="utf-8") as f2:
            f2.write(f1.read())
        create_files(p, n-1)

def create_dirs(cwd, n):
    if n == 0:
        return None
    else:
        p = cwd / str(n-1) # 拼接新文件夹的路径
        p.mkdir(exist_ok=True) # 确保文件夹已存在也不会报错
        create_files(p, 10) # 创建10个源代码文件拷贝
        create_dirs(cwd, n-1)

# create_dirs(Path.cwd(), 10)

```



# 15.异常

## 异常捕获

```python
# 异常捕获
# try-except 捕获异常
# 异常后加as 可以打印出异常来
# e 指向对应的异常类，比如这里是 TypeError，那么它就是 <class 'TypeError'>
try:
    1 / 0
except ZeroDivisionError as e:
    print(e) # division by zero

# 有时候没把握出现的会是哪个异常,，可以把可能出现的异常放到元组中
try:
    520 + "FishC"
    1 / 0 # 上一行异常，这行未运行
except (ZeroDivisionError, TypeError, ValueError) as e:
    print(e) #unsupported operand type(s) for +: 'int' and 'str'

try:
    1 / 0
    520 + "FishC" # 上一行异常，这行未运行
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("值不正确")
except TypeError:
    print("类型不正确")
# 除数不能为0

# locals(); 查看当前所有变量
# 测试是否定义过一个值 f in locals();
# 可以检测是否关闭文件

# assert：断言；当这个关键字后边的条件为假的时候，程序自动崩溃并抛出AssertionError的异常。 可以用 assert **Error 来自定断言异常类型

# 如果试图引用一个未曾定义过的变量，Python 会抛出NameError异常
# 如果试图访问一个对象中不存在的属性，Python 会抛出AttributeError异常

```



## ==异常练习==

```python
# 异常练习
# eval() 返回表达式的执行结果
# 利用异常捕获机制，使用 while 循环语句来实现 for 循环语句的功能。
# 相当于将下面代码使用 while 语句来实现：
# 8*BkG^xR&Nry_~aO69FIe3VHJYp
x = "FishC"
# for each in x:
#   print(each)
y = iter(x)
while True:
    try:
        print(next(y))
    except StopIteration:
        break


# 利用 Python 异常机制，编写一个检查用户输入语句是否有错误的程序。
# 程序能够识别出 “语法错误”、“索引错误”、“变量未定义”、“除数为0” 和 “传入参数类型不恰当” 这几个错误类型。

while True:
    text = input("请输入一行语句：")
    if text == "q":
        break
    try:
        # eval() 返回表达式的执行结果
        y = eval(text)
        if y:
            print(f"结果是：{y}")
    except ZeroDivisionError:
        print("除数不能为0")
    except NameError:
        print("变量未定义")
    except IndexError:
        print("索引错误")
    except SyntaxError:
        print("语法错误")
    except (TypeError, ValueError):
        print("传入参数类型不恰当")
print("程序结束")

```



## 主动异常

```python
# 异常
# try-except-else    try-except-finally
# raise语句 直接抛出异常，主动引发异常
# raise ValueError("值不正确") # 报错ValueError
# assert语句 断言 只能引发AssertionError异常    常用于调试    类似于if语句
s = "FishC"
assert s == "FishC" # 为真，什么都不发生
# assert s != "FishC" # 为假，报错AssertionError

# 用异常来实现goto语句（勿用）
try:
    while True:
        while True:
            for i in range(10):
                if i > 3:
                    # 可以无指定异常，但会爆红，抛出异常后，except捕获异常，直接跳出循环
                    raise
                    # raise 如果不带任何参数，抛出的异常为RuntimeError，
                    # 当检测到一个不归属于任何其他类别的错误时，就会引发 RuntimeError 异常，关联的值是一个指示问题原因的字符串，
                    # 由于我们是直接 raise 引发，所以它这个字符串 No active exception to reraise 的意思大概就是说这个异常属于 “无中生有”。
                print(i)
            print("break")
        print("break")
    print("break")
except:
    print("到这里来了")

# 实现在捕获异常之后，打印一句 “出错啦”，再重新抛出相对应的异常（注意，这里我们说的异常并不特指具体的哪一类，而是泛指所有的异常）。
# 利用不带参数的 raise 语句即可实现
try:
    1 / 0
except:
    print("出错啦~")
    raise
    
```



# 16. 类和对象

## 16.1. 对象

```python
# 对象
# 对象 = 属性 + 方法
# 封装 创建对象之前将相关的属性和方法通过类打包到一起
# 创建对象需要先创建一个类class，再创建对象
# 创建类
class Turtle: # 类命名以大写字母开头
    head = 1
    eyes = 2
    legs = 4
    shell = True # 壳

    # self 实例对象本身，调用时通过self传递对象信息
    # self 在对象访问方法时自动进行传递，不需要显式传递
    def crawl(self): # 爬
        print("爬")

    def run(self):
        print("跑")

    def bite(self):
        print("咬")

    def eat(self):
        print("吃")

    def sleep(self):
        print("睡觉")

# 创建对象
t1 = Turtle()
# 调用类的属性，方法
print(t1.head) # 1
t1.eat() # 吃


t2 = Turtle()
# 改变或创建对象特有属性和方法
t2.legs = 3
print(t2.legs) # 3
t2.mouth = 1
print(t2.mouth) # 1


# dir(t)查看属性
print(dir(t1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'bite', 'crawl', 'eat', 'eyes', 'head', 'legs', 'run', 'shell', 'sleep']
print(dir(t2))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'bite', 'crawl', 'eat', 'eyes', 'head', 'legs', 'mouth', 'run', 'shell', 'sleep']


# 基于统一个类的两个对象，但它们并不相同，也并不相等。但它们所拥有的属性，确都是来自于同一个类的

```



### 16.1.1 创建类

```python
# 创建类
# 设计一个 Person 类，该类有 name 和 age 两个属性（分别用于指定对象的姓名和年龄），该类还有 set_name()、set_age()、get_name() 和 get_age() 四个方法（分别用于设置、获取对象的姓名和年龄）
class Person:
    name = None
    age = None
    def set_name(self):
        self.name = input("请输入名字：")

    def set_age(self):
        self.age = input("请输入年龄：")

    def get_name(self):
        if self.name:
            return self.name
        else:
            print("名字未设置")

    def get_age(self):
        if self.age:
            return self.age
        else:
            print("年龄未设置")

# 设计一个 Rectangle 类，该类有 length 和 width 两个属性（分别用于指定长方形的长度和宽度），该类还有 set_length()、set_width()、get_ perimeter() 和 get_area() 四个方法（分别用于设置长方形的长和宽，以及获取长方形的周长和面积）
class Rectangle:
    length = None
    width = None

    def set_length(self):
        self.length = input("请输入矩形的长度：")

    def set_width(self):
        self.width = input("请输入矩形的宽度：")

    def get_perimeter(self):
        if not self.length:
            self.set_length()

        if not self.width:
            self.set_width()

        return (self.length + self.width) * 2

    def get_area(self):
        if not self.length:
            self.set_length()

        if not self.width:
            self.set_width()

        return self.length * self.width

```



## 16.2 继承

```python
# 继承
# 在类中定义类属性，并不会被类方法直接通过变量名访问到，需要通过 self.属性 来访问
class A:
    x = 520
    def hello(self):
        print("hello,我是A")

# class B(A) B类 继承 A类
class B(A):
    pass

b = B()
b.hello() # hello,我是A

class C(A):
    x = 888
    def hello(self):
        print("hello,我是C")
c = C()
print(c.x) # 888
c.hello() # hello,我是C

# isinstance() 判断对象是否属于某个类
print(isinstance(c, C)) # True
print(isinstance(c, A)) # True

# issubclass() 判断一个类是否为某个类的子类
print(issubclass(C, A)) # True

class B:
    x = 888
    y = 666
    def hello(self):
        print("hello,<UNK>B")

# 同时继承两个类，访问顺序从左到右
class C(A, B): pass
c = C()
print(c.x) # 520
print(c.y) # 666
c.hello() # hello,我是A


# 组合
# 将多个类的实例放到一个类中
class Turtle:
    def say(self):
        print("乌龟")

class Cat:
    def say(self):
        print("喵")

class Dog:
    def say(self):
        print("汪")

# 将多个类的实例化对象放到一个类中
class Garden:
    t = Turtle()
    cat = Cat()
    dog = Dog()
    def say(self):
        self.t.say()
        self.cat.say()
        self.dog.say()

g = Garden()
g.say()
# 乌龟
# 喵
# 汪

# 可以在子类中修改父类的属性
class D(B):
    B.y = 111
print(B.y) # 111

```



### 16.2.1 动物园组合

```python
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

```



## 16.3 绑定

```python
# 绑定
# self 将实例对象和类进行绑定
class C:
    y = 200
    def get_self(self):
        print(self)

c = C()
c.x = 100
# c.__dict__ 查看对象私有属性，公有属性不会显示
print(c.__dict__) # {'x': 100}
c.y = 300
print(c.__dict__) # {'x': 100, 'y': 300}


# 在类中给实例化对象赋予私有属性
class C:
    def set_x(self, x):
        self.x = x
c = C()
print(c.__dict__) # {}
# 在方法中传入参数
c.set_x(100)
print(c.x) # 100
print(c.__dict__) # {'x': 100}


# __init__ 初始化参数
class C:
    def __init__(self, x):
        self.x = x
# 直接在创建对象时传入参数
c = C(10)
print(c.x)  # 10

# 类还可以作为字典来使用，通过对象来作为字典使用更好
class F:
    pass
f = F()
f.x = 1
f.y = "FishC"
f.z = [1, 2, 3]
print(f.x, f.y, f.z) # 1 FishC [1, 2, 3]


# 字典
d = {}
d["x"] = 1
d["y"]= "FishC"
d["z"]= [1, 2, 3]
print(d["x"], d["y"], d["z"]) # 1 FishC [1, 2, 3]


x = 123
class C:
    x = 100
    def get_x(self):
        print(f"x = {x}")
        print(f"self.x = {self.x}")
c = C()
c.get_x()
# x = 123
# self.x = 100
c.x = 250
c.get_x()
# x = 123
# self.x = 250

```



### 16.3.1 菜单

```python
# 菜单
class Meet:
    nums = 0

class Egg(Meet):
    name = "鸡蛋"
    price = 1

class Beef(Meet):
    name = "牛肉"
    price = 25

class Mutoon(Meet):
    name = "羊肉"
    price = 30

class Vegetable:
    nums = 0

class Onion(Vegetable):
    name = "洋葱"
    price = 2

class Tomato(Vegetable):
    name = "番茄"
    price = 2

class Potato(Vegetable):
    name = "土豆"
    price = 3

class Radish(Vegetable):
    name = "萝卜"
    price = 3

class Memu:
    def order(self):
        self.x = []
        print("客官想要吃点什么？")

        dishes = input("1.洋葱炒牛肉；2.洋葱炒羊肉；3.煎蛋；4.番茄炒蛋；5.土豆萝卜炖羊肉：")
        dishes = dishes.split()
        while dishes:
            dish = dishes.pop(0)
            if dish == "1":
                mutoon = Mutoon()
                mutoon.nums = 1
                onion = Onion()
                onion.nums = 1
                self.x.append([mutoon, onion])

            if dish == '2':
                onion = Onion()
                onion.num = 1
                mutoon = Mutoon()
                mutoon.num = 1
                self.x.extend([mutoon, onion])

            if dish == '3':
                egg = Egg()
                egg.num = 2
                self.x.append(egg)

            if dish == '4':
                tomato = Tomato()
                tomato.num = 2
                egg = Egg()
                egg.num = 3
                self.x.extend([tomato, egg])

            if dish == '5':
                potato = Potato()
                potato.num = 2
                radish = Radish()
                radish.num = 1
                mutoon = Mutoon()
                mutoon.num = 2
                self.x.extend([potato, radish, mutoon])

    def pay(self):
        total = 0
        for each in self.x:
            total += each.price * each.num
            print(each.name, each.price, "*", each.num)
            print(f"感谢惠顾，您一共消费了 {total} 元，欢迎下次光临~")
            
```



## 16.4 构造函数

```python
# 构造函数
# __init__() 构造函数，在类中定义以个性化对象
class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def mul(self):
        return self.x * self.y
c = C(2, 3)
print(c.add()) # 5
print(c.mul()) # 6
print(c.__dict__) # {'x': 2, 'y': 3}


# 重写
# 子类重写父类的方法来覆盖为自己的方法
class A:
    def __init__(self):
        print("A")

class B1(A):
    def __init__(self):
        A.__init__(self)
        print("B1")

class B2(A):
    def __init__(self):
        A.__init__(self)
        print("B2")

class C(B1, B2):
    def __init__(self):
        B1.__init__(self)
        B2.__init__(self)
        print("C")
c = C()
# A
# B1
# A
# B2
# C
# A重复调用了

# super 父类，在多重继承时可以避免重复调用
# 自动根据 MRO 顺序查找， Method Resolution Order 方法解析顺序
class A:
    def __init__(self):
        print("A")

class B1(A):
    def __init__(self):
        super().__init__()
        print("B1")

class B2(A):
    def __init__(self):
        super().__init__()
        print("B2")

class C(B1, B2):
    def __init__(self):
        super().__init__()
        print("C")
c = C()
# A
# B2
# B1
# C

# 查看mro    mro() 或 __mro__
print(C.mro())
# [<class '__main__.C'>, <class '__main__.B1'>, <class '__main__.B2'>, <class '__main__.A'>, <class 'object'>]
print(B1.mro())
# [<class '__main__.B1'>, <class '__main__.A'>, <class 'object'>]

```



### ==16.4.1 文件搜索==

```python
# 文件搜索
# 先打印路径结构
# 然后通过类和对象的方式来存储每一个文件信息（包含文件名、文件尺寸、位置、创建时间、修改时间和访问时间），并定义相应的方法来获取这些文件信息
# 最后编写一个搜索函数，通过提供文件名的方式搜索对应的文件位置和信息
from time import strftime, localtime
from pathlib import Path
class File:
    def __init__(self, name, size, folder, ctime, mtime, atime):
        self.name = name
        self.size = size
        self.folder = folder
        self.ctime = ctime
        self.mtime = mtime
        self.atime = atime

    def get_name(self):
        return self.name

    def get_size(self):
        return f"{self.size}字节"

    def get_folder(self):
        return f"位置：{self.folder}"

    def get_ctime(self):
        return f"创建时间：{strftime("%Y-%m-%d %H:%M:%S", localtime(self.ctime))}"

    def get_mtime(self):
        return f"修改时间：{strftime("%Y-%m-%d %H:%M:%S", localtime(self.mtime))}"

    def get_atime(self):
        return f"访问时间：{strftime("%Y-%m-%d %H:%M:%S", localtime(self.atime))}"

def get_file_msg(path):
    p = Path(path)
    paths = []
    files = []
    for i in p.glob("**/*"):
        paths.append(i)
        if i.is_file():
            name = i.name
            size = i.stat().st_size
            folder = i.parent.resolve()
            ctime = i.stat().st_ctime
            mtime = i.stat().st_mtime
            atime = i.stat().st_atime
            files.append(File(name, size, folder, ctime, mtime, atime))

    print("路径结构如下：")
    for each in paths:
        print(each)

    return files

def sear_file(files):
    count = 0
    filename = input("\n请输入想要搜索的文件名：")
    for each in files:
        if filename in each.name:
            count += 1
            print(f"\n找到相关文件（{count}）-> {each.get_name()}（{each.get_size()}）")
            print(each.get_folder())
            print(each.get_ctime())
            print(each.get_mtime())
            print(each.get_atime())
        else:
            print("找不到相关文件！")

files = get_file_msg("target")
sear_file(files)

```



## 16.5Mixin（设计模式）混入

```python
# Mixin Mix-in 混入，临时加入 一种设计模式
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f"我叫{self.name}，今年{self.age}岁")

# 临时想给 pig 添加一个飞行的技能
class FlyMixin:
    def fly(self):
        print("我也会飞了")

# 多继承
class Pig(FlyMixin, Animal):
    def special(self):
        print("我的技能是拱白菜")

p = Pig("大肠", 5)
p.say() # 我叫大肠，今年5岁
p.special() # 我的技能是拱白菜
p.fly() # 我也会飞了


# ————————————————————————————————————————————————————————————
# super 与 MRO顺序
# 当 super 无直接父类时： 会根据对象直接对应的类的 MRO顺序 来找寻其“父类”
# self 也取决于当前对象
class Displayer:
    def display(self, message):
        print(message)

class LoggerMixin:
    def log(self, message, filename="logfile.txt"):
        with open(filename, "w") as f:
            f.write(message)

    def display(self, message):
        super().display(message)
        self.log(message)

class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, "subclasslog.txt")

subclass = MySubClass()
subclass.display("This is a test")

```



### ==16.5.1 鱼C超市会员管理系统==

```python
# 鱼C超市会员管理系统。
# 1. 会员开卡
# 会员开卡自动赋予一个新的卡号（默认从 10000 开始递增）
# 要求输入用户名和密码
# 密码要求长度不低于 6 位

# 2. 修改密码
# 先确认输入卡号是否存在
# 再判断旧密码是否正确
# 新密码长度同样不能低于 6 位
#
# 3. 商品支付
# 先确认输入卡号是否存在
# 再判断密码是否正确
# 根据输入的消费金额增加会员卡积分（比如输入 250 消费金额，那么积分增加 250）
#
# 4. 积分查询
# 先确认输入卡号是否存在
# 再判断密码是否正确
#
# 代码要求：
# 1. 创建一个会员类（Member），包含信息：卡号、用户名、密码（要求密码需要以 MD5 哈希值的形式存储）、积分、注册日期
# 2. 创建一个管理类（Manage），用于实现上方要求的主要程序功能
# 3. 创建一个 Mixin 类（PasswdMixin），用于实现密码相关的功能组件（密码长度检测和将明文密码转换为 MD5 的操作）
# 4. 创建一个 Mixin 类（LoggerMixin），用于实现日志记录相关的功能组件
import hashlib
import time

# 卡号、用户名、密码、积分、注册日期
class Member:
    def __init__(self, cardid, name, password, scores, regdata):
        self.cardid = cardid
        self.name = name
        self.password = password
        self.scores = scores
        self.regdata = regdata

# 密码长度检测和将明文密码转换为 MD5
class PasswdMixin:
    def tooshort(self, password, request=6):
        while len(password) < request:
            password = input(f"会员密码不能小于{request}位，请重新输入")
        return password

    def to_md5(self, password):
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        return password

# 实现日志记录相关的功能
class LoggerMixin:
    def log(self, message, filename="log.txt"):
        with open(filename, "a") as f:
            f.write(message)


# 主要功能
class Manager(PasswdMixin, LoggerMixin):
    def __init__(self):
        self.member = {}
        self.cardid = 10000

    def welcome(self):
        print("欢迎来到超市会员管理系统")
        command = 0
        while command != "5":
            command = input("\n1.创建新卡;2.修改密码;3.商品支付;4.积分查询;5.退出程序：")
            if command == "1":
                self.create_member()
            elif command == "2":
                self.change_password()
            elif command == "3":
                self.pay()
            elif command == "4":
                self.check_scores()
            elif command == "5":
                print("感谢使用超市会员管理系统")

    def create_member(self):
        name = input("请输入姓名：")
        password = input("请输入密码:")
        password = self.tooshort(password)
        password = self.to_md5(password)
        regdata = time.localtime()
        scores = 0
        member = Member(self.cardid, name, password, scores, regdata)
        self.member[self.cardid] = member
        print(f"创建成功，卡号为 {self.cardid}，关联用户 -> {name}")
        self.log(f"开卡成功: {self.cardid} -> {name}, 时间:{time.strftime("%Y-%m-%d %H:%M:%S", regdata)}")
        self.cardid = self.cardid + 1

    def confirm_password(self):
        cardid = int(input("请输入卡号:"))
        while cardid not in self.member:
            cardid = input("该卡号不存在,请重新输入:")

        password = input("请输入密码:")
        password = self.to_md5(password)
        while not self.member[cardid].password == password:
            password = input("密码错误,请重新输入:")
            password = self.to_md5(password)
        return cardid

    def change_password(self):
        cardid = self.confirm_password()
        newpassword = input("请输入新密码:")
        newpassword = self.tooshort(newpassword)
        newpassword = self.to_md5(newpassword)
        self.member[cardid].password = newpassword
        self.log(f"修改密码: 卡号 -> {cardid}, 时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())})")
        print("密码修改成功.")

    def pay(self):
        cardid = self.confirm_password()
        money = input("请输入支付金额:")
        self.member[cardid].scores += money
        self.log(f"积分累计: 卡号 -> {cardid}, +{money}分, 时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")

    def check_scores(self):
        cardid = self.confirm_password()
        print(f"卡号 {cardid} 当前的消费积分为: {self.member[cardid].scores}")

def main():
    m = Manager()
    m.welcome()

if __name__ == '__main__':
    main()

```



## 16.6 多态

```python
# 多态
# 指函数可以根据不同的对象执行不同的操作
# 类的继承与重写方法：类与对象中实现多态的一种方式
class Shape: # 形状
    def __init__(self, name):
        self.name = name
    def area(self):
        pass

class Square(Shape): # 正方形
    def __init__(self, length):
        super().__init__('正方形')
        self.length = length
    def area(self):
        return self.length * self.length

class Circle(Shape): # 圆形
    def __init__(self, radius): # 半径
        super().__init__('圆形')
        self.radius = radius
    def area(self):
        return self.radius * self.radius * 3.14

class Triangle(Shape): # 三角形
    def __init__(self, base, height): # 底和高
        super().__init__('三角形')
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height / 2

s = Square(5)
c = Circle(6)
t = Triangle(3, 4)
print(s.name, s.area()) # 正方形 25
print(c.name, c.area()) # 圆形 113.04
print(t.name, t.area()) # 三角形 6.0

# —————————————————————————————————————————————————————————
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"我是一只猫咪，我叫{self.name}，今年{self.age}岁")
    def say(self):
        print("喵~")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"我是一只修狗，我叫{self.name}，今年{self.age}岁")
    def say(self):
        print("汪~")

class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"我是一只猪，我叫{self.name}，今年{self.age}岁")
    def say(self):
        print("oink~")

c = Cat("web", 4)
d = Dog("布布", 7)
p = Pig("大肠", 5)

# 给函数传递不同的对象
# 鸭子类型 不需要关注传入的是什么类型，只要它符合这里面的 intro 和 say 方法， 它就属于这个类型
def animal(x):
    x.intro()
    x.say()

animal(c)
# 我是一只猫咪，我叫web，今年4岁
# 喵~
animal(d)
# 我是一只修狗，我叫布布，今年7岁
# 汪~
animal(p)
# 我是一只猪，我叫大肠，今年5岁
# oink~

class Bicycle:
    def intro(self):
        print("走过多远的路")
    def say(self):
        print("继续走")
b = Bicycle()
animal(b)
# 走过多远的路
# 继续走

```



### ==16.6.1 企业员工管理程序==

```python
# 企业员工管理程序
# a. 员工分类：普通员工（Employee）、组长（Teamleader）、经理（Manager）
# b. 员工属性：姓名（name）、职位（job）、级别（grade）、工龄（year）、工号（uid）
# c. 员工方法：
# get_uid() -- 获取工号
# get_name() -- 获取姓名
# get_job() -- 获取职位
# get_grade() -- 获取级别
# get_year() -- 获取工龄
# salary() -- 统计并返回工资（计算方法如下）
#
# d. 员工工资计算方法：
# 普通员工：3000 + 500 * 级别 + 50 * 工龄
# 组长：4000 + 800 * 级别 + 100 * 工龄
# 经理：5000 + 1000 * (级别 + 工龄)
#
# e. 程序功能：
# 录入员工数据功能（工号自动分配，由 10000 开始）
# 查询功能，分为员工查询和职位查询（见程序实现截图）
# 各类员工级别数量如下：
# 普通员工：10 级
# 组长：6 级
# 经理：3 级
# 升级功能：支持增加多级；当超过当前职位最高级别时，进行升职操作（无论增加多少个级别，只要发生升职，级别一律初始化为 1 级，见程序实现截图）.
# 降级功能：支持减少多级；当超过当前职位最高级别时，进行升职操作（无论减少多少个级别，只要发生降职，级别一律初始化为当前职位最高级别，见程序实现截图）
class Employee:
    def __init__(self, name, job, grade, year, uid):
        self.name = name
        self.job = job
        self.grade = grade
        self.year = year
        self.uid = uid

    def get_uid(self):
        return self.uid

    def get_name(self):
        return self.name

    def get_job(self):
        return self.job

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def get_year(self):
        return self.year

    def salary(self):
        return 3000 + 500 * self.grade + 50 * self.year

class Teamleader(Employee):
    def salary(self):
        return 4000 + 800 * self.grade + 100 * self.year

class Manager(Employee):
    def salary(self):
        return 5000 + 1000 * (self.grade + self.year)

def main():
    mems = {}
    jobs = {'E': [], 'T': [], 'M': []}
    uid = 10000
    MAX_E_GRADE = 10
    MAX_T_GRADE = 6
    MAX_M_GRADE = 3

    while True:
        ins = input("\n1.录入;2.查询;3.升级;4.降级;5.退出：")

        # 主线功能：录入
        if ins == '1':
            name = input("姓名：")
            job = input("职位（E.普通员工;T.组长;M.经理）：")
            year = int(input("工龄："))
            grade = int(input("级别："))

            if job == 'E':
                while grade > MAX_E_GRADE:
                    grade = int(input(f"该职位最高级别为{MAX_E_GRADE}，请重新录入级别："))

                e = Employee(name, job, grade, year, uid)
                mems[uid] = e
                jobs['E'].append(e)

            if job == 'T':
                while grade > MAX_T_GRADE:
                    grade = int(input(f"该职位最高级别为{MAX_T_GRADE}，请重新录入级别："))

                e = Teamleader(name, job, grade, year, uid)
                mems[uid] = e
                jobs['T'].append(e)

            if job == 'M':
                while grade > MAX_M_GRADE:
                    grade = int(input(f"该职位最高级别为{MAX_M_GRADE}，请重新录入级别："))

                e = Manager(name, job, grade, year, uid)
                mems[uid] = e
                jobs['M'].append(e)

            print(f"录入成功！姓名：{name}，工号：{uid}，薪资：{e.salary()}")
            uid += 1

        # 主线功能：查询
        if ins == '2':
            op = input("1.员工查询;2.职位查询：")

            # 支线功能：员工查询
            if op == '1':
                uid = int(input("请输入工号："))

                if mems.get(uid):
                    e = mems[uid]
                    print(f"姓名：{e.get_name()}")
                    print(f"职位：{e.get_job()}")
                    print(f"级别：{e.get_grade()}")
                    print(f"工龄：{e.get_year()}")
                    print(f"薪资：{e.salary()}")
                else:
                    print("该工号不存在！")

            # 支线功能：职位查询
            if op == "2":
                job = input("职位（E.普通员工;T.组长;M.经理）：")

                if job == 'E':
                    if jobs["E"]:
                        print(f"目前普通员工共有{len(jobs['E'])}人")
                        for each in jobs['E']:
                            print(f"{each.get_uid() - each.get_name()}")
                    else:
                        print("目前公司没有普通员工！")

                if job == 'T':
                    if jobs['T']:
                        print(f"目前组长共有 {len(jobs['T'])} 人：")
                        for each in jobs['T']:
                            print(f"{each.get_uid()} - {each.get_name()}")
                    else:
                        print("目前公司没有组长！")

                if job == 'M':
                    if jobs['M']:
                        print(f"目前经理共有 {len(jobs['M'])} 人：")
                        for each in jobs['M']:
                            print(f"{each.get_uid()} - {each.get_name()}")
                    else:
                        print("目前公司没有经理！")

        if ins == "3":
            uid = int(input("请输入工号："))

            if mems.get(uid):
                e = mems[uid]
                print(f"{e.get_name}, 工号：{e.get_uid()}, 当前职位：{e.get_job()}{e.get_grade()}，当前薪资：{e.salary()}")

                name = e.get_name()
                job = e.get_job()
                grade = e.get_grade()
                year = e.get_year()
                old_salary = e.get_salary()

                n = int(input("请输入需要增加的级数："))

                if job == 'E':
                    if grade + n > MAX_M_GRADE:
                        job = "T"
                        grade = 1
                        jobs['E'].remove(e)
                        e = Employee(name, job, grade, year, uid)
                        jobs['T'].append(e)
                        mems[uid] = e
                    else:
                        grade = grade + n


                elif job == 'T':
                    if grade + n > MAX_T_GRADE:
                        job = "M"
                        grade = 1
                        jobs['T'].remove(e)
                        e = Employee(name, job, grade, year, uid)
                        jobs['M'].append(e)
                        mems[uid] = e
                    else:
                        e.set_grade(grade + n)

                elif job == 'M':
                    if grade + n > MAX_M_GRADE:
                        print("已达到最高级别")
                        grade = MAX_M_GRADE
                    else:
                        e.set_grade(grade + n)

                new_salary = e.salary()
                print(f"升级成功！\n{e.get_name}, 工号：{e.get_uid()}, 升级后职位：{e.get_job()}{e.get_grade()}，升级后薪资：{e.salary()}（+{new_salary - old_salary}）")
            else:
                print("该工号不存在！")

        if ins == "4":
            uid = int(input("请输入工号："))

            if mems.get(uid):
                e = mems[uid]
                print(
                    f"{e.get_name}, 工号：{e.get_uid()}, 当前职位：{e.get_job()}{e.get_grade()}，当前薪资：{e.salary()}")

                name = e.get_name()
                job = e.get_job()
                grade = e.get_grade()
                year = e.get_year()
                old_salary = e.get_salary()

                n = int(input("请输入需要减少的级数："))

                if job == 'M':
                    if grade - n <= 0:
                        job = "T"
                        grade = MAX_T_GRADE
                        jobs['M'].remove(e)
                        e = Employee(name, job, grade, year, uid)
                        jobs['T'].append(e)
                        mems[uid] = e
                    else:
                        grade = grade - n

                elif job == 'T':
                    if grade - n <= 0:
                        job = "E"
                        grade = MAX_E_GRADE
                        jobs['T'].remove(e)
                        e = Employee(name, job, grade, year, uid)
                        jobs['E'].append(e)
                        mems[uid] = e
                    else:
                        e.set_grade(grade - n)

                elif job == 'E':
                    if grade - n <= 0:
                        print("已达到最低级别")
                        grade = 1
                    else:
                        e.set_grade(grade - n)

                new_salary = e.salary()
                print(
                    f"升级成功！\n{e.get_name}, 工号：{e.get_uid()}, 升级后职位：{e.get_job()}{e.get_grade()}，升级后薪资：{e.salary()}（+{new_salary - old_salary}）")
            else:
                print("该工号不存在！")

        if ins == "5":
            break

main()

```



## 16.7 私有变量

```python
# 私有变量
# __x  name mangling 设置"私有变量"
# 在类实例化时，名字会被改变， 需要通过 c._C__x 获取该“私有变量“
# 方法名同理 d._D__func() 调用方法
# 不建议使用
class C:
    def __init__(self, x):
        self.__x = x
    def set_x(self, x):
        self.__x = x
    def get_x(self):
        return self.__x

c = C(250)
# print(c.__x)  “私有变量”无法获取到值
print(c.get_x())  # 250
c.set_x(1)
print(c.get_x())  # 1
print(c.__dict__)  # {'_C__x': 1}
print(c._C__x)  # 1 通过 _C__x 获取“私有变量”

class D:
    def __func(self):
        print("hello world")
d = D()
# d.__func() 无法直接调用该方法
d._D__func() # hello world

# 动态添加“私有变量”，但动态添加的名字并不会改变，依旧是 c.__y
c.__y = 250
print(c.__dict__) # {'_C__x': 1, '__y': 250}

# _单个下横线开头或结尾的变量  都是内部变量，最好不要去访问它


c.x = 1
# 通过动态添加键值对添加属性
c.__dict__["z"] = 2
print(c.__dict__) # {'_C__x': 1, '__y': 250, 'x': 1, 'z': 2}


# 类 实际上 字典
# 字典会消耗大量空间，当遇到固定空间的对象时可以使用 __slots__属性

class C:
    # 该类的对象仅有 x,y两个属性可用
    __slots__ = ['x', 'y']
    def __init__(self, x):
        self.x = x
c = C(250)
print(c.x) # 250
c.y = 520
print(c.y) # 520

# 当继承该类时，不会在子类生效，仍可以添加额外属性，放置于__dict__属性
class E(C):
    pass
e = E(250)
e.x = 1
e.y = 2
e.z = 3
print(e.__slots__) # ['x', 'y']
print(e.__dict__) # {'z': 3}

# 想要 __slots__ 属性真正发挥功效，要求必须在整个继承链条中，每个父类和子类均做出一致的实现
class C:
    # __slots__ = ["x", "y"] 当父类和子类同时限制时生效
    pass
class D(C):
    __slots__ = ["x", "y"]
    def __init__(self, x, y):
        self.x = x
        self.y = y
d = D(3, 4)
d.z = 5
print(d.__dict__) # {'z': 5}

```



### ==16.7.1 汽车租赁系统==

```python
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

```



## 16.8 内置默认方法

### 内置默认方法基础

```python
# 内置默认方法基础
# __new__(cls[, ...]) 创建对象时第一个调用，返回 self  cls:类  作用于不可变量
class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return super().__new__(cls, string)
cs = CapStr("FishC")
print(cs)    # FISHC
print(cs.lower())    # fishc
print(cs.capitalize())    # Fishc

# ———————————————————————————————————————————
# __del__(self):    当类最后一个引用销毁时触发
class C:
    def __init__(self):
        print("我来了~")
    def __del__(self):
        print("我走了~")
c = C()
# 我来了~
print("1") # 1
del c
# 我走了~ 销毁时触发
print("2") # 2

c = C()
# 我来了~
d = c
del c # 最后一个引用销毁时触发
print("3") #3
# 我走了~    若程序中未销毁，程序运行结束时销毁，垃圾回收机制

# ———————————————————————————————————————————
# del方法可以通过创建一个该实例的新引用来推迟其销毁（对象的重生）（不建议，上下文环境改变，无法正常工作）
class D:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        # 一般不要使用全局变量，会污染命名空间
        global x
        x = self
d = D("tyz")
print(d, d.name) # <__main__.D object at 0x000001F2DED76F90> tyz
del d
print(x, x.name) # <__main__.D object at 0x0000028BF9DB6F90> tyz

class E:
    def __init__(self, name, func):
        self.name = name
        self.func = func
    def __del__(self):
        self.func(self)
# 闭包
def outer():
    x = 0
    def inner(y=None):
        nonlocal x
        if y:
            x = y
        else:
            return x
    return inner
f = outer()
e = E("tyz", f)
del e
# 销毁时给 func() f=inner(self)赋值，将 self 保存在 x 中，g=f()时调用
g = f()
print(g, g.name) # <__main__.E object at 0x00000219DDDF70E0> tyz

# ———————————————————————————————————————————
# 绕过类的构造函数，创建出它的实例对象
class C:
    def __init__(self, x):
        self.x = x
c = C.__new__(C)
print(isinstance(c, C)) # True
# c.x 不存在，仅创建了实例对象，未初始化

```



#### 银行账户管理系统

```python
# 银行账户管理系统
# a. 创建账户
# 需要提供姓名和密码（要求密码需要以 MD5 哈希值的形式存储）
# 银行卡号自动生成
# 支持预存款
#
# b. 删除账户
# 需要验证卡号、姓名和密码
#
# c. 查询余额
# 需要验证卡号和密码
#
# d. 存款
# 需要验证卡号和密码
# 输入金额
#
# e. 取款
# 需要验证卡号和密码
# 输入金额，并检查余额是否足够
#
# f. 转账
# 需验证我方卡号和密码，验证对方卡号是否存在
# 输入金额，并检查我方余额是否足够
#
# 程序输入限制（如用户不按要求输入，必须予以纠正）：
# 密码必须是 6 位数字
# 金额必须是非负数
# 卡号必须是正整数
#
# 相关类的实现可以参考下面结构（当然你也可以按照自己的想法去构造）：
# PasswdMixin（Mixin 类，用于实现与密码相关的功能组件）
# is_valid() -- 检测密码长度
# to_md5() -- 将明文密码转换为 MD5 存储
#
# Account（基本账户类）
# confirm_name() -- 确认姓名是否匹配
# confirm_passwd() -- 确认密码是否匹配
# withdraw() -- 取款
# deposit() -- 存款
# transfer() -- 转账
# get_balance() -- 查询余额
#
# UserManager（账户管理类）
# check_account() -- 检查账户是否存在及密码是否正确
# create_account() -- 创建账户
# delete_account() -- 删除账户
# get_account() -- 获取账户
import hashlib

class PasswdMixin:
    # 检测密码长度
    def is_valid(self, passwd):
        while True:
            if len(passwd) != 6 or not passwd.isdigit():
                passwd = input("密码需为6位数字，请重新输入：")
            else:
                break
        return passwd

    # 密码转换为 md5 存储
    def to_md5(self, passwd):
        passwd = hashlib.md5(passwd.encode("utf-8")).hexdigest()
        return passwd

class Account(PasswdMixin):
    def __init__(self, username, password, cardid, balance):
        self.username = username
        self.password = password
        self.cardid = cardid
        self.balance = balance

    # 确认姓名
    def confirm_name(self, name):
        return name == self.username

    # 确认密码
    def confirm_password(self, password):
        return password == self.password

    # 取款
    def withdraw(self, money):
        if self.balance < money:
            print(f"您的账户不足{money}元，无法取款")
        else:
            self.balance -= money
            print(f"成功取出{money}元。")

    # 存款
    def deposit(self, money):
        self.balance += money
        print(f"成功存入{money}元")

    # 转账
    def transfer(self, account, money):
        if self.balance < money:
            print(f"您的账户不足{money}元，无法转账")
        else:
            self.balance -= money
            account.balance += money
            print(f"成功转账{money}元。")

    # 查询余额
    def get_balance(self):
        return self.balance

class UserManager(PasswdMixin):
    def __init__(self):
        self.accounts = {}
        self.cardid = 88888888

    # 检测账户密码
    def check_account(self, cardid, password):
        if self.accounts.get(cardid):
            account = self.accounts[cardid]
            password = account.to_md5(password)
            if account.confirm_password(password):
                return True
            else:
                print("密码错误，请重新输入：")
                return False
        else:
            print("账户不存在")
            return False

    # 创建账户
    def create_account(self, name, password, money=0):
        password = self.is_valid(password)
        password = self.to_md5(password)
        account = Account(name, password, self.cardid, money)
        self.accounts[self.cardid] = account
        print(f"创建成功，卡号是：{self.cardid}")
        self.cardid += 1

    # 删除账户
    def delete_account(self, cardid, name, password):
        if self.check_account(cardid, password):
            account = self.accounts[cardid]
            if account.confirm_name(name):
                del self.accounts[cardid]
                print(f"卡号为：{cardid}的账号已删除已删除")
            else:
                print(f"用户名：{name}输入错误")

    def get_account(self, cardid, password, nopassword=False):
        if nopassword:
            if self.accounts.get(cardid):
                account = self.accounts[cardid]
                return account
            else:
                print("该账户不存在")
                return None
        else:
            if self.check_account(cardid, password):
                return self.accounts[cardid]
            else:
                return None

def main():
    bank = UserManager()

    # 需要获取那些信息
    def get_msg(cardid=False, name=False, passwd=False):
        msg = {"cardid":None, "name":None, "passwd":None}
        if cardid:
           msg["cardid"] = get_integer_input("请输入卡号：")
        if name:
            msg["name"] = input("请输入姓名：")
        if passwd:
            msg["password"] = input("请输入密码：")
        return msg

    # 获取整数
    def get_integer_input(str):
        while True:
            try:
                num = int(input(str))
                if num < 0:
                    raise ValueError
                break
            except ValueError:
                print("请输入一个有效的整数！")
        return num

    # 获取浮点数
    def get_float_input(str):
        while True:
            try:
                num = float(input(str))
                if num < 0:
                    raise ValueError
                break
            except ValueError:
                print("请输入一个有效的数值！")
        return num

    while True:
        ins = input("1.创建账户/2.删除账户/3.查询余额/4.存款/5.取款/6.转账/7.退出")
        if ins == "1":
            msg = get_msg(cardid=False, name=True, passwd=True)
            money = get_float_input("请输入预存款：")
            bank.create_account(msg["name"], msg["password"], round(money, 2))

        elif ins == "2":
            msg = get_msg(cardid=True, name=True, passwd=True)
            bank.delete_account(msg["cardid"], msg["name"], msg["password"])

        elif ins == "3":
            msg = get_msg(cardid=True, name=False, passwd=True)
            account = bank.get_account(msg["name"], msg["password"])
            if account:
                print(f"您的余额是：{account.get_balance()}")

        elif ins == "4":
            msg = get_msg(cardid=True, name=False, passwd=True)
            account = bank.get_account(msg["name"], msg["password"])
            if account:
                money = get_float_input("请输入金额：")
                account.deposit(round(money, 2))

        elif ins == "5":
            msg = get_msg(cardid=True, name=False, passwd=True)
            account = bank.get_account(msg["name"], msg["password"])
            if account:
                money = get_float_input("请输入金额：")
                account.withdraw(round(money, 2))

        elif ins == "6":
            msg = get_msg(cardid=True, name=False, passwd=True)
            account = bank.get_account(msg["name"], msg["password"])
            if account:
                target_cardid = get_integer_input("请输入卡号：")
                target_account = bank.get_account(target_cardid, None, True)
                if target_account:
                    money = get_float_input("请输入金额：")
                    account.transfer(target_account, round(money, 2))

        elif ins == "7":
            break

        else:
            print("请输入1~7的数字")

if __name__ == '__main__':
    main()

```



### 内置默认方法：运算

```python
# 内置默认方法：运算
# bin() 转换为二进制
# 优先级：增强赋值 > 算数运算 > 反算数运算
# 算术运算
# __add()__    加法
from idlelib.colorizer import prog_group_name_to_tag


class S(str):
    # 自定义重写 __add__ 为字符串长度相加
    def __add__(self, other):
        return len(self) + len(other)
s1 = S("FishC")
s2 = S("Python")
print(s1 + s2) # 11
print(s1.__add__(s2) ) # 11
print(s1 + "python") # 11
print("FishC" + s2) # FishCPython

# ——————————————————————————————————————————————————
# 反算数运算
# __radd()__    相加时，左右对象属于不同类，且左侧对象没有自定义__add()__方法，
# 或者其自定义__add()__方法返回 NotImplemented ，那么python就会从右侧对象寻找__radd()__
# NotImplemented 明确表示 没有实现
class S1(str):
    def __add__(self, other):
        return NotImplemented

class S2(str):
    def __radd__(self, other):
        return len(self) + len(other)
s1 = S1("FishC")
s2 = S2("Python")
print(s1 + s2) # 11


# ——————————————————————————————————————————————————
# 增强赋值运算
# __iadd()__ ++
class S1(str):
    def __iadd__(self, other):
        return len(self) + len(other)
s1 = S1("FishC")
s1 += s2
print(s1, type(s1)) # 11 <class 'int'>

# ——————————————————————————————————————————————————
# __int()__
class ZH_INT:
    def __init__(self, num):
        self.num = num

    def __int__(self):
        try:
            return int(self.num)
        except ValueError:
            zh = {"零":0, "一":1, "二":2, "三":3, "四":4, "五":5, "六":6, "七":7, "八":8, "九":9,
                  "壹":1, "贰":2, "叁":3, "肆":4, "伍":5, "陆":6, "柒":7, "捌":8, "玖":9}
            result = 0

            for each in self.num:
                if each in zh:
                    result += zh[each]
                else:
                    result += int(each)
                result *= 10
            return result // 10
n = ZH_INT("五贰零1314")
print(int(n)) # 5201314

# ——————————————————————————————————————————————————
import math
print(0.1 + 0.2 == 0.3 + math.ulp(0.3)) # True
print(math.pi)
print(math.tau / 2)

# ——————————————————————————————————————————————————
# __index()__ 当对象被用于索引值时，或内置的 bin()、hex()、oct() 函数将使用该魔法方法的返回值作为参数；
class C:
    def __index__(self):
        print("拦截")
        # 以3作为索引值
        return 3
c = C()
s = "FishC"
print(s[c])
# 拦截
# h
print(int(c))
# 拦截
# 3
print(bin(c))
# 拦截
# 0b11



# ——————————————————————————————————————————————————
# 算术运算
# __add__(self, other)    x + y（由运算符左侧的对象 x 触发）    加法运算
# __sub__(self, other)    x - y（由运算符左侧的对象 x 触发）    减法运算
# __mul__(self, other)    x * y（由运算符左侧的对象 x 触发）    乘法运算
# __matmul__(self, other)    x @ y（由运算符左侧的对象 x 触发）    矩阵乘法运算
# __truediv__(self, other)    x / y（由运算符左侧的对象 x 触发）    真除法运算
# __floordiv__(self, other)    x // y（由运算符左侧的对象 x 触发）    地板除法运算
# __mod__(self, other)    x % y（由运算符左侧的对象 x 触发）    求余数运算
# __divmod__(self, other)    divmod(x, y)（由对象 x 触发）    获取两个数字参数（非复数）的地板除结果和余数
# __pow__(self, other[, modulo])    x ** y 或 pow(x, y)（由运算符左侧的对象 x 触发）    幂运算
# __lshift__(self, other)    x << y（由运算符左侧的对象 x 触发）    按位左移运算
# __rshift__(self, other)    x >> y（由运算符左侧的对象 x 触发）    按位右移运算
# __and__(self, other)    x & y（由运算符左侧的对象 x 触发）    按位与运算
# __xor__(self, other)    x ^ y（由运算符左侧的对象 x 触发）    按位异或运算
# __or__(self, other)    x | y（由运算符左侧的对象 x 触发）    按位或运算

# 反算术运算
# __radd__(self, other)    x + y（由运算符右侧的对象 y 触发）    加法运算
# __rsub__(self, other)    x - y（由运算符右侧的对象 y 触发）    减法运算
# __rmul__(self, other)    x * y（由运算符右侧的对象 y 触发）    乘法运算
# __rmatmul__(self, other)     x @ y（由运算符右侧的对象 y 触发）    矩阵乘法运算
# __rtruediv__(self, other)    x / y（由运算符右侧的对象 y 触发）    真除法运算
# __rfloordiv__(self, other)    x // y（由运算符右侧的对象 y 触发）    地板除法运算
# __rmod__(self, other)    x % y（由运算符右侧的对象 y 触发）    求余数运算
# __rdivmod__(self, other)    divmod(x, y)（由对象 y 触发）    获取两个数字参数（非复数）的地板除结果和余数
# __rpow__(self, other[, modulo])    x ** y 或 pow(x, y)（由运算符右侧的对象 y 触发）    幂运算
# __rlshift__(self, other)    x << y（由运算符右侧的对象 y 触发）    按位左移运算
# __rrshift__(self, other)    x >> y（由运算符右侧的对象 y 触发）    按位右移运算
# __rand__(self, other)    x & y（由运算符右侧的对象 y 触发）    按位与运算 存在0即0
# __rxor__(self, other)    x ^ y（由运算符右侧的对象 y 触发）    按位异或运算 不同即1
# __ror__(self, other)    x | y（由运算符右侧的对象 y 触发）    按位或运算 存在1即1

# 增强赋值运算
# __iadd__(self, other)    x += y（由运算符左侧的对象 x 触发）    加法运算
# __isub__(self, other)    x -= y（由运算符左侧的对象 x 触发）    减法运算
# __imul__(self, other)    x *= y（由运算符左侧的对象 x 触发）    乘法运算
# __imatmul__(self, other)    x @= y（由运算符左侧的对象 x 触发）    矩阵乘法运算
# __itruediv__(self, other)    x /= y（由运算符左侧的对象 x 触发）    真除法运算
# __ifloordiv__(self, other)    x //= y（由运算符左侧的对象 x 触发）    地板除法运算
# __imod__(self, other)    x %= y（由运算符左侧的对象 x 触发）    求余数运算
# __ipow__(self, other[, modulo])    x **= y（由运算符左侧的对象 x 触发）    幂运算
# __ilshift__(self, other)    x <<= y（由运算符左侧的对象 x 触发）    按位左移运算
# __irshift__(self, other)    x >>= y（由运算符左侧的对象 x 触发）    按位右移运算
# __iand__(self, other)    x &= y（由运算符左侧的对象 x 触发）    按位与运算
# __ixor__(self, other)    x ^= y（由运算符左侧的对象 x 触发）    按位异或运算
# __ior__(self, other)    x |= y（由运算符左侧的对象 x 触发）    按位或运算

# 一元运算
# __neg__(self)    -x    取相反数运算
# __pos__(self)    +x    正数运算
# __abs__(self)    abs(x)    取绝对值
# __invert__(self)    ~x    按位非（按位取反）运算

# 其他运算
# __complex__(self)    complex(x)
# __int__(self)    int(x)
# __float__(self)    float(x)
#  __index__(self)    index(x)    当对象被用于索引值时，或内置的 bin()、hex()、oct() 函数将使用该魔法方法的返回值作为参数；
# 如果没有定义 __complex__()、__int__()、__float__()，则相应的 complex()、int()、float() 函数将使用该魔法方法的返回值作为参数
# __round__(self[, ndigits])    round(x)
# __trunc__(self)    math.trunc(x)
# __floor__(self)    math.floor(x)
# __ceil__(self)     math.ceil(x)

```



#### 自定义int,float

```python
# 自定义int,float
# 支持中文数字，及浮点数
from string import digits

class ZH_INT:
    def __init__(self, num):
        self.num = num

    def __int__(self):
        try:
            return int(self.num)
        except ValueError:
            units = {"十": 10, "拾": 10, "百": 100, "佰": 100, "千": 1000, "仟": 1000,
                     "万": 10000, "萬": 10000, "亿": 100000000, "億": 100000000}
            digits = {"零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6,
                      "七": 7, "八": 8, "九": 9, "壹": 1, "贰": 2, "叁": 3, "肆": 4,
                      "伍": 5, "陆": 6, "柒": 7, "捌": 8, "玖": 9, "两": 2}

            unit = 0  # 初始单位
            section = []  # 存放字符串拆解后的数据片段
            temp = 0  # 临时变量

            for i in range(len(self.num)-1, -1, -1):
                char = self.num[i]
                if char in units:
                    unit = units[char]
                    # 万和亿需要单独存储，因为需要考虑处理一百万，十亿这类重复单位的数字
                    if unit == 10000 or unit == 100000000:
                        section.append(unit)
                        units = 1
                elif char in digits:
                    temp = digits[char]
                    # 如果有单位，则乘以单位代表的数值
                    if unit:
                        temp *= unit
                        unit = 0
                    section.append(temp)
                else:
                    raise ValueError(f"[{char}]是无效字符。")

            # “十”要单独处理，因为我们不会说“一十五”，而是习惯直接说“十五”
            # 而对于百、千、万，我们会说是“一百”，“一千”或者“一百万”
            if unit == 10:
                section.append(10)

            # 接下来将数据片段拼接起来即可
            result = 0
            temp = 0

            for each in reversed(section):
                if each == 10000 or each == 100000000:
                    result += temp * each
                    temp = 0
                else:
                    temp += each
            result += temp

            return result


class ZH_FLOAT:
    def __init__(self, num):
        self.num = num

    def __float__(self):
        units = {"十": 10, "拾": 10, "百": 100, "佰": 100, "千": 1000, "仟": 1000,
                 "万": 10000, "萬": 10000, "亿": 100000000, "億": 100000000}
        digits = {"零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6,
                  "七": 7, "八": 8, "九": 9, "壹": 1, "贰": 2, "叁": 3, "肆": 4,
                  "伍": 5, "陆": 6, "柒": 7, "捌": 8, "玖": 9, "两": 2}

        # 处理整数部分
        def process_integer_part(n):
            unit = 0  # 初始单位
            section = []  # 存放字符串拆解后的数据片段
            temp = 0  # 临时变量

            for i in range(len(n) - 1, -1, -1):
                char = n[i]
                if char in units:
                    unit = units[char]
                    # 万和亿需要单独存储，因为需要考虑处理一百万，十亿这类重复单位的数字
                    if unit == 10000 or unit == 100000000:
                        section.append(unit)
                        unit = 1
                elif char in digits:
                    temp = digits[char]
                    # 如果有单位，则乘以单位代表的数值
                    if unit:
                        temp *= unit
                        unit = 0
                    section.append(temp)
                else:
                    raise ValueError(f"[{char}]是无效字符。")

            # “十”要单独处理，因为我们不会说“一十五”，而是习惯直接说“十五”
            # 而对于百、千、万，我们会说是“一百”，“一千”或者“一百万”
            if unit == 10:
                section.append(10)

            # 接下来将数据片段拼接起来即可
            result = 0
            temp = 0

            for each in reversed(section):
                if each == 10000 or each == 100000000:
                    result += temp * each
                    temp = 0
                else:
                    temp += each

            result += temp
            return result

        # 处理小数部分
        def process_decimal_part(d):
            result = 0
            # 0.2 = 2 * 10**(-1)
            # 0.25 = 2 * 10**(-1) + 5 * 10**(-2)
            # ...
            for i, char in enumerate(d):
                if char in digits:
                    result += digits[char] * (10 ** (i + 1))
                else:
                    try:
                        result += int(char) * (10 ** (i + 1))
                    except ValueError:
                        raise ValueError(f"[{char}]是无效字符。")

            return result

        try:
            return float(self.num)
        except ValueError:
            if "点" in self.num:
                integer_part, decimal_part = self.num.split("点", 1)
            elif "點" in self.num:
                integer_part, decimal_part = self.num.split("點", 1)
            else:
                # 如果没有小数点则直接当作整数处理完返回
                return process_integer_part(self.num)

            integer_result = process_integer_part(integer_part)
            decimal_result = process_decimal_part(decimal_part)

            return float(integer_result + decimal_result)

```



#### 自定义 一进制 与 电影票订购系统

```python
# 自定义 一进制 与 电影票订购系统
# 重载加（+）、减（-）、乘（*）、除（/）、地板除（//）五个运算符（为了简化实现逻辑，我们约定无论除法还是地板除，都统一采用地板除，即不考虑小数位）
from warnings import resetwarnings


class UnaryNumber:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value < 0:
            return '-' + '1' * abs(self.value)
        elif self.value == 0:
            return "没有"
        else:
            return '1' * self.value

    def __int__(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, UnaryNumber):
            return UnaryNumber(self.value + other.value)
        else:
            raise ValueError("类型不同无法相加")

    def __sub__(self, other):
        if isinstance(other, UnaryNumber):
            return UnaryNumber(self.value - other.value)
        else:
            raise ValueError("类型不同无法相减")

    def __mul__(self, other):
        if isinstance(other, UnaryNumber):
            return UnaryNumber(self.value * other.value)
        else:
            raise ValueError("类型不同无法相乘")

    def __truediv__(self, other):
        if isinstance(other, UnaryNumber):
            if other.value != 0:
                return UnaryNumber(self.value // other.value)
            else:
                raise ValueError("除数不能为0")
        else:
            raise ValueError("类型不同无法相除")

    def __floordiv__(self, other):
        if isinstance(other, UnaryNumber):
            if other.value != 0:
                return UnaryNumber(self.value // other.value)
            else:
                raise ValueError("除数不能为0")
        else:
            raise ValueError("类型不同无法相除")

x = UnaryNumber(3)
y = UnaryNumber(5)
print(x, y) # 111 11111
print(x + y) # 11111111
print(x * y) # 111111111111111
print(x // y) # 没有


# ——————————————————————————————————————————————————
# 电影票订购系统
# 需要实现的功能：
# 查看信息
# 预订座位
# 查看预订
#
# 推荐实现方案（当然你也可以按照自己的思路来定义）：
# a. 电影院（Cinema）：用于管理电影的添加和信息呈现
# 添加电影和播放时间（add_movie）
# 显示所有电影及其播放时间（show_movies）
#
# b. 座位（Seat）：用于管理座位
# 管理座位是否被预定（reserve）
#
# c. 预订系统（MovieBookingSystem）：用于管理预定信息
# 预定座位操作（reserve_seat）
# 查看预订信息（view_reservation）

# 定义电影类
class Cinema:
    def __init__(self, movie_name):
        self.movie_name = movie_name
        self.movies = {}

    # 添加电影名，电影时间
    def add_movie(self, movie_name, schedule):
        self.movies[movie_name] = schedule

    #  展示电影时间
    def show_movies(self):
        for movie_name, schedule in self.movies.items():
            print(f"{movie_name}")
            for date, times in schedule:
                print(f"{date}: {', '.join(times)}")

# 定义座位类
class Seat:
    def __init__(self, row, number):
        self.row = row          # 座位所在的排数
        self.number = number    # 座位号
        self.reserved = False   # 标志一个座位是否被预定

    # 预定座位
    def reserve(self):
        if not self.reserved:
            self.reserved = True
        else:
            raise ValueError("该座位已被预定。")

class MovieBookingSystem:
    def __init__(self, cinema, rows, seats_per_row):
        self.cinema = cinema
        self.reservations = {}  # 存储预订信息的字典

        # 创建座位实例并存储到字典中
        self.seats = {f"{row + 1}-{seat + 1}": Seat(row + 1, seat + 1) for row in range(rows) for seat in range(seats_per_row)}

    # 预订座位
    def reserve_seat(self, movie_name, date, time, seat_id):
        key = (movie_name, date, time)
        seat = self.seats.get(seat_id)

        # 如果位置不存在抛出异常
        if not seat:
            raise ValueError("无效的座位号")

        # 如果预订信息不存在，创建新的预订信息
        if key not in self.reservations:
            self.reservations[key] = []

        # 如果座位未被预定，预定座位并添加到预定信息
        if seat not in self.reservations[key]:
            seat.reserve()
            self.reservations[key].append(seat)
        else:
            raise ValueError("该座位已被预定。")

    # 查看座位信息
    def view_reservation(self, movie_name, date, time):
        key = (movie_name, date, time)
        return self.reservations.get(key, [])

def dispaly_menu():
    print("欢迎来到电影票订购系统")
    print("1. 查看电影")
    print("2. 预订座位")
    print("3. 查看预订")
    print("4. 退出系统")

# 获取用户输入
def user_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\n谢谢使用！")
        exit(0)

def main():
    # 创建电影院实例并添加电影
    cinema = Cinema("鱼C影院")
    cinema.add_movie("《小甲鱼的救赎》", {"2023-07-20": ["14:00", "18:00"]})
    cinema.add_movie("《不二如是的假日》", {"2023-07-20": ["16:00", "20:00"]})

    # 创建预定实例
    booking_system = MovieBookingSystem(cinema, 10, 10)

    while True:
        dispaly_menu()
        choice = user_input("请输入操作指令：")

        # 查看电影
        if choice == "1":
            print("电影时间表 >>>")
            cinema.show_movies()

        # 预定座位
        elif choice == "2":
            movie_name = user_input("请输入电影名称")
            data = user_input("请输入日期（年-月-日）：")
            time = user_input("请输入时间（时：分）：")
            seat_id = user_input("请输入座位号（排数-座位号）")

            try:
                booking_system.reserve_seat(movie_name, data, time, seat_id)
                print("预定成功！\n")
            except ValueError as e:
                print(f"预定失败：{e}\n")

        # 查看预定
        elif choice == "3":
            movie_name = user_input("请输入电影名称")
            data = user_input("请输入日期（年-月-日）：")
            time = user_input("请输入时间（时：分）：")

            reserved_seat = booking_system.view_reservation(movie_name, data, time)
            if reserved_seat:
                print("预定的座位：")
                for seat in reserved_seat:
                    print(f"{seat.row}排，{seat.number}号")
            else:
                print("没有预定的座位。")
            print()

        # 退出系统
        elif choice == "4":
            print("谢谢使用！")
            break

        # 无效选择处理
        else:
            print("无效选择，请输入1~4之间的数字。\n")

if __name__ == "__main__":
    main()

```



### 内置属性方法

```python
# 内置属性方法
# hasattr(ob, str) 是否有 str 这个属性
# getattr(ob, str) 获取 str 这个属性  __getattribute__()
# __getattr__() 当获取不存在的属性时触发
# setattr(ob, str) 给 str 这个属性赋值 __setattr__()
# delattr(ob, str) 删除 str这个属性 __delattr__()
class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # __age 私有变量

c = C("小甲鱼", 18)
print(hasattr(c, "name")) # True
print(getattr(c, "name")) # 小甲鱼
print(getattr(c, "_C__age")) # 18
setattr(c, "_C__age", 19)
print(getattr(c, "_C__age")) # 19
delattr(c, "_C__age")
print(hasattr(c, "_C__age")) # False

# ——————————————————————————————————————————————————————
# __getattribute__()
class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __getattribute__(self, attrname):
        print("截取")
        return super().__getattribute__(attrname)

c = C("小甲鱼", 18)
print(getattr(c, "name"))
# 截取
# 小甲鱼

# ——————————————————————————————————————————————————————
# __getattr__() 当获取对象不存在时触发
class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __getattribute__(self, attrname):
        print("截取")
        return super().__getattribute__(attrname)

    def __getattr__(self, attrname):
        if attrname == "FishC":
            print("I love FishC")
        else:
            raise AttributeError(attrname)
c = C("小甲鱼", 18)
print(c.FishC)
# 截取
# I love FishC
# None
print(c.name)
# 截取
# 小甲鱼

# ——————————————————————————————————————————————————————
# __setattr__()
class D:
    def __setattr__(self, name, value):
        self.__dict__[name] = value
d = D()
d.name = "小甲鱼"
print(d.name) # 小甲鱼

class D:
    def __setattr__(self, name, value):
        return super().__setattr__(name, value)
d = D()
d.name = "小甲鱼"
print(d.name) # 小甲鱼

# ——————————————————————————————————————————————————————
# __delattr__()
class D:
    def __setattr__(self, name, value):
        self.__dict__[name] = value
    def __delattr__(self, name):
        del self.__dict__[name]
d = D()
d.name = "小甲鱼"
del d.name
print(d.__dict__) # {}

```



#### 文件管理类

```python
# 文件管理类
# 定义一个名为 FileManager 的类，该类可以实现简单的文件管理功能，包括浏览目录、创建文件、重命名文件和删除文件。
# 提示：调用 pathlib 模块中的一些方法，来实现你目前不知道如何实现的文件管理操作
from pathlib import Path
class FileManager:
    def __init__(self, path=r"D:\临时\test"):
        self.path = Path(path)

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        else:
            raise AttributeError(f"{self.__class__.__name__} 对象没有 '{attr}' 属性")

    def __setattr__(self, attr, value):
        if attr == "path":
            object.__setattr__(self, attr, value)
        else:
            setattr(self, attr, value)

    def __delattr__(self, attr):
        if hasattr(self, attr):
            object.__delattr__(self, attr)
        else:
            raise AttributeError(f"{self.__class__.__name__} 对象没有 '{attr}' 属性")


    def browse(self):
        for i in self.path.iterdir():
            print(i.name)

    def create(self, path):
        n = self.path / path
        if not n.exists():
            n.touch()
        else:
            print(f"文件 '{n}' 已存在。")

    def rename(self, old_path, new_path):
        old_path = self.path / old_path
        new_path = self.path / new_path
        if old_path.exists() and not new_path.exists():
            old_path.rename(new_path)
        else:
            print(f"错误：'{old_path}' 不存在或 '{new_path}' 已存在。")

    def delete(self, file_path):
        file_path = self.path / file_path
        if file_path.is_file():
            file_path.unlink()
        elif file_path.is_dir():
            for i in file_path.glob("*"):
                self.delete(i.relative_to(self.path))
            file_path.remove(file_path)
        else:
            print(f"文件 '{file_path}' 未找到。")

fm = FileManager()
fm.browse()
fm.create("test.txt")
fm.browse()

from pathlib import Path

class FileManager:
    def __init__(self, path="."):
        self.path = Path(path)

    def __getattr__(self, attr):
        if attr == 'size':
            return self.get_size()
        else:
            raise AttributeError(f"{self.__class__.__name__} 对象没有 '{attr}' 属性")

    def __setattr__(self, attr, value):
        if attr == "path":
            object.__setattr__(self, attr, Path(value))
        else:
            object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        if hasattr(self, attr):
            object.__delattr__(self, attr)
        else:
            raise AttributeError(f"{self.__class__.__name__} 对象没有 '{attr}' 属性")

    def get_size(self, file_name=None):
        if file_name:
            file_path = self.path / file_name
            if file_path.is_file():
                return file_path.stat().st_size
            else:
                raise FileNotFoundError(f"文件 '{file_name}' 未找到。")
        else:
            total_size = 0
            for entry in self.path.glob('**/*'):
                if entry.is_file():
                    total_size += entry.stat().st_size
            return total_size

    def browse(self, recursive=False, sort_by=None, reverse=False):
        try:
            if recursive:
                for entry in sorted(self.path.glob('**/*'), key=sort_by, reverse=reverse):
                    print(entry.relative_to(self.path))
            else:
                for entry in sorted(self.path.iterdir(), key=sort_by, reverse=reverse):
                    print(entry.name)
        except Exception as e:
            print(f"浏览文件时出错: {e}")

    def create_file(self, file_name):
        try:
            file_path = self.path / file_name
            if not file_path.exists():
                file_path.touch()
            else:
                print(f"文件 '{file_name}' 已存在。")
        except Exception as e:
            print(f"创建文件时出错: {e}")

    def create_directory(self, dir_name):
        try:
            dir_path = self.path / dir_name
            if not dir_path.exists():
                dir_path.mkdir(parents=True)
            else:
                print(f"文件夹 '{dir_name}' 已存在。")
        except Exception as e:
            print(f"创建文件夹时出错: {e}")

    def delete(self, file_name):
        try:
            file_path = self.path / file_name
            if file_path.is_file():
                file_path.unlink()
            elif file_path.is_dir():
                for child in file_path.glob('*'):
                    self.delete(child.relative_to(self.path))
                file_path.rmdir()
            else:
                print(f"文件 '{file_name}' 未找到。")
        except Exception as e:
            print(f"删除文件时出错: {e}")

    def rename(self, old_name, new_name):
        try:
            old_path = self.path / old_name
            new_path = self.path / new_name
            if old_path.exists() and not new_path.exists():
                old_path.rename(new_path)
            else:
                print(f"错误: '{old_name}' 未找到 或 '{new_name}' 已存在。")
        except Exception as e:
            print(f"重命名文件时时出错: {e}")

    def search(self, pattern):
        try:
            for entry in self.path.glob(f"**/{pattern}"):
                print(entry.relative_to(self.path))
        except Exception as e:
            print(f"搜索文件时出错: {e}")


def main():
    fm = FileManager()
    while True:
        try:
            command = input("输入命令（1.浏览/2.创建文件/3.创建文件夹/4.删除/5.重命名/6.搜索/7.退出）：")
            if command == "1":
                recursive = input("递归浏览? (y/n): ").lower() == "y"
                fm.browse(recursive=recursive)
            elif command == "2":
                file_name = input("输入文件名: ")
                fm.create_file(file_name)
            elif command == "3":
                dir_name = input("输入文件夹名: ")
                fm.create_directory(dir_name)
            elif command == "4":
                file_name = input("输入文件或文件夹名: ")
                fm.delete(file_name)
            elif command == "5":
                old_name = input("输入旧文件或文件夹名: ")
                new_name = input("输入新文件或文件夹名: ")
                fm.rename(old_name, new_name)
            elif command == "6":
                pattern = input("输入搜索模式: ")
                fm.search(pattern)
            elif command == "7":
                break
            else:
                print("无效命令，请重试。")
        except KeyboardInterrupt:
            print("中断。退出。")
            break
        except Exception as e:
            print(f"错误: {e}")

main()

```




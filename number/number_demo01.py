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

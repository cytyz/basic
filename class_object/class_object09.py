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

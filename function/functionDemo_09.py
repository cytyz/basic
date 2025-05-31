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

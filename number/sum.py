i = 0
sum = 0
s = 1000000
while i <= s:
    if i % 2 == 0:
        sum += i
    i = i + 1
print(s, "以内的所有偶数的和是", sum)

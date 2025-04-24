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

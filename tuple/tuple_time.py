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

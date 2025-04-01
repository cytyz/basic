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
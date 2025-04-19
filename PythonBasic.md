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


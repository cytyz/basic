#交换变量值
x = 3
y = 5
x, y = y, x
print(x, y)
#5 3

#文本序列需要用''或""或'''   '''包括起来，在''或""其中的''或""前可加转义字符\，使得Python可以正确识别
print("I Love China!")
#I Love China!
print('"Life is short, you need Python"')
#"Life is short, you need Python"
print('"Life is short, let\'s learn Python."')
#"Life is short, let's learn Python."
print('"I love Python, \nI Love FishC"')
#I love Python,
#I Love FishC

#当需要传入路径时，路径中每个层级前都需要添加一个转义字符\，或者在其前添加r表示后面的为原始字符
print("D:\\three\\two\\one\\now")
#D:\three\two\one\now
print(r"D:\three\two\one\now")
#D:\three\two\one\now
#(IDLE特别注意)\不能放在末尾，每行行末的\是为了可以用回车键转到下一行，如果没有\直接回车，Python会直接运行

#变量值相加相乘
print(520 + 1314)
#1834
print('520'+'1314')
#'5201314'   字符串相加->拼接
print("我每天爱你三千遍!"*3000)
#我每天爱你三千遍!我每天爱你三千遍!我每天爱你三千遍!……

#字符串转换为数字 int(), float转为int时忽略后面小数
print(int('123') + 256)
#379
#数字转化为字符串 str()
print('123' + str(256))
# 123256

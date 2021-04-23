#range的三种创建方式
r=range(10) #默认从0开始，间隔1步长
print(r) #输出range(0,10)
print(list(r)) #查看range中的序列

r=range(1,10) #指定了range的起始位置和终止位置
print(list(r))

r=range(1,10,2)
print(list(r))

print('------------------判断整数是否在序列中-------------------')
print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)



print('---------------元组的创建-----------------')
'''使用（）'''
t=('hello','world',98)
print(t,type(t))

'''省略()'''
t='hello','world',98 #多个元素可以省略小括号
print(t,type(t))

t=('hello',) #只有一个元素时，需要加小括号与逗号
print(t,type(t))

'''使用内置函数'''
t=tuple(('hello','world',98)) #类似于数据类型转换
print(t,type(t))



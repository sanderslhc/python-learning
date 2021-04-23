#转义字符
print('hello\nworld') #换行
print('hello\tworld') #空格
print('hello\bworld') #退一格
print('hello\rworl') #重头输入，覆盖前文

print('http:\\\\baidu.com')
print('\'大家好\'')

print(r'hello\nworld') #原字符r/R，不希望转义字符起作用，而是输出本来意思
#注意，最后结尾不能是\
print(r'hello\nworld\\')

n1=90
print(n1,type(n1))
##
n2=1.1
n3=2.2
print(n2+n3)


x1='''我是
         XXX'''
print(x1)

name='张三'
age=88
print('我叫'+name+'今年'+str(age)+'岁') #str进行数据转化成字符型
print('-----------------字符串的替换与合并--------------')
s='hello python'
print(s.replace('python','Java')) #用Java替换

s1='hello python python'
print(s1.replace('python','Java',2)) #设置最大替换次数

lst=['hello','java','python']
print('|'.join(lst)) #用|连接列表元素
print(''.join(lst)) #默认直接连接

t=('hello','java','python') #连接元组元素
print('|'.join(t))

print('|'.join('python')) #字符串内连接


print('--------------字符串的分割-----------------')
s='hello world python'
print(s.split()) #默认以空格为分隔符
s1='hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1)) #设置最大分割次数

#rsplit从右开始分割
print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|',maxsplit=1))
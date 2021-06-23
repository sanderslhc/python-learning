print('------------字符串转化-------------------')
s='lihoucheng'
a=s.upper() #全部字符转化为大写
print(a,id(a))
print(s,id(s))

b=s.lower() #所有字符转化为小写
print(b,id(b)) #不论字符串在转化后有没有发生变化，其内存地址都会改变
prit(s,id(s))

c=s.swapcase() #大写转小写，小写转大写

d=s.capitalize() #第一个字符转大写，其余的都转小写

e=s.title() #每一个单词的第一个字符转大写，其余的转小写


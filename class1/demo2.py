print("-----------------算数运算符--------------------")
print(1+1)
print(2*2)
print(2/1)
print(5//2)
print(2**3)
print(5%2)
#一正一负整除向下取整
print(-9//4)
print(9//-4)
#余数=被除数-除数*商
print(9%-4)
print(-9%4)

print("---------------------赋值运算符---------------------")
a=b=c=20 #链式赋值
print(a,id(a),b,id(b),c,id(c))
a=20
a+=30
print(a)
a-=10
print(a)
a*=2
print(a,type(a))
a/=3
print(a,type(a))
a//=2
print(a,type(a))
a%=3
print(a,type(a))

a,b,c=1,2,3
print(a,b,c,id(a),id(b),id(c))
a,b=b,a
print(a,b)

print('----------------------比较运算符------------------------')
a,b=10,20
print(a==b) #数值相等
print(a>=b)
print(a<=b)
print(a!=b)
print(a is b) #id相同
print(a is not b)

lst1=[11,22,33]
lst2=[11,22,33]
print(lst1==lst2)
print(lst1 is lst2)
print(id(lst1),id(lst2))

print('-------------------布尔运算符------------------------------')
a,b=1,2
print(a==1 and b==2)
print(a==1 and b!=2)
print(a==1 or b!=2)
print(a!=1 or b!=2)

print('-------------------in 和not in----------------------------')
s='Hello'
print('H' in s)
print('h' in s)
print('H' not in s)
print('h' not in s)

print('--------------------位运算符------------------------------')
#依据二进制运算
#4（十进制）  00000100（二进制）
#8（十进制）  00001000（二进制）
#12         00001100
#0          00000000
print(4&8) #按位 与& 同为1时才为1
print(4|8) #按位 或| 同为0时才为0
print(4<<1) #二进制值向左移1位 相当于乘以2
print(4>>1) #二进制值向右移1位 相当于除以2

#运算符优先级
#赋值<布尔<比较<位运算<算数(幂运算>乘除>加减)

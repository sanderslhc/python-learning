a=0
b=0
 #判断条件表达式
while a<5:
    b+=a
    a+=1
print(b)

a=0
b=0
while a<=100:
    b+=a
    a+=2
print(b)

a=1
b=0
while a<=100:
    if a%2==0:
        b+=a
    a+=1
print(b)

a=1
b=0
while a<=100:
    if a%2: #为什么自动默认为True？？？
        b+=a
    a+=1
print(b)


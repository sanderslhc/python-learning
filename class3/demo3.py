for i in range(10):
    print(i)

for _ in range(5):
    print('我爱猫猫')

b=0
for a in range(1,101):
    if a%2==0:
        b+=a
print(b)

for a in range(100,999):
    if a==(a//100)*(a//100)*(a//100)+(a//10-a//100*10)*(a//10-a//100*10)*(a//10-a//100*10)+(a%10)*(a%10)*(a%10):
        print(a)
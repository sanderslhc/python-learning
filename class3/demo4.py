'''从键盘录入密码，达到三次就不录入'''
for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('对不起，账户已锁定')

i=0
while i<3:
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
    i+=1
else:
    print('对不起，账户已锁定')
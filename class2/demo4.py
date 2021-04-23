#嵌套语句
answer=input('您是会员吗？是/否')
money=float(input('请输入您的购物金额：'))
#外层判断是否是会员
if answer=='是':
    if money>=200:
        print('付款金额为：',money*0.8)
    elif 200>=money>=100:
        print('付款金额为：',money*0.9)
    else:
        print('付款金额为：',money)
else:
    if money>=200:
        print('付款金额为：',money*0.9)
    else:
        print('付款金额为：',money)
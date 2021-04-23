print('---------------遍历列表元素-----------------')
lst=[10,20,30,40]
for i in lst:
    print(i)

print('--------------添加元素------------------')
lst=[10,20,30]
print('添加元素之前',lst,id(lst))
lst.append(100) #在列表末尾添加一个元素
print('添加元素之后',lst,id(lst))

lst2=[11,22]
lst.append(lst2)
print(lst)
lst.extend(lst2) #添加多个元素
print(lst)

lst.insert(1,90) #指定位置插入元素
print(lst)

lst3=['hello']
lst[1:3]=lst3 #在列表指定位置替换元素
print(lst)


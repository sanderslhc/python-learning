print('-------------------列表元素的删除-------------------')
lst=[10,20,30,30,40,50,60,30]
lst.remove(30) #从列表中移除一个元素，若有重复则移除第一个
print(lst)

lst.pop(1)
print(lst)
lst.pop() #不指定则删除列表最后一个元素
print(lst)

lst[1:3]=[] #用空列表覆盖1:3的元素
print(lst)

lst[1]=100 #列表元素的替换
print(lst)

lst.clear() #清空列表元素
print(lst)

del lst #删除列表



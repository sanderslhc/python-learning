lst=[10,50,20,30,80]
print(lst,id(lst))
#对列表进行排序，默认升序
lst.sort()
print(lst,id(lst))

#降序排序
lst.sort(reverse=True)
print(lst)

print('--------------使用内置函数排序----------------')
lst1=sorted(lst) #将产生新的列表对象
print(lst1)
lst1=sorted(lst,reverse=True)
print(lst1)
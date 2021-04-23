#字典常用操作
scores={'张三':12,'李四':22,'王五':44}
s1=scores.keys()
print(s1,type(s1))
print(list(s1)) #将所有的keys存到列表中

#获取所有的values
values=scores.values()
print(values)
print(type(values))
print(list(values))

#获取所有的key-value对
items=scores.items()
print(items,type(items))
print(list(items))
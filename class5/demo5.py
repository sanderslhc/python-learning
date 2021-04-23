print('-----------------字典元素的遍历------------------')
scores={'张三':12,'李四':22,'王五':44}
for item in scores:
    print(item,scores[item],scores.get(item))

print('----------------------字典特点----------------------------')
d={'name':'张三','name':'李四'} #key不允许重复
print(d)
d={'name':'张三','nikename':'张三'} #value可以重复
print(d)

lst=[10,20,30]
lst.insert(1,100) #字典无法指定位置插入，因为是无序的
print(lst)





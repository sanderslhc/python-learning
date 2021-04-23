print('--------------------字典获取元素----------------------')
scores={'张三':12,'李四':22,'王五':44}
#使用[]
print(scores['张三'])

#使用get()
print(scores.get("张三"))
print(scores.get("里屋"))
print(scores.get('里屋',12)) #当查找的key不存在时，可以靠value来定位，但不能直接靠value定位


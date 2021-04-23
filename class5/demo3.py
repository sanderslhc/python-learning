#key的判断
scores={'张三':12,'李四':22,'王五':44}
print('张三' in scores)
print('张三' not in scores)

del scores['张三'] #删除指定key的value值
scores['陈留']=98 #添加新元素
print(scores)
scores.clear()
print(scores)


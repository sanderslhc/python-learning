print('-------------------获取元素索引-------------------')
lst=['hello',84,'world']
print(lst.index('hello')) #列表中有相同元素，只返回第一个的索引
print(lst.index('python')) #不存在的元素会报错
print(lst.index())
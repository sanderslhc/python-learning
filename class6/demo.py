print('-----------------可变序列与不可变序列-------------------------')
'''可变序列：列表，字典(可以在id不变的情况下增减元素)'''
lst=[1,3,4]
print(lst,id(lst))
lst.append(2)
print(lst,id(lst))

'''不可变序列：字符串，元组（增减元素id会改变）'''
s='hello'
print(s,id(s))
s=s+'world'
print(s,id(s))



print('----------------字典生成式------------------')
items=['Fruits','books','others']
prices=[44,43,22,66,77]
d={item:price   for item,price in zip(items,prices) }
print(d)
d={item.upper():price   for item,price in zip(items,prices) }
print(d)


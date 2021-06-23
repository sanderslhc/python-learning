print('-----------------字符串的对齐操作-----------------')
s='hello.python'
print(s.center(20,'*')) #长度20居中，用*填充
print(s.center(20)) #默认空格填充
print(s.center(10)) #长度小于原字符串，则返回原字符串

print(s.ljust(20,'*')) #长度20居左对齐
print(s.ljust(20))

print(s.rjust(20,'&')) #长度20居右对齐
print(s.rjust(20))

print(s.zfill(20)) #居右用0填充



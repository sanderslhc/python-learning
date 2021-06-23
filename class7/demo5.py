print('1.','hello,'.isidentifier()) #判断字符串是否是合法的标识符
print('2.','hello'.isidentifier())

print('3.','/t'.isspace()) #判断字符串里面是否都是空白值-回车，换行和水平制表符

print('4.','hello'.isalpha()) #判断字符串是否都是由字母组成

print('5.','123'.isdecimal()) #判断字符串是否都是由十进制数字组成
print('6.','123四'.isdecimal())

print('7.','123四'.isnumeric()) #是否由数字组成(任意形式)

print('8.','abc1张三'.isalnum()) #是否都是由数字和字母组成

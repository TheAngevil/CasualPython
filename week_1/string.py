# string
# 字串
print ('Hi')
print ("Hi")

#f-string
#格式化字串，以往使用%s，f-string比format更為方便
a = 3
b = 2
name = 'Chloe'
age = '26'
print (f"{a} plus {b} = {a+b} ")
print (f'Hi, My name is {name}, I am {age} years old.')
print ('Hi, My name is {}, I am {} years old.'.format(name, age))  #format用法

#r-string (raw string)
#針對字串內的斜線使用\
#以空格符號\n為例，不加r的話\n等於換行，加r將顯示完整字串
print ('ABC\nDEF') 
print (r'ABC\nDEF')
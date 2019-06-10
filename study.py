# -*- coding: utf-8 -*-
flag = False
if flag:
    print "True"
else:
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday']
    print "False"+ " "\
     "False"

print  days


#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

# 第一个注释

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

#!/usr/bin/python
print "Hello, Python!"  # 第二个注释

# raw_input("按下 enter 键退出，其他任意键显示...\n")

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y

print x,y

x=8;

if x>9 :
    print 111111
else:
    print  22222


var1 = 10.0
var2 = 20

print var1

del  var1

str = "0123456789"
print str[1:10:2]
print len(str)

tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print tuple
print tuple[1]
print tuple[0:4]


tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print  dict['one']
print dict[2]
print dict.keys()
print dict.values()
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

print int('12',16)
print complex(1)
print complex(1,2)
cpl = complex(2,4)

print cpl


print "max(80, 100, 1000) : ", max(80, 100, 1000)
print "max(-20, 100, 400) : ", max(-20, 100, 400)
print "max(-80, -20, -10) : ", max(-80, -20, -10)
print "max(0, 100, -400) : ", max(0, 100, -400)

tx = (1, 21, 88, 27, 99, 1827, 21, 908, 222)

print max(tx)


a='1,2,3,4'
print type(a)

print 2**5
a = 9
a **=6
print a

a = 10;

if a > 10000:
    print chr(a)+"比你打"
else:
    print chr(a)+"比你小"

print "比你小111"

print ord("Z")



count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"



for letter in 'Python':  # 第一个实例
    print '当前字母 :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print '当前水果 :', fruit,fruit

print "Good bye!"

print letter

for i in range(len(fruits)):
    print "当前水果:",fruits[i]


for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
          print num, '是一个质数'


for y in range(10,100):
    print "y is ",y
    for x in range(1,y):
        if x<20:
            print x,"--"
        else:
            print x
            break
    else:
        print "循环结束x:",x
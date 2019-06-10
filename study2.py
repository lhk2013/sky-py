# -*- coding: UTF-8 -*-
import time
import calendar


print time.time()

print time.localtime(time.time())

print time.asctime(time.localtime(time.time()))

print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
s = time.strptime("2019-02-19 10:22:19","%Y-%m-%d %H:%M:%S");
print "time is ",s

time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())


a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
print time.mktime(s)





cal = calendar.month(time.localtime().tm_year, time.localtime().tm_mon)
print "以下输出%d年%d月份的日历:" % (time.localtime().tm_year,time.localtime().tm_mon)
print cal


import datetime
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

def printme( str ):
   "打印传入的字符串到标准显示设备上"
   print str
   return

printme("我要调用用户自定义函数!");
printme("再次调用同一函数");


def ChangeInt(x):
    x = 10


b = 2
ChangeInt(b)
print b  # 结果是 2


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist

def changeMy(name=35,id=99):
    return name,id;

print changeMy()
ttx = changeMy(3333,88)
print ttx[0]

def tupppp(flag,* params):
    for param in params:
        print param
        print ttx

tupppp(22,23,21,421,53232,555,"两室")

l = (1,2,3)
for i in range(len(l)):
    print l[i]
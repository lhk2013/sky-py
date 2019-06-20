# -*- coding: utf-8 -*-


import time

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


emp = Employee("我的",22);

emp.displayCount()
emp.displayEmployee()



ticks = time.time()
ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print ticks
msg = "来来来"

list = [msg,ticks]

values = tuple(list)
print values

str = u"暗能量通信技术"
print str == u"暗能量通信技术"

import re

reg = r'\[(.*?)\]'
msg = u"[大哭]"
answer = re.findall(reg, msg , re.S)
print answer.__len__()
print msg.encode('utf-8').decode("utf-8").__len__()


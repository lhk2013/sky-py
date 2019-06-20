# -*- coding: utf-8 -*-
import sys


def fab(max):
    n ,a ,b = 0 ,0,1
    while(n<max):
        yield b
        a,b = b,a+b
        n += 1
    else:
        print max

if __name__ == '__main__':
    x = fab(100)
    print x.next()

    for i in range(10):
        print i
    for i in xrange(10):
        print i


a = 99999999
b = "-"
print "{0:{2}^{1},}\n{0:{2}>{1},}\n{0:{2}<{1},}".format(99999999,30,"-")

print "{0:{2}^{1}}\n".format(10000000,16,"-")

print range(1,10)

import random
a = {"result":[{"ss":2},{"ss":3},{"ss":7},{"ss":6}]}
print len(a["result"])
index = random.randint(1,len(a["result"]))-1
print "index %s" % index
l1 = list(a["result"])
print l1[index]
s3 = l1[index]
print s3["ss"]



print "问题 %s 答案 %s " % ("李老师", "来了个")

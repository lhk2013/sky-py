# -*- coding: UTF-8 -*-
from study2 import  tupppp
import study2
import random

print tupppp(111,"乐视","melngg")

Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    # global Money
    Money = 2009
    Money = Money + 1
    print Money


print Money
AddMoney()
print Money

# print dir(study2)

print locals()

reload(study2)



print random.uniform(1,1.5)

ua = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"

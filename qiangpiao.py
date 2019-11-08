# -*- coding: utf-8 -*-

import urllib3
import json
import requests
import random
import threading
import thread
import time
import threading, multiprocessing


import re
# 程序功能:要将所有<h1>..</h1>中的文本替换掉
key = "<html><body><h1>hello world</h1><h1>hello wjs</h1></body></html>"  # 这段是你要匹配的文本
p1 = r"(?<=<h1>).+?(?=</h1>)"  # 这是我们写的正则表达式规则
pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
print(pattern1.findall(key))  # 查看下匹配到什么

newKey = re.sub(p1, "替换成的文本", key)
print("原文本:"+key)
print("新文本:"+newKey)


text = u"\n         两室    \n          方法       \n"

reg = r"\s+"
text2 = re.sub(reg,"",text)

print 11111
print text2


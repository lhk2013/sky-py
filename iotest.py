# -*- coding: utf-8 -*-

fo = open("C:\\Users\\liuhaikuo\\Desktop\\test.txt", "a+")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace

list = fo.readlines()
print list
fo.seek(0,0)
list = fo.read()
print list


# fo = open("C:\\Users\\liuhaikuo\\Desktop\\test.txt", "a+")

fo.seek(0,0)
fo.write( "唑来膦酸绿绿绿绿绿绿")

fo.close()

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()


class Networkerror(Exception):
    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Bad Exception")
except Networkerror ,e:
    print e


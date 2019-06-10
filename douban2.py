# -*- coding: utf-8 -*-
import requests
from lxml import etree
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

if __name__ == '__main__':
    baseUrl = "https://www.douban.com/gallery/"
    content = requests.get(baseUrl).content.decode("utf8")
    # print content
    fo = open("content.txt","a+")
    fo.write(content)
    fo.close()
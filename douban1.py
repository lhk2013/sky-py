# -*- coding: utf-8 -*-
from lxml import etree
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )


if __name__ == '__main__':

    baseUrl = "https://www.douban.com/gallery/"
    content = "<html><div>测试1</div><div>测试2</div><script></script></html>"

    dom = etree.HTML(content)
    divList = dom.xpath("//div")

    for div in divList:
        print  (etree.tostring(div).decode())


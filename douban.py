# -*- coding: utf-8 -*-
import requests
from lxml import etree

if __name__ == '__main__':
    baseUrl = "https://www.douban.com/gallery/"
    content = requests.get(baseUrl).content.decode("utf8")
    dom = etree.HTML(content)
    divList = dom.xpath("//ul[contains(concat(' ', normalize-space(@class), ' '),' topics ')]/div")
    '''遍历话题'''

    for div in divList:
        print "-------------------------------------------------"
        print  etree.tostring(div, encoding="utf-8", pretty_print=True, method="xml")

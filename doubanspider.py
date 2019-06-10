# -*- coding: utf-8 -*-
import requests
from lxml import etree
import time
import random
import json
import os
import re
import sys
#
# reload(sys)
# sys.setdefaultencoding( "utf-8" )


def  parseUrl(baseUrl,i):
    print baseUrl % (i)

def page_Info(myPage):
    '''Regex'''
    mypage_Info = re.findall(r'<a href="(.*?)".*?>(.*?)</a>', myPage, re.S)
    return mypage_Info


def saveUrlList(save_path, filename, slist):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path+"/"+filename+".txt"
    with open(path, "a+") as fp:
        for s in slist:
            writeStr = "%s\t\t%s\n" % (s[0].encode("utf8"), s[1].encode("utf8"))
            fp.write(writeStr)
            try:
                spiderDetail(s)
            except Exception, e:
                print "spider detail error url: %s " % s[0].encode("utf8")
                print 'str(e):\t\t', str(e)
        else:
            fp.close()


def spiderDetail(urlInfo):
    print "spiderDetail url %s  name %s" % (urlInfo[0].encode("utf-8"),urlInfo[1].encode("utf-8"))
    detailHtml = requests.get(urlInfo[0].encode("utf-8")).content.decode("utf8")
    print "detail content---------------"
    dom = etree.HTML(detailHtml)
    new_items = dom.xpath("//div[@id='link-report']/div[contains(concat(' ', normalize-space(@class), ' '),' note ')]")
    print new_items
    detailContent = etree.tostring(new_items[0],encoding="utf8")
    detailContentInfo = [(urlInfo[0],detailContent)]
    savePath = u"豆瓣内容爬取"
    fileName = u"详情页面"
    path = savePath + "/" + fileName + ".txt"
    with open(path, "a+") as fp:
        writeStr = "%s\t\t%s\t\t%s\n" % (urlInfo[0].encode("utf8"),urlInfo[1].encode("utf8"), detailContent)
        fp.write(writeStr)
        fp.close()


if __name__ == '__main__':
    # baseUrl = "https://www.douban.com/gallery/"
    # content = requests.get(baseUrl).content.decode("utf8")
    # dom = etree.HTML(content)
    # divList = dom.xpath("//ul[contains(concat(' ', normalize-space(@class), ' '),' topics ')]/div")
    # '''遍历话题'''
    #
    # for div in divList:
    #     print "-------------------------------------------------"
    #     print etree.tostring(div, encoding="utf-8", pretty_print=True, method="xml")
    total = 10000;
    start = 1;
    while (start <= total):
        baseUrl = "https://www.douban.com/j/search?start=%d&q=白化病&cat=1015";
        baseUrl = baseUrl % (start)
        print "---------------baseUrl",baseUrl
        content = requests.get(baseUrl).content.decode("utf8")
        print content
        contentJson = json.loads(content)
        items = contentJson["items"]
        total = contentJson["total"]
        dataSize = len(items)
        for index in range(dataSize):
            print "item is %s" % index
            infoList =  page_Info(items[index])
            saveUrlList(u"豆瓣内容爬取",u"全部分类-白化病",infoList)
            time.sleep(random.uniform(1, 1.5))

        if(dataSize <=0):
            dataSize = 1;
        start += dataSize
        print start
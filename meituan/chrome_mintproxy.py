# -*- coding: utf-8 -*-
import requests

from selenium import webdriver
import browsermobproxy
from browsermobproxy import Server


from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time

import xlwt
from datetime import datetime
import json
import fontutils
import json
import meituan.database as db
cursor = db.connection.cursor()


pageCategoryMap = {}
woffPath = None

def init():
    server = Server(r'E:\work\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
    server.start()
    proxy = server.create_proxy()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))


    prefs = {
        'profile.default_content_setting_values': {
            'images': 2
        }
    }

    # chrome_options.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome(chrome_options=chrome_options)

    base_url = "https://h5.waimai.meituan.com/waimai/mindex/menu?mtShopId=986722685149968&utm_source=5913"
    proxy.new_har("meituan", options={'captureHeaders': True, 'captureContent': True})

    browser.get(base_url)

    browser.find_element_by_tag_name("style")

    jsScroll = 'document.getElementsByClassName("_3Eh5JLsA7ZO_myNmJgO9cv")[0].scrollTop=80000'
    time.sleep(10)
    browser.execute_script(jsScroll)
    time.sleep(5)

    ## 获取字体
    result = proxy.har
    for entry in result['log']['entries']:
        _url = entry['request']['url']
        if ".woff" in _url:
            print _url

            r = requests.get(_url)
            filePath = _url[_url.rindex("/")+1:_url.__len__()]
            with open(filePath, "wb") as f:
                f.write(r.content)
                global  woffPath
                woffPath = filePath


    tags = browser.find_elements_by_class_name("_367BRJY7OL8RJUjxqVmLe8")
    for index in range(1,1):
        jsClick = 'document.getElementsByClassName("_367BRJY7OL8RJUjxqVmLe8")[%s].click()' % (index)
        # js = 'document.getElementsByClassName("_367BRJY7OL8RJUjxqVmLe8")[2].click()'
        browser.execute_script(jsClick)
        time.sleep(10)
        browser.execute_script(jsScroll)
        time.sleep(5)




    result = proxy.har


    for entry in result['log']['entries']:
        _url = entry['request']['url']
        if "/openh5/poi/menuproducts" in _url:
            _response = entry['response']
            if 'text' in _response['content']:
                _content = _response['content']['text']
                # 获取接口返回内容
                # print(_content)
                result = json.loads(_content, "utf-8")
                result = result['data']['spuList']
            else:
                print "没有text"
            parseSaveData(result,None)
        elif "/openh5/poi/food" in _url:
            _response = entry['response']
            _content = _response['content']['text']
            # 获取接口返回内容
            # print(_content)
            result = json.loads(_content, "utf-8")
            pageCategoryList =  result['data']['pageCategoryList']
            spulist = pageCategoryList[0]["spuList"]
            pageCategoryMap = parseCatMap(pageCategoryList)
            pageCategoryMap['shopName'] = result['data']['shopInfo']['shopName']
            parseSaveData(spulist, None)
            ##处理折扣
            if result['data'].has_key('categoryList'):
                parseDiscountSpuData(result['data']['categoryList'])

    print "<<<<<<<<<<<<<<<<<<<解析完毕>>>>>>>>>>>>>>>>"
    time.sleep(10)
    proxy.close()
    # browser.quit()

## 处理分类
def parseCatMap(pageCategoryList):
    for i in xrange(len(pageCategoryList)):
        print pageCategoryList[i]
        pageCategoryMap[''+pageCategoryList[i]["tag"]+''] = pageCategoryList[i]["categoryName"]

    return pageCategoryMap

## 处理折扣商品
def parseDiscountSpuData(categoryList):
    for i in xrange(len(categoryList)):
        category =  categoryList[i]
        pageCategoryMap[''+category['tag']+''] = category['categoryName']
        parseSaveData(category['spuList'], category['categoryName'])



# 根据URL找到数据接口

def parseSaveData(result, tagName):

    print result

    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
    today = datetime.today()
    today_date = datetime.date(today)

    parseDict = fontutils.parseWoff(woffPath)

    for i in xrange(len(result)):
        # 对result的每个子元素作遍历，
        item = {}
        print "-----------------------------------------"
        try:

            print result[i]
            if(len(result[i])>0):
                item["shopName"] = pageCategoryMap['shopName']
                item["tag"] = result[i]["tag"]
                tag = result[i]["tag"]
                if tagName is not None:
                    item["tagName"] = tagName
                elif pageCategoryMap.has_key(tag) :
                    item["tagName"] = pageCategoryMap[tag]
                item["spuId"] = result[i]["spuId"]
                item["spuName"] = result[i]["spuName"]
                item["spuPromotionInfo"] = result[i]["spuPromotionInfo"]



                item["praiseNum"] = fontutils.parseString(result[i]["praiseNumDecoded"],parseDict)
                item["saleVolume"] = fontutils.parseString(result[i]["saleVolumeDecoded"],parseDict)
                sku = result[i]["skuList"][0]

                item["skuId"] =sku["skuId"]
                item["spec"] =sku["spec"]
                item["originPrice"] =sku["originPrice"]
                item["currentPrice"] =sku["currentPrice"]


                discount = result[i]["activityPolicy"]["discountByCount"]
                item["discount"] = discount["discount"]
                save_subject(item)


        except Exception as e :

            print e.args


def save_subject(item):

    keys = item.keys()
    values = tuple(item.values())
    fields = ','.join(keys)
    temp = ','.join(['%s'] * len(keys))
    sql = 'INSERT INTO meituan1 (%s) VALUES (%s)' % (fields, temp)
    print sql
    print values
    cursor.execute(sql, values)
    return db.connection.commit()

if __name__ == '__main__':
    init()

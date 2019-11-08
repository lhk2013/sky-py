# -*- coding: utf-8 -*-
import requests
from lxml import etree
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from browsermobproxy import Server

from selenium.webdriver.chrome.options import Options






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

    server = Server(r'E:\work\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
    server.start()
    proxy = server.create_proxy()

    chrome_options = Options()
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))

    baseUrl="https://h5.waimai.meituan.com/waimai/mindex/menu?mtShopId=934294019092390&initialLat=23.125207&initialLng=113.302035&actualLat=31.201409&actualLng=121.58195&source=searchresult";

    browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    browser.get(baseUrl)
    # print browser.page_source



    time.sleep(2)
    js = 'document.getElementsByClassName("_3Eh5JLsA7ZO_myNmJgO9cv")[0].scrollTop=80000'





    browser.execute_script(js);
    # browser.execute_script()
    # actions =browser.find_element_by_class_name("a_search_more");
    # ActionChains(browser).move_to_element(actions).click(actions).perform()  # 鼠标移动到某处双击

    # ActionChains.click()

    result = proxy.har

    for entry in result['log']['entries']:
        _url = entry['request']['url']
        # 根据URL找到数据接口
        if "/api/v2/aweme/post" in _url:
            _response = entry['response']
            _content = _response['content']['text']
            # 获取接口返回内容
            print(_content)





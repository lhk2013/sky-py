# -*- coding: utf-8 -*-
import requests
from lxml import etree
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains





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

    baseUrl="https://www.douban.com/search?q=%E7%99%BD%E5%8C%96%E7%97%85";

    browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    browser.get(baseUrl)
    # print browser.page_source

    time.sleep(2)
    js = 'window.scrollTo(0,5000)'

    browser.execute_script(js)
    # browser.execute_script()
    actions =browser.find_element_by_class_name("a_search_more");
    ActionChains(browser).move_to_element(actions).click(actions).perform()  # 鼠标移动到某处双击

    # ActionChains.click()
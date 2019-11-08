# -*- coding: utf-8 -*-
import requests

from selenium import webdriver
import browsermobproxy
from browsermobproxy import Server


from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time



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

base_url = "https://h5.waimai.meituan.com/waimai/mindex/menu?mtShopId=934294019092390&initialLat=23.125207&initialLng=113.302035&actualLat=31.201409&actualLng=121.58195&source=searchresult"
proxy.new_har("meituan", options={'captureHeaders': True, 'captureContent': True})

browser.get(base_url)

time.sleep(5)

js = 'document.getElementsByClassName("_367BRJY7OL8RJUjxqVmLe8")[%s].click()' % (3)
# js = 'document.getElementsByClassName("_367BRJY7OL8RJUjxqVmLe8")[2].click()'
jsScroll = 'document.getElementsByClassName("_3Eh5JLsA7ZO_myNmJgO9cv")[0].scrollTop=80000'
browser.execute_script(js)
time.sleep(3)
browser.execute_script(jsScroll)


result = proxy.har

for entry in result['log']['entries']:
    _url = entry['request']['url']
    # 根据URL找到数据接口
    print _url
    if "/openh5/poi/menuproducts" in _url:
        _response = entry['response']
        _content = _response['content']['text']
        # 获取接口返回内容
        print(_content)

result = proxy.har
print 2222

time.sleep(10)
proxy.close()
browser.quit()


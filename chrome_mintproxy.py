# -*- coding: utf-8 -*-
import requests

from selenium import webdriver
import browsermobproxy
from browsermobproxy import Server


BROWSERMOBPROXY = r'E:\work\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat'

# server = browsermobproxy.Server(BROWSERMOBPROXY, {'port': 8080})  # 初始化一个代理Manager服务，并监听8080端口
# server.start()  # 启动代理Manager服务
# proxy = server.create_proxy()  # 向代理Manager服务申请一个代理服务，会使用默认端口8081
# print(proxy.port)


proxy = browsermobproxy.Client('http://localhost:8080')     # 向已有代理Manager服务申请一个代理服务


def set_proxy_for_ff():
    profile = webdriver.FirefoxProfile()
    driver = webdriver.Firefox(firefox_profile=profile, proxy=proxy.selenium_proxy())  # 配置selenium使用指定的代理服务
    proxy.new_har("test", options={'captureContent': True, 'captureHeaders': True})  # 开启代理监控，如果不监控会拿不到请求内容
    driver.get("http://www.baidu.cn")  # 访问页面
    # TODO:其它页面操作
    proxy.wait_for_traffic_to_stop(1000, 6000)  # 停止代理监控
    print(proxy.har)  # 打印请求日志信息


def set_proxy_for_chrome():
    dc = webdriver.DesiredCapabilities
    proxy.add_to_capabilities(dc)
    driver = webdriver.Chrome(desired_capabilities=dc)  # 配置selenium使用指定的代理服务
    proxy.new_har("test", options={'captureContent': True, 'captureHeaders': True})  # 开启代理监控，如果不监控会拿不到请求内容
    driver.get("http://www.baidu.cn")  # 访问页面
    # TODO:其它页面操作
    proxy.wait_for_traffic_to_stop(1000, 6000)  # 停止代理监控
    print(proxy.har)  # 打印请求日志信息


if '__main__' == __name__:
    set_proxy_for_ff()
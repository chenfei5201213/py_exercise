#-*- coding: utf-8 -*-
# @Time    : 2017/8/17 15:35
# @File    : selenium_模拟手机屏幕.py
# @Author  : 守望@天空~

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
mobile_emulation = { "deviceMetrics": {"width": 414, "height": 736, "pixelRatio": 3.0},#  定义设备高宽，像素比
"userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1" #通过UA 模拟手机型号}
}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.set_window_size(width=414,height=736)
driver.get("http://www.taobao.com")
sleep(4)
driver.quit()
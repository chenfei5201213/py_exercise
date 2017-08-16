#-*- coding: utf-8 -*-

from twisted.internet import reactor
from selenium import webdriver
import time
# 设置线程池上限
reactor.suggestThreadPoolSize(5)
def tt(i,stop=19):
    driver= webdriver.Chrome()
    driver.get("http://www.baidu.com")
    time.sleep(0.5)
    driver.quit()
    print (i)
    if i==stop:
        # 标记线程池结束条件
        reactor.stop(5)

for index,value in enumerate(range(20)):
    # reactor.callFromThread(tt,index)
    reactor.callInThread(tt,index,19)

print ("Test start")
reactor.run()
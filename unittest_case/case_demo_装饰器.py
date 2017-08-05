#-*- coding: utf-8 -*-
# @Time    : 2017/7/24 15:51
# @File    : case_demo_装饰器.py
# @Author  : 守望at天空~
import logging
from time import sleep

def demo(func):
    def wapper(*args,**kwargs):
        logging.warn( "测试启动")
        sleep(0.3)
        result =  func(*args,**kwargs)
        sleep(0.3)
        logging.warn("测试结束")
        return result
    return wapper

import unittest
class case_01(unittest.TestCase):

    @demo
    def test_111(self):
        '''testdesc1'''
        print u'case1'

    @demo
    def test_112(self):
        '''testdesc2'''
        print u'case2'


    @demo
    def test_113(self):
        '''testdesc3'''
        print u'case3'

    @demo
    def test_114(self):
        '''testdesc4'''
        print u"case4"

if __name__ =="__main__":
    unittest.main()



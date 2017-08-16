#-*- coding: utf-8 -*-
# @Time    : 2017/8/15 9:54
# @File    : demo.py
# @Author  : 守望@天空~
from data_factory import data_mock

generater = data_mock()
state = generater.dist_code
print u"地区行政编码：{state}:{code}".format(**state)
id = generater.id(True)
print u"身份证号：{state}:{id}".format(**id)
#-*- coding: utf-8 -*-
# @Time    : 2017/8/15 9:54
# @File    : demo.py
# @Author  : 守望@天空~
data = {
  "object|2-4": {
    "110000": "北京市",
    "120000": "天津市",
    "130000": "河北省",
    "140000": "山西省"
  }
}
data0 = data.copy()
for key,value in data.items():
    if key.find("|"):
        key,rule = key.split('|')
        print rule
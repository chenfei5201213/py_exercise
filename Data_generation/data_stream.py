#-*- coding: utf-8 -*-
# @Time    : 2017/8/15 10:19
# @File    : data_stream.py
# @Author  : 守望@天空~
# 实现多个数据间的数据传输
result1 ={'a':{'dd':1},'b':'测试一下'}

data2= {'test1':'$result1.a.dd'}
for key,value in data2.items():
    if value.startswith('$'):
        text =  value[1:].split('.')
        data = locals()[text[0]].copy()
        for i in text[1:]:
            data = data[i]
        data2[key]=data
print data2
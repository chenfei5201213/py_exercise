#-*- coding: utf-8 -*-
"""
@Time    : 2015/11/19
@Author  : 守望@天空~
@File    : 冒泡排序.py
"""
def bubble_sort(lists):
    # 冒泡排序
    lists=list(lists)
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

lt=[32,12,3,27,6,9,1]
tp=(2,6,1,9,4)
print bubble_sort(lt)
print bubble_sort(tp)
print bubble_sort('adcaw')

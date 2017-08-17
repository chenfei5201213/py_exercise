#-*- coding: utf-8 -*-
# @Time    : 2017/8/17 16:19
# @File    : 插入排序.py
# @Author  : 守望@天空~

def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists
if __name__=='__main__':
    lt = [12, 34, 2, 5, 8, 1, 9]
    print insert_sort(lt)
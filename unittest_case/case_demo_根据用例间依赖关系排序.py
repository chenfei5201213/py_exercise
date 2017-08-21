# -*- coding: utf-8 -*-
"""
@Time    : 2017/6/19 10:48
@File    : case_demo2.py
# @Author  : 守望at天空~
"""
import unittest
from time import sleep

class demo(unittest.TestCase):
    """
    一个解决用例间参数依赖的小想法，取巧的利用了pythnon的内存机制实现中间参数传递
    """
    def __init__(self, case_id, depend, data, result={}):
        super(demo, self).__init__()
        self.depend = depend
        self.case_id = case_id
        self.result = result
        self.data = data

    def runTest(self):
        print ("运行测试用例 %s" % self.case_id)
        if self.depend:
            print ("- 依赖项为用例：%s" % self.depend)
            print ("- 提取依赖用例的结果为 %s" % self.result[self.depend])
        self.result[self.case_id] = {self.case_id: self.data}
        sleep(0.5)

    def tearDown(self):
        self._testMethodName = self.case_id


class test_sort(object):
    """
    根据用例间的依赖关系对用例列表进行排序
    参数说明 testlist
    [[caseid, depend, data],..]
    """
    def __init__(self, testlist):
        self._test = []
        self.testlist = testlist
        length = len(self.testlist)
        self.count = 0  # 迭代次数，用于排序复杂度判断指标
        while len(self.testlist) > 1:
            self._sort()
            if self.count > length:
                # 迭代次数超出，说明参数依赖可能出现闭环
                raise Exception("依赖关系错误：依赖闭环 %s" % str(self.testlist))
        if testlist[0][0] == testlist[0][1]:
            # 自相依赖，抛出异常
            raise Exception("依赖关系错误:自相依赖 %s" % str(self.testlist[0]))
        self._test.append(testlist[0])

    def _sort(self):
        tmp = map(list, zip(*self.testlist))
        for i, value in enumerate(tmp[1]):
            if value not in tmp[0]:
                self._test.append(self.testlist[i])
                self.testlist.pop(i)
                break
        self.count += 1

    def __iter__(self):
        return iter(self._test)

if __name__ == "__main__":
    from unittest import TestSuite

    testlists = [
        # [caseid, depend, data]
        ['test1', 'test2', '111'],
        ['test2', 'test3', '222'],
        ['test3', 'test4', '333'],
        ['test4', None, '444'],
        ['test5', 'test4', '555'],
        ['test6', 'test2', '666'],
        ['test7', 'test5', '777'],
        ['test8', 'test3', '888']
    ]

    # 按照依赖排序用例，可能逻辑不太严谨
    testlist = test_sort(testlists)
    suite = TestSuite()
    for i in testlist:
        suite.addTest(demo(*i))
    runner = unittest.TextTestRunner()
    runner.run(suite)
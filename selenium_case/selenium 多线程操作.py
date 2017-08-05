#-*- coding: utf-8 -*-

import unittest
from common import Runner
# from common import HTMLTestRunner_cn_2
import os
import time
import multiprocessing

project_path = "D:\webtest\webTest"

testsuites = unittest.TestLoader().discover(project_path, pattern="test*.py")

runner = Runner()
runner.run(testsuites)
print runner.get_details()


def func(test):
    runner.run(test)

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    result = []
    for test in testsuites:
        result.append(pool.apply_async(func, (test,)))
    pool.close()
    pool.join()

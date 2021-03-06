#-*- coding: utf-8 -*-

import unittest
# from common import HTMLTestRunner_cn_2
import os
import time
import multiprocessing

project_path = "D:/"

testsuites = unittest.TestLoader().discover(project_path, pattern="test*.py")

runner = unittest.TextTestRunner()


def func(test):
    runner.run(test)

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    result = []
    for test in testsuites:
        result.append(pool.apply_async(func, (test,)))
    pool.close()
    pool.join()

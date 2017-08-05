#-*- coding: utf-8 -*-

import unittest
from unittest import  TextTestRunner,TestResult,TestLoader


class case_01(unittest.TestCase):
    def setUp(self):
        print self._testMethodName,"up"

    def tearDown(self):
        print self._testMethodName,"down"

    def test_111(self):
        '''testdesc1'''
        print u'case1'
        self.assertIn('1', u'a')

    def test_112(self):
        '''testdesc2'''
        print u'case2'
        self.assertTrue(True)


    def test_113(self):
        '''testdesc3'''
        self.assertEqual(1,1)
        print u'case3'

    def test_114(self):
        '''testdesc4'''
        print u"case4"
        raise AssertionError('aaa')


class _TestResult(TestResult):
    def __init__(self,stream=None, descriptions=None, verbosity=None):
        super(_TestResult, self).__init__(stream, descriptions, verbosity)
        self.trys=0
        self.status=0

    def addFailure(self, test, err):
        super(_TestResult, self).addFailure(test, err)
        self.status =1

    def stopTest(self, test):
        super(_TestResult,self).stopTest(test)
        if self.status ==1:
            self.trys += 1
            if self.trys <= 3:
                print u"retesting... %d" % self.trys
                test(self)
            else:
                self.status = 0
                self.trys = 0


if __name__ =="__main__":
    suit =TestLoader().loadTestsFromTestCase(case_01)
    from common.HTMLTestRunner_2_beauty import HTMLTestRunner
    a = HTMLTestRunner(open("d:/report.html","wb"),title="123123123",description="412412asdasdasd")
    a.run(suit)
    # TextTestRunner(resultclass=_TestResult,verbosity=2).run(suit)




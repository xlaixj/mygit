# -*- coding:utf-8 -*-  '
'''
Created on 2015年9月21日

@author: Administrator
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import titletest
import logintest
import loginvertest
import openpublishtest 
import publishvertest
import deletetest
import exittest
import os
import time


class Test_Open(unittest.TestCase):


    def setUp(self):
        self.dr = webdriver.Firefox()
        self.url  = "http://www.caakaa.com"
#登录测试
    def test_main(self):
        dr = self.dr
        dr.get(self.url )
        dr.maximize_window()
        titletest.test_title(self)
        logintest.test_login(self)
        loginvertest.test_loginver(self)
        openpublishtest.test_openpublish(self)
        publishvertest.testpublishver(self)
        deletetest.test_delete(self)
        exittest.test_exit(self)

    def tearDown(self):
        #self.br.quit()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
# -*- coding:utf-8 -*-  '
'''
Created on 2015年9月21日

@author: Administrator
'''

def test_loginver(self):
    #用户名密码验证
    dr = self.dr
    #用户名为空验证
    dr.find_element_by_id("account_email").clear()
    dr.find_element_by_id("account_email").send_keys("")
    dr.find_element_by_id("account_password").clear()
    dr.find_element_by_id('account_password').submit()
    try:
        dr.find_element_by_link_text(u"写文章")
        flag = True
    except:
        flag = False
    if flag != True:
        print u"用户名为空验证...........passed"
    else:
        print u"用户名为空验证............failed"
    #用户名有误判断
    dr.find_element_by_id("account_email").clear()
    dr.find_element_by_id("account_email").send_keys("testaccount@gmail.com")
    dr.find_element_by_id("account_password").clear()
    dr.find_element_by_id('account_password').submit()
    try:
        dr.find_element_by_link_text(u"写文章")
        flag = True
    except:
        flag = False
    if flag != True:
        print u"用户名不匹配验证............passed"
    else:
        print u"用户名不匹配验证............failed"
        #密码为空判断
    dr.find_element_by_id("account_email").clear()
    dr.find_element_by_id("account_email").send_keys("wulliam@gmail.com")
    dr.find_element_by_id("account_password").clear()
    dr.find_element_by_id("account_password").send_keys("")
    dr.find_element_by_id('account_password').submit()
    try:
        dr.find_element_by_link_text(u"写文章")
        flag = True
    except:
        flag = False
    if flag != True:
        print u"密码为空验证............passed"
    else:
        print u"密码为空验证............failed"
        #密码有误判断
    dr.find_element_by_id("account_email").clear()
    dr.find_element_by_id("account_email").send_keys("wulliam@gmail.com")
    dr.find_element_by_id("account_password").clear()
    dr.find_element_by_id("account_password").send_keys("Db123456")
    dr.find_element_by_id('account_password').submit()
    try:
        dr.find_element_by_link_text(u"写文章")
        flag = True
    except:
        flag = False
    if flag != True:
        print u"密码不匹配验证............passed"
    else:
        print u"密码不匹配验证............failed"
        #正常登录
    dr.find_element_by_id("account_email").clear()
    dr.find_element_by_id("account_email").send_keys("wulliam@gmail.com")
    dr.find_element_by_id("account_password").clear()
    dr.find_element_by_id("account_password").send_keys("P@ssw0rd15")
    dr.find_element_by_id('account_password').submit()
    try:
        dr.find_element_by_link_text(u"写文章")
        flag = True
    except:
        flag = False
    if flag == True:
        print u"正常登录操作............passed"
    else:
        print u"正常登录操作............failed"
      
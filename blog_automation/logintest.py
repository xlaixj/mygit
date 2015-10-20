# -*- coding:utf-8 -*-  '
'''
Created on 2015年9月21日

@author: Administrator
'''

def test_login(self):
    dr = self.dr
    dr.find_element_by_link_text(u"登录").click() 
    try:
        dr.find_element_by_id("account_email")
        flag = True
    except:
        flag = False
    if flag == True:
        print u"打开登录............passed"
    else:
        print u"打开登录............failed"
            
# -*- coding:utf-8 -*-  '
'''
Created on 2015年9月21日

@author: Administrator
'''
def test_openpublish(self):
    dr = self.dr
    #发表文章页面打开验证
    dr.find_element_by_link_text(u"写文章").click()
    try:
        dr.find_element_by_css_selector("input.submit")
        flag = True
    except:
        flag = False
    if flag == True:
        print u"进入发表文章页面...........passed"
    else:
        print u"进入发表文章页面............failed"
# -*- coding:utf-8 -*-  
def test_title(self):
    dr = self.dr
    print u"开始测试...........pass"
    flagstr = dr.title
    if flagstr == "wulliam site":
        print u"网站打开............passed"
    else:
        print u"网站打开............failed"
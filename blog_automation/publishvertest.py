# -*- coding:utf-8 -*-  '
'''
Created on 2015年9月21日


@author: Administrator
'''
import time

def testpublishver(self):
    dr = self.dr
    #标题为空验证
    dr.find_element_by_id("blog_title").clear()
    dr.find_element_by_id("blog_title").send_keys(u"")
    dr.find_element_by_css_selector("input.submit").click()
    errorstr1 = dr.find_element_by_xpath("//div[@id='form-error-info']/span").text
    if errorstr1 == u"文章标题太短了;":
        print u"标题为空验证............passed"
    else:
        print u"标题为空验证............failed"
    #标题字符长度验证
    dr.find_element_by_id("blog_title").clear()
    dr.find_element_by_id("blog_title").send_keys(u"1")
    dr.find_element_by_css_selector("input.submit").click()
    errorstr1 = dr.find_element_by_xpath("//div[@id='form-error-info']/span").text
    if errorstr1 == u"文章标题太短了;":
        print u"标题字符长度验证............passed"
    else:
        print u"标题字符长度验证............failed"
    #文章内容必填验证
    dr.find_element_by_id("blog_title").clear()
    dr.find_element_by_id("blog_title").send_keys(u"文章标题")
    dr.find_element_by_id("blog_content").clear()
    dr.find_element_by_id("blog_content").send_keys(u"")  
    dr.find_element_by_css_selector("input.submit").click()
   # errorstr2 = dr.find_element_by_xpath("//div[@id='form-error-info']/span[2]").text
    errorstr1 = dr.find_element_by_xpath("//div[@id='form-error-info']/span").text
    if errorstr1 == u"文章内容太少了;":
        print u"文章内容必填验证............passed"
    else:
        print u"文章内容必填验证............failed"
    dr.find_element_by_id("blog_title").clear()
    dr.find_element_by_id("blog_title").send_keys(u"文章标题")
    dr.find_element_by_id("blog_content").clear()
    dr.find_element_by_id("blog_content").send_keys(u"w")  
    dr.find_element_by_css_selector("input.submit").click()
    errorstr1 = dr.find_element_by_xpath("//div[@id='form-error-info']/span").text
    if errorstr1  == u"文章内容太少了;":
        print u"文章内容字符长度验证............passed"
    else:
        print u"文章内容字符长度必填验证............failed"
    dr.find_element_by_id("blog_title").clear()
    dr.find_element_by_id("blog_title").send_keys(u"Linux的用户和用户组管理")
    dr.find_element_by_id("blog_content").clear()
    dr.find_element_by_id("blog_content").send_keys(u"Linux是个多用户多任务的分时操作系统，所有一个要使用系统资源的用户都必须先向系统管理员申请一个账号，然后以这个账号的身份进入系统。用户的账号一方面能帮助系统管理员对使用系统的用户进行跟踪，并控制他们对系统资源的访问；另一方面也能帮助用户组织文件，并为用户提供安全性保护。每个用户账号都拥有一个惟一的用户名和用户口令。用户在登录时键入正确的用户名和口令后，才能进入系统和自己的主目录。")
    dr.find_element_by_id("show_blog_content_preview").click()
    dr.find_element_by_css_selector("span").click()
    dr.find_element_by_id("blog_slug_url").clear()
    dr.find_element_by_id("blog_slug_url").send_keys("file-")  
    dr.find_element_by_css_selector("input.submit").click()
    time.sleep(2)
    errorstr2 = dr.find_element_by_id("flash-notice").text
   # errorstr2 = dr.find_element_by_xpath("//div[@id=''flash-notice]").text
    if errorstr2 == u"文章成功发布":
        print u"文章发表操作............passed"
    else:
        print u"文章发表操作............failed"
    #标题重复性验证
    #浏览
    dr.find_element_by_link_text(u"首页").click()
    dr.find_element_by_link_text(u"博客").click()
    dr.find_element_by_link_text(u"Linux的用户和用户组管理-删除测试数据").click()
    time.sleep(2)

    #dr.find_element_by_link_text(u"首页").click()
    try:
        dr.find_element_by_link_text(u"Linux的用户和用户组管理-删除测试数据")
        flag = True
    except:
        flag = False
    if flag == True:
        print u"浏览............passed"
    else:
        print u"浏览............failed"
    dr.find_element_by_link_text(u"首页").click()
    time.sleep(2)
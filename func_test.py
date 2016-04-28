#!/usr/bin/python3
#-*- coding:utf8 _*_
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.brower = webdriver.Firefox()
        self.brower.implicitly_wait(5)
    def tearDown(self):
        self.brower.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
             
        #老王听说有一个很酷的在线待办事项应用
        #他去看了这个应用的首页
        self.brower.get('http://localhost:8000')
        #他注意到网页的标题盒头部都包含“To-Do”这个词
        self.assertIn('To-Do',self.brower.title)
        self.fail('finish the test!')
        
        
        #应用邀请他输入一个待办事项
        #他在一个文本框中输入了"买一本书"
        #老王爱看书
        #他按回车键后，页面更新了
        #待办事项表格中显示了”1：买一本书“
        
        #页面中又显示利一个文本框，可以输入其他待办事项
        #他又输入了”看书后思考“
        
        #页面再次更新，他的清单中显示了两个待办事项
        
        #老王想知道这个网站是否会记住他的清单
        #他看到利网站为他生成了一个唯一的URL
        #而且页面中有一些文字解说这个功能
        #他访问这个URL，发现他的待办事项还在。
        #老王很满意，去吃饭利。

    if __name__ == '__main__':
        unittest.main()
       
       




#!/usr/bin/python3
#-*- coding:utf8 _*_
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.brower = webdriver.Firefox()
        self.brower.implicitly_wait(5)

    def tearDown(self):
        self.brower.quit()
        
    def check_for_row_in_list_table(self,row_text):
        table = self.brower.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])
        
        
        
    def test_can_start_a_list_and_retrieve_it_later(self):
             
        #老王听说有一个很酷的在线待办事项应用
        #他去看了这个应用的首页
        self.brower.get(self.live_server_url)
        #他注意到网页的标题盒头部都包含“To-Do”这个词
        self.assertIn('To-Do',self.brower.title)
        header_text = self.brower.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        
        
        #应用邀请他输入一个待办事项
        inputbox = self.brower.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        #他在一个文本框中输入了"买一本书"
        #老王爱看书
        inputbox.send_keys('买一本书')
        #他按回车键后，页面更新了
        #待办事项表格中显示了”1：买一本书“
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1:买一本书')
       
#        table = self.brower.find_element_by_id('id_list_table')
#        rows = table.find_elements_by_tag_name('tr')
#        self.assertTrue(any(row.text == '1:买一本书' for row in rows),
#                        "New to-do did not appear in table -- its text was:\n%s" %(
#                        table.text,
#                        ))
#        self.assertIn('1:买一本书',[row.text for row in rows],
#                        "New to-do did not appear in table -- its text was:\n%s" %(
#                        table.text,
#                        ))

        #页面中又显示了一个文本框，可以输入其他待办事项
        #他又输入了”看书后思考“
        inputbox = self.brower.find_element_by_id('id_new_item')        
        inputbox.send_keys("看书后思考")
        inputbox.send_keys(Keys.ENTER)
        #页面再次更新，他的清单中显示了两个待办事项
        self.check_for_row_in_list_table("1:买一本书")
        self.check_for_row_in_list_table("2:看书后思考")
#        table = self.brower.find_element_by_id('id_list_table')
#        rows = table.find_elements_by_tag_name('tr')
#        self.assertIn('1:买一本书',[row.text for row in rows],
#                        "New to-do did not appear in table -- its text was:\n%s" %(
#                        table.text,
#                        ))        
#        self.assertIn('2:看书后思考',[row.text for row in rows],
#                        "New to-do did not appear in table -- its text was:\n%s" %(
#                        table.text,
#                        ))
        #老王想知道这个网站是否会记住他的清单
        #他看到利网站为他生成了一个唯一的URL
        #而且页面中有一些文字解说这个功能
        #他访问这个URL，发现他的待办事项还在。
        #老王很满意，去吃饭利。
        self.fail('finish the test!')

#
#if __name__ == '__main__':
#    unittest.main()
       
       




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
        self.brower.set_window_size(1024,768)
        
        #他看到输入框完美居中
        inputbox = self.brower.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2,512,delta=5)
        
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
        #他按回车键后，页面更新了  -- 作废
        #待办事项表格中显示了”1：买一本书“  -- 作废
        #他按回车后，被带到了一个新URL
        #这个页面的待办事项清单中显示了“1:买一本书”

        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.brower.current_url
        self.assertRegex(edith_list_url,'/lists/.+')
        self.check_for_row_in_list_table('1:买一本书')
        
        #他看到新建的清单，输入框仍然完美居中
        inputbox = self.brower.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2,512,delta=5)
        
       
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
        
        #现在一个叫老李的新用户访问利网站
        
        ##我们使用一个新浏览器会话
        ##确保老王的信息不会从cookie中泄露出来。
        self.brower.quit()
        self.brower = webdriver.Firefox()
        
        #老李访问首页
        #页面中看不到老王的清单
        self.brower.get(self.live_server_url)
        page_text = self.brower.find_element_by_tag_name('body').text
        self.assertNotIn('1:买一本书',page_text)
        self.assertNotIn('2:看书后思考',page_text)
        
        #老李输入一个新待办事项，新建一个清单
        #她不像老王一样兴趣盎然
        inputbox = self.brower.find_element_by_id('id_new_item')
        inputbox.send_keys('买牛奶')
        inputbox.send_keys(Keys.ENTER)
        
        #老李获得了他的唯一URL
        laoli_list_url = self.brower.current_url
        self.assertRegex(laoli_list_url,'/lists/.+')
        self.assertNotEqual(laoli_list_url,edith_list_url)
        
        #这个页面还是没有老王的清单
        page_text = self.brower.find_element_by_tag_name('body').text
        self.assertNotIn('1:买一本书',page_text)
        self.assertNotIn('2:看书后思考',page_text)
        self.assertIn('1:买牛奶',page_text)
        #两人很满意，睡觉去了

       
#
#if __name__ == '__main__':
#    unittest.main()
       
       




#!/usr/bin/env python

from selenium import webdriver
import unittest
import HTMLTestRunner
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



class BaiduTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://www.baidu.com"
        self.driver = webdriver.Firefox()


    def test_search(self):
        self.driver.get(self.url)
        sleep(3)
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(3)
        self.assertIn("selenium",self.driver.title,"searche correct!!!")

    def test_shezhi(self):
        self.driver.get(self.url)
        sleep(3)
        hover = self.driver.find_element_by_link_text("设置")
        sleep(3)
        ActionChains(self.driver).move_to_element(hover).perform()
        self.driver.find_element_by_link_text("搜索设置").click()
        sleep(3)
        self.driver.find_element_by_id("SL_1").click()
        Select(self.driver.find_element_by_id("nr")).select_by_value("50")
        self.driver.find_element_by_link_text("保存设置").click()
        sleep(3)
        self.driver.switch_to.alert.accept()

    def tearDown(self):
        self.driver.quit()



def createsuite():
    suite = unittest.TestSuite()
    suite.addTest(BaiduTest('test_search'))
    suite.addTest(BaiduTest('test_shezhi'))
    return suite


if __name__ == "__main__":
    unittest.main()


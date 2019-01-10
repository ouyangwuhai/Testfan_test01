#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Testfan(unittest.TestCase):
    '''Test Testfan'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.testfan.cn"
        self.verificationErrors = []
        self.accept_next_alert = True
    #Testfan用例
    def test_testfan_link(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        mymouse = WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"学习资料")))
    #  mymouse = driver.find_element_by_link_text("学习资料")
    #   mymouse = driver.find_element_by_xpath("//a[@href = '/page/20/htm']")
        ActionChains(driver).move_to_element(mymouse).perform()
        driver.find_element_by_link_text("精品文章").click()
        time.sleep(2)
        self.assertEqual(driver.current_url, "http://www.testfan.cn/page/20.htm", "没找到精品文章...")
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
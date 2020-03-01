# -*- coding: utf-8" -*


import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)


class TestowanieWifi(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_is_notification(self):
      # self.driver.find_element_by_accessibility_id('Views').click()
      lista=self.driver.find_elements_by_class_name('android.widget.TextView')
      print(len(lista))
      lista[11].click()
      sleep(5)
      self.driver.find_element_by_accessibility_id('Expandable Lists').click()
      self.driver.find_element_by_accessibility_id('1. Custom Adapter').click()
      el1=self.driver.find_element_by_xpath('//android.widget.TextView[@text="People Names"]')
      el1.click()




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieWifi)
    unittest.TextTestRunner(verbosity=2).run(suite)

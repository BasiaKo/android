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

    def test_is_app1_installed(self):
        self.driver.find_element_by_accessibility_id('Preference').click()
        elementy=self.driver.find_elements_by_class_name("android.widget.TextView")
        elementy[3].click()
        box=self.driver.find_element_by_class_name('android.widget.CheckBox')
        if(box.is_selected()!=True):
            box.click()

        self.assertTrue(box.is_selected)

def test_wifi_setting(self):
    self.driver.find_element_by_accessibility_id('Preference').click()
    elementy=self.driver.find_elements_by_class_name("android.widget.TextView")
    elementy[3].click()
    box=self.driver.find_element_by_class_name('android.widget.CheckBox')
    if(box.is_selected()!=True):
        box.click()
    elementy=self.driver.find_elements_by_class_name('android.widget.RelativeLayout')
    elementy[1].click()
    self.driver.find_element_by_id('android:id/edit').send_keys('haslo12345')
    self.driver.find_element_by_id('android:id/button1').click()
    self.driver.keyevent(4)
    self.driver.find_element_by_accessibility_id('3. Preference dependencies').click()
    is_chcecked=self.driver.find_element_by_class_name('android.widget.CheckBox').get_attribute('checkable')

    self.assertEqual(is_chcecked, 'true')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieWifi)
    unittest.TextTestRunner(verbosity=2).run(suite)

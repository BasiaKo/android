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
        # desired_caps['app'] = PATH('ApiDemos-debug.apk')
        # desired_caps['appPackage'] = 'io.appium.android.apis'
        # desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_is_notification(self):
        self.driver.open_notifications()
        self.driver.implicitly_wait(3)
        elements = self.driver.find_elements_by_id('android:id/notification_main_column')
        is_body_and_title_found = False
        for el in elements:
            title = el.find_element_by_id('android:id/title').text
            body = el.find_element_by_id('android:id/text').text
            print(title)
            print(body)
            if title == "USB debugging connected" and body == "Tap to disable USB debugging.":
                is_body_and_title_found = True

        self.assertTrue(is_body_and_title_found)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieWifi)
    unittest.TextTestRunner(verbosity=2).run(suite)
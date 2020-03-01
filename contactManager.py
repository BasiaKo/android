# -*- coding: utf-8" -*


import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)


class TestowanieAplikacjiCM(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_is_app1_installed(self):
        self.driver.find_element_by_accessibility_id('Add Contact').click()
        sleep(5)
        imie=self.driver.find_element_by_id('contactNameEditText')
        imie.send_keys('Basia')
        telefon=self.driver.find_element_by_id('contactPhoneEditText')
        telefon.send_keys('789789789')
        mail=self.driver.find_element_by_id('contactEmailEditText')
        mail.send_keys('ja@jam.pl')
        self.assertEqual(imie.text, "Basia")
        self.assertEqual(telefon.text, '789789789')
        self.assertEqual(mail.text, 'ja@jam.pl')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacjiCM)
    unittest.TextTestRunner(verbosity=2).run(suite)

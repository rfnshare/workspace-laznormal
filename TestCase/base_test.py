import unittest

from appium import webdriver

from TestConf.data import TestData


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities={
                "appium:appPackage": "com.daraz.android.dev",
                "appium:appActivity": "com.daraz.android.defaultIcon",
                'app': f"{TestData.DARAZ_APK}",
                "platformName": "Android",
                "appium:uid": "8210fc8a7d24",
                "automationName": "UIAutomator2",
                "autoGrantPermissions": "true",
                "skipLogcatCapture": "true",
            })

    def tearDown(self):
        self.driver.quit()

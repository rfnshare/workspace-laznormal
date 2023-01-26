from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from TestConf.data import TestData

from Utils.locators import *


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.home_locator = HomePageLocator
        self.notification_locator = NotificationsPageLocator
        self.locator = IntroPageLocator

    def wait(self, method, locator):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located((method, locator)))

    def go_to_home_page(self):
        driver = self.driver
        # sleep(2)
        # driver.find_element(AppiumBy.XPATH, self.locator.country).click()
        sleep(2)
        driver.find_element(AppiumBy.ID, self.locator.language).click()
        sleep(2)
        driver.find_element(AppiumBy.ID, self.locator.skip).click()
        sleep(15)
        self.wait(AppiumBy.ID, self.locator.location)
        driver.find_element(AppiumBy.ID, self.locator.location).click()

        sleep(5)

        try:
            driver.find_element(AppiumBy.ID, self.locator.add_skip).click()
            # element = driver.find_element(AppiumBy.ID, self.locator.add_skip).is_displayed()
            # print(element)
            # self.driver.execute_script("mobile: clickGesture", {'elementId': element, 'duration': 1000})
        except:
            return True

        sleep(5)

    def login(self):
        driver = self.driver
        sleep(2)
        # driver.find_element(AppiumBy.XPATH, self.home_locator.back).click()

        driver.find_element(AppiumBy.XPATH, self.home_locator.account_tab).click()
        self.wait(AppiumBy.ID, self.home_locator.login)
        driver.find_element(AppiumBy.ID, self.home_locator.login).click()
        self.wait(AppiumBy.ID, self.home_locator.signin_with_email)
        driver.find_element(AppiumBy.ID, self.home_locator.signin_with_email).click()
        sleep(5)
        driver.find_element(AppiumBy.XPATH, self.home_locator.email_field).send_keys(TestData.EMAIL)
        sleep(2)
        driver.find_element(AppiumBy.XPATH, self.home_locator.pass_field).send_keys(TestData.PASSWORD)
        sleep(2)
        driver.find_element(AppiumBy.ID, self.home_locator.final_login).click()
        sleep(5)
        self.wait(AppiumBy.ID, self.home_locator.val_name)
        text = driver.find_element(AppiumBy.ID, self.home_locator.val_name).text
        assert "COV" in text

    def change_to_stage(self):
        driver = self.driver
        sleep(5)
        driver.open_notifications()
        sleep(5)
        list_of_notification = driver.find_elements(AppiumBy.ID, self.notification_locator.check_notifications)
        print(len(list_of_notification))
        if len(list_of_notification) > 0:
            driver.find_element(AppiumBy.XPATH, self.notification_locator.entry).click()
        else:
            return False
        # sleep(10)
        self.wait(AppiumBy.XPATH, self.notification_locator.mtop)
        driver.find_element(AppiumBy.XPATH, self.notification_locator.mtop).click()
        driver.find_element(AppiumBy.XPATH, self.notification_locator.stage_option).click()

    def change_to_online(self):
        driver = self.driver
        sleep(5)
        driver.open_notifications()
        sleep(5)
        list_of_notification = driver.find_elements(AppiumBy.ID, self.notification_locator.check_notifications)
        print(len(list_of_notification))
        if len(list_of_notification) > 0:
            driver.find_element(AppiumBy.XPATH, self.notification_locator.entry).click()
        else:
            return False
        # sleep(10)
        self.wait(AppiumBy.XPATH, self.notification_locator.mtop)
        driver.find_element(AppiumBy.XPATH, self.notification_locator.mtop).click()
        driver.find_element(AppiumBy.XPATH, self.notification_locator.online_option).click()


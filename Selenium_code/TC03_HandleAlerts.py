import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Selenium_code.Login import Login
from Selenium_code.Logout import Logout
from funcUtils.funcUtils import funcUtils
from commonUtils.comUtils import commonUtilities
from objectRepo.objRepo import objRepo

class TC03_HandleAlerts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cu = commonUtilities()
        cls.OR = objRepo()
        # cls.login = Login()
        # cls.logout = Logout()
        # cls.driver = cls.login.login("user", "password123")
        cls.properties = cls.cu.readPropertyFile("config.properties")
        cls.driver = cls.cu.getDriver(cls.properties['browser'])

    # def getDriver(self):
    #     return self.driver
    #
    # def setDriver(self, driver):
    #     self.driver = driver

    def test_TC1_handleSimpleAlert(self):
        self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
        self.driver.find_element(By.CLASS_NAME, "btn.btn-default").click()
        alertBox = self.driver.switch_to.alert
        print(alertBox.text)
        alertBox.accept()

    def test_TC2_handleConfirmationAlert(self):
        self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
        self.driver.find_element(By.CLASS_NAME, "btn.btn-default.btn-lg").click()
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.dismiss()
        msgElement = self.driver.find_element(By.ID, "confirm-demo")
        print(msgElement.is_displayed())
        print("what happened?", msgElement.text)
        self.driver.find_element(By.CLASS_NAME, "btn.btn-default.btn-lg").click()
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()
        print("what happened?", msgElement.text)

    def test_TC3_handleInputPromptAlert(self):
        self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
        self.driver.find_element(By.XPATH, "//button[text()='Click for Prompt Box']").click()
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.dismiss()
        msgElement = self.driver.find_element(By.ID, "prompt-demo")
        print(msgElement.is_displayed())
        print("what happened?", msgElement.text)
        self.driver.find_element(By.XPATH, "//button[text()='Click for Prompt Box']").click()
        alert = self.driver.switch_to.alert
        alert.send_keys("ABCDEFGH")
        print(alert.text)
        alert.accept()
        print("what happened?", msgElement.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        # cls.logout.logout(cls.driver)


if __name__ == '__main__':
    unittest.main()

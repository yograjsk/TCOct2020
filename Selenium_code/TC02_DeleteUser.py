import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Selenium_code.Login import Login
from Selenium_code.Logout import Logout
from funcUtils.funcUtils import funcUtils
from commonUtils.comUtils import commonUtilities
from objectRepo.objRepo import objRepo

class TC02_DeleteUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cu = commonUtilities()
        cls.OR = objRepo()
        cls.login = Login()
        cls.logout = Logout()
        cls.driver = cls.login.login("user", "password123")
        cls.properties = cls.cu.readPropertyFile("config.properties")

    def getDriver(self):
        return self.driver

    def setDriver(self, driver):
        self.driver = driver

    def test_deleteUser(self):
        username = self.properties['user']
        # self.fu.searchUserByUsername(username)
        self.cu.menuNav(self.driver, "Admin", "User Management", "Users")
        self.cu.sendKeysToElement(self.driver, self.OR.searchUserTxt, username)
        self.cu.clickElement(self.driver, self.OR.searchBtn)
        locatorTuple = (By.XPATH, "//a[text()='"+username+"']/ancestor::tr//input")
        self.cu.selectCheckbox(self.driver, locatorTuple)
        self.cu.clickElement(self.driver, self.OR.deleteBtn)
        print(">>>>>",self.cu.checkElementPresent(self.driver, self.OR.alertOK))
        self.cu.clickElement(self.driver, self.OR.alertOK)
        # self.fu.searchUserByUsername(username)
        self.cu.menuNav(self.driver, "Admin", "User Management", "Users")
        self.cu.sendKeysToElement(self.driver, self.OR.searchUserTxt, username)
        self.cu.clickElement(self.driver, self.OR.searchBtn)
        resultTextElement = (By.XPATH, "//table[@id='resultTable']/tbody//td")
        text = self.cu.getText(self.driver, resultTextElement)
        print(text)
        assert self.cu.getText(self.driver, resultTextElement) == "No Records Found"

    @classmethod
    def tearDownClass(cls):
        cls.logout.logout(cls.driver)


if __name__ == '__main__':
    unittest.main()


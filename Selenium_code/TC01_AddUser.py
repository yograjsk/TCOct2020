import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Selenium_code.Login import Login
from Selenium_code.Logout import Logout
from funcUtils.funcUtils import funcUtils
from commonUtils.comUtils import commonUtilities
from objectRepo.objRepo import objRepo

class TC01_AddUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cu = commonUtilities()
        cls.OR = objRepo()
        cls.login = Login()
        cls.logout = Logout()
        cls.driver = cls.login.login("user", "password123")

    def getDriver(self):
        return self.driver

    def setDriver(self, driver):
        self.driver = driver

    def test_addUser(self):
        self.cu.menuNav(self.driver, "Admin", "User Management", "Users")
        self.cu.clickElement(self.driver, self.OR.addUserBtn)
        self.cu.sendKeysToElement(self.driver, self.OR.employeeNameTxt, "testAdminAuto1 m last")
        self.cu.sendKeysToElement(self.driver, self.OR.usernameTxt, "OrangeTest")
        self.cu.sendKeysToElement(self.driver, self.OR.passwordTxt, "admin123")
        self.cu.sendKeysToElement(self.driver, self.OR.confirmPasswordTxt, "admin123")
        # self.cu.clickElement(self.driver, self.OR.saveBtn)
        self.cu.clickElementByAction(self.driver, self.OR.saveBtn)
        print("checking username field",self.cu.checkElementPresent(self.driver, (By.ID, "searchSystemUser_userName")))
        self.cu.sendKeysToElement(self.driver, self.OR.searchUserTxt, "OrangeTest")
        self.cu.clickElement(self.driver, self.OR.searchBtn)

    @classmethod
    def tearDownClass(cls):
        cls.logout.logout(cls.driver)


if __name__ == '__main__':
    unittest.main()


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Selenium_code.Login import Login
from Selenium_code.Logout import Logout
from funcUtils.funcUtils import funcUtils
from commonUtils.comUtils import commonUtilities
from objectRepo.objRepo import objRepo

class TC04_DownloadUploadCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cu = commonUtilities()
        cls.OR = objRepo()
        cls.login = Login()
        cls.logout = Logout()
        cls.driver = cls.login.login("user", "password123")

    def test_TC1_verifyDownload(self):
        self.cu.menuNav(self.driver, "PIM", "Configuration", "Data Import")
        # self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/admin/pimCsvImport")
        self.driver.find_element(By.LINK_TEXT, "Download").click()

    def test_TC2_verifyUpload(self):
        self.cu.menuNav(self.driver, "PIM", "Configuration", "Data Import")
        # self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/admin/pimCsvImport")
        self.driver.find_element(By.ID, "pimCsvImport_csvFile").send_keys("C:/Users/USER/PycharmProjects/TCOct2020/backup/resources/importData.csv")
        self.driver.find_element(By.ID, "btnSave").click()

    @classmethod
    def tearDownClass(cls):
        cls.logout.logout(cls.driver)


if __name__ == '__main__':
    unittest.main()

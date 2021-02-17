import unittest
from selenium.webdriver.common.by import By

from Selenium_code.Login import Login
from Selenium_code.Logout import Logout
from commonUtils.comUtils import commonUtilities
from commonUtils.Constants import Constants
from objectRepo.objRepo import objRepo

class TC02_DeleteLocation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cu = commonUtilities()
        cls.OR = objRepo()
        const = Constants()
        cls.login = Login()
        cls.logout = Logout()
        cls.driver = cls.login.login("user", "password123")
        cls.properties = cls.cu.readPropertyFile(const.propFilePath)

    def test_deleteLocation(self):
        location = "Mumbai"
        self.cu.menuNav(self.driver, "Admin", "Organization", "Locations")
        self.cu.clickElement(self.driver, (By.XPATH, "//table[@id='resultTable']//td/a[text()='"+location+"']/../..//input"))
        self.cu.clickElement(self.driver, (By.ID, "btnDelete"))
        self.cu.clickElement(self.driver, (By.ID, "dialogDeleteBtn"))
        self.driver.save_screenshot("evidences/DeleteLocation")
        self.assertTrue(self.driver.find_element(By.ID, "btnDelete"))

    @classmethod
    def tearDownClass(cls):
        cls.logout.logout(cls.driver)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


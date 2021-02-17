import unittest
from selenium.webdriver.common.by import By

from Selenium_code.Login import Login
from Selenium_code.Logout import Logout
from commonUtils.comUtils import commonUtilities
from commonUtils.Constants import Constants
from objectRepo.objRepo import objRepo

class TC01_AddLocation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cu = commonUtilities()
        cls.OR = objRepo()
        const = Constants()
        cls.login = Login()
        cls.logout = Logout()
        cls.driver = cls.login.login("user", "password123")
        # cls.properties = cls.cu.readPropertyFile("config.properties")
        cls.properties = cls.cu.readPropertyFile(const.propFilePath)

    def test_addLocation(self):
        location = "Mumbai"
        self.cu.menuNav(self.driver, "Admin", "Organization", "Locations")
        self.cu.clickElement(self.driver, self.OR.addUserBtn)
        self.cu.sendKeysToElement(self.driver, (By.ID, "location_name"), location)
        self.cu.selectDropdown(self.driver, (By.ID, "location_country"), "India")
        self.cu.sendKeysToElement(self.driver, (By.ID, "location_province"), "Maharashtra")
        self.cu.sendKeysToElement(self.driver, (By.ID, "location_city"), location)
        self.cu.sendKeysToElement(self.driver, (By.ID, "location_address"), "Goregaon, Mumbai, Maharashtra.\nIndia")
        self.cu.sendKeysToElement(self.driver, (By.ID, "location_zipCode"), "123456")
        self.cu.sendKeysToElement(self.driver, (By.ID, "location_phone"), "9876543210")
        self.cu.sendKeysToElement(self.driver, (By.ID, "location_fax"), "123123123")
        self.cu.sendKeysToElement(self.driver, (By.ID, "location_notes"), "Sample Notes for location details")
        self.cu.clickElement(self.driver, self.OR.saveBtn)
        # self.driver.save_screenshot("evidences/AddLocation")
        self.cu.takeScreenshot(self.driver, "AddLocation.png")
        self.assertTrue(self.driver.find_element(By.XPATH, "//table[@id='resultTable']//td/a[text()='"+location+"']"))

    @classmethod
    def tearDownClass(cls):
        cls.logout.logout(cls.driver)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


from selenium.webdriver.common.by import By

from commonUtils.comUtils import commonUtilities
from objectRepo.objRepo import objRepo

class funcUtils(commonUtilities, objRepo):

    def login(self):
        cu = commonUtilities
        self.driver = cu.getDriver("chrome")
        self.driver.get(self.url)
        print("verify login page is available", self.cu.checkElementPresent(self.driver, self.OR.username))
        # self.cu.sendKeysToElement(self.driver, By.NAME, "txtUsername", "admin")
        # self.cu.sendKeysToElement(self.driver, (By.NAME, "txtUsername"), "admin")
        # self.cu.sendKeysToElement(self.driver, (self.OR.username), "admin")
        self.cu.sendKeysToElementByAction(self.driver, (self.OR.username), "admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.cu.clickElement(self.driver, By.ID, "btnLogin")
        check = self.cu.checkElementPresent(self.driver, self.OR.logout)


    def logout(self):
        print("tearDown method - logging out")
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")
        lblWelcome = self.driver.find_element_by_id("welcome")
        lblWelcome.click()
        lnkLogout = self.driver.find_element_by_link_text("Logout")
        lnkLogout.click()


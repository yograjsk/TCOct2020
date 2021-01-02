from selenium.webdriver.common.by import By

from commonUtils.comUtils import commonUtilities
from objectRepo.objRepo import objRepo

class funcUtils(commonUtilities, objRepo):

    def login(self, username, password):
        cu = commonUtilities()
        OR = objRepo()
        self.driver = cu.getDriver("chrome")
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/auth/login")
        print("verify login page is available", self.cu.checkElementPresent(self.driver, OR.username))
        # self.cu.sendKeysToElement(self.driver, By.NAME, "txtUsername", "admin")
        # self.cu.sendKeysToElement(self.driver, (By.NAME, "txtUsername"), "admin")
        # self.cu.sendKeysToElement(self.driver, (self.OR.username), "admin")
        self.cu.sendKeysToElementByAction(self.driver, (OR.username), username)
        self.driver.find_element_by_name("txtPassword").send_keys(password)
        self.cu.clickElement(self.driver, By.ID, "btnLogin")
        check = self.cu.checkElementPresent(self.driver, OR.logout)
        return self.driver


    def logout(self):
        print("tearDown method - logging out")
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")
        lblWelcome = self.driver.find_element_by_id("welcome")
        lblWelcome.click()
        lnkLogout = self.driver.find_element_by_link_text("Logout")
        lnkLogout.click()

    def searchUserByUsername(self, username, driver):
        self.cu.menuNav(driver, "Admin", "User Management", "Users")
        self.cu.sendKeysToElement(driver, self.OR.searchUserTxt, username)
        self.cu.clickElement(driver, self.OR.searchBtn)

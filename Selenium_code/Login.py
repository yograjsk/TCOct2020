from selenium.webdriver.common.by import By

from commonUtils.comUtils import commonUtilities
from objectRepo.objRepo import objRepo


class Login():

    def login(self, username, password):
        cu = commonUtilities()
        OR = objRepo()
        self.driver = cu.getDriver("chrome")
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/auth/login")
        print("verify login page is available", cu.checkElementPresent(self.driver, OR.username))
        # self.cu.sendKeysToElement(self.driver, By.NAME, "txtUsername", "admin")
        # self.cu.sendKeysToElement(self.driver, (By.NAME, "txtUsername"), "admin")
        # self.cu.sendKeysToElement(self.driver, (self.OR.username), "admin")
        cu.sendKeysToElementByAction(self.driver, (OR.username), username)
        self.driver.find_element_by_name("txtPassword").send_keys(password)
        cu.clickElement(self.driver, (By.ID, "btnLogin"))
        check = cu.checkElementPresent(self.driver, OR.welcomePage.welcomeLogo)
        return self.driver
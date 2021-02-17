from selenium.webdriver.common.by import By

from commonUtils.comUtils import commonUtilities
from objectRepo.objRepo import objRepo
from commonUtils.Constants import Constants


class Login():

    def login(self, username, password):
        cu = commonUtilities()
        OR = objRepo()
        const = Constants()
        properties = cu.readPropertyFile(const.propFilePath)
        self.driver = cu.getDriver(properties)
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/auth/login")
        print("verify login page is available", cu.checkElementPresent(self.driver, OR.username))
        cu.sendKeysToElementByAction(self.driver, (OR.username), username)
        self.driver.find_element_by_name("txtPassword").send_keys(password)
        cu.clickElement(self.driver, (By.ID, "btnLogin"))
        assert cu.checkElementPresent(self.driver, OR.welcomePage.welcomeLogo) is True
        return self.driver


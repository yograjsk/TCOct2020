import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from commonUtils.comUtils import commonUtilities
from objectRepo.objRepo import objRepo

class unittest_example(unittest.TestCase):
    cu = commonUtilities()
    OR = objRepo()

    @classmethod
    def setUpClass(self):
        print("setUpClass method - creating the driver instance")
        # self.readPropFile("config.properties")
        # self.readPropFile("C:\\Users\\USER\PycharmProjects\\TCOct2020\\Selenium_code\\config.properties")

        # filePath = "config.properties"
        prop = self.cu.readPropertyFile("config.properties")
        print(prop["browser"])
        print(prop["impliciteTime"])
        print(prop["headless"])
        # data = open(filePath, 'r')
        # prop = dict(i.strip().split("=") for i in data)
        # dictNew = None
        # for a in data:
        #     dictNew = dict(a.strip().split("="))

        self.driver = self.cu.getDriver(prop["browser"])
        self.driver.implicitly_wait(prop["impliciteTime"])
        self.url = "https://opensource-demo.orangehrmlive.com/"
        self.action = ActionChains(self.driver)

    def setUp(self):
        print("setUp method - logging into the application")
        self.driver.get(self.url)
        print("verify login page is available", self.cu.checkElementPresent(self.driver, self.OR.username))
        # self.cu.sendKeysToElement(self.driver, By.NAME, "txtUsername", "admin")
        # self.cu.sendKeysToElement(self.driver, (By.NAME, "txtUsername"), "admin")
        # self.cu.sendKeysToElement(self.driver, (self.OR.username), "admin")
        self.cu.sendKeysToElementByAction(self.driver, (self.OR.username), "admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.cu.clickElement(self.driver, (By.ID, "btnLogin"))
        check = self.cu.checkElementPresent(self.driver, self.OR.welcomePage.welcomeLogo)
        print("Verify login is successful:", check)

    def readPropFile(self, filePath):
        data = open(filePath, 'r')
        for i in data:
            print(i)

    def tearDown(self):
        print("tearDown method - logging out")
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")
        lblWelcome = self.driver.find_element_by_id("welcome")
        lblWelcome.click()
        lnkLogout = self.driver.find_element_by_link_text("Logout")
        lnkLogout.click()

    @classmethod
    def tearDownClass(self):
        print("setDownClass method - quiting driver instance")
        self.driver.quit()

    def test_addUser(self):
        self.cu.menuNav(self.driver, "Admin", "User Management", "Users")
        self.cu.clickElement(self.driver, self.OR.addUserBtn)
        self.cu.sendKeysToElement(self.driver, self.OR.employeeNameTxt, "Orange Test")
        self.cu.sendKeysToElement(self.driver, self.OR.usernameTxt, "OrangeTest")
        self.cu.sendKeysToElement(self.driver, self.OR.passwordTxt, "admin123")
        self.cu.sendKeysToElement(self.driver, self.OR.confirmPasswordTxt, "admin123")
        self.cu.clickElement(self.driver, self.OR.saveBtn)
        print("checking username field",self.cu.checkElementPresent(self.driver, (By.ID, "searchSystemUser_userName")))
        self.cu.sendKeysToElement(self.driver, self.OR.searchUserTxt, "OrangeTest")
        self.cu.clickElement(self.driver, self.OR.searchBtn)


    def test_rightClick(self):
        # self.driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
        self.driver.get("http://demo.guru99.com/test/simple_context_menu.html")
        # check = self.driver.find_element_by_class_name("context-menu-one btn.btn-neutral").is_displayed()
        button = self.driver.find_element(By.XPATH, "//span[text()='right click me']")
        check = button.is_displayed()
        print(check)
        self.cu.rightClickOnElement(self.driver, (By.XPATH, "//span[text()='right click me']"))
        print(self.cu.checkElementPresent(self.driver, (By.XPATH, "//span[text()='Edit']")))
        # self.cu.clickElement(self.driver, (By.XPATH, "//span[text()='Edit']"))
        # self.cu.clickElement(self.driver, (By.XPATH, "//li[contains(@class,'context-menu-icon-edit')]"))
        # self.action.context_click(button)
        # self.action.move_to_element(button).context_click()
        # self.action.perform()
        # self.action.context_click(button).perform()
        self.cu.doubleClickOnElement(self.driver, (By.XPATH, "//button[text()='right click meDouble-Click Me To See Alert']"))
        alert = self.driver.switch_to.alert()
        print(alert.text)
        alert.accept()

    def test_doubleClick(self):
        self.driver.get("http://demo.guru99.com/test/simple_context_menu.html")
        self.cu.doubleClickOnElement(self.driver, (By.XPATH, "//button[text()='right click meDouble-Click Me To See Alert']"))
        alert = self.driver.switch_to.alert()
        print(alert.text)
        alert.accept()

    def test_TC1_verifyWelcomePageAvailable(self):
        print("test medhod: verifying if the welcome page is available after successful login")
        check = self.cu.checkElementPresent(self.driver, self.OR.welcomePage.welcomeLogo)
        print(check)
        checkWelcome = self.driver.find_element_by_id("welcome").is_displayed()
        print("check welcome page is available", checkWelcome)
        self.cu.menuNavigation(self.driver, self.action, "PIM", "Configuration", "Optional Fields")


    def test_TC2_verifyWelcomePage(self):
        print("TC2 method - unit test method")

    def test_TC3_verifyLogout(self):
        print("TC3 method - unit test method")

    def test_TC4_verifyDownload(self):
        print("TC5 method - unit test method")
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
        self.driver.find_element(By.LINK_TEXT, "Download").click()

    def test_TC5_verifyUpload(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
        self.driver.find_element(By.ID, "pimCsvImport_csvFile").send_keys("C:/Users/USER/PycharmProjects/TCOct2020/backup/resources/importData.csv")
        self.driver.find_element(By.ID, "btnSave").click()

    def test_TC6_handleSimpleAlert(self):
        self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
        self.driver.find_element(By.CLASS_NAME, "btn.btn-default").click()
        # self.driver.switch_to_alert()
        alertBox = self.driver.switch_to.alert
        print(alertBox.text)
        alertBox.accept()

    def test_TC5_handleConfirmationAlert(self):
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

    def test_TC6_handleInputPromptAlert(self):
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


if __name__ == '__main__':
    unittest.main()


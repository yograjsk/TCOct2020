from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class commonUtilities():

    props = {}

    def clickElement(self, driver, locatorTuple):
        driver.find_element(locatorTuple[0], locatorTuple[1]).click()

    def getText(self, driver, locatorTuple):
        return driver.find_element(locatorTuple[0], locatorTuple[1]).text

    def selectCheckbox(self, driver, locatorTuple):
        if not self.getElement(driver, locatorTuple).is_selected():
            self.clickElement(driver, locatorTuple)

    def deselectCheckbox(self, driver, locatorTuple):
        if self.getElement(driver, locatorTuple).is_selected():
            self.clickElement(driver, locatorTuple)

    def sendKeysToElement(self, driver, locatorTuple, textToPass):
        driver.find_element(locatorTuple[0], locatorTuple[1]).send_keys(textToPass)

    def selectDropdown(self, driver, locatorTuple, dropdownValue):
        elementFound = driver.find_element(locatorTuple[0], locatorTuple[1]).is_displayed()
        dropdown = Select(driver.find_element(locatorTuple[0], locatorTuple[1]))
        # dropdown.select_by_value(dropdownValue)
        dropdown.select_by_visible_text(dropdownValue)

    def sendKeysToElementByAction(self, driver, identifierTpl, textToPass):
        action = ActionChains(driver)
        element = driver.find_element(identifierTpl[0], identifierTpl[1])
        action.send_keys_to_element(element, textToPass)
        action.perform()

    def rightClickOnElement(self, driver, locatorTuple):
        action = ActionChains(driver)
        element = driver.find_element(locatorTuple[0], locatorTuple[1])
        action.context_click(element)
        action.perform()

    def doubleClickOnElement(self, driver, locatorTuple):
        action = ActionChains(driver)
        element = driver.find_element(locatorTuple[0], locatorTuple[1])
        action.double_click(element)
        action.perform()

    def getElement(self, driver, locatorTuple):
        return driver.find_element(locatorTuple[0], locatorTuple[1])

    def checkElementPresent(self, driver, locatorTuple):
        return driver.find_element(locatorTuple[0], locatorTuple[1]).is_displayed()

    def getDriver(self, properties):
        browserName = properties['browser']
        headless = properties['headless']
        if browserName.lower() in ('chrome', "chromeheadless"):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximize")
            # chrome_options.add_argument("--window-size=1920,1024")
            if headless.lower() == "true":
                chrome_options.add_argument("--headless")
            # return webdriver.Chrome(chrome_options=chrome_options, executable_path='../drivers/chromedriver.exe')
            return webdriver.Chrome(chrome_options=chrome_options, executable_path='drivers/chromedriver.exe')
        elif browserName in ('firefox', 'ff', 'FireFox'):
            return webdriver.Firefox(executable_path='./drivers/geckodriver.exe')
        else:
            raise Exception("Invalid browser value passed")

    def menuNavigation(self, driver, action, *menus):
        for menuitem in menus:
            action.move_to_element(driver.find_element_by_link_text(menuitem)).perform()
        action.click()
        action.perform()

    def menuNav(self, driver, *menuItems):
        #     Admin, User Management, Users
        action = ActionChains(driver)
        for menu in menuItems:
            action.move_to_element(driver.find_element(By.LINK_TEXT, menu))
            action.perform()
        action.click()
        action.perform()

    def readPropertyFile(self, filePath):
        print("prop file path:", filePath)
        data = open(filePath, 'r')
        prop = dict(i.strip().split("=") for i in data)
        return prop

    def setProperties(self, properties):
        self.props = properties

    def getProperties(self):
        return self.props




from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class commonUtilities():

    # def clickElement(self, driver, byType, byValue):
    #     driver.find_element(byType, byValue).click()

    def clickElement(self, driver, locatorTuple):
        driver.find_element(locatorTuple[0], locatorTuple[1]).click()

    # def sendKeysToElement(self, driver, byType, byValue, textToPass):
    #     driver.find_element(byType, byValue).send_keys(textToPass)

    def sendKeysToElement(self, driver, identifierTpl, textToPass):
        driver.find_element(identifierTpl[0], identifierTpl[1]).send_keys(textToPass)

    def sendKeysToElementByAction(self, driver, identifierTpl, textToPass):
        action = ActionChains(driver)
        element = driver.find_element(identifierTpl[0], identifierTpl[1])
        action.send_keys_to_element(element, textToPass)
        action.perform()
        # driver.find_element(identifierTpl[0], identifierTpl[1]).send_keys(textToPass)

    def rightClickOnElement(self, driver, identifierTpl):
        action = ActionChains(driver)
        element = driver.find_element(identifierTpl[0], identifierTpl[1])
        action.context_click(element)
        action.perform()

    def doubleClickOnElement(self, driver, identifierTpl):
        action = ActionChains(driver)
        element = driver.find_element(identifierTpl[0], identifierTpl[1])
        action.double_click(element)
        action.perform()

    def getElement(self, driver, identifierTpl):
        return driver.find_element(identifierTpl[0], identifierTpl[1])

    def checkElementPresent(self, driver, identifierTuple):
        return driver.find_element(identifierTuple[0], identifierTuple[1]).is_displayed()

    def getDriver(self, browserName):
        if browserName in ('chrome', 'Chrome', "CHROME"):
            return webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        elif browserName in ('firefox', 'ff', 'FireFox'):
            return webdriver.Firefox(executable_path='../drivers/geckodriver.exe')
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
        data = open(filePath, 'r')
        prop = dict(i.strip().split("=") for i in data)
        print(prop)
        return prop

    def readPropFile(self, filePath):
        fileData = list(open(filePath, 'r'))
        props = dict(p.strip().split('=') for p in fileData)
        return props






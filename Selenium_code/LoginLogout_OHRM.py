
from selenium import webdriver
import time

class OHRM_Cases:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.url = "https://opensource-demo.orangehrmlive.com/"

    def login(self, username, password):
        self.driver.get(self.url)
        txtUsername = self.driver.find_element_by_name("txtUsername")
        txtPassword = self.driver.find_element_by_name("txtPassword")
        btnLogin = self.driver.find_element_by_id("btnLogin")

        print(self.driver.title)
        txtUsername.send_keys(username)
        txtPassword.send_keys(password)
        btnLogin.click()
        lblWelcome = self.driver.find_element_by_id("welcome")

        checkWelcome = lblWelcome.is_displayed()
        if checkWelcome:
            print("Login successful")
        else:
            print("Login Faild")

    def logout(self):
        lblWelcome = self.driver.find_element_by_id("welcome")
        lblWelcome.click()
        lnkLogout = self.driver.find_element_by_link_text("Logout")
        lnkLogout.click()
        self.driver.quit()

ohrm = OHRM_Cases()
ohrm.login("Admin", "admin123")
ohrm.logout()

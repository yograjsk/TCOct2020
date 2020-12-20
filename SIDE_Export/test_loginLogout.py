# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLoginLogout():
  def setup_method(self, method):
    # self.driver = webdriver.Chrome(executable_path='C:\\Users\\USER\\PycharmProjects\\TCOct2020\\SIDE_Export\\drivers\\chromedriver.exe')
    # self.driver = webdriver.Chrome(executable_path='C:/Users/USER/PycharmProjects/TCOct2020/SIDE_Export/drivers/chromedriver.exe')
    self.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    # self.driver = webdriver.Firefox(executable_path='drivers/geckodriver.exe')
    # self.driver = webdriver.Ie(executable_path='drivers/IEDriverServer.exe')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loginLogout(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/")
    self.driver.set_window_size(1382, 784)
    self.driver.find_element(By.ID, "frmLogin").click()
    self.driver.find_element(By.ID, "frmLogin").click()
    self.driver.find_element(By.ID, "txtUsername").click()
    self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    self.driver.find_element(By.ID, "txtPassword").send_keys("admin1234")
    self.driver.find_element(By.ID, "btnLogin").click()
    self.driver.find_element(By.ID, "spanMessage").click()
    self.driver.find_element(By.ID, "divLoginButton").click()
    self.driver.find_element(By.ID, "txtUsername").click()
    self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    self.driver.find_element(By.ID, "btnLogin").click()
    self.driver.find_element(By.ID, "welcome").click()
    self.driver.find_element(By.CSS_SELECTOR, ".inner").click()
    self.driver.find_element(By.ID, "welcome").click()

  
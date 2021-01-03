


class Logout():

    def logout(self, driver):
        print("tearDown method - logging out")
        # driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")
        lblWelcome = driver.find_element_by_id("welcome")
        lblWelcome.click()
        lnkLogout = driver.find_element_by_link_text("Logout")
        lnkLogout.click()
        # driver.quit()
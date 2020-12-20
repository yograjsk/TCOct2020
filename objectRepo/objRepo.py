from selenium.webdriver.common.by import By


class objRepo:

    username = (By.NAME, "txtUsername")
    password = (By.NAME, "txtPassword")
    # logout = (By.LINK_TEXT, "Logout")
    logout = (By.XPATH, "//a[@href='/index.php/auth/logout']")

    class welcomePage:
        welcomeLogo = (By.ID, "welcome")
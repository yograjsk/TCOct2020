from selenium.webdriver.common.by import By


class objRepo:

    username = (By.NAME, "txtUsername")
    password = (By.NAME, "txtPassword")
    logout = (By.XPATH, "//a[@href='/index.php/auth/logout']")
    addUserBtn = (By.ID, "btnAdd")
    employeeNameTxt = (By.ID, "systemUser_employeeName_empName")
    usernameTxt = (By.ID, "systemUser_userName")
    passwordTxt = (By.ID, "systemUser_password")
    confirmPasswordTxt = (By.ID, "systemUser_confirmPassword")
    saveBtn = (By.NAME, "btnSave")
    searchUserTxt = (By.ID, "searchSystemUser_userName")
    searchBtn = (By.ID, "searchBtn")
    deleteBtn = (By.ID, "btnDelete")
    alertOK = (By.ID, "dialogDeleteBtn")
    alertCancel = (By.XPATH, "//input[@value='Cancel']")



    class welcomePage:
        welcomeLogo = (By.ID, "welcome")
        # self.OR.welcomePage.welcomeLogo
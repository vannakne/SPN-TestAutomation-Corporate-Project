from selenium.webdriver.common.by import By


class HomePage:
    text_userID_id = 'crpusr__BasePage__DB_UserName'
    text_corporateID_id = 'crpusr__BasePage__DB_CorpName'
    text_lastLogin_id = 'crpusr__BasePage__DB_LastLogin'
    button_menu_id = 'crpusr__BasePage__menuButton'
    button_belt_notification_id = 'crpusr__BasePage__el_btn_3'

    def __init__(self, driver):
        self.driver = driver

    def getCorporateID(self):
        corpID = self.driver.find_element(By.ID, self.text_corporateID_id).text
        return corpID

    def getUserID(self):
        userId = self.driver.find_element(By.ID, self.text_userID_id).text
        return userId

    def getLastLogin(self):
        lastLogin = self.driver.find_element(By.ID, self.text_lastLogin_id).text
        return lastLogin

    def clickMenu(self):
        self.driver.find_element(By.ID, self.button_menu_id).click()

    def clickBeltNotification(self):
        self.driver.find_element(By.ID, self.button_belt_notification_id).click()
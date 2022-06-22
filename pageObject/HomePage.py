from time import sleep

from selenium.webdriver.common.by import By


class HomePage:
    text_userID_id = 'crpusr__BasePage__DB_UserName'
    text_corporateID_id = 'crpusr__BasePage__DB_CorpName'
    text_lastLogin_id = 'crpusr__BasePage__DB_LastLogin'
    button_menu_id = 'crpusr__BasePage__menuButton'
    button_belt_notification_id = 'crpusr__BasePage__el_btn_3'

    # Bill Payment
    text_acc_00021832_balance_id = 'dshbrd__DB_AcctList__i__acctList__balanceAmt_1_txtcnt'


    # Waller & Card transfer
    button_quick_link_wallet_id = 'dshbrd__DB_QckLink__i__DashBrdLinks__linkDesc_0_txtcnt'

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

    def getAccountBalance(self):
        acc_balance = self.driver.find_element(By.ID, self.text_acc_00021832_balance_id).text
        acc_balance = acc_balance.replace(',', '')
        return float(acc_balance)

    def clickWalletAndCard(self):
        self.driver.find_element(By.ID, self.button_quick_link_wallet_id).click()
        sleep(1.5)
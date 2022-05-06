from time import sleep
from selenium.webdriver.common.by import By


class Menu:
    button_menu_id = 'crpusr__BasePage__menuButton'
    button_closeMenu_id = 'crpusr__BasePage__el_btn_7'
    button_home_id = 'ui-id-1'
    button_account_id = 'ui-id-2'

    ## Payment
    button_payment_id = 'ui-id-3'
    button_payment_under_payment_id = 'crpusr__BasePage__ct_mnu_2_UJJ_MENU_PAYMENT_li'

    button_transfer_id = 'ui-id-4'
    button_wallet_and_card_Transfer_id = 'ui-id-5'
    button_mobile_topUp_id = 'ui-id-6'
    button_sending_instructions_id = 'ui-id-7'
    button_services_id = 'ui-id-8'
    button_retail_pay_id = 'ui-id-9'
    button_CBCHealth_check_id = 'ui-id-10'
    button_sweep_in_out_id = 'ui-id-11'
    button_payrolls_id = 'ui-id-12'
    button_cash_management_id = 'ui-id-13'
    button_setting_id = 'ui-id-15'
    button_logout_id = 'ui-id-16'

    def __init__(self, driver):
        self.driver = driver

    def clickMenu(self):
        self.driver.find_element(By.ID, self.button_menu_id).click()

    def click_closeMenu_button(self):
        self.driver.find_element(By.ID, self.button_closeMenu_id).click()

    def click_home_button(self):
        self.driver.find_element(By.ID, self.button_home_id).click()

    def click_account_button(self):
        self.driver.find_element(By.ID, self.button_account_id).click()

    def click_payment_button(self):
        self.driver.find_element(By.ID, self.button_payment_id).click()

    def click_payment_under_payment(self):
        self.driver.find_element(By.ID, self.button_payment_under_payment_id).click()

    def click_transfer_button(self):
        self.driver.find_element(By.ID, self.button_transfer_id).click()

    def click_wallet_and_card_Transfer_button(self):
        self.driver.find_element(By.ID, self.button_wallet_and_card_Transfer_id).click()

    def click_mobile_topUp_button(self):
        self.driver.find_element(By.ID, self.button_mobile_topUp_id).click()

    def click_sending_instructions_button(self):
        self.driver.find_element(By.ID, self.button_sending_instructions_id).click()

    def scrollDown(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(1)

    def click_services_button(self):
        self.scrollDown()
        self.driver.find_element(By.ID, self.button_services_id).click()

    def click_retail_pay_button(self):
        self.scrollDown()
        self.driver.find_element(By.ID, self.button_retail_pay_id).click()

    def click_CBCHealth_check_button(self):
        self.scrollDown()
        self.driver.find_element(By.ID, self.button_CBCHealth_check_id)

    def click_sweep_in_out_button(self):
        self.scrollDown()
        self.driver.find_element(By.ID, self.button_sweep_in_out_id).click()

    def click_payroll_button(self):
        self.scrollDown()
        self.driver.find_element(By.ID, self.button_payrolls_id).click()

    def click_cash_management_button(self):
        self.scrollDown()
        self.driver.find_element(By.ID, self.button_cash_management_id).click()

    def click_setting_button(self):
        self.scrollDown()
        self.driver.find_element(By.ID, self.button_setting_id).click()

    def click_logout_button(self):
        self.scrollDown()
        self.driver.find_element(By.ID, self.button_logout_id).click()
        
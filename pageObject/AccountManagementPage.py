from time import sleep
from selenium.webdriver.common.by import By

class SourceAccount:

    # Fund Transfer from acc
    btn_fndtrf_search_button_id = 'fndtfr__FundTransfer__container_list_2_row_5'
    textbox_fndtrf_seach_acc_num_id = 'fndtfr__FundTransfer__AP_SearchAccNum'
    btn_fndtrf_account_id = 'fndtfr__FundTransfer__ct_lst_1_row_0'

    # Fund Transfer Payee acc
    textbox_fndtrf_search_payee_acc_id = 'fndtfr__FundTransfer__choose_pay'
    bnt_fndtrf_payee_acc_id = 'fndtfr__FundTransfer__sc_row_375_row'


    def __init__(self, driver):
        self.driver = driver

    def click_fndtrf_search_acc_btn(self):
        self.driver.find_element(By.ID, self.btn_fndtrf_search_button_id).click()

    def search_acc_num(self, acc_num):
        self.driver.find_element(By.ID, self.textbox_fndtrf_seach_acc_num_id).send_keys(acc_num)

    def click_top_search_account(self):
        self.driver.find_element(By.ID, self.btn_fndtrf_account_id).click()

    def select_a_source_acc(self, acc_num):
        self.click_fndtrf_search_acc_btn()
        sleep(0.3)
        self.search_acc_num(acc_num)
        sleep(0.1)
        self.click_top_search_account()

    def search_payee_acc_num(self, accNum):
        self.driver.find_element(By.ID, self.textbox_fndtrf_search_payee_acc_id).send_keys(accNum)

    def click_top_payee_search_account(self):
        self.driver.find_element(By.ID, self.bnt_fndtrf_payee_acc_id).click()

    def select_a_payee_acc(self, accNum):
        self.search_payee_acc_num(accNum)
        sleep(1)
        self.click_top_payee_search_account()
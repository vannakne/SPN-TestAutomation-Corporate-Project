from time import sleep

from selenium.webdriver.common.by import By

class WalletTransferPage:

    ## wallet type
    all_wallet_type = {
        'Wing': 'fndtfr__WalletTransfer__sc_col_316_li',
        'Pipay': 'fndtfr__WalletTransfer__sc_col_317_li',
        'True Money': 'fndtfr__WalletTransfer__sc_col_319_li',
        'Bakong': 'fndtfr__WalletTransfer__sc_col_314_li',
        'Ly Hour Veluy': 'fndtfr__WalletTransfer__sc_col_320_li',
        'eMoney': 'fndtfr__WalletTransfer__sc_col_322_li',
        'Visa Direct': 'fndtfr__WalletTransfer__sc_col_323_li',
        'Local Bank via Bakong': 'fndtfr__WalletTransfer__sc_col_321_li'
    }

    wallet_wing_id = 'fndtfr__WalletTransfer__sc_col_316_li'
    wallet_pipay_id = 'fndtfr__WalletTransfer__sc_col_313_li'
    wallet_true_money_id = 'fndtfr__WalletTransfer__sc_col_319_li'
    wallet_bakong_id = 'fndtfr__WalletTransfer__sc_col_314_li'
    wallet_lyhour_veyluy_id = 'fndtfr__WalletTransfer__sc_col_320_li'
    wallet_emoney_id = 'fndtfr__WalletTransfer__sc_col_322_li'
    wallet_visa_direct_id = 'fndtfr__WalletTransfer__sc_col_323_li'
    wallet_local_bank_via_bakong_id = 'fndtfr__WalletTransfer__sc_col_321_li'


    ## Select Account
    selectAccount_KHR_id = 'fndtfr__WalletTransfer__container_list_2_row_0'
    selectAccount_USD_id = 'fndtfr__WalletTransfer__container_list_2_row_1'

    ## Wallet Transfer Input Screen
    textbox_consumer_number_id = 'fndtfr__WalletTransfer__consno'
    textbox_amount_id = 'fndtfr__WalletTransfer__amt'
    text_amount_ccy_id = 'fndtfr__WalletTransfer__currdpd'
    textbox_remark_id = 'fndtfr__WalletTransfer__rmrk'

    button_dropDown_currency_id = 'fndtfr__WalletTransfer__currdpd_span'
    currency_USD_id = 'fndtfr__WalletTransfer__currdpd_option_USD'
    currency_KHR_id = 'fndtfr__WalletTransfer__currdpd_option_KHR'

    button_pay_id = 'fndtfr__WalletTransfer__el_btn_2'

    button_confirm_id = 'fndtfr__WalletTransfer__el_btn_5'
    textbox_Tpin_id = 'fndtfr__WalletTransfer__tpininp'
    button_submit_tpin_id = 'fndtfr__WalletTransfer__el_btn_13'
    linkTest_makerAnotherTrf_id = 'fndtfr__WalletTransfer__el_hpl_12_txtcnt'

    message_error_message_class = 'msg'
    button_ok_class = 'ok'

    def __init__(self, driver):
        self.driver = driver

    def clickWing(self):
        self.driver.find_element(By.ID, self.wallet_wing_id).click()

    def clickPipay(self):
        self.driver.find_element(By.ID, self.wallet_pipay_id).click()
        sleep(1)

    def clickTrueMoney(self):
        self.driver.find_element(By.ID, self.wallet_true_money_id).click()

    def clickBakong(self):
        self.driver.find_element(By.ID, self.wallet_bakong_id).click()

    def clickeMoney(self):
        self.driver.find_element(By.ID, self.wallet_emoney_id).click()

    def clickVisaDirect(self):
        self.driver.find_element(By.ID, self.wallet_visa_direct_id).click()

    def clickLocalBankViaBakong(self):
        self.driver.find_element(By.ID, self.wallet_local_bank_via_bakong_id).click()

    def selectUSDaccount(self):
        self.driver.find_element(By.ID, self.selectAccount_USD_id).click()

    def selectKHRaccount(self):
        self.driver.find_element(By.ID, self.selectAccount_KHR_id).click()

    def choose_a_Wallet_type(self, wallet):
        self.driver.find_element(By.ID, self.all_wallet_type[wallet]).click()

    def enter_consumer_number(self, acc_number):
        self.driver.find_element(By.ID, self.textbox_consumer_number_id).send_keys(acc_number)

    def enter_Amount(self, amount):
        self.driver.find_element(By.ID, self.textbox_amount_id).send_keys(amount)

    def click_Amount(self):
        self.driver.find_element(By.ID, self.textbox_amount_id).click()

    def clickRemark(self):
        self.driver.find_element(By.ID, self.textbox_remark_id).click()

    def clickPay(self):
        self.driver.find_element(By.ID, self.button_pay_id).click()

    def getAmountCCY(self):
        self.currency = self.driver.find_element(By.ID, self.text_amount_ccy_id).get_attribute('value')
        return self.currency

    def clickConfirm(self):
        self.driver.find_element(By.ID, self.button_confirm_id).click()

    def enter_Tpin(self, tpin):
        self.driver.find_element(By.ID, self.textbox_Tpin_id).send_keys(tpin)

    def clickSubmit(self):
        self.driver.find_element(By.ID, self.button_submit_tpin_id).click()

    def clickAnotherTrf(self):
        self.driver.find_element(By.ID, self.linkTest_makerAnotherTrf_id).click()

    def getPopUpMessage(self):
        self.msg = self.driver.find_element(By.CLASS_NAME, self.message_error_message_class).text
        return self.msg

    def clickOK(self):
        self.driver.find_element(By.CLASS_NAME, self.button_ok_class).click()


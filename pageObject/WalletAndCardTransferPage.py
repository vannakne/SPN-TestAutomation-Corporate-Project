from selenium.webdriver.common.by import By

class WalletTransferPage:

    ## wallet type
    wallet_wing_id = 'fndtfr__WalletTransfer__sc_col_316_li'
    wallet_pipay_id = 'fndtfr__WalletTransfer__sc_col_317_li'
    wallet_true_money_id = 'fndtfr__WalletTransfer__sc_col_319_li'
    wallet_bakong_id = 'fndtfr__WalletTransfer__sc_col_314_li'
    wallet_lyhour_veyluy_id = 'fndtfr__WalletTransfer__sc_col_320_li'
    wallet_emoney_id = 'fndtfr__WalletTransfer__sc_col_322_li'
    wallet_visa_direct_id = 'fndtfr__WalletTransfer__sc_col_323_li'
    wallet_local_bank_via_bakong_id = 'fndtfr__WalletTransfer__sc_col_321_li'

    ## Select Account
    selectAccount_KHR_id = 'inblpy__InstantBillPayment__container_list_2_row_0'
    selectAccount_USD_id = 'inblpy__InstantBillPayment__container_list_2_row_1'

    ## Wallet Transfer Input Screen
    textbox_consumer_number_id = 'fndtfr__WalletTransfer__consno'
    textbox_amount_id = 'fndtfr__WalletTransfer__amt'

    button_dropDown_currency_id = 'fndtfr__WalletTransfer__currdpd_span'
    currency_USD_id = 'fndtfr__WalletTransfer__currdpd_option_USD'
    currency_KHR_id = 'fndtfr__WalletTransfer__currdpd_option_KHR'

    button_pay_id = 'fndtfr__WalletTransfer__el_btn_2'



    def __init__(self, driver):
        self.driver = driver

    def clickWing(self):
        self.driver.find_element(By.ID, self.wallet_wing_id).click()

    def clickPipay(self):
        self.driver.find_element(By.ID, self.wallet_pipay_id).click()

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
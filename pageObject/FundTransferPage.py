from selenium.webdriver.common.by import By


class FundTransfer:
    btn_own_accoutn_id = 'fndtfr__FundTransfer__TransferType_option_FT_OAC_span_'
    btn_within_spn_id = 'fndtfr__FundTransfer__TransferType_option_FT_OTHER_span_'
    btn_other_bank_accounts_id = 'fndtfr__FundTransfer__TransferType_option_FT_OTHER_BANK_span_'
    btn_international_transfer_id = 'fndtfr__FundTransfer__TransferType_option_FT_INTERNATIONALTRANSFER_span_'

    ## Transfer Type dic
    all_trf_type = {
        "Own Account": 'fndtfr__FundTransfer__TransferType_option_FT_OAC_span_',
        "Within Sathapana": 'fndtfr__FundTransfer__TransferType_option_FT_OTHER_span_',
        "Other Bank Accounts": 'fndtfr__FundTransfer__TransferType_option_FT_OTHER_BANK_span_',
        "International Transfer": 'fndtfr__FundTransfer__TransferType_option_FT_INTERNATIONALTRANSFER_span_'
    }

    # Input Page
    field_amnt_ccy_id = 'fndtfr__FundTransfer__currdpd'
    textbox_amount_id = 'fndtfr__FundTransfer__amnt_si_inp'
    textbox_remark_id = 'fndtfr__FundTransfer__remark_inp'
    btn_pay_id = 'fndtfr__FundTransfer__btn_submt'

    # Confirmation Page
    btn_confirm_id = 'fndtfr__FundTransfer__btn_cnfm'
    textbox_tpin_id = 'fndtfr__FundTransfer__tpininp'
    btn_submit_tpin_id = 'fndtfr__FundTransfer__el_btn_26'

    def __init__(self, driver):
        self.driver = driver

    def choose_a_trf_type(self, trf_type):
        self.driver.find_element(By.ID, self.all_trf_type[trf_type]).click()

    def get_amount_ccy(self):
        amount_ccy = self.driver.find_element(By.ID, self.field_amnt_ccy_id).get_attribute('value')
        return amount_ccy

    def enter_amount(self, amnt):
        self.driver.find_element(By.ID, self.textbox_amount_id).send_keys(amnt)

    def click_remark(self):
        self.driver.find_element(By.ID, self.textbox_remark_id).click()

    def click_pay(self):
        self.driver.find_element(By.ID, self.btn_pay_id).click()

    def click_confirm(self):
        self.driver.find_element(By.ID, self.btn_confirm_id).click()

    def enter_tpin(self, tpin):
        self.driver.find_element(By.ID, self.textbox_tpin_id).send_keys(tpin)

    def click_submit_tpin(self):
        self.driver.find_element(By.ID, self.btn_submit_tpin_id).click()

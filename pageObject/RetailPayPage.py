from selenium.webdriver.common.by import By


class RetailPay:

    ## Select Account
    selectAccount_KHR_id = 'Retail__RetailPayment__container_list_2_row_0'
    selectAccount_USD_id = 'Retail__RetailPayment__container_list_2_row_1'

    ## input screen
    dropdown_payee_bank_id = 'Retail__RetailPayment__to_bank_name_span'
    all_payee_bank = {
        "3333": "Retail__RetailPayment__to_bank_name_option_3333",
        "Acleda Bank": "Retail__RetailPayment__to_bank_name_option_Acleda Bank",
        "Amret": "Retail__RetailPayment__to_bank_name_option_Amret",
        "KOOKMIN BANK CAMBODIA PLC": "Retail__RetailPayment__to_bank_name_option_KOOKMIN BANK CAMBODIA PLC",
        "KRUNG THAI BANK PUBLIC CO,LTD PHNOM PEHN BRANCH": "Retail__RetailPayment__to_bank_name_option_KRUNG THAI BANK PUBLIC CO,LTD PHNOM PEHN BRANCH" ,
        "Kraitai": "Retail__RetailPayment__to_bank_name_option_Kraitai",
        "PRASACMFI": "Retail__RetailPayment__to_bank_name_option_PRASACMFI",
        "PRINCE BANK PLC": "Retail__RetailPayment__to_bank_name_option_PRINCE BANK PLC",
        "Phnom Penh Commercial Bank": "Retail__RetailPayment__to_bank_name_option_Phnom Penh Commercial Bank",
        "VATTANAC BANK": "Retail__RetailPayment__to_bank_name_option_VATTANAC BANK"
        }
    textbox_account_number_id = 'Retail__RetailPayment__toAcc'
    text_amount_ccy_id = 'Retail__RetailPayment__currdpd'
    button_dropDown_currency_id = 'Retail__RetailPayment__currdpd_span'
    currency_USD_id = 'Retail__RetailPayment__currdpd_option_USD'
    currency_KHR_id = 'Retail__RetailPayment__currdpd_option_KHR'
    textbox_amount_id = 'Retail__RetailPayment__amt'
    textbox_remark_id = 'Retail__RetailPayment__rmrk'
    button_pay_id = 'Retail__RetailPayment__el_btn_2'
    textbox_phone_number_id = 'Retail__RetailPayment__phnNo'
    textbox_receiver_name_id = 'Retail__RetailPayment__consno'

    # Confirmation
    button_confirm_id = 'Retail__RetailPayment__el_btn_5'
    textbox_Tpin_id = 'Retail__RetailPayment__tpininp'
    button_submit_tpin_id = 'Retail__RetailPayment__el_btn_13'
    linkTest_makerAnotherTrf_id = 'Retail__RetailPayment__el_hpl_12_txtcnt'

    message_error_message_class = 'msg'
    button_ok_class = 'ok'
    
    # Trf detail
    text_from_acc_id = 'Retail__RetailPayment__frmacntnocnf'
    text_acc_balance_id = 'Retail__RetailPayment__blncecnf'

    text_trf_amount_id = 'Retail__RetailPayment__amtcnf'
    text_fee_charge_id = 'Retail__RetailPayment__feecnf'

    text_converted_value_id = 'Retail__RetailPayment__cnvvalcnf'
    text_exchange_rate_id = 'Retail__RetailPayment__cnvratevalcnf'

    def __init__(self, driver):
        self.driver = driver

    def selectUSDaccount(self):
        self.driver.find_element(By.ID, self.selectAccount_USD_id).click()

    def clickPayeeBank_Dropdown(self):
        self.driver.find_element(By.ID, self.dropdown_payee_bank_id).click()

    def choose_a_payee_bank(self, bank):
        self.driver.find_element(By.ID, self.all_payee_bank[bank]).click()

    def enter_consumer_number(self, account):
        self.driver.find_element(By.ID, self.textbox_account_number_id).send_keys(account)

    def enter_phone_number(self, number):
        self.driver.find_element(By.ID, self.textbox_phone_number_id).send_keys(number)

    def enter_receiver_name(self, name):
        self.driver.find_element(By.ID, self.textbox_receiver_name_id).send_keys(name)

    def clickRemark(self):
        self.driver.find_element(By.ID, self.textbox_remark_id).click()

    def clickPay(self):
        self.driver.find_element(By.ID, self.button_pay_id).click()

    def click_Amount(self):
        self.driver.find_element(By.ID, self.textbox_amount_id).click()

    def enter_Amount(self, amount):
        self.driver.find_element(By.ID, self.textbox_amount_id).send_keys(amount)

    def getPopUpMessage(self):
        self.msg = self.driver.find_element(By.CLASS_NAME, self.message_error_message_class).text
        return self.msg

    def clickOK(self):
        self.driver.find_element(By.CLASS_NAME, self.button_ok_class).click()

    def getAmountCCY(self):
        self.currency = self.driver.find_element(By.ID, self.text_amount_ccy_id).get_attribute('value')
        return self.currency
    
    # Confirmation
    def clickConfirm(self):
        self.driver.find_element(By.ID, self.button_confirm_id).click()

    def enter_Tpin(self, tpin):
        self.driver.find_element(By.ID, self.textbox_Tpin_id).send_keys(tpin)

    def clickSubmit(self):
        self.driver.find_element(By.ID, self.button_submit_tpin_id).click()

    def clickAnotherTrf(self):
        self.driver.find_element(By.ID, self.linkTest_makerAnotherTrf_id).click()

    # trf deatail
    def get_converted_value(self):
        try:
            balance = self.driver.find_element(By.ID, self.text_converted_value_id).text
            balance = balance.replace(',', '')
            balance = balance.replace('USD', '')
            balance = balance.replace('KHR', '')
            return float(balance)
        except:
            return 0

    def get_trf_amount(self):
        balance = self.driver.find_element(By.ID, self.text_trf_amount_id).text
        balance = balance.replace(',', '')
        balance = balance.replace('USD', '')
        balance = balance.replace('KHR', '')
        return float(balance)

    def get_fee_charge(self):
        try:
            balance = self.driver.find_element(By.ID, self.text_fee_charge_id).text
            balance = balance.replace('USD', '')
            balance = balance.replace('KHR', '')
            balance = balance.replace(',', '')
            return float(balance)
        except:
            return 0

    def get_exchange_rate(self):
        try:
            rate = self.driver.find_element(By.ID, self.text_exchange_rate_id).text
            splitRate = rate.split("=")
            KHRValue = splitRate[-1]
            KHRValue = KHRValue.replace("KHR", '')
            KHRValue = KHRValue.replace(",", '')
            return float(KHRValue)
        except:
            return 0

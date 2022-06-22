from time import sleep

from selenium.webdriver.common.by import By


class MobileTopUp:
    ## Select Account
    selectAccount_KHR_id = 'Topup__MobileTopup__container_list_2_row_0'
    selectAccount_USD_id = 'Topup__MobileTopup__container_list_2_row_1'

    ## input screen
    radio_btn_pin_id = 'Topup__MobileTopup__topupType_option_Two_span_'
    textbox_phone_number_id = 'Topup__MobileTopup__mobileNumber'
    dropdown_topUP_amount_id = 'Topup__MobileTopup__amount_span'
    dropdown_topUP_amount_pin_id = 'Topup__MobileTopup__amount1_span'
    all_amount_topup = {
        "1 USD": "Topup__MobileTopup__amount_option_1.00 USD",
        "2 USD": "Topup__MobileTopup__amount_option_2.00 USD",
        "5 USD": "Topup__MobileTopup__amount_option_5.00 USD",
        "10 USD": "Topup__MobileTopup__amount_option_10.00 USD",
        "20 USD": "Topup__MobileTopup__amount_option_20.00 USD",
        "50 USD": "Topup__MobileTopup__amount_option_50.00 USD",
    }
    all_amount_topup_pin = {
        "1 USD": "Topup__MobileTopup__amount1_option_1.00 USD",
        "2 USD": "Topup__MobileTopup__amount1_option_2.00 USD",
        "5 USD": "Topup__MobileTopup__amount1_option_5.00 USD",
        "10 USD": "Topup__MobileTopup__amount1_option_10.00 USD",
        "20 USD": "Topup__MobileTopup__amount1_option_20.00 USD",
        "50 USD": "Topup__MobileTopup__amount1_option_50.00 USD",
    }
    textbox_remark_id = 'Topup__MobileTopup__remarks'
    textbox_remark_pin_id = 'Topup__MobileTopup__remarks1'
    button_pay_id = 'Topup__MobileTopup__el_btn_10'

    # Confirmation
    button_confirm_id = 'Topup__MobileTopup__el_btn_22'
    textbox_Tpin_id = 'Topup__MobileTopup__tpininp'
    button_submit_tpin_id = 'Topup__MobileTopup__el_btn_16'

    message_error_message_class = 'msg'
    button_ok_class = 'ok'

    # Trf detail
    text_from_acc_id = 'Retail__RetailPayment__frmacntnocnf'
    text_acc_balance_id = 'Retail__RetailPayment__blncecnf'

    text_trf_amount_id = 'Topup__MobileTopup__coAmount'
    text_fee_charge_id = 'Topup__MobileTopup__coFeeCharges'

    text_converted_value_id = 'Topup__MobileTopup__coConvValue'
    text_exchange_rate_id = 'Topup__MobileTopup__ConfBill_con_cry'

    def __init__(self, driver):
        self.driver = driver

    def scrollDown(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(0.3)

    def selectUSDaccount(self):
        self.driver.find_element(By.ID, self.selectAccount_USD_id).click()

    def click_pin_radio(self):
        self.driver.find_element(By.ID, self.radio_btn_pin_id).click()
        sleep(0.1)

    def clickTopUP_amount_Dropdown(self):
        self.driver.find_element(By.ID, self.dropdown_topUP_amount_id).click()

    def clickTopUP_amount_Dropdown_pin(self):
        self.driver.find_element(By.ID, self.dropdown_topUP_amount_pin_id).click()

    def choose_an_amount(self, amount):
        self.driver.find_element(By.ID, self.all_amount_topup[amount]).click()

    def choose_an_amount_pin(self, amount):
        self.driver.find_element(By.ID, self.all_amount_topup_pin[amount]).click()

    def enter_phone_number(self, number):
        self.driver.find_element(By.ID, self.textbox_phone_number_id).send_keys(number)

    def clickRemark(self):
        self.driver.find_element(By.ID, self.textbox_remark_id).click()

    def clickRemark_pin(self):
        self.driver.find_element(By.ID, self.textbox_remark_pin_id).click()

    def clickPay(self):
        # self.scrollDown()
        self.driver.find_element(By.ID, self.button_pay_id).click()

    def getPopUpMessage(self):
        self.msg = self.driver.find_element(By.CLASS_NAME, self.message_error_message_class).text
        return self.msg

    def clickOK(self):
        self.driver.find_element(By.CLASS_NAME, self.button_ok_class).click()


    # Confirmation
    def clickConfirm(self):
        self.driver.find_element(By.ID, self.button_confirm_id).click()

    def enter_Tpin(self, tpin):
        self.driver.find_element(By.ID, self.textbox_Tpin_id).send_keys(tpin)

    def clickSubmit(self):
        self.driver.find_element(By.ID, self.button_submit_tpin_id).click()


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

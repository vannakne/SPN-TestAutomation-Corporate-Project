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

        ## Local Bank via Bakong
    field_payee_bank_bakong_id = 'fndtfr__WalletTransfer__payeebank'
    all_payee_bank_bakong = {
        "AMRET MFI": "fndtfr__WalletTransfer__payeebank_option_AMRET MFI",
        "AMK Microfinance Plc.": "fndtfr__WalletTransfer__payeebank_option_AMK Microfinance Plc." ,
        "Acleda Bank": "fndtfr__WalletTransfer__payeebank_option_Acleda Bank",
        "Advanced Bank of Asia LTD": "fndtfr__WalletTransfer__payeebank_option_Advanced Bank of Asia LTD",
        "Asia Wei Luy": "fndtfr__WalletTransfer__payeebank_option_Asia Wei Luy",
        "Cambodia Asia Bank": "fndtfr__WalletTransfer__payeebank_option_Cambodia Asia Bank",
        "Cambodia Post Bank Plc": "fndtfr__WalletTransfer__payeebank_option_Cambodia Post Bank Plc",
        "Cambodian Public Bank Plc": "fndtfr__WalletTransfer__payeebank_option_Cambodian Public Bank Plc",
        "Canadia Bank PLC": "fndtfr__WalletTransfer__payeebank_option_Canadia Bank PLC",
        "Chief (Cambodia) Commercial Bank Plc.": "fndtfr__WalletTransfer__payeebank_option_Chief (Cambodia) Commercial Bank Plc.",
        "Chip Mong Commercial Bank Plc.": "fndtfr__WalletTransfer__payeebank_option_Chip Mong Commercial Bank Plc.",
        "Bank for Investment and Development of Cambodia Pic": "fndtfr__WalletTransfer__payeebank_option_Bank for Investment and Development of Cambodia Pic",
        "Coolcash": "fndtfr__WalletTransfer__payeebank_option_Coolcash",
        "Dev Bank": "fndtfr__WalletTransfer__payeebank_option_Dev Bank",
        "Foreign Trade Bank of Cambodia": "fndtfr__WalletTransfer__payeebank_option_Foreign Trade Bank of Cambodia",
        "Hattha Bank Plc.": "fndtfr__WalletTransfer__payeebank_option_Hattha Bank Plc.",
        "Kookmin Bank Cambodia PLC": "fndtfr__WalletTransfer__payeebank_option_Kookmin Bank Cambodia PLC",
        "LOLC (Cambodia) Plc.": "fndtfr__WalletTransfer__payeebank_option_LOLC (Cambodia) Plc.",
        "MayBank (Cambodia) PLC": "fndtfr__WalletTransfer__payeebank_option_MayBank (Cambodia) PLC",
        "National Bank of Cambodia": "fndtfr__WalletTransfer__payeebank_option_National Bank of Cambodia",
        "National Bank of Cambodia (Operation)": "fndtfr__WalletTransfer__payeebank_option_National Bank of Cambodia (Operation)",
        "PRASAC MFI Plc": "fndtfr__WalletTransfer__payeebank_option_PRASAC MFI Plc",
        "PRINCE BANK PLC": "fndtfr__WalletTransfer__payeebank_option_PRINCE BANK PLC",
        "Phillip Bank PLC": "fndtfr__WalletTransfer__payeebank_option_Phillip Bank PLC",
        "Phnom Penh Commercial Bank": "fndtfr__WalletTransfer__payeebank_option_Phnom Penh Commercial Bank",
        "Wing (Cambodia) Limited Specialised Bank": "fndtfr__WalletTransfer__payeebank_option_Wing (Cambodia) Limited Specialised Bank",
        "Speedpay PLC": "fndtfr__WalletTransfer__payeebank_option_Speedpay PLC",
        "TrueMoney Cambodia": "fndtfr__WalletTransfer__payeebank_option_TrueMoney Cambodia",
        "Vattanac Bank": "fndtfr__WalletTransfer__payeebank_option_Vattanac Bank",
        "WB Finance Co., Ltd.": "fndtfr__WalletTransfer__payeebank_option_WB Finance Co., Ltd."
        }

    button_dropDown_currency_id = 'fndtfr__WalletTransfer__currdpd_span'
    currency_USD_id = 'fndtfr__WalletTransfer__currdpd_option_USD'
    currency_KHR_id = 'fndtfr__WalletTransfer__currdpd_option_KHR'

    button_pay_id = 'fndtfr__WalletTransfer__el_btn_2'

    # Confirmation
    button_confirm_id = 'fndtfr__WalletTransfer__el_btn_5'
    textbox_Tpin_id = 'fndtfr__WalletTransfer__tpininp'
    button_submit_tpin_id = 'fndtfr__WalletTransfer__el_btn_13'
    linkTest_makerAnotherTrf_id = 'fndtfr__WalletTransfer__el_hpl_12_txtcnt'

    message_error_message_class = 'msg'
    button_ok_class = 'ok'

    # trf detail
    text_from_acc_id = 'fndtfr__WalletTransfer__frmacntnocnf'
    text_acc_balance_id = 'fndtfr__WalletTransfer__blncecnf'

    text_trf_amount_id = 'fndtfr__WalletTransfer__amtcnf'
    text_fee_charge_id = 'fndtfr__WalletTransfer__feecnf'

    text_converted_value_id = 'fndtfr__WalletTransfer__cnvvalcnf'
    text_exchange_rate_id = 'fndtfr__WalletTransfer__cnvratevalcnf'


    #Home
    button_quick_link_wallet_id = 'dshbrd__DB_QckLink__i__DashBrdLinks__linkDesc_0_txtcnt'

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

    def get_acc_balance_b4_txn(self):
        balance = self.driver.find_element(By.ID, self.text_acc_balance_id).text
        balance = balance.replace('USD', '')
        balance = balance.replace(',', '')
        return float(balance)

    # trf detail
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

    def clickWalletAndCard(self):
        self.driver.find_element(By.ID, self.button_quick_link_wallet_id).click()

    def choose_a_local_bank(self, bank):
        self.driver.find_element(By.ID, self.field_payee_bank_bakong_id).click()
        sleep(0.1)
        self.driver.find_element(By.ID, self.all_payee_bank_bakong[bank]).click()
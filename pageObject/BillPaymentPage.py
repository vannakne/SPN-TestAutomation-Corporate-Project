from time import sleep

from selenium.webdriver.common.by import By


class BillPaymentPage:

    img_SPN_logo_id = 'crpusr__BasePage__homebtn'
    img_SPN_logo2_id = 'crpusr__BasePage__el_btn_5'

    ## Bill Type
    button_electricity_id = 'inblpy__InstantBillPayment__ct_lst_1_row_0'
    button_water_supply_id = 'inblpy__InstantBillPayment__ct_lst_1_row_1'
    button_waste_id = 'inblpy__InstantBillPayment__ct_lst_1_row_2'
    button_education_id = 'inblpy__InstantBillPayment__ct_lst_1_row_4'
    button_real_estate_id = 'inblpy__InstantBillPayment__ct_lst_1_row_8'
    button_internet_id = 'inblpy__InstantBillPayment__ct_lst_1_row_3'
    button_insurance_id = 'inblpy__InstantBillPayment__ct_lst_1_row_5'
    button_financial_service_id = 'inblpy__InstantBillPayment__ct_lst_1_row_9'
    button_general_bills_id = 'inblpy__InstantBillPayment__ct_lst_1_row_10'

    # all bill type
    all_bill_type = {
        'Electricity': 'inblpy__InstantBillPayment__ct_lst_1_row_0',
        'Water Supply': 'inblpy__InstantBillPayment__ct_lst_1_row_1',
        'Waste': 'inblpy__InstantBillPayment__ct_lst_1_row_2',
        'Education': 'inblpy__InstantBillPayment__ct_lst_1_row_4',
        'Real Estate': 'inblpy__InstantBillPayment__ct_lst_1_row_8',
        'Internet': 'inblpy__InstantBillPayment__ct_lst_1_row_3',
        'Insurance': 'inblpy__InstantBillPayment__ct_lst_1_row_5',
        'Financial Service': 'inblpy__InstantBillPayment__ct_lst_1_row_9',
        'General Bill': 'inblpy__InstantBillPayment__ct_lst_1_row_10',
        'Trading': 'inblpy__InstantBillPayment__ct_lst_1_row_6',
    }

    ## Select Account
    selectAccount_KHR_id = 'inblpy__InstantBillPayment__container_list_2_row_0'
    selectAccount_USD_id = 'inblpy__InstantBillPayment__container_list_2_row_1'

    ## Payment Input screen
    button_biller_dropDown_id = 'inblpy__InstantBillPayment__bilsel_span'
    textbox_consumer_number_id = 'inblpy__InstantBillPayment__consno'
    button_currency_dropDown_id = 'inblpy__InstantBillPayment__currdpd_span'
    currencybox_currency_id = 'inblpy__InstantBillPayment__currdpd'
    option_KHR_currency_id = 'inblpy__InstantBillPayment__currdpd_option_KHR'
    option_USD_currency_id = 'inblpy__InstantBillPayment__currdpd_option_USD'
    textbox_input_amount_id = 'inblpy__InstantBillPayment__amt'
    textbox_remark_id = 'inblpy__InstantBillPayment__rmrk'
    button_cancel_id = 'inblpy__InstantBillPayment__el_btn_1'
    button_pay_id = 'inblpy__InstantBillPayment__el_btn_2'

    popUp_message_msg_class = 'msg'
    button_ok_class = 'ok'
    text_confirmationPage_id = 'inblpy__InstantBillPayment__el_txt_18_txtcnt'

    text_feecharge_input_screen_id = 'inblpy__InstantBillPayment__feetxt'

    ## confirm page
    button_confirm_id = 'inblpy__InstantBillPayment__el_btn_5'
    textbox_Tpin_id = 'inblpy__InstantBillPayment__tpininp'
    button_submit_tpin_id = 'inblpy__InstantBillPayment__el_btn_13'
    linkText_Make_another_transfer_id = 'inblpy__InstantBillPayment__el_hpl_12_txtcnt'

    text_from_acc_id = 'inblpy__InstantBillPayment__blncecnf'
    text_acc_balance_id = 'inblpy__InstantBillPayment__blncecnf'

    text_trf_amount_id = 'inblpy__InstantBillPayment__amtcnf'
    text_fee_charge_id = 'inblpy__InstantBillPayment__feecnf'

    text_converted_value_id = 'inblpy__InstantBillPayment__cnvvalcnf'
    text_exchange_rate_id = 'inblpy__InstantBillPayment__cnvratevalcnf'

    ## Electricity
    all_biller_electric_id = {
        'Electric Khum O': 'inblpy__InstantBillPayment__bilsel_option_Electric Khum O',
        'Kok Tieng L Y P Group Co.ltd (OMC)': 'inblpy__InstantBillPayment__bilsel_option_Kok Tieng L Y P Group Co.ltd (OMC)',
        'Plork Vannak Electricity': 'inblpy__InstantBillPayment__bilsel_option_Plork Vannak Electricity ',
        'Tnalbek Chamcarleu Electricity': 'inblpy__InstantBillPayment__bilsel_option_Tnalbek Chamcarleu Electricity',
        'EDC Kampong Cham': 'inblpy__InstantBillPayment__bilsel_option_EDC Kampong Cham',
        'EDC Ratanakiri': 'inblpy__InstantBillPayment__bilsel_option_EDC Ratanakiri',
        'EDC Siem Reap': 'inblpy__InstantBillPayment__bilsel_option_EDC Siem Reap',
        'Electricite Du Cambodge (Phnom Penh)': 'inblpy__InstantBillPayment__bilsel_option_Electricite Du Cambodge (Phnom Penh)',
    }

    ## Real Estatep
    all_biller_real_estate_id = {
        'Borey Leng Navatra': 'inblpy__InstantBillPayment__bilsel_option_Borey Leng Navatra',
        'Borey Peng Huoth': 'inblpy__InstantBillPayment__bilsel_option_Borey Peng Huoth',
    }

    ## Education
    all_biller_education_id = {
        'National University of Management': 'inblpy__InstantBillPayment__bilsel_option_National University of Management',
        'Western International School Plc': 'inblpy__InstantBillPayment__bilsel_option_Western International School Plc',
    }

    ## Water Supply
    all_water_supply_id = {
        'Chamkar Leu Water Supply': 'inblpy__InstantBillPayment__bilsel_option_Chamkar Leu Water Supply',
        'Phnom Penh Water Supply': 'inblpy__InstantBillPayment__bilsel_option_Phnom Penh Water Supply',
        'Siem Reap Water Supply Authority': 'inblpy__InstantBillPayment__bilsel_option_Siem Reap Water Supply Authority',
        'Traeng Water Supply': 'inblpy__InstantBillPayment__bilsel_option_Traeng Water Supply',
    }

    ## Internet
    all_biller_internet_id = {
        'MekongNet ISP': 'inblpy__InstantBillPayment__bilsel_option_MekongNet ISP',
        'Telecom Cambodia': 'inblpy__InstantBillPayment__bilsel_option_Telecom Cambodia',
    }

    ## Insurance
    all_biller_insurance_id = {
        'AIA CAMBODIA': 'inblpy__InstantBillPayment__bilsel_option_AIA CAMBODIA',
        'Manulife Cambodia': 'inblpy__InstantBillPayment__bilsel_option_Manulife Cambodia',
        'Mekong Microinsurance': 'inblpy__InstantBillPayment__bilsel_option_Mekong Microinsurance',
        'Prudential Cambodia': 'inblpy__InstantBillPayment__bilsel_option_Prudential Cambodia',
    }

    ## Financial Service
    all_biller_financial_service_id = {
        'Cambodian Labor Care': 'inblpy__InstantBillPayment__bilsel_option_Cambodian Labor Care',
    }

    ## General Bills
    all_biller_general_bills_id = {
        'Banh Ji': 'inblpy__InstantBillPayment__bilsel_option_Banh Ji',
    }

    ## Waste
    all_biller_waste_id = {
        'GAEA Waste Management': 'inblpy__InstantBillPayment__bilsel_option_GAEA Waste Management',
        'Song Kimla Solid Waste Ang Snuol': 'inblpy__InstantBillPayment__bilsel_option_Song Kimla Solid Waste Ang Snuol',
        'Phnom Penh Solid Waste Management Authority': 'inblpy__InstantBillPayment__bilsel_option_Phnom Penh Solid Waste Management Authority',
        'Viphou Phopudh Utility': 'inblpy__InstantBillPayment__bilsel_option_Viphou Phopudh Utility',
    }

    # Trading
    all_biller_trading_id = {
    'GREENFEED (Cambodia) Co., Ltd.': 'inblpy__InstantBillPayment__bilsel_option_GREENFEED (Cambodia) Co., Ltd.'
    }

    # biller for each bill
    biller_dic = {
        # Electricity
        'Electric Khum O': 'inblpy__InstantBillPayment__bilsel_option_Electric Khum O',
        'Kok Tieng L Y P Group Co.ltd (OMC)': 'inblpy__InstantBillPayment__bilsel_option_Kok Tieng L Y P Group Co.ltd (OMC)',
        'Plork Vannak Electricity': 'inblpy__InstantBillPayment__bilsel_option_Plork Vannak Electricity ',
        'Tnalbek Chamcarleu Electricity': 'inblpy__InstantBillPayment__bilsel_option_Tnalbek Chamcarleu Electricity',
        'EDC Kampong Cham': 'inblpy__InstantBillPayment__bilsel_option_EDC Kampong Cham',
        'EDC Ratanakiri': 'inblpy__InstantBillPayment__bilsel_option_EDC Ratanakiri',
        'EDC Siem Reap': 'inblpy__InstantBillPayment__bilsel_option_EDC Siem Reap',
        'Electricite Du Cambodge (Phnom Penh)': 'inblpy__InstantBillPayment__bilsel_option_Electricite Du Cambodge (Phnom Penh)',

        # Real Estate
        'Borey Leng Navatra': 'inblpy__InstantBillPayment__bilsel_option_Borey Leng Navatra',
        'Borey Peng Huoth': 'inblpy__InstantBillPayment__bilsel_option_Borey Peng Huoth',

        # Education
        'National University of Management': 'inblpy__InstantBillPayment__bilsel_option_National University of Management',
        'Western International School Plc': 'inblpy__InstantBillPayment__bilsel_option_Western International School Plc',

        # Water Supply
        'Chamkar Leu Water Supply': 'inblpy__InstantBillPayment__bilsel_option_Chamkar Leu Water Supply',
        'Phnom Penh Water Supply': 'inblpy__InstantBillPayment__bilsel_option_Phnom Penh Water Supply',
        'Siem Reap Water Supply Authority': 'inblpy__InstantBillPayment__bilsel_option_Siem Reap Water Supply Authority',
        'Traeng Water Supply': 'inblpy__InstantBillPayment__bilsel_option_Traeng Water Supply',

        # Internet
        'MekongNet ISP': 'inblpy__InstantBillPayment__bilsel_option_MekongNet ISP',
        'Telecom Cambodia': 'inblpy__InstantBillPayment__bilsel_option_Telecom Cambodia',

        # Insurance
        'AIA CAMBODIA': 'inblpy__InstantBillPayment__bilsel_option_AIA CAMBODIA',
        'Manulife Cambodia': 'inblpy__InstantBillPayment__bilsel_option_Manulife Cambodia',
        'Mekong Microinsurance': 'inblpy__InstantBillPayment__bilsel_option_Mekong Microinsurance',
        'Prudential Cambodia': 'inblpy__InstantBillPayment__bilsel_option_Prudential Cambodia',

        # Financial Service
        'Cambodian Labor Care': 'inblpy__InstantBillPayment__bilsel_option_Cambodian Labor Care',

        # General Bill
        'Banh Ji': 'inblpy__InstantBillPayment__bilsel_option_Banh Ji',

        # Waste
        'GAEA Waste Management': 'inblpy__InstantBillPayment__bilsel_option_GAEA Waste Management',
        'Song Kimla Solid Waste Ang Snuol': 'inblpy__InstantBillPayment__bilsel_option_Song Kimla Solid Waste Ang Snuol',
        'Phnom Penh Solid Waste Management Authority': 'inblpy__InstantBillPayment__bilsel_option_Phnom Penh Solid Waste Management Authority',
        'Viphou Phopudh Utility': 'inblpy__InstantBillPayment__bilsel_option_Viphou Phopudh Utility',

        # Trading
        'GREENFEED (Cambodia) Co., Ltd.': 'inblpy__InstantBillPayment__bilsel_option_GREENFEED (Cambodia) Co., Ltd.'
    }

    def __init__(self, driver):
        self.driver = driver

    def click_SPN_Logo(self):
        try:
            self.driver.find_element(By.ID, self.img_SPN_logo_id).click()
        except:
            self.driver.find_element(By.ID, self.img_SPN_logo2_id).click()

    def clickElectricity(self):
        self.driver.find_element(By.ID, self.button_electricity_id).click()

    def clickWaterSupply(self):
        self.driver.find_element(By.ID, self.button_water_supply_id).click()

    def clickWaste(self):
        self.driver.find_element(By.ID, self.button_waste_id).click()

    def clickEducation(self):
        self.driver.find_element(By.ID, self.button_education_id).click()

    def clickRealEstate(self):
        self.driver.find_element(By.ID, self.button_real_estate_id).click()

    def clickInternet(self):
        self.driver.find_element(By.ID, self.button_internet_id).click()

    def clickInsurance(self):
        self.driver.find_element(By.ID, self.button_insurance_id).click()

    def clickFinancialService(self):
        self.driver.find_element(By.ID, self.button_financial_service_id).click()

    def clickGeneralBill(self):
        self.driver.find_element(By.ID, self.button_general_bills_id).click()

    def clickBillerDropDown(self):
        self.driver.find_element(By.ID, self.button_biller_dropDown_id).click()

    def choose_an_electric_biller(self, biller):
        self.driver.find_element(By.ID, self.all_biller_electric_id[biller]).click()

    def choose_an_education_biller(self, biller):
        self.driver.find_element(By.ID, self.all_biller_education_id[biller]).click()

    def choose_an_realEstate_biller(self, biller):
        self.driver.find_element(By.ID, self.all_biller_real_estate_id[biller]).click()

    def choose_a_water_supply_biller(self, biller):
        self.driver.find_element(By.ID, self.all_water_supply_id[biller]).click()

    def choose_an_internet_biller(self, biller):
        self.driver.find_element(By.ID, self.all_biller_internet_id[biller]).click()

    def choose_an_insurance_biller(self, biller):
        self.driver.find_element(By.ID, self.all_biller_insurance_id[biller]).click()

    def choose_a_financial_service_biller(self, biller):
        self.driver.find_element(By.ID, self.all_biller_financial_service_id[biller]).click()

    def choose_a_general_bill_biller(self, biller):
        self.driver.find_element(By.ID, self.all_biller_general_bills_id[biller]).click()

    def selectUSDaccount(self):
        self.driver.find_element(By.ID, self.selectAccount_USD_id).click()

    def selectKHRaccount(self):
        self.driver.find_element(By.ID, self.selectAccount_KHR_id).click()

    def fillConsumer(self, consumer):
        self.driver.find_element(By.ID, self.textbox_consumer_number_id).send_keys(consumer)

    def clearConsumer(self):
        self.driver.find_element(By.ID, self.textbox_consumer_number_id).clear()

    def clickCurrencyDropDown(self):
        self.driver.find_element(By.ID, self.button_currency_dropDown_id).click()

    def click_USD_Amount_Currency(self):
        self.driver.find_element(By.ID, self.option_USD_currency_id).click()

    def click_KHR_Amount_Currency(self):
        self.driver.find_element(By.ID, self.option_KHR_currency_id).click()

    def enterAmount(self, amount):
        self.driver.find_element(By.ID, self.textbox_input_amount_id).send_keys(amount)

    def clearAmount(self):
        self.driver.find_element(By.ID, self.textbox_input_amount_id).clear()

    def clickPay(self):
        self.driver.find_element(By.ID, self.button_pay_id).click()

    def clickRemark(self):
        self.driver.find_element(By.ID, self.textbox_remark_id).click()

    def getPopUpMessage(self):
        self.message = self.driver.find_element(By.CLASS_NAME, self.popUp_message_msg_class).text
        return self.message

    def getConfirmationPage(self):
        self.text_confirmation = self.driver.find_element(By.ID, self.text_confirmationPage_id).text

    def getPayButtonText(self):
        try:
            self.pay_button_text = self.driver.find_element(By.ID, self.button_pay_id).text
        except:
            self.pay_button_text = self.driver.find_element(By.ID, self.button_confirm_id).text
        return self.pay_button_text

    def getConfirmButtonText(self):
        self.pay_button_text = self.driver.find_element(By.ID, self.button_confirm_id).text
        return self.pay_button_text

    def clickConfirm(self):
        self.pay_button_text = self.driver.find_element(By.ID, self.button_confirm_id).click()

    def enterTPIN(self, tpin):
        self.driver.find_element(By.ID, self.textbox_Tpin_id).send_keys(tpin)

    def clickSubmitTpin(self):
        self.driver.find_element(By.ID, self.button_submit_tpin_id).click()

    def clickMakeAnotherTrf(self):
        self.driver.find_element(By.ID, self.linkText_Make_another_transfer_id).click()

    def clickOK(self):
        self.driver.find_element(By.CLASS_NAME, self.button_ok_class).click()

    def getAmountCurrency(self):
        self.currency = self.driver.find_element(By.ID, self.currencybox_currency_id).get_attribute('value')
        return self.currency

    def choose_a_bill_type(self, type):
        self.driver.find_element(By.ID, self.all_bill_type[type]).click()

    def choose_a_biller(self, biller):
        self.driver.find_element(By.ID, self.biller_dic[biller]).click()

    def get_acc_balance_b4_txn(self):
        balance = self.driver.find_element(By.ID, self.text_acc_balance_id).text
        balance = balance.replace('USD', '')
        balance = balance.replace(',', '')
        return float(balance)

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

    def get_feecharge_input_screen(self):
        text_fee = self.driver.find_element(By.ID, self.text_feecharge_input_screen_id).text
        return text_fee
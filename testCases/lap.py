from time import sleep

import pytest
from selenium.webdriver.common.by import By
from termcolor import colored

from pageObject.HomePage import HomePage
from pageObject.LoginPage import LoginPage
from pageObject.WalletAndCardTransferPage import WalletTransferPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperty import ReadConfig_Wallet
from pageObject.Menu import Menu
from pageObject.BillPaymentPage import BillPaymentPage


class Test_010_Wallet:
    baseURL = ReadConfig_Wallet.getApplicationURL()
    corpID = ReadConfig_Wallet.getWalletCorpID()
    userID = ReadConfig_Wallet.getWalletUserID()
    password = ReadConfig_Wallet.getWalletPassword()
    path = '../TestData/Test_Data.xlsx'
    sheetName = 'Temp'

    log = LogGen.genlog()

    result_passed = []
    result_failed = []

    def test_010_wallet(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        sleep(7)
        self.lp = LoginPage(self.driver)

        ## Login Wallet Wallet User
        self.lp.setCorpoateID(self.corpID)
        self.lp.setUserID(self.userID)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.log.info("Clicked Login")
        self.lp.setOtp()
        self.log.info("OTP set successfully")

        self.menu = Menu(self.driver)
        self.home = HomePage(self.driver)
        self.wallet = WalletTransferPage(self.driver)
        self.bill = BillPaymentPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, self.sheetName)
        for r in range(2, self.rows + 1):
            ## menu
            self.menu.clickMenu()
            self.menu.click_wallet_and_card_Transfer_button()
            # self.home.clickWalletAndCard()

            self.WalletType = XLUtils.readData(self.path, self.sheetName, r, 1)

            ## Choose a Wallet type
            self.wallet.choose_a_Wallet_type(self.WalletType)
            self.wallet.selectUSDaccount()
            all_payee_bank_bakong = {
                "AMRET MFI": "fndtfr__WalletTransfer__payeebank_option_AMRET MFI",
                "AMK Microfinance Plc.": "fndtfr__WalletTransfer__payeebank_option_AMK Microfinance Plc.",
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
            for i in all_payee_bank_bakong:
                self.driver.find_element(By.ID, "fndtfr__WalletTransfer__payeebank").click()
                sleep(0.1)
                self.driver.find_element(By.ID, all_payee_bank_bakong[i]).click()
                sleep(0.3)
            assert False
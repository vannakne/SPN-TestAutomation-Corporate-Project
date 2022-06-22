from time import sleep

import pytest
from termcolor import colored

from pageObject.HomePage import HomePage
from pageObject.LoginPage import LoginPage
from pageObject.MobileTopUpPage import MobileTopUp
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperty import ReadConfig_Wallet
from pageObject.Menu import Menu
from pageObject.BillPaymentPage import BillPaymentPage


class Test_Mobile_TopUP:
    baseURL = ReadConfig_Wallet.getApplicationURL()
    corpID = ReadConfig_Wallet.getWalletCorpID()
    userID = ReadConfig_Wallet.getWalletUserID()
    password = ReadConfig_Wallet.getWalletPassword()
    path = '../TestData/Test_Data.xlsx'
    sheetName = 'Mobile TopUP'

    log = LogGen.genlog()

    result_passed = []
    result_failed = []

    @pytest.mark.mobileTopUP
    def test_pin(self, setup):
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
        self.mobile = MobileTopUp(self.driver)
        self.bill = BillPaymentPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, self.sheetName)
        for r in range(1):
            ## menu
            self.menu.clickMenu()
            self.menu.click_mobile_topUp_button()
            self.menu.click_top_up_button()
            self.mobile.selectUSDaccount()
            self.mobile.click_pin_radio()
            self.amount = '5 USD'
            self.mobile.clickTopUP_amount_Dropdown_pin()
            self.mobile.choose_an_amount_pin(self.amount)
            self.mobile.clickRemark_pin()
            sleep(1)
            try:
                self.message = self.mobile.getPopUpMessage()
                print()
                print("PIN Base")
                print(colored("============================================", 'red'))
                print(colored(self.amount, 'yellow'))
                print('Message: ', '\"' + self.message + '\"')
                print(colored("==> Failed", 'red'))
                print(colored("============================================", 'red'))
                self.result_failed.append("Failed")
                self.mobile.clickOK()
                sleep(2)
                try:
                    self.bill.click_SPN_Logo()
                    sleep(2)
                    continue
                except:
                    sleep(2)
                    continue
            except:
                self.mobile.clickRemark_pin()
                sleep(0.1)
                self.mobile.clickPay()
                self.log.info("Pay button clicked.")
                sleep(1.5)
            # Confirmation Screen
            try:
                self.amt = self.mobile.get_trf_amount()
                self.mobile.clickConfirm()
                sleep(0.5)
                self.mobile.enter_Tpin('000000')
                sleep(0.5)
                self.mobile.clickSubmit()
                sleep(3)
                try:
                    self.message = self.mobile.getPopUpMessage()
                    print()
                    print("PIN Base")
                    print(colored("============================================", 'red'))
                    print(colored("PIN Base", 'yellow'))
                    print(colored(self.amount, 'yellow'))
                    print('Message: ', '\"' + self.message + '\"')
                    print(colored("==> Failed", 'red'))
                    print(colored("============================================", 'red'))
                    self.result_failed.append("Failed")
                    self.mobile.clickOK()
                    sleep(2)
                    try:
                        self.bill.click_SPN_Logo()
                        sleep(2)
                        continue
                    except:
                        sleep(2)
                        continue
                except:
                    self.bill.click_SPN_Logo()
                    self.log.info("***************Test %s***************", "PIN Base")
                    print()
                    print("PIN Base")
                    print(colored("============================================", 'green'))
                    print(colored("PIN Base", 'green'))
                    print(colored(self.amount, 'green'))
                    print(colored("==> Passed", 'green'))
                    print("Details:")
                    print("Transfer Amount: ", self.amt)
                    print(colored("============================================", 'green'))
                    self.result_passed.append("Passed")
                    sleep(2)
                    continue
            except:
                self.message = self.mobile.getPopUpMessage()
                print()
                print("PIN Base")
                print(colored("============================================", 'red'))
                print(colored("PIN Base", 'yellow'))
                print(colored(self.amount, 'yellow'))
                print('Message: ', '\"' + self.message + '\"')
                print(colored("==> Failed", 'red'))
                print(colored("============================================", 'red'))
                self.result_failed.append("Failed")
                self.mobile.clickOK()
                sleep(2)
                try:
                    self.bill.click_SPN_Logo()
                    sleep(2)
                    continue
                except:
                    sleep(2)
                    continue
        print(colored("Passed:", 'green'), len(self.result_passed))
        print(colored("Failed:", 'red'), len(self.result_failed))
        self.driver.close()
        assert False

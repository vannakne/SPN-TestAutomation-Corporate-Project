from time import sleep

import pytest
from termcolor import colored

from pageObject.HomePage import HomePage
from pageObject.LoginPage import LoginPage
from pageObject.RetailPayPage import RetailPay
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperty import ReadConfig_Wallet
from pageObject.Menu import Menu
from pageObject.BillPaymentPage import BillPaymentPage


class Test_RetailPay:
    baseURL = ReadConfig_Wallet.getApplicationURL()
    corpID = ReadConfig_Wallet.getWalletCorpID()
    userID = ReadConfig_Wallet.getWalletUserID()
    password = ReadConfig_Wallet.getWalletPassword()
    path = '../TestData/Test_Data.xlsx'
    sheetName = 'RetailPay Phone'

    log = LogGen.genlog()

    result_passed = []
    result_failed = []

    @pytest.mark.retailPay
    def test_to_phone_number(self, setup):
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
        self.retail = RetailPay(self.driver)
        self.bill = BillPaymentPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, self.sheetName)
        for r in range(2, self.rows + 1):
            ## menu
            self.menu.clickMenu()
            self.menu.click_retail_pay_button()
            self.menu.click_retail_pay_to_phone()

            self.number = XLUtils.readData(self.path, self.sheetName, r, 1)

            self.retail.selectUSDaccount()
            self.retail.enter_phone_number(self.number)
            self.receiver_name = XLUtils.readData(self.path, self.sheetName, r, 2)
            self.retail.enter_receiver_name(self.receiver_name)
            self.retail.clickRemark()
            sleep(1)
            try:
                self.message = self.retail.getPopUpMessage()
                print()
                print(self.number)
                print(colored("============================================", 'red'))
                print(colored(self.number, 'yellow'))
                print(colored(self.receiver_name, 'yellow'))
                print('Message: ', '\"' + self.message + '\"')
                print(colored("==> Failed", 'red'))
                print(colored("============================================", 'red'))
                self.result_failed.append("Failed")
                self.retail.clickOK()
                sleep(2)
                try:
                    self.bill.click_SPN_Logo()
                    sleep(2)
                    continue
                except:
                    sleep(2)
                    continue
            except:
                self.amount_ccy = self.retail.getAmountCCY()
                if self.amount_ccy == 'USD':
                    self.retail.enter_Amount('1')
                elif self.amount_ccy == 'KHR':
                    self.retail.enter_Amount('4000')
            self.retail.clickRemark()
            sleep(0.1)
            self.retail.clickPay()
            self.log.info("Pay button clicked.")
            sleep(1.5)
            try:
                self.amt = self.retail.get_trf_amount()
                self.retail.clickConfirm()
                sleep(0.5)
                self.retail.enter_Tpin('000000')
                sleep(0.5)
                self.retail.clickSubmit()
                sleep(3)
                try:
                    self.message = self.retail.getPopUpMessage()
                    print()
                    print(self.number)
                    print(colored("============================================", 'red'))
                    print(colored(self.number, 'yellow'))
                    print(colored(self.receiver_name, 'yellow'))
                    print('Message: ', '\"' + self.message + '\"')
                    print(colored("==> Failed", 'red'))
                    print(colored("============================================", 'red'))
                    self.result_failed.append("Failed")
                    self.retail.clickOK()
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
                    self.log.info("***************Test %s***************", self.number)
                    print()
                    print(self.number)
                    print(colored("============================================", 'green'))
                    print(colored(self.number, 'green'))
                    print(colored(self.receiver_name, 'green'))
                    print(colored("==> Passed", 'green'))
                    print("Details:")
                    print("Transfer Amount: ", self.amt)
                    print(colored("============================================", 'green'))
                    self.result_passed.append("Passed")
                    sleep(2)
                    continue
            except:
                self.message = self.retail.getPopUpMessage()
                print()
                print(self.number)
                print(colored("============================================", 'red'))
                print(colored(self.number, 'yellow'))
                print(colored(self.receiver_name, 'yellow'))
                print('Message: ', '\"' + self.message + '\"')
                print(colored("==> Failed", 'red'))
                print(colored("============================================", 'red'))
                self.result_failed.append("Failed")
                self.retail.clickOK()
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

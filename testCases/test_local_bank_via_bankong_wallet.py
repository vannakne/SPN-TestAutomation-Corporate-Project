from time import sleep

import pytest
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
    sheetName = 'Local Bank via Bakong'

    log = LogGen.genlog()

    result_passed = []
    result_failed = []

    @pytest.mark.wallet
    def test_020_local_bank_via_bakong(self, setup):
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

            self.bank = XLUtils.readData(self.path, self.sheetName, r, 2)
            self.conusmerNum = XLUtils.readData(self.path, self.sheetName, r, 3)
            self.wallet.choose_a_local_bank(self.bank)
            self.wallet.enter_consumer_number(self.conusmerNum)
            self.wallet.clickRemark()
            sleep(1)
            try:
                self.message = self.wallet.getPopUpMessage()
                print()
                print(self.WalletType)
                print(colored("============================================", 'red'))
                print(colored(self.WalletType, 'yellow'))
                print(colored(self.conusmerNum, 'yellow'))
                print('Message: ', '\"' + self.message + '\"')
                print(colored("==> Failed", 'red'))
                print(colored("============================================", 'red'))
                self.result_failed.append("Failed")
                self.wallet.clickOK()
                sleep(2)
                try:
                    self.bill.click_SPN_Logo()
                    sleep(2)
                    continue
                except:
                    sleep(2)
                    continue
            except:
                self.amount_ccy = self.wallet.getAmountCCY()
                if self.amount_ccy == 'USD':
                    self.wallet.enter_Amount('1')
                elif self.amount_ccy == 'KHR':
                    self.wallet.enter_Amount('4000')
            self.wallet.clickRemark()
            sleep(0.1)
            self.wallet.clickPay()
            self.log.info("Pay button clicked.")
            sleep(1.5)
            try:
                self.amt = self.wallet.get_trf_amount()
                self.wallet.clickConfirm()
                sleep(0.5)
                self.wallet.enter_Tpin('000000')
                sleep(0.5)
                self.wallet.clickSubmit()
                sleep(3)
                try:
                    self.message = self.wallet.getPopUpMessage()
                    print()
                    print(self.WalletType)
                    print(colored("============================================", 'red'))
                    print(colored(self.WalletType, 'yellow'))
                    print(colored(self.conusmerNum, 'yellow'))
                    print('Message: ', '\"' + self.message + '\"')
                    print(colored("==> Failed", 'red'))
                    print(colored("============================================", 'red'))
                    self.result_failed.append("Failed")
                    self.wallet.clickOK()
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
                    self.log.info("***************Test %s***************", self.WalletType)
                    print()
                    print(self.WalletType)
                    print(colored("============================================", 'green'))
                    print(colored(self.WalletType, 'green'))
                    print(colored(self.conusmerNum, 'green'))
                    print(colored("==> Passed", 'green'))
                    print("Details:")
                    print("Transfer Amount: ", self.amt)
                    print(colored("============================================", 'green'))
                    self.result_passed.append("Passed")
                    sleep(2)
                    continue
            except:
                self.message = self.wallet.getPopUpMessage()
                print()
                print(self.WalletType)
                print(colored("============================================", 'red'))
                print(colored(self.WalletType, 'yellow'))
                print(colored(self.conusmerNum, 'yellow'))
                print('Message: ', '\"' + self.message + '\"')
                print(colored("==> Failed", 'red'))
                print(colored("============================================", 'red'))
                self.result_failed.append("Failed")
                self.wallet.clickOK()
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

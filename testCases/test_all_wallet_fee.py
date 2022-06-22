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
    sheetName = 'All Wallet'

    log = LogGen.genlog()

    result_passed = []
    result_failed = []
    acc_balance_list = []
    passed_list = {}
    failed_list = {}

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
            self.home_acc_blnc = self.home.getAccountBalance()
            self.acc_balance_list.append(self.home_acc_blnc)

            ## menu
            self.menu.clickMenu()
            self.menu.click_wallet_and_card_Transfer_button()
            # self.home.clickWalletAndCard()

            self.walletType = XLUtils.readData(self.path, self.sheetName, r, 1)

            ## Choose a Wallet type
            self.wallet.choose_a_Wallet_type(self.walletType)
            self.wallet.selectUSDaccount()

            self.conusmerNum = XLUtils.readData(self.path, self.sheetName, r, 2)
            self.wallet.enter_consumer_number(self.conusmerNum)
            self.wallet.clickRemark()
            sleep(1)
            try:
                self.message = self.wallet.getPopUpMessage()
                print()
                print(self.walletType)
                print(colored("============================================", 'red'))
                print(colored(self.walletType, 'yellow'))
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
                self.log.info("Attempt to Get Amount Transfer.")
                self.amt = self.wallet.get_trf_amount()
                self.log.info("Attempt to Get Converted Value.")
                self.cvt_value = self.wallet.get_converted_value()
                self.log.info("Attempt to Get Fee Charge.")
                self.fee_charge = self.wallet.get_fee_charge()
                self.log.info("Attempt to get exchange rate value.")
                self.exchane_rate = self.wallet.get_exchange_rate()
                self.log.info("Attempt to Click Confirm Button.")
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
                    print(self.walletType)
                    print(colored("============================================", 'red'))
                    print(colored(self.walletType, 'yellow'))
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
                    self.log.info("***************Test %s***************", self.walletType)
                    sleep(2)
                    self.home_acc_blnc = self.home.getAccountBalance()
                    self.acc_balance_list.append(self.home_acc_blnc)
                    print(self.acc_balance_list)
                    self.initialBlnc = self.acc_balance_list[-2]
                    self.total = self.amt + self.fee_charge
                    if self.amount_ccy == 'KHR':
                        self.total_cvt = self.total / self.exchane_rate
                        self.total_cvt = round(self.total_cvt, 2)
                        self.debitedBlnc1 = self.initialBlnc - self.total_cvt
                    else:
                        self.debitedBlnc1 = self.initialBlnc - self.total
                    self.debitedBlnc = round(self.debitedBlnc1, 2)
                    if self.debitedBlnc == self.acc_balance_list[-1]:
                        self.passed_list[self.walletType] = ["Nothing", self.conusmerNum, self.amt, self.fee_charge,
                                                           self.cvt_value, self.amt + self.fee_charge, self.initialBlnc,
                                                           self.debitedBlnc]
                    else:
                        self.result_failed.append("Failed")
                        print()
                        print(self.walletType)
                        print(colored("============================================", 'red'))
                        print(colored(self.conusmerNum, 'yellow'))
                        print("Initial Balance:", self.acc_balance_list[-2], ", TXN Amount:", self.amt, self.amount_ccy,
                              "Fee Charge:", self.fee_charge, self.amount_ccy, ", Exchange Rate:", self.exchane_rate,
                              self.amount_ccy)
                        print("Debited Balance: ", self.acc_balance_list[-1])
                        print("It should be: ", self.debitedBlnc)
                        print(colored('Fee Charge does not deducted!!!', 'yellow'))
                        print(colored("==> Failed", 'red'))
                        print(colored("============================================", 'red'))
                    continue
            except:
                self.message = self.wallet.getPopUpMessage()
                print()
                print(self.walletType)
                print(colored("============================================", 'red'))
                print(colored(self.walletType, 'yellow'))
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
        for i in self.passed_list:
            print(i)
            print(colored("============================================", 'green'))
            print("Biller:", self.passed_list[i][0])
            print("Consumer No:", self.passed_list[i][1])
            print("Details: ")
            print("Transfer Amount:", self.passed_list[i][2])
            print("Fee Charge:", self.passed_list[i][3])
            print("Converted Value:", self.passed_list[i][4])
            print("Total:", self.passed_list[i][5])
            print("Initial Balance:", self.passed_list[i][6])
            print("Debited Balance:", self.passed_list[i][7])
            print(colored("============================================\n", 'green'))
        print(colored("Passed:", 'green'), len(self.passed_list))
        print(colored("Failed:", 'red'), len(self.result_failed))
        self.driver.close()
        assert False

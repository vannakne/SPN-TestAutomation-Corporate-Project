from time import sleep

from pageObject.FundTransferPage import FundTransfer
from pageObject.HomePage import HomePage
from pageObject.AccountManagementPage import SourceAccount
from utilities.readProperty import ReadConfig_Transfer
from pageObject.BillPaymentPage import BillPaymentPage
from pageObject.Menu import Menu
from pageObject.LoginPage import LoginPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from termcolor import colored

class Test_013_Transfer:
    baseURL = ReadConfig_Transfer.getApplicationURL()
    corpID = ReadConfig_Transfer.getCorpID()
    userID = ReadConfig_Transfer.getUserID()
    password = ReadConfig_Transfer.getPassword()
    path = '../TestData/Test_Data.xlsx'

    log = LogGen.genlog()

    result_passed = []
    result_failed = []
    acc_balance_list = []
    passed_list = {}
    def test_013_Transfer(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        sleep(7)

        self.lp = LoginPage(self.driver)

        ## Login Bill Payment User
        self.lp.setCorpoateID(self.corpID)
        self.lp.setUserID(self.userID)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.setOtp()

        self.home = HomePage(self.driver)
        self.account = SourceAccount(self.driver)
        self.menu = Menu(self.driver)
        self.bill = BillPaymentPage(self.driver)
        self.transfer = FundTransfer(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'FundTransfer')

        for r in range(2, self.rows+1):
            self.trf_type = XLUtils.readData(self.path, 'FundTransfer', r, 1)
            self.src_acc = XLUtils.readData(self.path, 'FundTransfer', r, 2)
            self.src_acc_ccy = XLUtils.readData(self.path, 'FundTransfer', r, 3)
            self.payee_acc = XLUtils.readData(self.path, 'FundTransfer', r, 4)
            self.payee_acc_ccy = XLUtils.readData(self.path, 'FundTransfer', r, 5)
            ## menu
            self.menu.clickMenu()
            self.menu.click_transfer_button()
            self.menu.click_transfer_under_transfer()
            sleep(5)

            self.account.select_a_source_acc(self.src_acc)
            sleep(1)

            self.transfer.choose_a_trf_type(self.trf_type)
            sleep(0.2)

            self.account.select_a_payee_acc(self.payee_acc)
            sleep(0.1)

            self.amnt_ccy = self.transfer.get_amount_ccy()
            print(self.amnt_ccy)
            if self.amnt_ccy == 'USD':
                self.transfer.enter_amount('1')
            elif self.amnt_ccy == 'KHR':
                self.transfer.enter_amount('4000')
            self.transfer.click_remark()
            sleep(1)

            ## incase error due to fee charge
            try:
                self.message = self.bill.getPopUpMessage()
                print()
                print(self.trf_type)
                print(colored("============================================", 'red'))
                print(colored("From Account: ", 'yellow'))
                print(colored(self.src_acc, 'yellow'), colored(self.src_acc_ccy, 'yellow'), "To Payee", colored(self.payee_acc, 'yellow'), colored(self.src_acc_ccy, 'yellow'))
                print('Message: ', '\"' + self.message + '\"')
                print(colored("==> Failed", 'red'))
                print(colored("============================================", 'red'))
                self.result_failed.append("Failed")
                self.bill.clickOK()
                sleep(2)
                try:
                    self.bill.click_SPN_Logo()
                    sleep(2)
                    continue
                except:
                    sleep(2)
                    continue
            except:
                self.transfer.click_pay()
                sleep(3)
            try:
                self.transfer.click_confirm()
                sleep(0.5)
                self.transfer.enter_tpin('000000')
                self.transfer.click_submit_tpin()
                try:
                    self.message = self.bill.getPopUpMessage()
                    print()
                    print(self.trf_type)
                    print(colored("============================================", 'red'))
                    print(colored("From Account: ", 'yellow'))
                    print(colored(self.src_acc, 'yellow'), colored(self.src_acc_ccy, 'yellow'), "To Payee",
                          colored(self.payee_acc, 'yellow'), colored(self.src_acc_ccy, 'yellow'))
                    print('Message: ', '\"' + self.message + '\"')
                    print(colored("==> Failed", 'red'))
                    print(colored("============================================", 'red'))
                    self.result_failed.append("Failed")
                    self.bill.clickOK()
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
                    sleep(2)
                    continue
            except:
                self.message = self.bill.getPopUpMessage()
                print()
                print(self.trf_type)
                print(colored("============================================", 'red'))
                print(colored("From Account: ", 'yellow'))
                print(colored(self.src_acc, 'yellow'), colored(self.src_acc_ccy, 'yellow'), "To Payee",
                      colored(self.payee_acc, 'yellow'), colored(self.src_acc_ccy, 'yellow'))
                print('Message: ', '\"' + self.message + '\"')
                print(colored("==> Failed", 'red'))
                print(colored("============================================", 'red'))
                self.result_failed.append("Failed")
                self.bill.clickOK()
                sleep(2)
                try:
                    self.bill.click_SPN_Logo()
                    sleep(2)
                    continue
                except:
                    sleep(2)
                    continue
        if "Failed" not in self.result_failed:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
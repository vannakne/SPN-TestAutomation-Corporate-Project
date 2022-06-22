from time import sleep

from pageObject.HomePage import HomePage
from utilities.readProperty import ReadConfig_bill
from pageObject.BillPaymentPage import BillPaymentPage
from pageObject.Menu import Menu
from pageObject.LoginPage import LoginPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from termcolor import colored

class Test_011_Payment:
    baseURL = ReadConfig_bill.getApplicationURL()
    corpID = ReadConfig_bill.getBillPaymentCorpID()
    userID = ReadConfig_bill.getBillPaymentUserID()
    password = ReadConfig_bill.getBillPaymentPassword()
    path = '../TestData/Test_Data.xlsx'

    log = LogGen.genlog()

    result_passed = []
    result_failed = []
    acc_balance_list = []
    passed_list = {}
    def test_011_Payment(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        sleep(5)

        self.lp = LoginPage(self.driver)

        ## Login Bill Payment User
        self.lp.setCorpoateID(self.corpID)
        self.lp.setUserID(self.userID)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.setOtp()

        self.home = HomePage(self.driver)
        self.menu = Menu(self.driver)
        self.bill = BillPaymentPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Waste')
        for r in range(2, self.rows+1):
            # self.home_acc_blnc = self.home.getAccountBalance()
            # self.acc_balance_list.append(self.home_acc_blnc)
            ## menu
            self.menu.clickMenu()
            self.menu.click_payment_button()
            self.menu.click_payment_under_payment()

            self.billType = 'Waste'
            ## Choose a bill type
            self.bill.choose_a_bill_type(self.billType)

            self.bill.selectUSDaccount()

            self.biller = XLUtils.readData(self.path, 'Waste', r, 1)
            self.bill.clickBillerDropDown()
            self.bill.choose_a_biller(self.biller)
            self.log.info("%s Found", self.biller)

            self.consumer = XLUtils.readData(self.path, 'Waste', r, 2)
            self.bill.fillConsumer(self.consumer)
            self.bill.clickRemark()
            sleep(1)
            try:
                self.message = self.bill.getPopUpMessage()
                print()
                print(self.billType)
                print(colored("============================================", 'red'))
                print(colored(self.biller, 'yellow'))
                print(colored(self.consumer, 'yellow'))
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
                self.amount_ccy = self.bill.getAmountCurrency()
                if self.amount_ccy == 'USD':
                    self.bill.enterAmount('1')
                    sleep(1)
                elif self.amount_ccy == 'KHR':
                    self.bill.enterAmount('4000')
                    sleep(1)
            self.bill.clickRemark()
            sleep(0.1)
            self.bill.clickPay()
            self.log.info("Pay button clicked.")
            sleep(1)
            try:
                self.log.info("Attempt to Get Amount Transfer.")
                self.amt = self.bill.get_trf_amount()
                self.log.info("Attempt to Get Converted Value.")
                self.cvt_value = self.bill.get_converted_value()
                self.log.info("Attempt to Get Fee Charge.")
                self.fee_charge = self.bill.get_fee_charge()
                self.log.info("Attempt to Click Confirm Button.")
                self.bill.clickConfirm()
                sleep(0.5)
                self.bill.enterTPIN('000000')
                sleep(0.5)
                self.bill.clickSubmitTpin()
                sleep(3)
                try:
                    self.message = self.bill.getPopUpMessage()
                    print()
                    print(self.billType)
                    print(colored("============================================", 'red'))
                    print(colored(self.biller, 'yellow'))
                    print(colored(self.consumer, 'yellow'))
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
                    self.log.info("***************Test %s***************", self.billType)
                    # print()
                    # print(self.billType)
                    self.passed_list[self.billType] = [self.biller, self.consumer, self.amt, self.fee_charge, self.cvt_value]
                    # print(colored("============================================", 'green'))
                    # print(colored(self.biller, 'green'))
                    # print(colored(self.consumer, 'green'))
                    # print(colored("==> Passed", 'green'))
                    # print('Details: ')
                    # print("Transfer Amount: ", self.amt, self.amount_ccy)
                    # print("Fee Charge: ", self.fee_charge, 'USD')
                    # print("Converted Value: ", self.cvt_value, 'USD')
                    # print(colored("============================================", 'green'))
                    self.result_passed.append("Passed")
                    sleep(2)
                    continue
            except:
                self.message = self.bill.getPopUpMessage()
                print()
                print(self.billType)
                print(colored("============================================", 'red'))
                print(colored(self.biller, 'yellow'))
                print(colored(self.consumer, 'yellow'))
                print('Message: ', '\"'+self.message+'\"')
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
        print("Passed:", len(self.result_passed), self.result_passed)
        print("Failed:", len(self.result_failed), self.result_failed)
        print(self.passed_list)
        if "Failed" not in self.result_failed:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

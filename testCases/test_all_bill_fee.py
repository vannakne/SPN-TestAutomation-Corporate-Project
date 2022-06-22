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
    sheetName = 'All BillPayment'

    log = LogGen.genlog()

    result_passed = []
    result_failed = []
    acc_balance_list = []
    passed_list = {}
    failed_list = {}
    def test_012_Payment_Fee(self, setup):
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
        self.menu = Menu(self.driver)
        self.bill = BillPaymentPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, self.sheetName)
        for r in range(2, self.rows+1):
            self.home_acc_blnc = self.home.getAccountBalance()
            self.acc_balance_list.append(self.home_acc_blnc)

            # assert False
            ## menu
            self.menu.clickMenu()
            self.menu.click_payment_button()
            self.menu.click_payment_under_payment()

            self.billType = XLUtils.readData(self.path, self.sheetName, r, 1)
            ## Choose a bill type
            self.bill.choose_a_bill_type(self.billType)

            self.bill.selectUSDaccount()

            self.biller = XLUtils.readData(self.path, self.sheetName, r, 2)
            self.bill.clickBillerDropDown()
            self.bill.choose_a_biller(self.biller)
            self.log.info("%s Found", self.biller)

            self.consumer = XLUtils.readData(self.path, self.sheetName, r, 3)
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
            sleep(3)
            try:
                self.log.info("Attempt to Get Amount Transfer.")
                self.amt = self.bill.get_trf_amount()
                self.log.info("Attempt to Get Converted Value.")
                self.cvt_value = self.bill.get_converted_value()
                self.log.info("Attempt to Get Fee Charge.")
                self.fee_charge = self.bill.get_fee_charge()
                self.log.info("Attempt to get exchange rate value.")
                self.exchane_rate = self.bill.get_exchange_rate()
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
                    sleep(2)
                    self.home_acc_blnc = self.home.getAccountBalance()
                    self.acc_balance_list.append(self.home_acc_blnc)
                    print(self.acc_balance_list)
                    self.initialBlnc = self.acc_balance_list[-2]
                    self.total = self.amt + self.fee_charge
                    if self.amount_ccy == 'KHR':
                        self.total_cvt = self.total/self.exchane_rate
                        self.total_cvt = round(self.total_cvt, 2)
                        self.debitedBlnc1 = self.initialBlnc - self.total_cvt
                    else:
                        self.debitedBlnc1 = self.initialBlnc - self.total
                    self.debitedBlnc = round(self.debitedBlnc1, 2)
                    if self.debitedBlnc == self.acc_balance_list[-1]:
                        self.passed_list[self.billType] = [self.biller, self.consumer, self.amt, self.fee_charge, self.cvt_value, self.amt+self.fee_charge, self.initialBlnc, self.debitedBlnc]
                    else:
                        self.result_failed.append("Failed")
                        print()
                        print(self.billType)
                        print(colored("============================================", 'red'))
                        print(colored(self.biller, 'yellow'))
                        print(colored(self.consumer, 'yellow'))
                        print("Initial Balance:", self.acc_balance_list[-2], ", TXN Amount:", self.amt,self.amount_ccy, "Fee Charge:", self.fee_charge,self.amount_ccy, ", Exchange Rate:", self.exchane_rate,self.amount_ccy)
                        print("Debited Balance: ", self.acc_balance_list[-1])
                        print("It should be: ", self.debitedBlnc)
                        print(colored('Fee Charge does not deducted!!!', 'yellow'))
                        print(colored("==> Failed", 'red'))
                        print(colored("============================================", 'red'))
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

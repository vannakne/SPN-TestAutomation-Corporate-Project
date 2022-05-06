from time import sleep
from utilities.readProperty import ReadConfig_bill
from pageObject.BillPaymentPage import BillPaymentPage
from pageObject.Menu import Menu
from pageObject.LoginPage import LoginPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from termcolor import colored

class Test_004_Electric:
    baseURL = ReadConfig_bill.getApplicationURL()
    corpID = ReadConfig_bill.getBillPaymentCorpID()
    userID = ReadConfig_bill.getBillPaymentUserID()
    password = ReadConfig_bill.getBillPaymentPassword()
    path = '../TestData/Test_Data.xlsx'

    log = LogGen.genlog()

    result_passed = []
    result_failed = []

    def test_005_education(self, setup):
        print("Start test 005")
        self.driver = setup
        self.driver.get(self.baseURL)
        sleep(5)

        self.lp = LoginPage(self.driver)

        ## Login Bill Payment User
        self.lp.setCorpoateID(self.corpID)
        self.lp.setUserID(self.userID)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.otp = input("OTP: ")
        self.lp.setOtp(self.otp)

        self.menu = Menu(self.driver)
        self.bill = BillPaymentPage(self.driver)

        ## menu
        self.menu.clickMenu()
        sleep(1)
        self.menu.click_payment_button()
        self.menu.click_payment_under_payment()
        sleep(1)

        self.rows = XLUtils.getRowCount(self.path, 'Education')

        ## Electricity
        self.bill.clickEducation()
        self.bill.selectUSDaccount()

        for r in range(2, self.rows+1):
            self.biller = XLUtils.readData(self.path, 'Education', r, 1)
            self.bill.clickBillerDropDown()
            self.bill.choose_an_education_biller(self.biller)
            self.log.info("%s Found", self.biller)

            self.consumer = XLUtils.readData(self.path, 'Education', r, 2)
            self.bill.fillConsumer(self.consumer)
            self.amount_ccy = self.bill.getAmountCurrency()

            # self.bill.clearConsumer()
            if self.amount_ccy == 'USD':
                self.bill.enterAmount('1')
                sleep(1)
            elif self.amount_ccy == 'KHR':
                self.bill.enterAmount('4000')
                sleep(1)
            self.bill.clickPay()
            sleep(1)
            try:
                self.bill.clickPay()
                sleep(1)
                self.buttonText = self.bill.getConfirmButtonText()
                self.bill.clickConfirm()
                sleep(0.5)
                self.bill.enterTPIN('000000')
                sleep(0.5)
                self.bill.clickSubmitTpin()
                print(colored("Submit TPIN Clicked", 'red'))
                sleep(3)
                self.bill.clickMakeAnotherTrf()
                print(colored("Make Another Transfer clicked", 'red'))
                print()
                print(colored("============================================", 'green'))
                print(colored(self.biller, 'green'))
                print(colored(self.consumer, 'green'))
                print(colored("==> Passed", 'green'))
                print(colored("============================================", 'green'))
                self.result_passed.append("Passed")
                sleep(2)
                ## electicity
                self.bill.clickEducation()
                print("Electricity CLicked")
                self.bill.selectUSDaccount()
                print("USD account selected")
            except:
                self.message = self.bill.getPopUpMessage()
                print()
                print(colored("============================================", 'red'))
                print(colored(self.biller, 'yellow'))
                print(colored(self.consumer, 'yellow'))
                print('Message: ', '\"'+self.message+'\"')
                print(colored("==> Failed", 'red'))
                print(colored("============================================", 'red'))
                self.result_failed.append("Failed")
                if self.message == 'Invalid Request':
                    self.bill.clickOK()
                    sleep(2)
                    ## menu
                    self.menu.clickMenu()
                    sleep(1)
                    self.menu.click_payment_button()
                    self.menu.click_payment_under_payment()
                    sleep(1)
                    self.bill.clickEducation()
                    self.bill.selectUSDaccount()
                else:
                    self.bill.clickOK()
                    self.bill.clearConsumer()
                    self.bill.clearAmount()
        self.driver.close()
        print(len(self.result_passed))
        print(len(self.result_failed))

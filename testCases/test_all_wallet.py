from termcolor import colored
from trio import sleep

from pageObject.LoginPage import LoginPage
from pageObject.WalletAndCardTransferPage import WalletTransferPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperty import ReadConfig_Wallet
from pageObject.Menu import Menu
from pageObject.BillPaymentPage import BillPaymentPage

class Test_010_Wallet:
    baseURL = ReadConfig_Wallet.getApplicationURL()
    corpID = ReadConfig_Wallet.getBillWalletCorpID()
    userID = ReadConfig_Wallet.getBillWalletUserID()
    password = ReadConfig_Wallet.getBillWalletPassword()
    path = '../TestData/Test_Data.xlsx'

    log = LogGen.genlog()

    result_passed = []
    result_failed = []

    def Test_010_Wallet(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        sleep(3)

        self.lp = LoginPage(self.driver)

        ## Login Wallet Wallet User
        self.lp.setCorpoateID(self.corpID)
        self.lp.setUserID(self.userID)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.setOtp()

        self.menu = Menu(self.driver)
        self.wallet = WalletTransferPage(self.driver)
        self.bill = BillPaymentPage(self.driver)
        
        self.rows = XLUtils.getRowCount(self.path, 'All Wallet')
        for r in range(2, self.rows+1):
            ## menu
            self.menu.clickMenu()
            self.menu.click_wallet_and_card_Transfer_button()

            self.WalletType = XLUtils.readData(self.path, 'All Wallet', r, 1)

            ## Choose a Wallet type
            self.wallet.choose_a_Wallet_type(self.WalletType)
            self.wallet.selectUSDaccount()

            self.conusmerNum = XLUtils.readData(self.path, 'All Wallet', r, 2)
            self.wallet.enter_consumer_number(self.conusmerNum)

            self.amount_ccy = self.wallet.getAmountCCY()

            if self.amount_ccy == 'USD':
                self.wallet.enter_Amount('1')
                sleep(1)
            elif self.amount_ccy == 'KHR':
                self.wallet.enter_Amount('4000')
                sleep(1)
            self.wallet.clickRemark()
            sleep(0.5)
            self.wallet.clickPay()
            self.log.info("Pay button clicked.")
            sleep(1)
            try:
                self.wallet.clickConfirm()
                sleep(0.5)
                self.wallet.enter_Tpin('000000')
                sleep(0.5)
                self.wallet.clickSubmit()
                print(colored("Submit TPIN Clicked", 'red'))
                sleep(3)
                self.wallet.clickAnotherTrf()
                print(colored("Make Another Transfer clicked", 'red'))
                self.log.info("***************Test %s***************", self.WalletType)
                print()
                print(self.WalletType)
                print(colored("============================================", 'green'))
                print(colored(self.WalletType, 'green'))
                print(colored(self.conusmerNum, 'green'))
                print(colored("==> Passed", 'green'))
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
                print('Message: ', '\"'+self.message+'\"')
                print(colored("==> Failed", 'red'))
                print(colored("============================================", 'red'))
                self.result_failed.append("Failed")
                if self.message == 'Invalid Request':
                    self.wallet.clickOK()
                    sleep(2)
                    continue
                else:
                    self.wallet.clickOK()
                    self.bill.click_SPN_Logo()
                    sleep(2)
                    continue
        self.driver.close()
        print(len(self.result_passed))
        print(len(self.result_failed))


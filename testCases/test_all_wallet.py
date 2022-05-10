from trio import sleep

from pageObject.LoginPage import LoginPage
from pageObject.WalletAndCardTransferPage import WalletTransferPage
from utilities.readProperty import ReadConfig_Wallet
from pageObject.Menu import Menu

class Test_010_Wallet:
    baseURL = ReadConfig_Wallet.getApplicationURL()
    corpID = ReadConfig_Wallet.getBillPaymentCorpID()
    userID = ReadConfig_Wallet.getBillPaymentUserID()
    password = ReadConfig_Wallet.getBillPaymentPassword()
    path = '../TestData/Test_Data.xlsx'


    def Test_010_Wallet(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        sleep(3)

        self.lp = LoginPage(self.driver)

        ## Login Bill Payment User
        self.lp.setCorpoateID(self.corpID)
        self.lp.setUserID(self.userID)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.setOtp()

        self.menu = Menu(self.driver)
        self.wallet = WalletTransferPage(self.driver)



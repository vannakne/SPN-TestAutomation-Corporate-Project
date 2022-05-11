from time import sleep
from pageObject.LoginPage import LoginPage
from pageObject.HomePage import HomePage
from utilities.readProperty import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DataDriven_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = '../TestData/Test_Data.xlsx'

    mylogger = LogGen.genlog()
    # user = input("User to Login: ")

    def test_login(self, setup):
        self.driver = setup
        while True:
            self.user = input("User to Login: ")
            self.mylogger.info("**************** Test_002_DDT_Login ****************")
            self.mylogger.info("**************** Start Login Test ****************")
            self.lp = LoginPage(self.driver)
            self.hp = HomePage(self.driver)

            self.driver.get(self.baseURL)
            sleep(4)

            self.rows = XLUtils.getRowCount(self.path, 'Sheet2')
            for r in range(2, self.rows+1):
                self.corporateId = XLUtils.readData(self.path, 'Sheet2', r, 1)
                self.userId = XLUtils.readData(self.path, 'Sheet2', r, 2)
                self.password = XLUtils.readData(self.path, 'Sheet2', r, 3)
                # self.exp = XLUtils.readData(self.path, 'Sheet2', r, 4)
                if self.userId == self.user:
                    print("...........Login", self.user, "............")
                    self.lp.setCorpoateID(self.corporateId)
                    self.lp.setUserID(self.userId)
                    self.lp.setPassword(self.password)
                    self.lp.clickLogin()
                    sleep(1)
                    self.lp.setOtp()
            i = input(":")
            if i == '':
                continue
            elif i == 'close':
                self.driver.close()

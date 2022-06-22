from time import sleep
import time
from pageObject.LoginPage import LoginPage
from pageObject.HomePage import HomePage
from utilities.readProperty import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DataDriven_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = '../TestData/User_for_Corp0720376.xlsx'

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
            sleep(5)
            start_time = time.time()
            self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
            for r in range(2, self.rows+1):
                self.corporateId = XLUtils.readData(self.path, 'Sheet1', r, 1)
                self.userId = XLUtils.readData(self.path, 'Sheet1', r, 2)
                self.password = XLUtils.readData(self.path, 'Sheet1', r, 3)
                # self.exp = XLUtils.readData(self.path, 'Sheet1', r, 4)
                if self.userId == self.user:
                    print("--- %s seconds ---" % (time.time() - start_time))
                    print("...........Login", self.user, "............")
                    self.lp.setCorpoateID(self.corporateId)
                    self.lp.setUserID(self.userId)
                    self.lp.setPassword(self.password)
                    print(self.corporateId, self.userId, self.password)
                    self.lp.clickLogin()
                    sleep(1)
                    self.lp.setOtp()
            i = input(":")
            if i == '':
                continue
            elif i == 'close':
                self.driver.close()

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

    def test_login(self, setup):
        self.mylogger.info("**************** Test_002_DDT_Login ****************")
        self.mylogger.info("**************** Start Login Test ****************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

        self.driver.get(self.baseURL)
        sleep(3)

        self.rows = XLUtils.getRowCount(self.path, 'Temp')
        print("Number of Rows: ", self.rows)

        self.result_status = []

        for r in range(2, self.rows+1):
            self.corporateId = XLUtils.readData(self.path, 'Temp', r, 1)
            self.userId = XLUtils.readData(self.path, 'Temp', r, 2)
            self.password = XLUtils.readData(self.path, 'Temp', r, 3)
            # self.exp = XLUtils.readData(self.path, 'Temp', r, 4)
            self.lp.setCorpoateID(self.corporateId)
            self.lp.setUserID(self.userId)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            sleep(1)

            self.otpMessage = self.lp.getOtpMessage()
            if self.otpMessage == "OTP has been sent to your registered Mobile number" or self.otpMessage == "Generated OTP is not yet expired":
                self.result_status.append('Passed')
                print(self.userId, "Passed")
                self.lp.OkAndCancelOtp()
                self.lp.clearLoginCredential()
            else:
                self.result_status.append("Failed")
                print(self.corporateId, self.userId, self.password, "==> Failed")
                self.lp.clickWrongCredentialOk_button()
                self.lp.clearLoginCredential()

        if 'Failed' not in self.result_status:
            assert True
            self.driver.close()
        else:
            self.mylogger.info("************** Test Finished *******************")
            self.driver.close()
            assert False




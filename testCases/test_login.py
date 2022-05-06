from time import sleep
from pageObject.LoginPage import LoginPage
from pageObject.HomePage import HomePage
from utilities.readProperty import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    corporateId = ReadConfig.getCorporateID()
    userId = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    mylogger = LogGen.genlog()
    mylogger.info("test test")

    def test_login(self, setup):
        self.mylogger.info("**************** Test_001_Login ****************")
        self.mylogger.info("**************** Start Login Test ****************")
        self.driver = setup
        self.mylogger.info("******** Opening URL **********")
        self.driver.get(self.baseURL)
        sleep(7)

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

        self.lp.setCorpoateID(self.corporateId)
        self.lp.setUserID(self.userId)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.otpMessage = self.lp.getOtpMessage()
        if self.otpMessage == "OTP has been sent to your registered Mobile number":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("../ScreenShots/Test_001_Login.png")
            self.driver.close()
            # self.mylogger.error("******************* Actual Corp ID was:  *******************")
            assert False

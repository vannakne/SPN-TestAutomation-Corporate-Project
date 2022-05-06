from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_corporateId_id = 'clogin__FirstLaunch__PL_corpId'
    textbox_userId_id = 'clogin__FirstLaunch__PL_userId1'
    textbox_password_id = 'clogin__FirstLaunch__PL_password'
    button_login_id = 'clogin__FirstLaunch__PL_loginBtn'
    linktext_forgotPassword_id = 'clogin__FirstLaunch__forglbl_txtcnt'

    message_otp_class = 'msg'
    button_otpOk_class = 'ok'
    button_wrongCredentialOk_class = 'ok'
    textbox_otp_id = 'clogin__FirstLaunch__loginOtpVal'
    button_otpCancel_id = 'clogin__FirstLaunch__element_button_6'
    button_confirmOtp_id = 'clogin__FirstLaunch__element_button_7'

    button_promotion_id = 'clogin__FirstLaunch__el_btn_1'
    button_locateUs_id = 'clogin__FirstLaunch__el_btn_4'
    button_contactUs_id = 'clogin__FirstLaunch__el_btn_5'

    def __init__(self, driver):
        self.driver = driver

    def setCorpoateID(self, corporateID):
        self.driver.find_element(By.ID, self.textbox_corporateId_id).clear()
        self.driver.find_element(By.ID, self.textbox_corporateId_id).send_keys(corporateID)

    def setUserID(self, userID):
        self.driver.find_element(By.ID, self.textbox_userId_id).clear()
        self.driver.find_element(By.ID, self.textbox_userId_id).send_keys(userID)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_login_id).click()
        sleep(3)

    def getOtpMessage(self):
        otpMessage = self.driver.find_element(By.CLASS_NAME, self.message_otp_class).text
        return otpMessage

    def setOtp(self, otp):
        self.driver.find_element(By.CLASS_NAME, self.button_otpOk_class).click()
        self.driver.find_element(By.ID, self.textbox_otp_id).send_keys(otp)
        self.driver.find_element(By.ID, self.button_confirmOtp_id).click()
        sleep(5)

    def OkAndCancelOtp(self):
        self.driver.find_element(By.CLASS_NAME, self.button_otpOk_class).click()
        self.driver.find_element(By.ID, self.button_otpCancel_id).click()

    def clearLoginCredential(self):
        self.driver.find_element(By.ID, self.textbox_corporateId_id).clear()
        self.driver.find_element(By.ID, self.textbox_userId_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).clear()

    def clickWrongCredentialOk_button(self):
        self.driver.find_element(By.CLASS_NAME, self.button_wrongCredentialOk_class).click()


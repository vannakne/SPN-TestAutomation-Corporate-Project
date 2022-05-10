from time import sleep

from selenium.webdriver.common.by import By


class Test_002_DataDriven_Login:
    def test_login(self, setup):
        self.driver = setup
        while True:
            self.user = input("User to Login: ")
            self.driver.get("http://172.17.250.2:7003/CorporateAdmin/")
            sleep(2)
            # self.exp = XLUtils.readData(self.path, 'Sheet2', r, 4)
            if self.user == "mk":
                self.driver.find_element(By.ID, 'CorpAdmin__LoginPage__LoginCorpId').send_keys("CORP0720376")
                self.driver.find_element(By.ID, 'CorpAdmin__LoginPage__login_input__user_id').send_keys("USER0720376")
                self.driver.find_element(By.ID, 'CorpAdmin__LoginPage__login_input__password').send_keys("Pass@234")
                self.driver.find_element(By.ID, 'CorpAdmin__LoginPage__element_button_1').click()
                sleep(1)
            if self.user == "ck":
                self.driver.find_element(By.ID, 'CorpAdmin__LoginPage__LoginCorpId').send_keys("CORP0720376")
                self.driver.find_element(By.ID, 'CorpAdmin__LoginPage__login_input__user_id').send_keys("AUTH0720376")
                self.driver.find_element(By.ID, 'CorpAdmin__LoginPage__login_input__password').send_keys("Pass@234")
                self.driver.find_element(By.ID, 'CorpAdmin__LoginPage__element_button_1').click()
                sleep(1)
            i = input(":")
            if i == '':
                continue
            elif i == 'user':
                self.driver.close()

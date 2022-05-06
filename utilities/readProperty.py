import configparser

config = configparser.RawConfigParser()
config.read("../Configurations/config.ini")


class ReadConfig:

    @staticmethod
    def getFirefoxPath():
        firefox_path = config.get('firefox path', 'firefox_location')
        return firefox_path

    @staticmethod
    def getApplicationURL():
        url = config.get("common login info", "baseURL")
        return url

    @staticmethod
    def getCorporateID():
        corpID = config.get("common login info", "corporateId")
        return corpID

    @staticmethod
    def getUserID():
        userID = config.get("common login info", "userId")
        return userID

    @staticmethod
    def getPassword():
        password = config.get("common login info", "password")
        return password


class ReadConfig_bill:
    @staticmethod
    def getApplicationURL():
        url = config.get("Bill Payment login info", "baseURL")
        return url

    @staticmethod
    def getBillPaymentCorpID():
        corpID = config.get('Bill Payment login info', 'corporateId_bill')
        return corpID

    @staticmethod
    def getBillPaymentUserID():
        userID = config.get("Bill Payment login info", "userId_bill")
        return userID

    @staticmethod
    def getBillPaymentPassword():
        password = config.get("Bill Payment login info", "password_bill")
        return password
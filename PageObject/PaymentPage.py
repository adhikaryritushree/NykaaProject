from selenium.webdriver.common.by import By


class PaymentPage:
    paytm = (By.LINK_TEXT, "Mobile Wallets")
    txt = (By.XPATH, "//div[@class='media-body info']")
    # vpa = (By.NAME, "vpa")
    pay = (By.CSS_SELECTOR, ".proceed")
    paytmupi = (By.XPATH, "(//div[contains(@class,'_3-zL border-global')])[1]")
    vpa = (By.XPATH, "(//input[@class='form-ctrl fl undefined w100 xs-w100 xs-input '])[1]")
    verify = (By.LINK_TEXT, "Verify VPA")
    verifytext = (By.XPATH, "//span[contains(@class,'_KaHx')]")
    finalpay = (By.XPATH, "//button[contains(@class, 'btn btn-primary w100 pos-r _2fNU')]")

    def __init__(self, driver):
        self.driver = driver

    def mobilewallet(self):
        return self.driver.find_element(*PaymentPage.paytm).click()

    def clickpay(self):
        if self.driver.find_element(*PaymentPage.txt).text == 'Paytm':
            self.driver.find_element(*PaymentPage.pay).click()
        else:
            print("Payment cannot be done")

    def clickonupioption(self):
        self.driver.find_element(*PaymentPage.paytmupi).click()

    def entervpa(self):
        self.driver.find_element(*PaymentPage.vpa).send_keys("7980710131@paytm")
        self.driver.find_element(*PaymentPage.verify).click()

        assert self.driver.find_element(*PaymentPage.verifytext).text == "Verified VPA ID", "Assertion faild due to mismatched text"

    def finalpayment(self):
        self.driver.find_element(*PaymentPage.finalpay).click()







    #
    # def enterupi(self):
    #     return self.driver.find_element(*PaymentPage.vpa)
    #
    # def makepayment(self):
    #     return self.driver.find_element(*PaymentPage.pay)


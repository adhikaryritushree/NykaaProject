from selenium.webdriver.common.by import By


class PaymentPage:
    upi = (By.LINK_TEXT, "UPI")
    vpa = (By.NAME, "vpa")
    pay = (By.CSS_SELECTOR, ".proceed")

    def __init__(self, driver):
        self.driver = driver

    def selectupi(self):
        return self.driver.find_element(*PaymentPage.upi).click()

    def enterupi(self):
        return self.driver.find_element(*PaymentPage.vpa)

    def makepayment(self):
        return self.driver.find_element(*PaymentPage.pay)


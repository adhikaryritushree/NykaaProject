from selenium.webdriver.common.by import By


class SecondPaymentPage:
    upi = (By.LINK_TEXT, "UPI")
    placeholder = (By.XPATH, "//input[contains(@placeholder,'VPA/UPI ID (eg. 9876543210@upi)')]")
    pay = (By.CSS_SELECTOR, ".proceed")


    def __init__(self, driver):
        self.driver = driver

    def clickupi(self):
        self.driver.find_element(*SecondPaymentPage.upi).click()

    def sendupi(self):
        return self.driver.find_element(*SecondPaymentPage.placeholder)

    def makepayment(self):
        self.driver.find_element(*SecondPaymentPage.pay).click()





from selenium.webdriver.common.by import By


class UserDetailsPage:
    continueasguest = (By.XPATH, "//button[text()='CONTINUE AS GUEST']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    phone = (By.NAME, "phoneNumber")
    pin = (By.NAME, "pinCode")
    address = (By.CSS_SELECTOR, ".textarea-control")
    submit = (By.CSS_SELECTOR, "button[type='submit']")


    def __init__(self, driver):
        self.driver = driver

    def continueasaguest(self):
        return self.driver.find_element(*UserDetailsPage.continueasguest).click()

    def entername(self):
        return self.driver.find_element(*UserDetailsPage.name)

    def enteremail(self):
        return self.driver.find_element(*UserDetailsPage.email)

    def enterphone(self):
        return self.driver.find_element(*UserDetailsPage.phone)

    def pincode(self):
        return self.driver.find_element(*UserDetailsPage.pin)

    def enteraddress(self):
        return self.driver.find_element(*UserDetailsPage.address)

    def submitdetails(self):
        return self.driver.find_element(*UserDetailsPage.submit).click()

















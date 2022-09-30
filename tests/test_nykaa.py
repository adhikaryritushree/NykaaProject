import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.AddToCartPage import AddToCartPage
from PageObject.HomePage import HomePage
from PageObject.PaymentPage import PaymentPage
from PageObject.SecondPaymentPage import SecondPaymentPage
from PageObject.UserDetailsPage import UserDetailsPage
from utilities.BaseClass import BaseClass



class TestNykaa(BaseClass):
    def testshopping(self):
        log = self.getLogger()
        homepg = HomePage(self.driver)
        homepg.searchproducttobuy()
        log.info("Product search successful")
        addtocart = AddToCartPage(self.driver)
        addtocart.addtocart()
        addtocart.scrollpageup()
        time.sleep(5)
        addtocart.scrollpg()
        self.verifyAddtoCarttextpresence()
        addtocart.addtocartfinal()
        addtocart.clickcarticon()
        time.sleep(3)
        addtocart.switchtoframe()
        wait1 = WebDriverWait(self.driver, 10)
        wait1.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Proceed']")))
        addtocart.proceedasaguest()
        log.info("Proceed successful, now time to fill up details")
        userdetails = UserDetailsPage(self.driver)
        userdetails.continueasaguest()

    def testdataloading(self, dataload):
        log = self.getLogger()
        userdetails1 = UserDetailsPage(self.driver)
        userdetails1.entername().send_keys(dataload[0])
        userdetails1.enteremail().send_keys(dataload[1])
        userdetails1.enterphone().send_keys(dataload[2])
        userdetails1.pincode().send_keys(dataload[3])
        userdetails1.enteraddress().send_keys(dataload[4])
        userdetails1.submitdetails()
        paymentpg = PaymentPage(self.driver)
        paymentpg.mobilewallet()
        paymentpg.clickpay()
        paymentpg.clickonupioption()
        paymentpg.entervpa()
        paymentpg.finalpayment()
        self.driver.back()
    def testsecondpay(self, dataload1):
        paymentpg2 = SecondPaymentPage(self.driver)
        paymentpg2.clickupi()
        paymentpg2.sendupi().send_keys(dataload1)
        time.sleep(2)
        paymentpg2.makepayment()
        self.driver.refresh()


    @pytest.fixture(params=[("Ritushree Adhikary", "adhikaryritushree1@gmail.com", "7980710131", "700059", "Baguiati, Joramandir", "demo@upi")])
    def dataload(self, request):
        return request.param

    @pytest.fixture(params=['abc@upi', '7980710131@upi', 'demo@upi'])
    def dataload1(self, request):
        return request.param

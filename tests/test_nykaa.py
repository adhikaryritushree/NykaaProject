import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.AddToCartPage import AddToCartPage
from PageObject.HomePage import HomePage
from PageObject.PaymentPage import PaymentPage
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
        time.sleep(5)
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
        paymentpg.selectupi()
        log.info("UPI selected successfully")
        paymentpg.enterupi().send_keys(dataload[5])
        time.sleep(1)
        paymentpg.makepayment().click()
        time.sleep(5)
        self.driver.get("https://www.nykaa.com/shoppingBag?ptype=cartAddress")

    @pytest.fixture(
        params=[("Ritushree Adhikary", "adhikaryritushree1@gmail.com", "7980710131", "700059", "Baguiati, Joramandir", "demo@upi"),
                ("Srinjan Adhikary", "adhikarysrinjan@gmail.com", "8017758703", "700059", "Saltlake", "demo1@upi")])
    def dataload(self, request):
        return request.param

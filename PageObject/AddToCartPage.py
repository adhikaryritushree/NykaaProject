from selenium.webdriver.common.by import By


class AddToCartPage:
    cart = (By.CSS_SELECTOR, ".css-vp18r8")
    shade = (By.CSS_SELECTOR, "#variant_683153")
    addcart = (By.CSS_SELECTOR, "div[class='css-vp18r8']")
    carticon = (By.CSS_SELECTOR, ".css-g4vs13")
    framelocator = (By.TAG_NAME, "iframe")
    proceed = (By.XPATH, "//span[text()='Proceed']")

    def __init__(self, driver):
        self.driver = driver

    def addtocart(self):
        return self.driver.find_element(*AddToCartPage.cart).click()

    def scrollpageup(self):
        return self.driver.execute_script("window.scrollTo(400, 0);")

    def selectshade(self):
        return self.driver.find_element(*AddToCartPage.shade).click()

    def scrollpg(self):
        return self.driver.execute_script("window.scrollTo(300, 100);")

    def addtocartfinal(self):
        return self.driver.find_element(*AddToCartPage.addcart).click()

    def clickcarticon(self):
        return self.driver.find_element(*AddToCartPage.carticon).click()

    def switchtoframe(self):
        frames = self.driver.find_elements(*AddToCartPage.framelocator)
        frame = frames[0]
        return self.driver.switch_to.frame(frame)

    def proceedasaguest(self):
        return self.driver.find_element(*AddToCartPage.proceed).click()

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:
    searchproduct = (By.NAME, "search-suggestions-nykaa")

    def __init__(self, driver):
        self.driver = driver

    def searchproducttobuy(self):
        i = self.driver.find_element(*HomePage.searchproduct)
        i.send_keys("lipstick")
        i.send_keys(Keys.RETURN)
        self.driver.execute_script("window.scrollTo(0, 400);")
        lipsticks = self.driver.find_elements(By.XPATH, "//div[@class='css-jtn0l5']")
        for lipstick in lipsticks:
            if lipstick.find_element(By.CSS_SELECTOR, ".css-xrzmfa").text == "Nykaa So Creme! Creamy Matte Lipstick":
                lipstick.find_element(By.CSS_SELECTOR, ".css-xrzmfa").click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])




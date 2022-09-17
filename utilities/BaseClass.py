import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyAddtoCarttextpresence(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='css-vp18r8']/button/span[text()='Add to Bag']")))


    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s %(name)s : %(message)s")
        filehandler = logging.FileHandler("C:\\Users\\RITUSHREE\\PycharmProjects\\MyProject\\utilities\\filelog.log")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger



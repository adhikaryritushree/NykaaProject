import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == 'chrome':
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\RITUSHREE\\Downloads\\chromedriver_win32\\chromedriver.exe")

    elif browser_name == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\\Users\\RITUSHREE\\Downloads\\geckodriver-v0.31.0-win64\\geckodriver.exe")

    elif browser_name == 'edge':
        driver = webdriver.Edge(executable_path="C:\\Users\\RITUSHREE\\Downloads\\edgedriver_win32\\msedgedriver.exe")


    driver.get("https://tinyurl.com/nykaaritu")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()




import re
from dotenv import load_dotenv
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.url = "https://kursusvmlepkom.gunadarma.ac.id/login/index.php"

    def load_env(self):
        load_dotenv()
        dotenv = dotenv_values()
        USERNAME = dotenv.get('USERNAME')
        PASSWORD = dotenv.get('PASSWORD')
        return USERNAME, PASSWORD

    def get_driver_options(self, headless=False):
        # Web Driver
        CHROMEDRIVER_PATH = self.driver
        WINDOW_SIZE = '1920,1080'
        driver_options = Options()

        if headless:
            driver_options.add_argument('--headless')

        driver_options.add_argument(f"--window-size={WINDOW_SIZE}")

        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                                options=driver_options)
        
        return browser

    def login(self, headless=False):
        browser = self.get_driver_options(headless)
        USERNAME, PASSWORD = self.load_env()

        browser.get(self.url)

        username = browser.find_element_by_xpath(
            "//*[@id='username']").send_keys(USERNAME)  # Username Lepkom
        username_exist = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(username)
        )

        password = browser.find_element_by_xpath(
            "//*[@id='password']").send_keys(PASSWORD)  # Password Lepkom
        password_exist = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(password)
        )

        login = browser.find_element_by_xpath(
            "//*[@id='loginbtn']").send_keys(Keys.ENTER)  # Enter

        enter_login = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(login)
        )

    def send_enter(element):
        element.send_keys(Keys.ENTER)

    def send_back(self):
        self.driver.back()


driver = './chromedriver'
utils = Browser(driver)
utils.login()
print('Logged in')
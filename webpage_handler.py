import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv("G:\My Drive\.env")

OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_experimental_option('detach', True)

URL = 'https://itax.kra.go.ke/KRA-Portal/'

PIN = os.getenv('pin_KRA')
PASSWORD = os.getenv('password_KRA')


class WebPageHandler:
    @staticmethod
    def login():
        driver = webdriver.Chrome(options=OPTIONS)
        driver.get(URL)

        # wait for page to load. timeout = 20 seconds
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="logid"]')))

        pin_input = driver.find_element(By.ID, value='logid')
        pin_input.send_keys(PIN)

        continue_button = driver.find_element(By.XPATH, value='//*[@id="normalDiv"]/table/tbody/tr[3]/td[2]/a')
        continue_button.click()

        # wait for the password input to be displayed on page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="xxZTT9p2wQ"]')))

        password_input = driver.find_element(By.ID, value='xxZTT9p2wQ')
        password_input.send_keys(PASSWORD)

        # get captcha image, saves it in root directory
        captcha = driver.find_element(By.ID, value='captcha_img')
        captcha.screenshot('captcha.png')

        # captcha_input = driver.find_element(By.XPATH, value='//*[@id="captcahText"]')
        # captcha_input.send_keys()


page = WebPageHandler()
page.login()

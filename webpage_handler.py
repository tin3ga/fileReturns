import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from captcha_handler import CaptchaHandler

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

        # download captcha image, saves it in root directory
        with open('captcha.png', 'wb') as file:
            captcha = driver.find_element(By.XPATH, value='//*[@id="captcha_img"]').screenshot_as_png
            file.write(captcha)
        captcha_ans = CaptchaHandler().process_captcha()

        captcha_input = driver.find_element(By.XPATH, value='//*[@id="captcahText"]')
        captcha_input.send_keys(captcha_ans)

        login_button = driver.find_element(By.XPATH, value='//*[@id="loginButton"]')
        login_button.click()
        returns_menu = driver.find_element(By.XPATH, value='//*[@id="ddtopmenubar"]/ul/li[3]/a')

        actions = ActionChains(driver)

        actions.move_to_element(returns_menu).perform()
        file_nil = driver.find_element(By.XPATH, value='//*[@id="Returns"]/li[4]/a')
        actions.move_to_element(file_nil).perform()

        file_nil.click()

        # click on tax obligation dropdown list
        driver.find_element(By.XPATH, value='//*[@id="regType"]').click()

        # select resident individual
        driver.find_element(By.XPATH, value='//*[@id="regType"]/option[2]').click()

        # click on next
        driver.find_element(By.XPATH, value='//*[@id="btnSubmit"]').click()


if __name__ == '__main__':
    page = WebPageHandler()
    page.login()

import time;
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PruebaQA.Objects.Locators import Locators
import pickle


class Metodos():
    def __init__(self,myDriver):
        self.driver = myDriver

    def login(self, user, password):
            user_field = self.driver.find("//*[contains(text(), 'E-mail')]").click()
            user_field.send_keys(user)
            password_field = self.driver.find_element_by_xpath("//*[contains(text(), 'Password')]").click()
            password_field.send_keys(password)

    def waitForLoad(self, xpath):
        Wait = WebDriverWait(self.driver, 10)
        Wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, xpath)))
    #Método para clicar botón:
    def click_methodID(self, boton_name):
        boton=self.driver.find_element_by_id(boton_name)
        boton.click()
        time.sleep(2)

    def save_cookie(self, path):
        with open(path, 'wb') as filehandler:
            pickle.dump(self.driver.get_cookies(), filehandler)

    def load_cookie(self, path):
        with open(path, 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                self.driver.add_cookie(cookie)

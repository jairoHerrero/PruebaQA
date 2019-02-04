from selenium import webdriver;
from Objects.Locators import Locators
import unittest;
import time;
import math
import datetime
import random
import os





class Test(unittest.TestCase):

    def setUp(self):

        """Abrir la web"""
        #self.driver = webdriver.PhantomJS("C:\\Python37\\Lib\\site-packages\\selenium\\webdriver\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
        self.driver = webdriver.Firefox(executable_path="C:\Python37\Lib\site-packages\selenium\webdriver\geckodriver.exe")
        self.driver.get("http://stage.panel.stage.do.linkitox.com/")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(Locators.cookies_button).click()
        cookies = self.driver.get_cookies()
        print(len(cookies))
        print(cookies)
        print(self.driver.current_url)
        self.driver.find_element_by_xpath(Locators.login).click()
        self.driver.delete_all_cookies()


        time.sleep(2)





    def test_1_login(self):

        """Realiza el login en la web"""
        print(self.driver.current_url)
        email = self.driver.find_element_by_css_selector(Locators.email)
        email.send_keys("jairohm81@outlook.es")
        password = self.driver.find_element_by_css_selector(Locators.password)
        password.send_keys("qajairo")
        self.driver.find_element_by_xpath(Locators.singin).click()
        print('done')
        time.sleep(10)

        """Creación de nueva app"""
        self.driver.find_element_by_css_selector(Locators.new_app_button).click()
        self.driver.find_element_by_css_selector(Locators.new_app_button2).click()
        random_name = "Prueba" + str(datetime.datetime.now().microsecond)
        self.driver.find_element_by_css_selector(Locators.app_name).send_keys(random_name)
        print(random_name)
        time.sleep(3)
        random_number = math.floor((random.random() * 100000000) + 1);
        print(random_number)
        bundle = str(random_number) + "com.app.test"
        self.driver.find_element_by_css_selector(Locators.select_os).click()
        self.driver.find_element_by_css_selector(Locators.bundle_id).send_keys(bundle)
        print(bundle)
        time.sleep(3)
        self.driver.find_element_by_css_selector(Locators.description).send_keys(bundle)
        Imagepath = os.path.abspath('C:\\Python37\Images\shiningforce.jpg')
        self.driver.find_element_by_class_name(Locators.image).send_keys(Imagepath)
        time.sleep(3)
        self.driver.find_element_by_css_selector(Locators.create_button).click()
        time.sleep(3)


        """Comprobación de la nueva app"""
        self.driver.find_element_by_css_selector(Locators.apps).click()
        time.sleep(3)
        select = self.driver.find_element_by_css_selector(Locators.tabla).text
        elemento = self.driver.find_element_by_xpath('//*[contains(text(), "' + random_name + '")]')
        time.sleep(3)

        i = 1;
        x = str(i)
        while i < 50:
            x = str(i)
            app = self.driver.find_element_by_css_selector(':nth-child(' + x + ') > .text-xs-left > .app-container > .app__text').text

            if app == random_name:
                self.driver.find_element_by_css_selector(':nth-child('+x+') > .text-xs-left > .app-container > .v-menu > .v-menu__activator > .activator > .v-icon').click()
                break;


            i += 1


        time.sleep(3)

        self.driver.find_element_by_css_selector(Locators.edit_button).click()
        time.sleep(3)

        """Confirmamos que los datos introducidos son correctos"""
        result_app_name = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div/div/div/form/div[1]/div/div[1]/div/input').get_attribute("value")

        print(result_app_name)

        result_bundle = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div/div/div/form/div[4]/div/div[1]/div/input').get_attribute("value")
        print(result_bundle)


        assert result_app_name == random_name
        assert result_bundle == bundle








    def tearDown(self):
        self.driver.quit()

        return True

    if __name__ == '__main__':
        unittest.main(verbosity=2)

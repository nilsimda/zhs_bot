#/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ZHS_Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def reserve(self, sport):
        web_page = "https://www.buchung.zhs-muenchen.de/angebote/aktueller_zeitraum_0/_" + sport + ".html"
        self.driver.get(web_page)

        # click by sending return because clicking does not work for whatever reason
        b_list = self.driver.find_elements(by=By.XPATH, value="//input[@value='buchen']")
        for b in b_list:
            b.send_keys('\n')

        # switch to the new tabs and fill out the forms one by one
        tabs = self.driver.window_handles
        for tab in tabs[1:]:
            self.driver.switch_to.window(tab)
            self.fill_in_form()

        print("Reserved a spot in all available courses for " + sport)

    def fill_in_form(self):
        """
        Fill out the form to complete the booking. For this function to work you need to have
        saved your data behind a passowrd at ZHS.
        """

        pswd_arrow = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "bs_pw_anmlink")))
        pswd_arrow.click()
        
        # enter username
        username_field = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.NAME, "pw_email")))
        username_field.send_keys(self.username)
        
        #enter password
        self.driver.find_element(by=By.XPATH, value="//input[@type='password']").send_keys(self.password)
        
        self.driver.find_element(by=By.XPATH, value="//input[@value='weiter zur Buchung']").click()
        
        # for some reason the nationality does not get saved and needs to be selected every time
        el = self.driver.find_element_by_name("freifeld4")
        for option in el.find_elements(by=By.TAG_NAME, value='option'):
            if option.text == 'Deutschland (Germany)':
                option.click() 
                break
        
        # click the checkbox to accept the terms
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "tnbed"))).click()
        
        self.driver.find_element(by=By.XPATH, value="//input[@value='weiter zur Buchung']").click()
        
        submit_button = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='verbindlich buchen']"))
        )
        submit_button.click()

    def __del__(self):
        self.driver.quit()
    

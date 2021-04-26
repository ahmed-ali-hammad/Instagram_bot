from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from config import *
import time
import wget
import os


class Instagram:
    def __init__(self, keyword, username, password):
        self.keyword  = keyword
        self.username = username
        self.password = password
        self.driver   = webdriver.Chrome('chromedriver.exe')

    def login(self):
        self.driver.get('https://www.instagram.com/')

        username_field = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))

        password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))

        username_field.clear() # to make sure the field is empty
        username_field.send_keys(self.username)

        password_field.clear() # to make sure the field is empty
        password_field.send_keys(self.password)

        login_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

        login_button.click()
        time.sleep(4)

        self.driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
        time.sleep(4)

        self.driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()

        time.sleep(4)

    def search(self):
        search_box = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))

        search_box.send_keys(self.keyword)

        time.sleep(2)

        self.driver.find_element_by_xpath("//a[@class='-qQT3'][1]").click()

        time.sleep(5)



    def run(self):
        self.login()



if __name__ == '__main__':
    search = Instagram("#cats", username, password)
    search.run()

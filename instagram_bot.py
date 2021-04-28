from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from config import *
import time
import wget
import os

options =  webdriver.ChromeOptions()
# options.add_argument("--headless")

class Instagram:
    def __init__(self, keyword, username, password):
        self.keyword  = keyword
        self.username = username
        self.password = password
        self.driver   = webdriver.Chrome('chromedriver.exe', options = options)

        #running the search
        self.login()
        self.search()
        self.collect_images()
        self.search()
        self.driver.quit()


    def login(self):
        self.driver.get('https://www.instagram.com/')

        # Explicit  wait for the page to load the element
        username_field = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))

        # Explicit  wait for the page to load the element
        password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))

        username_field.clear() # to make sure the field is empty
        username_field.send_keys(self.username)

        password_field.clear() # to make sure the field is empty
        password_field.send_keys(self.password)

        # Explicit  wait for the page to load the element
        login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        login_button.click()

        # Explicit  wait for the page to load the element
        WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.cmbtv button"))).click()

        # Explicit  wait for the page to load the element
        WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='aOOlW   HoLwm ']"))).click()


    def search(self):
        # Explicit  wait for the page to load the element
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))

        search_box.send_keys(self.keyword)

        # picking the first choice from the search results
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='-qQT3'][1]"))).click()

        time.sleep(3)

    def save(self, imgs_urls):
        path = os.getcwd()
        download_to = os.path.join(path, "downloads")
        os.mkdir(download_to)

        counter = 0
        for image in imgs_urls:
            save_as = os.path.join(download_to,('cat'+ str(counter) +'.jpg'))
            wget.download(image, save_as)
            counter = counter + 1
        print('Data was saved successfully')


    def collect_images(self):
        images = self.driver.find_elements_by_tag_name('img')
        imgs_urls = [image.get_attribute('src') for image in images]

        len_of_page = 0
        condition = False

        while condition == False:

            last_count = len_of_page

            # to scroll down we execute this Javascript code
            len_of_page = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight;")

            # sleep for 5 secs to give time for the page to load
            time.sleep(3)

            images_new = self.driver.find_elements_by_tag_name('img')

            # removing the duplicates
            for image in images_new:
                if image.get_attribute('src') not in imgs_urls:
                    imgs_urls.append(image.get_attribute('src'))
            
            if last_count == len_of_page :
                condition = True

        self.save(imgs_urls)
        # self.driver.quit()
        

if __name__ == '__main__':
    search_item = Instagram("#gjhkg", username, password)

from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib
import lxml
import re
import time
import requests



driver = webdriver.Chrome("C:\\Users\\The Slacker\\python_automate\\webdrivers\\chromedriver.exe")

def playstore_search():
    #Browsing to required apps
    driver.get("https://play.google.com/store?hl=en_IN")
    text = driver.find_element_by_id("gbqfq")
    button = driver.find_element_by_id("gbqfb")
    text.clear()
    text.send_keys("fitness app")
    button.click()
    
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "action-dropdown-parent-All results")))
    element.click()
    element2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='action-dropdown-children-All results']/div/ul/li[2]/div/a")))
    element2.click()
    
    current_url = driver.current_url
    store_scrap(current_url)

def store_scrap(url):
    driver.get(url)    
    response = driver.execute_script("return document.documentElement.innerHTML")
    soup = BeautifulSoup(response,'lxml')
    Apps = soup.find_all('div',class_="WsMG1c nnK0zc")
    time.sleep(5)
    for app in Apps:
        print(app.text)
          
            




playstore_search()



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
import itertools


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
    r = requests.get(url) 
    htmlcontent = r.content
    
    soup = BeautifulSoup(htmlcontent,'html.parser')
    
    #time.sleep(6)  
    #response = driver.execute_script("return document.documentElement.outerHTML")
    #soup = BeautifulSoup(response,'lxml')

    Apps = soup.find_all('div',class_="WsMG1c nnK0zc")
    time.sleep(10)
    i = soup.find_all('div',class_="pf5lIe")
    #time.sleep(3)
    #reviews = soup.find_all('div',class_="BHMmbe")
    for app, a in zip(Apps, i):
        print(app.text)
        children = a.findChildren('div',recursive = False)
        print(list(children))
        
    
    
    
         
        #butt = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"")))
        #butt.click()
        
    



    #i=0
    #for rev in reviews:
        #print(i)
        #print(rev)
        #i=i+1    
            


playstore_search()





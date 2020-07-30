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
import operator


driver = webdriver.Chrome("C:\\Users\\The Slacker\\python_automate\\webdrivers\\chromedriver.exe")
driver.maximize_window()
def playstore_search():
    #Browsing to required apps
    driver.get("https://play.google.com/store?hl=en_IN")
    text = driver.find_element_by_id("gbqfq")
    button = driver.find_element_by_id("gbqfb")
    text.clear()
    text.send_keys("simulator games")
    button.click()
    
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "action-dropdown-parent-All results")))
    element.click()
    element2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='action-dropdown-children-All results']/div/ul/li[2]/div/a")))
    element2.click()
    
    current_url = driver.current_url
    store_scrap(current_url)

# collecting the ratings of apps
def store_scrap(url):
    
    driver.get(url)#open url
    for loop in range(6): 
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")#for scrolling the page to load all content
        time.sleep(3)
    
    response = driver.execute_script("return document.documentElement.outerHTML")# to retrieve the html of the page 
    soup = BeautifulSoup(response,'lxml')
    time.sleep(3)
    Apps = soup.find_all('div',class_="WsMG1c nnK0zc")# to find all the apps
    time.sleep(10)
    i = soup.find_all('div',class_="pf5lIe")# to find the parent class of ratings
    
    ratings = {}
    g=1 
    for app, a in zip(Apps, i):
        children = a.findChildren('div',recursive = False)# to get the children of the parent class to retrieve the rating
        res = str(children[0])
        stars = str(res[23:26])
        print(g,": ",app.text,"----->",stars)# printing the details
        value = float(stars)
        ratings[app.text] = value
        g=g+1 
        
    sorted_d = dict(sorted(ratings.items(), key=operator.itemgetter(1))) #sorting the apps based on rating
    print("********************************************************")
    print("Apps\t\t\t\tratings")
    print("********************************************************")

    for key,value in sorted_d.items():
        print(key,"----------------------------------",value)    
            


playstore_search()





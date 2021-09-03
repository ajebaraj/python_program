from selenium import webdriver
from selenium.webdriver.common import keys

import requests
from bs4 import BeautifulSoup as bs

import time
import os
from datetime import datetime
import re

search_input = input('Type defect here:')
output_path_directory = input('Crete a folder:')
output_path_directory = os.getcwd()+'/'+output_path_directory

if not os.path.isdir(output_path_directory):
    os.mkdir(output_path_directory)


driver = webdriver.Firefox(executable_path='./geckodriver')
driver.maximize_window()


url = 'https://www.google.com/search?q='+search_input

# driver.get('https://www.google.com/search?q=burr+defects+on+steel&client=ubuntu&hs=aBo&channel=fs&sxsrf=ALeKk03OeUqZwyO3DIWR6lprvh8Cj7QyVg:1613659686040&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj4l__i1vPuAhU77HMBHQskAtkQ_AUoAnoECBMQBA&biw=1322&bih=667')
driver.get(url)
# driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[4]/div/div/div[1]/div/div[1]/div/div[3]/a').click()
driver.find_element_by_xpath("//a[contains(text(),'Images')]").click()


# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
def  scroll_to_end():
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True


scroll_to_end()



# all = driver.find_elements_by_xpath("//img")

all = driver.find_elements_by_tag_name('img')

print(all)
print(len(all))

for img in all:

    print(img.get_attribute('alt'))
    if img.get_attribute('src') != None:
        if img.get_attribute('src').startswith('http'):
            print(img.get_attribute('src'))

            image_data = requests.get(img.get_attribute('src')).content
            fw = open(output_path_directory+'/'+str(datetime.now())+'.jpeg','wb')
            fw.write(image_data)
            fw.close()



# rg_i Q4LuWd === png
# rg_i Q4LuWd === jpeg

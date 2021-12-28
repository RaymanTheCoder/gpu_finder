from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def gpu_finder():
    #Google Chrome driver for Selenium
    driver = webdriver.Chrome('./chromedriver')

    #Website that we want to look at
    driver.get("https://amazon.com")

    print(driver.title)

    #Search for the name of the search bar
    search_bar = driver.find_element_by_name("field-keywords") #Find the value_name of the searchbar

    search_bar.clear()
    search_bar.send_keys("3060 TI") #Type this "..."
    search_bar.send_keys(Keys.RETURN) #Return means enter

    print(driver.current_url)
    time.sleep(10)
    driver.close()

while True:
    gpu_finder()
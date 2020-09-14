from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time 

def calc(x, y):
  return int(x) + int(y)
  
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element_by_id("num1")
    x1 = x1_element.text
	
    x2_element = browser.find_element_by_id("num2")
    x2 = x2_element.text
	
    res = calc(x1, x2)
	
    select = Select(browser.find_element_by_tag_name("select"))
    opt = select.select_by_value(str(res))
    
    button = browser.find_element_by_css_selector ("[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
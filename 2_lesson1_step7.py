from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
   
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
   
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
   
    button = browser.find_element_by_css_selector ("[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
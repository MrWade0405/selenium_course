from selenium import webdriver
import time 
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_css_selector("[type='text']")
    for element in elements:
       element.send_keys("x")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
	
    input_file = browser.find_element_by_id("file")
    input_file.send_keys(file_path)
   
    button = browser.find_element_by_css_selector ("[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
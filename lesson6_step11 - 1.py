from selenium import webdriver
import time


try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ваш код, который запомнит обязательные поля
    firstname = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.first_class > input")
    firstname.send_keys("Bohdan")
    lastname = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.second_class > input")
    lastname.send_keys("QA")
    email = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.third_class > input")
    email.send_keys("drevnickiy@gmail.com")
    button = browser.find_element_by_css_selector("body > div > form > button")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_elements_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()


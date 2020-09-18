import time
import math
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', 
["https://stepik.org/lesson/236895/step/1", 
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_lesson6_step3(browser, url):
    browser.get(url)
	
    answer = math.log(int(time.time()))
	
    input = browser.find_element_by_css_selector(".ember-text-area")
    input.send_keys(str(answer))
	
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
	
    res = browser.find_element_by_css_selector(".smart-hints__hint")
    print(res.text)
    assert res.text != "Correct!", res.text
	
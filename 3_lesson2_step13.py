from selenium import webdriver
import time
import unittest

class Test(unittest.TestCase):
	def test_1(self):
		try:
			link = "http://suninjuly.github.io/registration1.html"
			browser = webdriver.Chrome()
			browser.get(link)

			input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
			input1.send_keys("Ivan")
			input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
			input2.send_keys("Petrov")
			input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
			input3.send_keys("test@gmail.com")

			button = browser.find_element_by_css_selector("button.btn")
			button.click()

			time.sleep(1)

			welcome_text_elt = browser.find_element_by_tag_name("h1")
			welcome_text = welcome_text_elt.text

			self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
		finally:
			time.sleep(10)
			browser.quit()
        
	def test_2(self):
		try: 
			link = "http://suninjuly.github.io/registration2.html"
			browser = webdriver.Chrome()
			browser.get(link)

			input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
			input1.send_keys("Ivan")
			input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
			input2.send_keys("Petrov")
			input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
			input3.send_keys("test@gmail.com")

			button = browser.find_element_by_css_selector("button.btn")
			button.click()

			time.sleep(1)

			welcome_text_elt = browser.find_element_by_tag_name("h1")
			welcome_text = welcome_text_elt.text

			self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
		finally:
			time.sleep(10)
			browser.quit()
        
if __name__ == "__main__":
    unittest.main()
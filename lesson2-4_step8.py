from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")



try:
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    num1 = browser.find_element(By.ID, 'input_value').text

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(num1))

    button_send = browser.find_element(By.ID, 'solve')
    button_send.click()

    time.sleep(5)
    


except Exception:
    print('Error')
finally:
    browser.quit()
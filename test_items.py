from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_exist(browser):
    browser.get(link)
    time.sleep(30) #Проверить лично, открылся ли тот язык, который нужно.
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
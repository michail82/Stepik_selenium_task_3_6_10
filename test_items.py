import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_guest_should_language(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element(By.XPATH, "//*[@id='add_to_basket_form']/button")



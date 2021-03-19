import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestLanguage:

    def test_add_to_basket_button_label_is_correct_for_different_languages(self, browser):
        browser.get(link)
        browser.maximize_window()

        # Navigating to some book card
        wait = WebDriverWait(browser, 10)
        button_add_to_basket = wait.until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, 'button.btn-add-to-basket'))
                                          )
        button_label = button_add_to_basket.text
        correct_button_tiles = ['Añadir al carrito', 'Ajouter au panier']
        # Debug
        # print(button_add_to_basket.text)
        assert button_label in correct_button_tiles, f"Button title should be on of {correct_button_tiles}"
        time.sleep(30)

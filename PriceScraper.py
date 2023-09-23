from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

target_product = input("Which product you looking for? : ")


class PriceScraper():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def amazon_list(self):
        self.driver.get("https://www.amazon.com.tr/")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "nav-input")))
        search_engine = self.driver.find_element(By.CLASS_NAME, "nav-input")
        search_engine.send_keys(target_product)
        search_engine.send_keys(Keys.ENTER)

        product_names = self.driver.find_elements(By.CLASS_NAME, "a-size-base-plus")
        product_prices = self.driver.find_elements(By.CLASS_NAME, "a-price-whole")

        product_data = []
        for product_name, product_price in zip(product_names, product_prices):
            product_data.append({
                "Product Name": product_name.text,
                "Price ": product_price.text + " " + "TL"
            })
        return product_data

    def trendyol_list(self):
        self.driver.get("https://www.trendyol.com/")
        WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "V8wbcUhU")))
        search_engine = self.driver.find_element(By.CLASS_NAME, "V8wbcUhU")
        search_engine.send_keys(target_product)
        search_engine.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "prdct-cntnr-wrppr")))

        product_names = self.driver.find_elements(By.CLASS_NAME, "prdct-desc-cntnr-name")
        product_prices = self.driver.find_elements(By.CLASS_NAME, "prc-box-dscntd")

        product_data = []
        for product_name, product_price in zip(product_names, product_prices):
            product_data.append({
                "Product Name": product_name.text,
                "Price ": product_price.text
            })
        return product_data


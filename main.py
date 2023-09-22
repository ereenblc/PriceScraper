
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

product_name = input("Which product you looking for?:")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.trendyol.com/")

# searching the product you are looking for
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "V8wbcUhU")))
search_engine = driver.find_element(By.CLASS_NAME, "V8wbcUhU")
search_engine.send_keys(product_name)
search_engine.send_keys(Keys.ENTER)
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "prdct-cntnr-wrppr")))

# listing the top 10 prices of your product
for i in range(2, 12):
    name_path = (f"/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/div[1]/div/div[{i}]/div["
                 f"1]/a/div[2]/div[1]/div/h3/span[2]")
    phone_name = driver.find_element(By.XPATH, name_path)

    price_path = (f"/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/div[1]/div/div[{i}]"
                  f"/div[1]/a/div[2]/div[3]/div/div")
    phone_price = driver.find_element(By.XPATH, price_path)

    if "TL" in phone_price.text:
        print(f"\n*** Product {i - 1} ***"
              f"\n{phone_name.text}"
              f"\n{phone_price.text}")

    else:
        price_path = (f"/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/div[1]/div/div[{i}]"
                  f"/div[1]/a/div[2]/div[3]/div/div[2]/div")
        phone_price = driver.find_element(By.XPATH, price_path)
        print(f"\n*** Product {i - 1} ***"
              f"\n{phone_name.text}"
              f"\n{phone_price.text}")

driver.quit()
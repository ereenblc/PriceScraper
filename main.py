from PriceScraper import PriceScraper
import pandas as pd

scraper = PriceScraper()

amazon_data = scraper.amazon_list()
trendyol_data = scraper.trendyol_list()

amazon_df = pd.DataFrame(amazon_data)
trendyol_df = pd.DataFrame(trendyol_data)

print(f"------------------------TRENDYOL DATA-----------------------------"
      f"\n{trendyol_df}\n"
      f"\n------------------------AMAZON DATA-----------------------------"
      f"\n{amazon_df}")
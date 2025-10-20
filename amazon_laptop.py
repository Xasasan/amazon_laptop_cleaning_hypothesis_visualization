from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
import pandas as pd


laptop_brand = []
laptop_model_name = []
laptop_screen_size = []
laptop_ram = []
laptop_storage = []
laptop_cpu_model = []
laptop_operating_system = []
laptop_price = []
laptop_rating = []
laptop_rating_review = []
laptop_graphics_card_description = []



#___________________________________

#   next page ulash

next_url = "https://www.amazon.in/s?k=laptop"
driver.get(next_url)


# for i in range ga bizani saytimizda nechta page bosa osha sonni yozamiza

for i in range(10):   # oldin  next page ishlavotganiga uveren bose keyin 20 yozaman
    driver.get(next_url)
    try:
        next_url = driver.find_element(By.XPATH, "//a[@class= 's-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator']")
        next_url = next_url.get_attribute('href')
        # hozir  next_url ichida next buttoni ichidigi link saqlanvotti
    except:
        print("this is the last page")
        break

#______________________________________

# next page ulaganimizdan keyin pasdigi 2 ta line keremas uni tepada yozdm next page gacha turishi kere

#
# url = "https://www.amazon.in/s?k=laptop"
# driver.get(url)


    laptop_urls = driver.find_elements(By.XPATH,
                                   "//a[@class='a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal']")


    laptop_links = []

    for url in laptop_urls:
        link = url.get_attribute('href')
        laptop_links.append(link)
    print(f" number of laptops: {len(laptop_links)}")


    for link in laptop_links:
        driver.get(link)

        try:
            brand = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                      "//tr[@class='a-spacing-small po-brand']"
                                                       "//td[@class='a-span9']"
                                                       "//span[@class='a-size-base po-break-word']"))).text

        except:
            brand = 'no brand'
        print(f" laptop brand: {brand}")
        laptop_brand.append(brand)


        try:
            model_name = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                            "//tr[@class='a-spacing-small po-model_name']"
                                                             "//td[@class='a-span9']"
                                                             "//span[@class='a-size-base po-break-word']"))).text

        except:
            model_name = 'no model_name'
        print(f" laptop model_name: {model_name}")
        laptop_model_name.append(model_name)


        try:
            rating = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                        "//i[@class='a-icon a-icon-star a-star-3-5 cm-cr-review-stars-spacing-big']"
                                                       "/preceding-sibling::span"))).text

        except:
            rating = 'no rating'
        print(f" laptop rating: {rating}")
        laptop_rating.append(rating)


        try:
            rating_review = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                             "//a[@class='a-link-normal']"
                                                              "//span[@id='acrCustomerReviewText']"))).text

        except:
            rating_review = 'no rating_review'
        print(f" laptop rating_review: {rating_review}")
        laptop_rating_review.append(rating_review)


        try:
            price = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                     "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']"
                                                     "//span/span[@class='a-price-whole']"))).text

        except:
            price = 'no price'
        print(f" laptop price: {price}")
        laptop_price.append(price)

        # Muzaffarniki pasdigi  description

        # try:
        #     description = WebDriverWait(driver, 5).until(
        #         expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='featurebullets_feature_div']"
        #                                                                    "//div[@class='a-section a-spacing-medium a-spacing-top-small']"
        #                                                                    "//ul[@class='a-unordered-list a-vertical a-spacing-mini']"))).text
        #
        # except:
        #     description = 'No description'
        # print(f"Graphic card description: {description}")
        # laptop_graphics_card_description.append(description)


        try:
            graphics_card_description = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH,
            "//th[@class='a-color-secondary a-size-base prodDetSectionEntry'][contains(text(), 'Graphics Card Description')]/../td"))).text

        except:
            graphics_card_description = 'no graphics_card_description'
        print(f" laptop graphics_card_description: {graphics_card_description}")
        laptop_graphics_card_description.append(graphics_card_description)


        try:
            screen_size = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                            "//tr[@class='a-spacing-small po-display.size']"
                                                             "//td[@class='a-span9']"
                                                            "//span[@class='a-size-base po-break-word']"))).text
        except:
            screen_size = 'no screen_size'
        print(f" laptop screen_size: {screen_size}")
        laptop_screen_size.append(screen_size)


        try:
            ram = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                    "//tr[@class='a-spacing-small po-ram_memory.installed_size']"
                                                     "//td[@class='a-span9']"
                                                    "//span[@class='a-size-base po-break-word']"))).text
        except:
            ram = 'no ram'
        print(f" laptop ram: {ram}")
        laptop_ram.append(ram)


        try:
            storage = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                        "//tr[@class='a-spacing-small po-hard_disk.size']"
                                                         "//td[@class='a-span9']"
                                                        "//span[@class='a-size-base po-break-word']"))).text
        except:
            storage = 'no storage'
        print(f" laptop storage: {storage}")
        laptop_storage.append(storage)


        try:
            cpu_model = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                        "//tr[@class='a-spacing-small po-cpu_model.family']"
                                                         "//td[@class='a-span9']"
                                                         "//span[@class='a-size-base po-break-word']"))).text
        except:
            cpu_model = 'no cpu_model'
        print(f" laptop cpu_model: {cpu_model}")
        laptop_cpu_model.append(cpu_model)


        try:
           operating_system = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                "//th[@class='a-color-secondary a-size-base prodDetSectionEntry'][contains (text(), ' Operating System ')]/../td"))).text
        except:
            operating_system = 'no operating_system'
        print(f" laptop operating_system: {operating_system}")
        laptop_operating_system.append(operating_system)


        print('/' * 30 )



df = pd.DataFrame(
    {
        'brand': laptop_brand,
        'model_name': laptop_model_name,
        'screen_size(inches)': laptop_screen_size,
        'price(₹)': laptop_price,
        'ram': laptop_ram,
        'storage': laptop_storage,
        'cpu_model': laptop_cpu_model,
        'operating_system': laptop_operating_system,
        'rating': laptop_rating,
        'rating_review': laptop_rating_review,
        'graphics_card_description': laptop_graphics_card_description,

    }
             )

df.to_csv('amazon_laptops_latest_version.csv')

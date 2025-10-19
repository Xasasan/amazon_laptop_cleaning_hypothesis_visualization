from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pandas as pd



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

book_title = []
book_author = []
book_rating = []
book_price = []
book_reading_age = []
book_page = []
book_language = []
book_description = []
book_publisher = []
book_weight = []
book_quantity = []
book_country = []

# next page
#
next_url = 'https://www.amazon.in/s?k=books'
driver.get(next_url)


# for i in range ga bizani saytimizda nechta page bosa osha sonni yozamiza
for i in range(20):
    #url
    driver.get(next_url)
    try:
        #next_page edi
        next_url = driver.find_element(By.XPATH, "//a[@class= 's-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator']")
        next_url = next_url.get_attribute('href')
        # hozir 22 line digi next_page ichida next buttoni ichidigi link saqlanvotti
    except:
        print("this is the last page")
        break



#____________________

    book_urls = driver.find_elements(By.XPATH,
                                 "//a[@class='a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal']")

    book_links = []
    for url in book_urls:
        link = url.get_attribute('href')
        book_links.append(link)
    print(f"Number of books:{len(book_links)}")

    for link in book_links:
        driver.get(link)


        try:
            title = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                                   "//span[@id='productTitle']"))).text
        except:
            title = 'No title'
        print(f"Book title: {title}")
        book_title.append(title)


        try:
            author = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                         "//span[@class= 'author notFaded']/a[@class='a-link-normal']"))).text
        except:
            author = 'no author'
        print(f" book author: {author}")
        book_author.append(author)


        try:
            rating = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='a-declarative']"
                                                   "//a[@class= 'a-popover-trigger a-declarative']"
                                                   "//span[@class= 'a-size-base a-color-base']"))).text

        except:
            rating = 'no rating'
        print(f" book rating: {rating}")
        book_rating.append(rating)


        try:
            price = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class= 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay']"
                                                  "//span/span[@class= 'a-price-whole']"))).text

        except:
            price = 'no price'
        print(f" book price: {price}")
        book_price.append(price)


        try:
            reading_age = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id= 'detailBullets_feature_div']"
                                                         "//div[@id= 'detailBulletsWrapper_feature_div']"
                                                         "//div[@id= 'detailBullets_feature_div']"
                                                         "//ul[@class= 'a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']"
                                                         "//span[contains(text(), 'years')]"))).text
            if 'Customer suggested age' in reading_age:
                reading_age_cleaned = reading_age.split(':')[1]
            else:
                reading_age_cleaned = reading_age

        except:
            reading_age_cleaned = 'no reading age'
        print(f" book reading age: {reading_age_cleaned}")
        book_reading_age.append(reading_age_cleaned)

         # list varianti reading_page ni
        # try:
        #     table = driver.find_elements(By.XPATH,
        #                                 "//ul[@class='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']/li")
        #     reading_age = table[5].find_element(By.XPATH, "//span[@class= 'a-list-item']"
        #                                                 "//span[@class= 'a-text-bold']/span").text
        # except:
        #     reading_age = 'no reading age'
        # print(f" book reading age: {reading_age}")
        # book_reading_age.append(reading_age)


        try:
            page = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id= 'detailBullets_feature_div']"
                                                 "//div[@id= 'detailBulletsWrapper_feature_div']"
                                                 "//div[@id= 'detailBullets_feature_div']"
                                                 "//ul[@class= 'a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']"
                                                 "//span[contains(text(), 'pages')]"))).text
            page_cleaned = int(page.split()[0])

        except:
            page_cleaned = 'no page'
        print(f" book page: {page_cleaned}")
        book_page.append(page_cleaned)


        try:
            language = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id= 'detailBullets_feature_div']"
                                                 "//div[@id= 'detailBulletsWrapper_feature_div']"
                                                 "//div[@id= 'detailBullets_feature_div']"
                                                 "//ul[@class= 'a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']"
                                                 "//span[contains(text(), 'Language')]"
                                                 "/following-sibling::span"))).text
        except:
            language = 'no language'
        print(f" book language: {language}")
        book_language.append(language)


        try:
            publisher = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id= 'detailBullets_feature_div']"
                                                 "//div[@id= 'detailBulletsWrapper_feature_div']"
                                                 "//div[@id= 'detailBullets_feature_div']"
                                                 "//ul[@class= 'a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']"
                                                 "//span[contains(text(), 'Publisher')]"
                                                 "/following-sibling::span"))).text

        except:
            publisher = 'no publisher'
        print(f" book publisher: {publisher}")
        book_publisher.append(publisher)


        try:
            weight = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id= 'detailBullets_feature_div']"
                                                 "//div[@id= 'detailBulletsWrapper_feature_div']"
                                                 "//div[@id= 'detailBullets_feature_div']"
                                                 "//ul[@class= 'a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']"
                                                 "//span[contains(text(), 'Weight')]"
                                                 "/following-sibling::span"))).text
        except:
            weight = 'no weight'
        print(f" book weight: {weight}")
        book_weight.append(weight)


        try:
            quantity = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id= 'detailBullets_feature_div']"
                                                 "//div[@id= 'detailBulletsWrapper_feature_div']"
                                                 "//div[@id= 'detailBullets_feature_div']"
                                                 "//ul[@class= 'a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']"
                                                 "//span[contains(text(), 'Quantity')]"
                                                 "/following-sibling::span"))).text
        except:
            quantity = 'no quantity'
        print(f"book quantity: {quantity}")
        book_quantity.append(quantity)


        try:
            country = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id= 'detailBullets_feature_div']"
                                                 "//div[@id= 'detailBulletsWrapper_feature_div']"
                                                 "//div[@id= 'detailBullets_feature_div']"
                                                 "//ul[@class= 'a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']"
                                                 "//span[contains(text(), 'Country')]"
                                                 "/following-sibling::span"))).text


        except:
            country = 'no country'
        print(f"book country: {country}")
        book_country.append(country)


        try:
            description = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class= 'a-section a-spacing-small a-padding-base']"
                                                        "//div[@class= 'a-section a-spacing-small a-padding-small']/span"))).text


        except:
            description = 'no description'
        print(f"book description: {description}")
        book_description.append(description)


        print('/' * 45)

df = pd.DataFrame(
    {
        'title': book_title,
        'author': book_author,
        'rating': book_rating,
        'price(₹)': book_price,
        'reading_age': book_reading_age,
        'page': book_page,
        'language': book_language,
        'publisher': book_publisher,
        'weight(g)': book_weight,
        'quantity': book_quantity,
        'country': book_country,
        'description': book_description,

    }
             )


df.to_csv('amazon_books_new.csv')

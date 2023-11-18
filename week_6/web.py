import requests
from bs4 import BeautifulSoup

creditcard_discount_html = requests.get('https://cathaybk.com.tw/cathaybk/personal/event/overview/')
soup = BeautifulSoup(creditcard_discount_html.text, 'html.parser')

count = 0
for creditcard_discount in soup.findAll('div', {'class': 'cubre-m-eventCard__title'}):
    if count < 10:
        print(creditcard_discount.text)
        count += 1
    else:
        break

'''import requests
from bs4 import BeautifulSoup

creditcard_discount_html = requests.get('https://cathaybk.com.tw/cathaybk/personal/event/overview/')
soup = BeautifulSoup(creditcard_discount_html.text, 'html.parser')
for creditcard_discount in soup.findAll('div', {'class': 'cubre-m-eventCard__title'}):
    print(creditcard_discount.text)
'''




'''
import requests
from bs4 import BeautifulSoup

creditcard_discount_html = requests.get('https://cathaybk.com.tw/cathaybk/personal/event/overview/')
soup = BeautifulSoup(creditcard_discount_html.text,'html.parser')
for creditcard_discount in soup.findAll('div class="cubre-m-eventCard__content"'):
    print(creditcard_discount.text)
'''


'''from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome(options=options)
chrome.get("https://cathaybk.com.tw/cathaybk/personal/event/overview/")
'''


'''from selenium import webdriver

driver_path = '/Users/wenby/Downloads/chromedriver_mac_arm64/chromedriver'
url = 'https://cathaybk.com.tw/cathaybk/personal/event/overview/'

options = webdriver.ChromeOptions()
options.binary_location = '/path/to/chrome'  # 如果指定了 Chrome 執行檔的路徑，也可以在這裡設定

driver = webdriver.Chrome(options=options)
driver.get(url)

# 使用 XPath 選擇器來找到該元素
element = driver.find_element_by_xpath("//div[contains(text(), 'PChome 24h購物')]")

'''


'''# Chrome driver path
driver_path = '/Users/wenby/Downloads/chromedriver_mac_arm64/chromedriver'
url = 'https://cathaybk.com.tw/cathaybk/personal/event/overview/'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)

# 使用找到的適當選擇器找到前10個優惠元素
promotions = driver.find_elements_by_css_selector('your-selector-for-promotions')[:10]

for index, promotion in enumerate(promotions, start=1):
    # 在這裡處理每個優惠元素的操作或資訊擷取
    pass

driver.quit()
'''

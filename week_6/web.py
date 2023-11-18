import requests
from bs4 import BeautifulSoup

creditcard_discount_html = requests.get('https://cathaybk.com.tw/cathaybk/personal/event/overview/')
soup = BeautifulSoup(creditcard_discount_html.text, 'html.parser') 
# 用requests套件連結網頁取資料
# 物件 = BeautifulSoup('網頁原始碼資料','解析器名稱')
# 使用內建解析器html.parser

count = 0
for creditcard_discount in soup.findAll('div', {'class': 'cubre-m-eventCard__title'}): 
    if count < 10:
        print(creditcard_discount.text)
        count += 1
    else:
        break
# 使用findAll函式時，限制 class 屬性是 'cubre-m-eventCard__title'(從網頁中開發者模式內尋找標題可見)
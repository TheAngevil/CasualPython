# -for活動專區這頁的測試

from selenium.webdriver import Chrome # 導入Chrome Webdriver
from week_7.base_page import base_page
from week_7.locator import elements_locator

# 測試
test = base_page(Chrome()) # 給予瀏覽器類型
test.get_page("https://cathaybk.com.tw/cathaybk/personal/event/overview/") # 取得目標網站


# ★抓取非空值的前十項資料
'''
所需的元素有
優惠內容: cubre-m-eventCard__content
or
標題: title > cubre-m-eventCard__title
內文: text > cubre-m-eventCard__text
期間: date > cubre-m-eventCard__date
'''
'''
# 拆分存取法
eventCard_title = test.get_elements(elements_locator.title)
eventCard_text = test.get_elements(elements_locator.text)
eventCard_date = test.get_elements(elements_locator.date)
eventCard_content = [eventCard_title,eventCard_text,eventCard_date] #把標題、內文、期間集合於一個list內，但這樣拆分有可能數量位置會對不上，ex.非空值的起點不一樣，要再另外做處理，
所以我直接使用下面的方法>>
'''

# 直接使用content讀取
eventCard_content = test.get_elements(elements_locator.content)

# 印出前10項優惠
i = 1 #計算印出到第幾個優惠了
j = 0 #for讀取清單第j個項目用
while i <= 10:
    if eventCard_content[j] != '':
        print(f"{i}. {eventCard_content[j]}\n")
        i = i+1
    j = j+1
from selenium import webdriver #導入Selenium的webdriver模組，可用於控制瀏覽器
from selenium.webdriver.common.by import By #導入方法來根據不同抓取方法定位網頁元素
import time #可以控制有關時間的功能

# 設定Chrome driver的執行路徑
chrome_options = webdriver.ChromeOptions()
chrome_options.chrome_executable_path = "C:/Users/User/PycharmProjects/chromedriver-win64/chromedriver.exe" #放webdriver的路徑

'''
備註: 這邊也可以改成導入Selenium的Options模組來使用 >> from selenium.webdriver.chrome.options import Options
options = Options()
options.chrome_executable_path = "C:/Users/User/PycharmProjects/chromedriver-win64/chromedriver.exe"
'''

#透過瀏覽器Driver開啟Chrome
driver = webdriver.Chrome(options=chrome_options)

#連線到目標網站
driver.get("https://cathaybk.com.tw/cathaybk/personal/event/overview/")

#等待網頁載入
#time.sleep(2)

#取得title
get_title = driver.find_elements(By.XPATH,'//*[@id="lnk_Button1Link"]/div[2]') #找到符合該XPath的元素(標題)
get_content = driver.find_elements(By.XPATH,'//*[@id="lnk_Button1Link"]/div[2]/div[2]') #內文
get_date = driver.find_elements(By.XPATH,'//*[@id="lnk_Button1Link"]/div[2]/div[3]') #日期

#濾掉空值及將換行符號取代成空格
def filter(b): #篩選並回傳至新清單
    return [i.text.replace("\n", " ") for i in b if i.text.strip() != ""] #存取清單中非空值的網頁文字元素，並且如有換行符號的元素改以空格間隔

# 將過濾過的文字存於新清單
title = filter(get_title)
content = filter(get_content)
date = filter(get_date)

# 印出前10項優惠
for i in range(10):
    print(f"{i+1}. {title[i]}\n內文: {content[i]}\n活動期間: {date[i]}\n")

#關閉網頁
driver.close()
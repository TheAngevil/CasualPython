# -for定位網頁元素用
from selenium.webdriver.common.by import By #導入方法來根據不同抓取方法定位網頁元素
class elements_locator:
    content = (By.XPATH, '//*[@id="lnk_Button1Link"]/div[2]') #整組優惠內容

    # 這裡用不到但我先放著
    title = (By.XPATH, '//*[@id="lnk_Button1Link"]/div[2]')  # 標題
    text = (By.XPATH, '//*[@id="lnk_Button1Link"]/div[2]/div[2]')  # 內文
    period = (By.XPATH, '//*[@id="lnk_Button1Link"]/div[2]/div[3]')  # 日期

# 備註for我自己 > driver.find_elements(By.XPATH, '//*[@id="lnk_Button1Link"]/div[2]/div[2]')
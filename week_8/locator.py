# -for定位網頁元素用
from selenium.webdriver.common.by import By #導入方法來根據不同抓取方法定位網頁元素
class elements_locator:
    content = (By.XPATH, '//*[@id="lnk_Button1Link"]/div[2]') #整組優惠內容
    result_num = (By.XPATH,'//*/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/span') #優惠數量
    more_btn = (By.XPATH,'//*/div[1]/div/div/div/div[4]/a/span[2]') #展開更多btn
    page_title = (By.XPATH, '//*/main/div/div[2]/div[1]/p') #上方title

    # 這裡用不到但我先放著
    title = (By.XPATH, '//*[@id="lnk_Button1Link"]/div[2]')  # 標題
    text = (By.XPATH, '//*[@id="lnk_Button1Link"]/div[2]/div[2]')  # 內文
    period = (By.XPATH, '//*[@id="lnk_Button1Link"]/div[2]/div[3]')  # 日期

# 備註for我自己 > driver.find_elements(By.XPATH, '//*[@id="lnk_Button1Link"]/div[2]/div[2]')
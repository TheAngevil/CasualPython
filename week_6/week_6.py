from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = ("https://cathaybk.com.tw/cathaybk/personal/event/overview/")
driver.get(url)


title = driver.find_elements(By.XPATH, '//*[@id="lnk_Button1Link"]/div[2]') 
content = driver.find_elements(By.XPATH, '//*[@id="lnk_Button1Link"]/div[2]/div[2]') # 如果要by ID就是By.ID, 'id'以此類推


title = [i.text.replace("\n", " ") for i in title if i.text.strip() != ""] 
content = [i.text.replace("\n", " ") for i in content if i.text.strip() != ""]
# text.strip() -> 去除字串兩側(開頭和結尾)空白字符的方法
# i.text.strip() != "" -> 檢查 i.text 是否為空字串，如果不是空字串，則保留在列表中
# i.text.replace("\n", " ") -> 將 i.text 中的換行符（\n）替換為空格（" "）


for i in range(10):
    print(f"{i+1}. {title[i]}")
    print(f"內容: {content[i]}\n")


driver.close()


# element.send_keys(“xxx”) -> 傳入字串
# element = driver.find_element_by_class_name(“xxx”) -> 定位搜尋框
# element.clear() -> 清掉原本的搜尋字串
# button.click() -> 點擊



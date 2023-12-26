# -所有頁面的base page，未來如果需要取得元素或篩選東西都可以引用這裡的方法
import pytest
from selenium import webdriver # 導入Webdriver

#fixture不可直接被調用，而是視測試需要使用
@pytest.fixture(autouse=True)
def driver_setting():
    # 測試
    driver = webdriver.Chrome()  # 給予瀏覽器類型
    driver.maximize_window() #全螢幕執行
    driver.get("https://cathaybk.com.tw/cathaybk/personal/event/overview/")  # 取得目標網站

    yield driver

    driver.quit() #結束測試後關閉driver

#補充
# driver.close() > 關閉當下分頁
# driver.quit()  > 關閉所有關聯視窗
# driver.set_window_size(width, height) > 指定視窗大小

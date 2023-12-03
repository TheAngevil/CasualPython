# -for活動專區這頁的測試
from week7.locator import elements_locator
#from conftest import test_driver_setting #fixture不可直接被調用，而是視測試需要使用
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def get_elements(driver,element):  # 取得driver設定及元素文字
    find_element = driver.find_elements(*element)  # 取得需要的元素來源，這時候獲取到的是一個原始(?)未經處理的list
    # 備註:使用"*"運算符可以展開容器內的元素，ex.在elements_locator.title中有兩個元素(定位類型&來源值)，運用*將其展開即可使find_elements方法可以正確接收兩個引數

    element_list = []  # 生成一個list
    for i in find_element:
        element_list.append(i.text)  # 讀取所有的元素並將元素轉換為的文字全部存於上方生成的list(element_list)內
    return element_list  # 回傳找到的所有文字元素值

@allure.title("活動專區信用卡優惠數量")
def test_event_num(driver_setting): # 取得conftest中的driver作為參數使用於此

    #page_content_num = driver_setting.find_element(elements_locator.result_num).text
    try:
        # 使用 WebDriverWait 進行元素的等待
        result_num_element = WebDriverWait(driver_setting, 5).until(
            EC.visibility_of_element_located(elements_locator.result_num)
        )
        page_content_num = result_num_element.text # page_content_num = 實際頁面上顯示的優惠總數

    except TimeoutException:
        assert False,"網頁載入超時"

    # 取得頁面寫的優惠數量
    # 先展開所有更多
    btn = WebDriverWait(driver_setting, 5).until(
            EC.visibility_of_element_located(elements_locator.more_btn)
        )

    while True:
        btn.click()
        try:
            # 等待元素消失的話則跳出迴圈
            btn = WebDriverWait(driver_setting, 1.5).until_not(
                EC.visibility_of_element_located(elements_locator.more_btn)
            )
            break

        except TimeoutException:
            pass
            # 如果等待超時則繼續點擊


    # 取得所有優惠元素
    try:
        WebDriverWait(driver_setting, 5).until(EC.presence_of_all_elements_located(elements_locator.content))
        eventCard_content = get_elements(driver_setting, elements_locator.content)

        # 取得有值的數量
        content_num = len(eventCard_content) - eventCard_content.count('')

        # 因為page_content_num是str、content_num是int，故轉換為相同type來判斷值是否相等
        # assert Expected == Actual
        assert content_num == int(page_content_num)


    except TimeoutException:
        assert False,"網頁載入超時"


@allure.title("活動專區標題(Fail案例)")
def test_fail_name(driver_setting):
    try:
        title = WebDriverWait(driver_setting, 5).until(EC.visibility_of_element_located(elements_locator.page_title))
        assert title.text == "活動專區"

    except TimeoutException:
        assert False, "標題載入超時"
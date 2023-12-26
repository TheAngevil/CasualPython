# -for活動專區這頁的測試
import allure
import time
from week_8.locator import elements_locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains #模擬滑鼠操作

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
        page_content_num = result_num_element.text # page_content_num = 頁面上顯示的優惠總數
        # 附圖
        allure.attach(driver_setting.get_screenshot_as_png(), name="頁面總計優惠數量", attachment_type=allure.attachment_type.PNG)
    except TimeoutException:
        assert False,"網頁載入超時"

    # 取得頁面實際的優惠數量
    # 先展開所有更多

    # 設定展開更多的變數
    btn = WebDriverWait(driver_setting, 5).until(
            EC.visibility_of_element_located(elements_locator.more_btn)
        )

    while True:
        #滑到"展開更多"後截圖
        ActionChains(driver_setting).scroll_to_element(elements_locator.more_btn)
        # 附圖
        allure.attach(driver_setting.get_screenshot_as_png(),attachment_type=allure.attachment_type.PNG)
        btn.click()
        try:
            # 等待元素消失的話則跳出迴圈
            btn = WebDriverWait(driver_setting, 2).until_not(
                EC.visibility_of_element_located(elements_locator.more_btn))
            break

        except TimeoutException:
            pass
            # 如果等待超時則繼續點擊


    # 取得所有優惠元素
    try:
        WebDriverWait(driver_setting, 5).until(EC.presence_of_all_elements_located(elements_locator.content))
        time.sleep(5)
        # 如果使用這個的方法的話，他會在任一元素出現時就繼續執行，但可能不是所有元素都載入完畢了，
        # 所以我加個time.sleep去強制等待，但這樣也不能確保元素真的會載入完成 or 已經載入完成了還浪費時間等待

        # 等待整個網頁載入完成
        # 這個方法會等到網頁載入完畢才繼續，但缺點是如果某個元素壞掉(?)那這邊就會發生錯誤
        # WebDriverWait(driver_setting, 5).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

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
    """這個是失敗案例"""
    try:
        title = WebDriverWait(driver_setting, 5).until(EC.visibility_of_element_located(elements_locator.page_title))
        # 附圖
        ActionChains(driver_setting).scroll_to_element(elements_locator.page_title)
        allure.attach(driver_setting.get_screenshot_as_png(), name="標題名稱", attachment_type=allure.attachment_type.PNG)
        assert title.text == "非活動專區"


    except TimeoutException:
        assert False, "標題載入超時"
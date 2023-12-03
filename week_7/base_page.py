# -所有頁面的base page，未來如果需要取得元素或篩選東西都可以引用這裡的方法

class base_page:

    def __init__(self,driver):
        self.driver = driver

    def get_page(self,url): # 取得目標頁面
        self.driver.get(url)

    def get_elements(self,element): # 取得元素文字
        find_element = self.driver.find_elements(*element) # 取得需要的元素來源，這時候獲取到的是一個原始(?)未經處理的list
        # 備註:使用"*"運算符可以展開容器內的元素，ex.在elements_locator.title中有兩個元素(定位類型&來源值)，運用*將其展開即可使find_elements方法可以正確接收兩個引數

        element_list = [] #生成一個list
        for i in find_element:
            element_list.append(i.text) #讀取所有的元素並將元素轉換為的文字全部存於上方生成的list(element_list)內
        return  element_list #回傳找到的所有文字元素值
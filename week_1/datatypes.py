def data_types(): #def是用來定義function的關鍵字，()放參數
    types = {
        int: '整數|可以是正整數、負整數或零 (ex. -1、0、100)',
        float: '浮點數|有小數的數字 (ex. 3.14、-0.001)',
        str: '字串|文字或字元串，用單引號或雙引號括起來 (ex. "Hello")',
        bool: '布林|只有兩個值 (ex. True (真) 和 False (假))',
        list: '列表|代表有序且可變(可新增、刪除或修改列表中的元素)的元素集合，可包含不同型別的元素 (ex. [3.21, "hello", True])', 
        tuple: '元組|代表有序不可變(一旦創建，就無法修改其元素)的元素集合，可包含不同型別的元素 (ex. (1, "hello", True))。', 
        dict: '字典|是一個無序、可變且具有鍵值對的集合，每個鍵(key)都與唯一的值(value)相關聯 (ex. {"name": "Alice", "age": 30})',
        set: '集合|是一個無序且不可重複的集合類型 (ex. (set = {1, 2, 3, 4, 4, 3} 會輸出1234)'
    }

    for data_types, a in types.items(): #types.items()：用來取得types裡面的值
        print(f'{data_types.__name__}: {a}') #不使用name的話int:會變成<class

# 呼叫函式印出types
data_types()

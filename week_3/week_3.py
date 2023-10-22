def des(var, var_id):
    """
    我懶惰寫來產String用的，不要太計較 XD
    """
    return f"id of {var} = {var_id}"


# Week 3
# 理解值與址。

# 1. 學會id()的作用以及出現的數字代表的意義，並利用此點學習址跟值的差異。
# 1.1 試試看print(id(999)）與 print(id(10))
print(f'{"~" * 50}1.1{"~" * 50}')
print(des("999", id(999)))
print(des("a", id(10)))

# Ans + Note
# id() 函數返回的是一個整數，表示該物件的唯一標識符，通常標識符是以十進制表示的整數，代表物件在記憶體中的位置
# 應用：判斷兩個物件是否相同 / 檢查物件的唯一性
# 址跟值的差異：每個變數都包含兩個主要元素 - 值value(可變的整數/字串) / 址address(唯一不可變的)


# 1.2 將10, 99 與999，分別賦予給三個變數a,b與z，印出 id(a), id(b) 與 id(z) 並與 id(10), id(99) 與 id(999)作比較。為何是這樣的結果?
print(f'{"~" * 50}1.2{"~" * 50}')
a = 10 # a是變數名稱，10是該變數所儲存的值
b = 99
z = 999
print(des("10", id(10))) # id(10)是他內存的址
print(des("a", id(a)))
print(des("99", id(99)))
print(des("b", id(b)))
print(des("999", id(999)))
print(des("z", id(z)))

# Ans + Note
print(id(a)==id(10)) #True 
# 因為多個變數指向同一個值的結果會是一樣的


# 1.3 直接印出id(c)，會發生什麼事情? 為什麼?
print(f'{"~" * 50}1.3{"~" * 50}')
# print(id(c)) 

# Ans + Note
# 直接印出id(c)會顯示name 'c' is not defined, 因為在前面的題目中皆沒有給變數c一個值
# 如果c = 99
# print(id(c)) #給了他跟b一樣的值所以他的址會跟b一樣，接下題


# 1.4 讓 c = b，再度印出id(c)並跟上面的id(99)與id(b)比較，有差異嗎?
print(f'{"~" * 50}1.4{"~" * 50}')
c = b
print(des("b", id(b)))
print(des("c", id(c)))
print(des("99", id(99)))

# Ans + Note
# 在1.3中印出id(c)會出現錯誤訊息，在1.4中我們使c=b，由前幾題可知b=99，因此c=b=99所以id(c) id(b) id(99)的結果在這題中是無差異的


# 1.5 嘗試印出(a==b) 以及(a is b) 結果是?
print(f'{"~" * 50}1.5{"~" * 50}')
print(a == b) # False
print(a is b) # False
print(a == b - 89) # True
print(a is b - 89) # True 

# Ans + Note
# 結果都一樣是False
# print(a) 10
# print(b) 99
# print(z) 999
# print(c) 99

# 1.6 讓 d = 99 +1 嘗試印出(d == 99+1 ) 以及(y is b+1) 結果是?
print(f'{"~" * 50}1.6{"~" * 50}')
d = 99 + 1  # d = 100
# y = b + 1 # 直接印出y is b + 1是不行的要先y = b + 1
print(d == 99 + 1) # True
print(d is b + 1) # True
# print(y is b + 1) # True
# print(y is d) # True

# Ans + Note
# 印出(d == 99 + 1 )是True，因為前面有先定義d = 99 + 1（100）
# 直接印出 “y is b + 1”顯示：name 'y' is not defined > 變數需要被定義一個值，但這邊先不訂正這個錯誤怕後面亂掉僅用註解解釋，所以若這邊定義了y的值則y=100
print(d == 100 ) # True
print(d is b ) # False 
# print(a) 10
# print(b) 99
# print(z) 999
# print(c) 99
# print(d) 100


# 1.7 讓 y = 999+1 嘗試印出(y == 999+1 ) 以及(y is z+1) 結果是?
print(f'{"~" * 50}1.7{"~" * 50}')
y = 999 + 1 # 1000
print(y == 999 + 1) # True
print(y is z + 1) # False

# Ans + Note
# 結果為一個True一個False，is 跟 == 的差異：is檢查是否為同一個物件｜==檢查內容
# print(a) 10
# print(b) 99
# print(z) 999
# print(c) 99
# print(d) 100
# print(y) 1000


# 1.8: 1.6 的結果與 1.7有何不同，為什麼? 提示，找看看"Python 整數緩存機制"。
print(f'{"~" * 50}1.8{"~" * 50}')
#把兩個程式放在一起做比較
d = 99 + 1 
print(d == 99 + 1) #True
print(d is b + 1) #True

y = 999 + 1 
print(y == 999 + 1) #True
print(y is z + 1) #False

# Ans
# 在1.6題print(d is b + 1)是True，但在1.7題看起來一樣print(y is z + 1)卻是False
# 是因為Python 的整數緩存機制，Python會對一些常用的整數進行緩存以節省記憶體
# 當進行像 z + 1 或 b + 1 這樣的計算時，Python 可能會創建新的整數而不使用緩存中的整數
# 在這邊"y != z + 1" 是因為z + 1已經被認定為新的整數，因此雖然他們的值都是1000但id()是不一樣的


# 1.9: 根據 1.6 說明 == 與 is ， != 與 is not 分別的差異在? 提示，印出1.6與1.7 中分別的id
print(f'{"~" * 50}1.9{"~" * 50}')
# print(a) 10
# print(b) 99
# print(z) 999
# print(c) 99
# print(d) 100
# print(y) 1000

# Ans
# is/is not 跟 ==/!= 的差異："is/is not"檢查是否為同一個物件(址)｜"==/!="" 檢查內容(值)
print(id(y))
print(id(z)) # id不一樣

print(id(y) is not id(z)) # True
print(id(y) != id(z)) # True


# 理解mutable and immutable
# 1.10 解釋為何 id(str_1)的前後id不一樣 但 id(list_1)的前後id沒有變化。請用記憶體的角度來進行說明。
print(f'{"~" * 50}1.10{"~" * 50}')
str_1 = str() 
print(id(str_1)) 
print(str_1) # 空的字串
str_1 = str_1.join("2") # 新增一個字串2
print(str_1) # 2
print(id(str_1))

print(f'{"~" * 10}list_1{"~" * 10}')
list_1 = list()
print("list_1:", id(list_1))
print(list_1) # 空的表[]
list_1.append("2") # append是在原地修改列表，因此 list_1 的內容被更新為['2']
print(list_1) # ['2']
print("list_1:", id(list_1))
list_1.append("1234556")
print(list_1)
print(id(list_1))

print(f'{"~" * 10}list_2{"~" * 10}')
list_2 = list()
print("list_2:",id(list_2))
print(list_2)
list_2.append("2") # 一樣append2
print(list_2)
print("list_2:", id(list_2))

print(id(list_1) != id(list_2))

# Ans
# 字串是不可變的列表是可變的

# 為何 id(str_1)的前後id不一樣?，join("2")是將原本的空字串更新為2，表示2跟原本的字串是不一樣的，id(str_1)的前後不一樣是因為修改了str_1，指向了新的物件2
# 任何對字串的修改是創建了一個新的字串物件

# 為何id(list_1)的前後id沒有變化?，是因為 list_1 一直指向同一個物件，原本的空表[]和修改後的['2'] 都是同一個物件(在同一個list裡面)
# 所以不管append多少東西id都會是一樣的因為他們都在同一個list，但不同list的id就會不一樣(參考list_2)

# 1.11 請列出基本型別中，哪一些是mutable 以及 哪一些是 immutable
print(f'{"~" * 50}1.11{"~" * 50}')
# Ans
mutable = "mutable(可變)：列表（list）/ 字典（dict） / 集合（set）"
immutable = "immutable(不可變)：整數（int）/ 浮點數（float）/ 字串（str）/ 元組（tuple)"
print(mutable)
print(immutable)


# 1.12 請說明id()的用法以及出來的數字的意義，並自行查閱並根據上敘練習，說明值(value)，址(address)，引用(Reference)的概念。如有針對上敘問題的額外心得，請直接加入前面題目的說明中
print(f'{"~" * 50}1.12{"~" * 50}')
value = "值(value)：指數值、文字、物件等｜x=10，10是值"
address = "址(address)：指記憶體中儲存變數或物件的位置，每個變數或物件在記憶體中都有一個唯一的址，可以用來準確定位記憶體中的位置"
Reference = "引用(Reference)：是變數指向該資料位址的關係｜ex. 1.2 & 1.4"
print("總結")
print(value)
print(address)
print(Reference)




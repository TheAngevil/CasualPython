def des(var, var_id):
    """
    我懶惰寫來產String用的，不要太計較 XD
    """
    return f"id of {var} = {var_id}"

# Week 3
# 理解值與址。

# 1. 學會id()的作用以及出現的數字代表的意義，並利用此點學習址跟值的差異。
# 🖍️透過等號指定給變數，呼叫id()函式來取得變數的記憶體位址
# 1.1 試試看print(id(999)）與 print(id(10))
print(f'{"~" * 50}1.1{"~" * 50}')
print(des("999", id(999)))
print(des("a", id(10)))

# 1.2 將10, 99 與999，分別賦予給三個變數a,b與z，印出 id(a), id(b) 與 id(z) 並與 id(10), id(99) 與 id(999)作比較。為何是這樣的結果?
print(f'{"~" * 50}1.2{"~" * 50}')
a = 10
b = 99
z = 999
print(des("10", id(10)))
print(des("a", id(a)))
print(des("99", id(99)))
print(des("b", id(b)))
print(des("999", id(999)))
print(des("z", id(z)))
print('🥸 ：id()函數是一個內建函數，可以用來取得物件的識別碼，結果將會回傳一個整數，代表該物件在記憶體中的位置。')
print('🥸 ：也可以把變數傳入函數中，就可以取得該物件的識別碼，所以a = 10和b = 99和z = 999時，就會得到相同的結果。')

# 1.3 直接印出id(c)，會發生什麼事情? 為什麼?
print(f'{"~" * 50}1.3{"~" * 50}')
print("🥸 ：直接print id(c)時，因為沒有賦予變數所以得到結果 NameError: name 'c' is not defined。")
print("🥸 ：可以給變數後測試看看，例如：c = 5再print(id(c))，就會得到結果如下")
c = 5
print(id(c))

# 1.4 讓 c = b，再度印出id(c)並跟上面的id(99)與id(b)比較，有差異嗎?
print(f'{"~" * 50}1.4{"~" * 50}')
c = b
print(des("b", id(b)))
print(des("c", id(c)))
print('🥸 ：沒有差異，因為賦予變數後，c 和 b 和99將認為是同一個物件，所以 id() 函數回傳的識別碼會是相同的140663266203056')

# 1.5 嘗試印出(a==b) 以及(a is b) 結果是?
print(f'{"~" * 50}1.5{"~" * 50}')
print(a == b)
print(a is b)
print('🥸 ：id()可以用來檢查物件的識別碼是否相同，如果確定兩個物件不為相同一個物件時，將會回傳Flase。')
print(b == c)
print(b is c)
print('🥸 ：id()可以用來檢查物件的識別碼是否相同，如果確定兩個物件為同一個物件時，將會回傳Ture。')
print('🥸 ：以下把a、b、c依序印出檢查看看～')
print(id(a))
print(id(b))
print(id(c))

# 1.6 讓 d = 99 +1 嘗試印出(d == 99+1 ) 以及(d is b+1) 結果是?
print(f'{"~" * 50}1.6{"~" * 50}')
d = 99 + 1
print(d == 99 + 1)
print(d is b + 1)
print('🥸 ：以下把d、99 + 1、b + 1依序印出檢查看看～')
print(id(d))
print(id(99 + 1))
print(id(b + 1))

# 1.7 讓 y = 999+1 嘗試印出(y == 999+1 ) 以及(y is y+1) 結果是?
print(f'{"~" * 50}1.7{"~" * 50}')
y = 999 + 1
print(y == 999 + 1)
print(y is y + 1)
print('🥸 ：y被賦予變數為999 + 1，所以y和999 + 1會為相同物件而回傳Ture')
print('🥸 ：以下把y、999 + 1、y + 1依序印出檢查看看是否真的回傳不同識別碼，故為不同物件。')
print(id(y))
print(id(999+1))
print(id(y + 1))

# 1.8: 1.6 的結果與 1.7有何不同，為什麼? 提示，找看看"Python 整數緩存機制"。
print(f'{"~" * 50}1.8{"~" * 50}')
print('🥸 ：在Python的世界，為節省內存資源所以預先對-5～256範圍內的所有整數進行緩存，此範圍中賦予變數時，只是引用緩存並不會重新創建。')
print('當case1.6時，d的值為99 + 1為100，而d與99 + 1進行比較時，兩邊是相同的值與址，所以結果皆回傳True')
d = 99 + 1
print(d == 99 + 1)
print(d is b + 1)
print('當case1.7時，y與999 + 1進行比較時，y == 999 + 1為相同的值1000，回傳True。')
print('而y is y + 1時，y已經被賦予為1000，而 y +1 的值1000加1為1001，1001不在整數緩存範圍内，所以創建新的一個對象，y 和 y + 1 引用的就不是同一個對象，所以回傳False')
y = 999 + 1
print(y == 999 + 1)
print(y is y + 1)

# 1.9: 根據 1.6 說明 == 與 is ， != 與 is not 分別的差異在? 提示，印出1.6與1.7 中分別的id
print(f'{"~" * 50}1.9{"~" * 50}')
print('🥸 ：== 用來比較兩邊變數的值是否相同 ; is 則是比較兩邊變數引用的對象是否為同一個(確認內存的址是否相同)')
print('🥸 ：!= 用來比較兩邊變數的值是否不同 ; is not 則是比較兩邊變數引用的對象是否不同(確認內存的址是否不同)')
print('🥸 ：== 和 != 用來比較兩邊變數的值是否相同(對象的相等性) ; is 和 is not 則用來比較兩個變數引用的對象是否指向同一個內存地址')
print('🥸 ：以下透過case1.6可以看到d = 99 + 1 且 print(d == 99 + 1)的結果是回傳True，因為賦予變數後兩邊值相同')
print('🥸 ：而透過印出d、99 + 1、b + 1，三個的址都是140183974696400，所以透過is比較址時，結果也是回傳True')
d = 99 + 1
print(d == 99 + 1)
print(d is b + 1)
print('🥸 ：以下把d、99 + 1、b + 1依序印出址')
print(id(d))
print(id(99 + 1))
print(id(b + 1))

print('🥸 ：以下透過case1.7可以看到y = 999 + 1 且 print(y == 999 + 1)的結果是回傳True，因為賦予變數後兩邊值相同')
print('🥸 ：而透過印出y的址為140667964359696，z + 1則為140667964359920，所以透過is比較址時，結果是回傳Flase')
y = 999 + 1
print(y == 999 + 1)
print(y is z + 1)
print('🥸 ：y被賦予變數為999 + 1，所以y和999 + 1會為相同物件而回傳Ture')
print('🥸 ：反之，套入 != 和 is not，就會得到相反的結果')
print(y != 999 + 1)
print(y is not z + 1)
print('🥸 ：以下把y、999 + 1、z + 1依序印出址')
print(id(y))
print(id(999+1))
print(id(z + 1))

# 理解mutable and immutable
# 1.10 解釋為何 id(str_1)的前後id不一樣 但 id(list_1)的前後id沒有變化。請用記憶體的角度來進行說明。
print(f'{"~" * 50}1.10{"~" * 50}')
str_1 = str()
print(id(str_1))
str_1 = str_1.join("2")
print(id(str_1))
print('🥸 ：因為str是Immutable不可變物件，所以當join"2"時將創建一個新的物件(就會有新的值)，所以指向的內存記憶體位址也會改變。')
print('此狀態下原本內存就沒有被指向引用，就會被銷毀並釋放相應的內存空間')

list_1 = list()
print("hello", id(list_1))
list_1.append("2")
print("hello", id(list_1))
print('🥸 ：因爲list是Mutable可變物件，所以當append"2"其值改變時，內存指向的記憶體位址沒有改變。')

# 1.11 請列出基本型別中，哪一些是mutable 以及 哪一些是 immutable
print(f'{"~" * 50}1.11{"~" * 50}')
print('🥸 小筆記 : 在Python的世界，所有的東西都是物件(object)，每個object各包含一個identity、type和value。')
print('identity：可理解為object的記憶體空間，其值可由id()函數獲取，當object被建立，其identity不可改變。')
print('type：可理解為object的類型，其值可由type()函數獲取，當object被建立，其type不可改變。')
print('value：可理解為object的值，和identity與type不同，有些object的value可變動，有些object的value不可變動。')
print('value可變動的object稱為mutable object ; value不可變動的object稱為immutable object。')

print('🥸 ： mutable 可變物件 包含以下：')
print('物件以傳址（by reference）方式被儲存，內存址不改變')
print('list列表、dict字典、set集合')

print('🥸 ： immutable 不可變物件 包含以下：')
print('物件以傳值（by value）方式被儲存，內存址改變')
print('int整數、str字符串、float浮點數、tuple元組、forzenset凍結集合')

# 1.12 請說明id()的用法以及出來的數字的意義，並自行查閱並根據上敘練習，說明值(value)，址(address)，引用(Reference)的概念。如有針對上敘問題的額外心得，請直接加入前面題目的說明中
print(f'{"~" * 50}1.2{"~" * 50}')
print('🥸 ：id()是python的內建函式，透過等號賦予變數後，可以呼叫id()函式來取得變數的記憶體位址，語法為id(object)')
print('🥸 ：關於值(value)，址(address)，引用(Reference)')
print('透過以下範例，將a賦予變數100，為整數值，就等同創建一個a，並儲存(value)整數值100在其中，而b = a時，b和a將引用(Reference)同一個對象，所以回傳a和b的址(address)時會是相同的。')
a = 100
b = a
print(id(a))
print(id(b))

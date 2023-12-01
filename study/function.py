#function
'''
函式(Function)結構
函式(Function)參數
函式(Function) *args、**kwargs運算子
函式(Function)種類
函式(Function)變數範圍(Scope)
'''

#1、函式(Function)結構
print('1、函式Function結構')
print('函式包含def定義、函式名稱、參數')
print('(1)開頭def')
print('(2)函式名稱的命名習慣上會使用小寫字母，並且以底線來分隔單字。')
print('(3)參數為接收外部資料，實作的內容為函式所要執行的任務，🔺需注意縮排。')
def saysomething(name):
    print(f'hello,{name}!')

saysomething("Wenby")
saysomething("Ybnew")

#2、函式(Function)參數
print('2、函式(Function)參數')
print('(1)參數，如上')
print('(2)多參數，可以將多種資訊傳遞給函式')
def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(7, 3)  # 傳遞兩個參數給函式
print(sum_result)  # 印出：10

print('(3)指定參數，指定哪些參數要傳遞給函式，並略過其他參數')
def saysomething(name, age):
    print(f"My name is {name} and I am {age} years old")

saysomething(name="Ben", age=10)

print('(4)回傳值，如(2)多參數')
print('(5)多回傳值，可以使用多個變數來接收這些回傳的值。需要注意的是，函式可以有一個回傳值(使用return)或多個回傳值(使用逗號分隔)')
def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference

sum, diff = calculate(10, 5)
print(sum)   # 印出：15
print(diff)  # 印出：5

print('(6)參數預設值，如果呼叫函式時沒有提供特定參數的值，該參數將使用預設值。')
print('Case1：')
def hello(x,y=10):
    z = x + y
    print(z)

hello(1,2)    # 3
hello(5)      # 15
print('🔺帶有預設值的參數應該放在參數列表的末尾，以確保在呼叫函式時能正確對應參數。')
print('Case2：def saysomething(message="Hi", name) 是無效的，而 def saysomething(name, message="Hi") 是有效的。')
def saysomething(name, message="Hi"):
    print(f"{message}, {name}!")

saysomething("Wu")           # 輸出：Hi, Wu!
saysomething("Lin", "Morning")  # 輸出：Morning, Lin!

print('(7)for...in迴圈')
print('for 變數 in 資料: 是固定用法')
def my_function(pets):
    for a in pets:
        print(a)

allmypets = ["meowmeow,wanwan,moomoo"]
my_function(allmypets)

print('🖍️3、可變參數：*args和**kwargs')
print('*args：允許將不確定數量的非關鍵字參數傳遞給函式。args 在函式內部被視為一個包含所有非關鍵字參數的元組。')
print('**kwargs：允許將不確定數量的關鍵字參數傳遞給函式。kwargs 在函式內部被視為一個包含所有關鍵字參數的字典。')
print('args 和 kwargs 的英文名稱只是「變數名稱」，可以自由更換，🔺重點在於前方的一個星號與兩個星號。')
def print_args(*args):
    for arg in args:
        print(arg)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_args(1, 2, 3)  # 印出：1 2 3
print_kwargs(a=10, b=20, c=30)  # 印出：a: 10 b: 20 c: 30

print('🖍️4、全域變數(Global Variables)與區域變數(Local Variables)')
print('(1)全域變數：是在整個程式中都能夠被存取和使用的變數，它們的作用範圍延伸到程式的任何部分。')
print('全域變數通常在程式的最外層定義，或者在函式外部定義。')
print('如果在函式內部想要使用全域變數，需要使用 global 關鍵字進行聲明，這樣才能修改全域變數的值。')

print('(2)區域變數：區域變數是在特定區域（例如函式內部）中有效的變數，只能在定義它們的區域內使用。')
print('區域變數通常在函式內部定義，它們的作用範圍僅限於該函式的內部。')
print('區域變數在函式呼叫結束後就會被清除，無法在函式外部使用。')
print('Case1：')
global_var = 10  # 全域變數

def example_function():
    local_var = 5  # 區域變數
    print(local_var)  # 印出：5
    print(global_var)  # 印出：10

example_function()
print(global_var)  # 印出：10
#print(local_var)  #語法產生錯誤，local_var為區域變數，無法在函式外部存取

print('Case2：使用global修改全域變數')
global_var = 10  # 全域變數

def modify_global():
    global global_var  # 使用 global 關鍵字聲明變數為全域變數
    global_var = 20  # 修改全域變數的值

print("Before:", global_var)  # 印出：Before: 10
modify_global()
print("After:", global_var)  # 印出：After: 20

print('5、匿名函式又稱為lambda函式，是一種在程式中定義的簡單的、無名稱的函式')
print('Case1：')
numbers = [5, 2, 8, 1, 3]

# 使用匿名函式對清單中的數字進行排序
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)
#使用了內建的 sorted 函式，透過 key 參數指定了一個匿名函式（lambda函式）。
# 這個匿名函式會將每個數字作為參數，並直接返回該數字，這樣就實現了對數字的排序。

print('Case2：只需要一個簡單的函式來執行某些操作，不需要特別命名或定義整個函式。')
add = lambda x, y: x + y
result = add(5, 3)
print(result)  # 印出：8

print('6、Pass空函式，想做一個什麼都不做的函式，後續可以用在判斷式')
def test():
    pass



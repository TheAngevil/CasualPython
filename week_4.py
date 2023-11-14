# Week 4
# 理解def 及 邏輯控制
def customize_print(input_str):
    print(f"Hello~{input_str}")
    #After printing a value, you can no longer use it

def compose_str(input_str):
    return (f"Hello~{input_str}")
    #Can use the returned value later by storing it in a variable.

def print_by_position(p1, p2):
    print(f"{p1}{p2}")

# 1.  學會def 如何宣告及使用
# 1.1 嘗試呼叫customize_print並執行，說明結果與輸入不同的原因
print("-----1.1-----")
customize_print("str")
print("因為輸入的值是回傳給customize_print這個function的input_str，並且會執行這個function的內容，故會執行print設定的內容(回傳「Hello~」這個字串還有input_str的內容)")

# 1.2 嘗試呼叫compose_str並列印出結果，說明與customize_print執行流程不同的原因
print("-----1.2-----")
compose_str("str")
print("1.2與1.1結果不同的原因是因為return僅回傳值回去，並不會幫忙印出，而1.1使用了print()，呼叫funtion的時候會直接印出內容\n"
      "如果要在不改變該function內容的狀況下印出compose_str可以像下面這樣加上print")
print(compose_str("str"))

# 1.3 嘗試呼叫print_by_position並使用"Hello", "world"作為p1, p2輸入並印出結果
print("-----1.3-----")
print_by_position("Hello","world")

# 1.4 嘗試呼叫print_by_position並使用"world", "Hello"作為p1, p2輸入並解釋與1.3印出結果不同的原因
print("-----1.4-----")
print_by_position("world","Hello")
print('print_by_position這個function會印出p1及p2的值\n'
      '1.3中p1,p2對應的回傳值分別是"Hello"、"world"\n'
      '1.4中p1,p2對應的回傳值分別是"world"、"Hello"，故兩者結果會不同')

# 1.5 觀察print_by_position(p2="world", p1="Hello")的輸出結果並解釋與1.4印出結果不同的原因
print("-----1.5-----")
print_by_position(p2="world", p1="Hello")
print("因為world是直接指派給p2這個參數，而Hello則是指派給p1這個參數\n"
      "此function是印出 p1p2 ，故結果會是Helloworld，與1.4不同")

# 2.  學會while迴圈的使用
# 2.1 使用while印出1~10
print("-----2.1-----")
num = 0
while num <= 10:
    print(num,end=" ")
    num += 1

# 3.  學會使用if/else的使用
# 3.1 使用if/else搭配while印出1~10之中所有雙數
print("\n-----3.1-----")
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num,end=" ")
    num += 1

# 3.2 使用if/else搭配finally印出1~10之中所有雙數並且將當前數字開平方
print("\n-----3.2-----")
num = 1
while num <= 10:
    if num % 2 == 0:
        try:
            num**2
        finally:
            print(f"{num}、平方為{num**2}")
    num += 1

# 3.3 使用巢狀if/else印出1~10之中小於5的所有雙數
print("-----3.3-----")
num = 1
while num <= 10:
    if num % 2 == 0:
        if num < 5:
            print(num,end=" ")
    num += 1

# 4.  學會使用for的使用
# 4.1 使用for印出1~10
print("\n-----4.1-----")
for i in range(1,11):
    print(i,end=" ")

# 4.2 使用多重for迴圈印出以"*"構成的直角三角形
print("\n-----4.2-----")
for i in range(1,6):
    for j in range(1,6):
        if (j <= i):
            print("*",end="")
    print()

# 5.  其他迴圈控制
# 5.1 使用for和continue印出1~10之中所有單數
print("-----5.1-----")
for i in range(1,10):
    if i % 2 == 0:
        continue
    print(i,end=" ")

# 5.2 使用while和break印出小於10的正整數(1~9)
print("\n-----5.2-----")
num = 1
while num % 1 == 0:
    if num < 10:
        print(num, end=" ")
        num += 1
    else:
        break

# 6.  綜合題目
# 請利用上面所教，寫出猜數字遊戲，且猜題次數限制為10次，提示:可利用input()函式擷取console的輸入
print("\n------6------")
import random
times=10
def check_type(str):
    while True:
        try:
            num = int(input(str))
            if num < 0: #判斷user輸入的值是不是正整數
                print("請輸入正整數")
            else:
                return num #輸入的值是數字時回傳值
        except ValueError: #偵測到異常時執行
            print("請輸入整數數字")

start = check_type("起始數字:") #呼叫check_type確認user輸入的型態正確
end = check_type("結尾數字:")

while  end <= start: #如果結尾小於等於起始數字 則需重新輸入結尾數字
    if end <= start:
        print(f"結尾數字請大於起始數字 {start} 喔!")
        end = check_type("結尾數字:")

ans=random.randint(start,end) #產生user輸入範圍內隨機的整數
#print(ans) #自己偷看答案用

while times >= 10:
    for i in range(10):
        guess = check_type(f"請猜出{start}~{end}的任意數字:")
        if guess == ans:
            print("答對了!")
            break
        elif times == 1:
            print(f"你的猜題次數皆用完! 正確答案是{ans}")
        elif (guess < start) | (guess > end):
            times -= 1
            print(f"超出猜題範圍囉! 你剩{times}次機會了")
        elif guess > ans:
            times -= 1
            end = guess
            print(f"答錯了! 請往更小的數字猜，你剩{times}次機會囉")
        else:
            times -= 1
            start = guess
            print(f"答錯了! 請往更大的數字猜，你剩{times}次機會囉")
    break #保險起見用
# Week_4
# 理解def 及 邏輯控制

def customize_print(input_str):
  print(f"Hello~{input_str}")

def compose_str(input_str):
  return(f"Hello~{input_str}")
  
def print_by_position(p1, p2):
	print(f"{p1}{p2}")

# 1.  學會def 如何宣告及使用
# 1.1 嘗試呼叫customize_print並執行，說明結果與輸入不同的原因
print('🥸 1.1 先定義函數customize_print')
def customize_print():
    print("定義print函數")
# 呼叫 customize_print 函數
customize_print()

def customize_print():
    print("函數來了！")
customize_print()

# 1.2 嘗試呼叫compose_str並列印出結果，說明與customize_print執行流程不同的原因
print('🥸 1.2 嘗試呼叫compose_str並列印出結果，說明與customize_print執行流程不同的原因')
# 語法為
'''def compose_str(input_str):
    return f"自訂字串{input_str}"'''
print('🥸 這邊的return會將f後面的字串和{input_str}連接在一起，輸出新的字串')
print('定義完compose_str後還要引用它，所以結果要再多執行一個變數來印出')

def compose_str(input_str):
    return f"Hello~{input_str}"

result = compose_str("Wenby")
print(result)

# 1.3 嘗試呼叫print_by_position並使用"Hello", "world"作為p1, p2輸入並印出結果
print('🥸 1.3 嘗試呼叫print_by_position並使用"Hello", "world"作為p1, p2輸入並印出結果')
# 先定義
def print_by_position(p1, p2):
    print(f"{p1}{p2}")

p1 = "Hello"
p2 = "world"
print_by_position(p1, p2)

# 1.4 嘗試呼叫print_by_position並使用"world", "Hello"作為p1, p2輸入並解釋與1.3印出結果不同的原因
print('🥸 1.4 嘗試呼叫print_by_position並使用"world", "Hello"作為p1, p2輸入並解釋與1.3印出結果不同的原因')
def print_by_position(p1, p2):
    print(f"{p1}{p2}")

p1 = "world"
p2 = "Hello"
print_by_position(p1, p2)
print('🖍️當改把p1參數定為"world"，把p2參數定為"Hello"，印出的結果就會依照所定呈現，確保函數已經正確定義。')

# 1.5 觀察print_by_position(p2="world", p1="Hello")的輸出結果並解釋與1.4印出結果不同的原因
print('🥸 1.5 觀察print_by_position(p2="world", p1="Hello")的輸出結果並解釋與1.4印出結果不同的原因')
def print_by_position(p2="world", p1="Hello"):
    print(f"{p1}{p2}")

print_by_position(p1, p2)
print('🖍️因為定義時函式已經定好p2="world", p1="Hello"，所以結果一樣是依照參數順序印出')

# 2.  學會while迴圈的使用
# 2.1 使用while印出1~10
print('2.1 使用while印出1~10')
# 記得"w"要小寫～
# 起始為1
number = 1
while number < 11:
    print(number)
    number = number + 1

# 3.  學會使用if/else的使用
# 資料輸入 input()，用於讀取使用者輸入的資料
# (1)單向選擇 if
print('🥸 (1)單向選擇if，當條件判斷成立時即執行該程式內容')
#   if 條件式 :
#      執行的程式內容
        # 執行的程式內容前有「四個空格」，這叫作「縮排」
score = int(input('請輸入英文成績?'))
if score >= 80:
    print('great')

#(2)雙向選擇 if...else
print('🥸 (2)雙向選擇if...else，當條件成立與不成立時都有做執行該程式內容')
#   if 條件式:
#      條件成立時執行的程式內容
#   else:
#      條件不成立時執行的程式內容
score = int(input('請輸入英文成績?'))
if score >= 60:
    print('及格！')
else:
    print('不及格')

# 3.1 使用if/else搭配while印出1~10之中所有雙數
print('🥸 3.1 使用if/else搭配while印出1~10之中所有雙數')
# 起始為1
# % 是一個運算符，下方為運算出除2時為0
# 如果不為0是奇數，那就pass不執行
# 接續透過number += 1，增加下一個數字執行運算
number = 1 
while number <= 10:
    if number % 2 == 0:
        print(number)
    else:
        pass  
    number += 1  

# 3.2 使用if/else搭配finally印出1~10之中所有雙數並且將當前數字開平方
print('🥸 3.2 使用if/else搭配finally印出1~10之中所有雙數並且將當前數字開平方')
# ** 是一個運算符，下方為運算出平方
number = 1
while number <=10:
    if number % 2 == 0:
        square = number ** 2
        print(number)
        print(f"這個雙數值[{number}]的平方是[{square}] ! ")
    else:
        pass  
    number += 1  

# 3.3 使用巢狀if/else印出1~10之中小於5的所有雙數
# 巢狀if，若要更進一步的判斷條件時，就需要用到巢狀if結構。是指在if-else敘述當中，還有另一組if-else敘述。')
print('🥸 3.3 使用巢狀if/else印出1~10之中小於5的所有雙數')
number = 1
while number <=10:
    if number < 5:
        if number % 2 == 0:
            print(number)
    else:
        pass
    number += 1

# 4.  學會使用for的使用
# for loop，以for進行迴圈，語法為下：
# for 變數<variable> in 任何序列物件<sequence>:　　
#     執行內容(statements)

# 4.1 使用for印出1~10
print('🥸 4.1 使用for印出1~10')
number = [1,2,3,4,5,6,7,8,9,10]
for a in number:
    print(a)

# 4.2 使用多重for迴圈印出以"*"構成的直角三角形
# 利用內建的range()函式，可以建立出一個整數序列，讓程式依照序列中的數值執行迴圈的內容。
print('🥸 4.2 使用多重for迴圈印出以"*"構成的直角三角形')
# 先設好要執行5次外部迴圈(因為看起來好像有像了，所以用5次)
# 不換行可以用end的方式，且讓*和*之間不要空白
# print() > 就會換行
for i in range(1,6):        
    for j in range(1,i+1):  
        print("*", end="")  
    print()                 

# 5.  其他迴圈控制
# 5.1 使用for和continue印出1~10之中所有單數
# 迴圈中還可以透過break和continue來結束迴圈。
# 差別在於break會將整個迴圈停止，而continue是將迴圈目前執行的程式停止，然後再次執行迴圈。
# continue，強制跳出本次迴圈，直接進入下一個迴圈
print('🥸 5.1 使用for和continue印出1~10之中所有單數')
# 指定範圍1~10之間，當number是偶数
# % 是一個運算符，下方為運算出除2時為0
for number in range(1, 11):
    if number % 2 == 0:  
        continue  
    print(number)  

# 5.2 使用while和break印出小於10的正整數(1~9)
# break，強制跳出整個迴圈    
print('🥸 5.2使用while和break印出小於10的正整數(1~9)')
number = 1 
while number < 10:
    print(number)
    if number >=10:
        break
    number += 1  

print('還有可以用pass，pass是執行時程式不做任何事情，將繼續往下執行  如果一樣以印出1~10的正整數，如下：')
for number in range(1,11):
    if number % 2 == 0:
        pass
    print(number)


# 6.  綜合題目
# 請利用上面所教，寫出猜數字遊戲，且猜題次數限制為10次，提示:可利用input()函式擷取console的輸入
print('🥸 6.')
# 引入一個random語法
# 語法為：random.randint(start, stop)
# 資料輸入 input()，用於讀取使用者輸入的資料
# if 1 <= player <= 15: ，用於確保使用者輸入的數值是在1~15之間，如果不是就請重新輸入～
import random

answer = random.randint(1, 15)

count = 0
while count < 10:
    player = int(input('您有10次機會，猜猜看1~15之間的數字～'))
    if 1 <= player <= 15: 
     if answer == player:
        print('中了 !')
        break
     else:
        print('沒中 !')
    else:
        print('超過遊戲範圍了，請重新輸入1~15之間的數字～')
    count += 1

print('遊戲結束 !')

'''
以下memo運算符
加	+
減	-
乘	*
除	/
取餘數	%
取整數	//
次方	**
'''

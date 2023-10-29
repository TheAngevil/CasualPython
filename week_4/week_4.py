
# Week 4
# 理解def 及 邏輯控制

def customize_print(input_str):
    print(f"Hello~{input_str}")

def compose_str(input_str):
    return(f"Hello~{input_str}")

def print_by_position(p1, p2):
    print(f"{p1}{p2}")


# 1.  學會def 如何宣告及使用
# 1.1 嘗試呼叫customize_print並執行，說明結果與輸入不同的原因
customize_print("Hi") #使用print將輸入的字串(也就是input_str)連同Hello一起印出來 

# 1.2 嘗試呼叫compose_str並列印出結果，說明與customize_print執行流程不同的原因
result = compose_str("Hi")
print(result) #不直接使用 print 函數來將結果印出，而是將結果作為字串返回，可以注意到在上方compose_str函數的回傳方式為return

# 1.3 嘗試呼叫print_by_position並使用"Hello", "world"作為p1, p2輸入並印出結果
print_by_position("Hello","World")

# 1.4 嘗試呼叫print_by_position並使用"world", "Hello"作為p1, p2輸入並解釋與1.3印出結果不同的原因
print_by_position("World","Hello") #print_by_position顧名思義就是會依照輸入的字串的順序依序印出p1, p2

# 1.5 觀察print_by_position(p2="world", p1="Hello")的輸出結果並解釋與1.4印出結果不同的原因
print_by_position(p2="world", p1="Hello") #p1="Hello", p2="world", 結果不同是因為依序輸入的字串會代表(p1,p2)是有順序性的


# 2.  學會while迴圈的使用
# 2.1 使用while印出1~10
num = 1 #訂一個變數為num從1開始
while num <= 10: #因為是1~10所以迴圈條件要<=10
    print(num) #印出符合上方條件的num
    num += 1 #將num遞增，會回到while繼續檢查下一個數字


# 3.  學會使用if/else的使用
# 3.1 使用if/else搭配while印出1~10之中所有雙數
num = 1  
while num <= 10: 
    if num % 2 == 0: # %=除
        print(num)  
    num += 1  

# 3.2 使用if/else搭配finally印出1~10之中所有雙數並且將當前數字開平方
import math
for i in range(1, 11):
    if i % 2 == 0:
        try:
            square_root = math.sqrt(i) #補充：**是平方
            print(f"{i} 的平方根是 {square_root}")
        finally:
            print("finally")

# 3.3 使用巢狀(Nesting) if/else印出1~10之中小於5的所有雙數
num = 1  
while num <= 10:
    if num <= 5:
        if num % 2 == 0:
            print(num)  
    num += 1  


# 4.  學會使用for的使用
# 4.1 使用for印出1~10
for num in range(1, 11): #若11那邊寫10就只會印出到9
    print(num)

# 4.2 使用多重for迴圈印出以"*"構成的直角三角形
height = 5  # 三角形的高度
for i in range(1, height + 1):  #三角形的行數
    for j in range(i):  #在每一行中打印 "*" 的数量等于行数
        print("*", end="") #沒有end=""的話*就會呈一直線
    print() #換行，若沒有換行就會是一行*


# 5.  其他迴圈控制
# 5.1 使用for和continue印出1~10之中所有單數
for num in range(1, 11):
    if num % 2 == 0: 
        continue #用來跳過此次回圈的條件，當num＝偶數時則不印出
    print(num)

# 5.2 使用while和break印出小於10的正整數(1~9)
#num = 1 
#while num < 10:
    # print(num)
    # num += 1 #一直到這邊跟前面練習的一樣，只是在while那邊沒有<=取而代之的是將設條件的方式用break
    # if num == 10:
    #     break #當上方if的條件成立時即結束回圈
# while num < 10: 跟 if num == 10: break 檢查重複了
num = 1
while True:
    if num >= 10:
        break
    print(num)
    num += 1

# 6.  綜合題目
# 請利用上面所教，寫出猜數字遊戲，且猜題次數限制為10次，提示:可利用input()函式擷取console的輸入
import random

ans = random.randint(1, 100) #用來生成一個1~100的隨機數，即猜數字的答案
num = 0  #預設猜測次數為0，意思跟上方練習的num=1一樣

while num < 10:
    guess_ans = input("請輸入1~100間的整數： ") #input用于從用戶獲取輸入的東西

    try:
        guess_ans = int(guess_ans)
        if 1 <= guess_ans <= 100:  #檢查是否在1~100之間
            if guess_ans < ans:
                print("太小了")
            elif guess_ans > ans:
                print("太大了")
            else:
                print(f"答對惹！答案是 {ans}。")
                break
            num += 1
        else:
            print("請輸入1~100之間的整數")
    except ValueError:
        print("請輸入一個有效的整數")

if num == 10:
    print(f"已經猜10次了，答案是 {ans}。")






#關於math的補充筆記：
#math.sqrt(x): x 的平方根。
#math.log(x): x 的自然对数。
#math.sin(x), math.cos(x), math.tan(x): 用于计算 x 的正弦、余弦和正切值。
#math.pow(x, y): x 的 y 次方。




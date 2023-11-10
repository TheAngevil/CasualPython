#流程控制: if, else, elif, while, break, pass
#Python流程控制：判斷的三種語法：單向選擇語法、雙向選擇語法、多向選擇語法

#1、單向選擇 if
print('1、單向選擇if，單向選擇if(如果...就...)：當判斷式成立時即執行該程式區塊')
#   if 條件式 :
#      執行的程式內容
        # 執行的程式內容前有「四個空格」，這叫作「縮排」
score = int(input('請輸入英文成績?'))
if score >= 80:
    print('great')

#2、雙向選擇 if...else
print('2、雙向選擇if...else')
#   if 條件式:
#      條件成立時執行的程式內容
#   else:
#      條件不成立時執行的程式內容
score = int(input('請輸入英文成績?'))
if score >= 60:
    print('及格！')
else:
    print('不及格')

#3、多向選擇 if...elif...else
print('🖍️3、多向選擇 if...elif...else(如果...就...否則就...)：當第一個條件成立時可以執行if下的程式區塊，不然就看第二個條件是否成立，成立時就執行該elif下的程式區塊，以此類推。')
print('當所有條件都不成立時就執行else下的程式區塊。elif沒有個數的限制，可以依照自己的需求而定。')
'''if 條件式1 :
    條件1成立時執行的程式內容1
elif 條件式2 :
    條件2成立時執行的程式內容2
elif 條件式3 :
    條件3成立時執行的程式內容3
else :
    條件都不成立時執行的程式內容4'''
bmi = eval(input("請輸入BMI"))
if bmi <18.5 :
    print("體重過輕")
elif bmi <24.5 :
    print("體重正常")
elif bmi <29.9 :
    print("體重過重")
else :
    print("請注意身體健康")

#4、巢狀if
print('🖍️4、巢狀if，若要更進一步的判斷條件時，就需要用到巢狀if結構了。所謂的巢狀if是指在if-else敘述當中，還有另一組if-else敘述')

goal = 80 #目標體重

health = 75 #理想體重

print("請輸入您的體重")
weight = int(input())

if weight <= goal: #判斷體重是否 小於等於 80
    #條件成立 體重確實 小於等於 80 執行
    if weight <= health: #判斷是否 小於等於75
        print("恭喜您達到理想體重")
    else:
        print("恭喜您達到目標")

else: #條件成立 體重 大於 80
    print("再努力一下,還差 " + str(weight - goal) + " 公斤到達目標體重\n" + "還差 " +
          str(weight - health) + "公斤到達理想體重")

#5、迴圈for / while
print('迴圈方法 for 以及while 是依其條件布林運算結果進而判斷迴圈執行的控制方式。')
print('當我們使用 for 或 while 語句時，python直譯器會判斷接續在 for 或 while後直至冒號 : 的程式碼之序列歷遍(for loop)或布林運算結果(while loop)， 決定在迴圈內部程式碼的執行與否')
print('(1)for loop，以for進行迴圈，語法為下：')
# for 變數<variable> in 任何序列物件<sequence>:　　
#     執行內容(statements)
example_list = [1,2,3,456,789,101,3,2,5]
for a in example_list:
    print(a)

# for是一個迴圈控制結構，用於對集合(例如清單、字串、元組等)中的每個元素進行迭代操作。語法為下：
# for 變數 in 集合:
# 集合們的範例：
print('元素')
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(fruit)

print('字串')
message = "Hello, World!"
for char in message:
    print(char)

print('數字')
for num in range(1, 6):
    print(num)
#或負數也可以
for num in range(-10, -5):
    print(num)

print('鍵或值')
student_scores = {"Alice": 85, "Bob": 92, "Carol": 78}
for name in student_scores:
    print(f"{name}: {student_scores[name]}")

print('(2)while loop，while迴圈，使用while 以布林運算結果判斷進行迴圈控制，語法為下：')
'''
while 布林條件判斷(condition)：
      執行內容(statements)
或
while 條件:
    # 執行迴圈內的程式碼
'''
#判斷Ture / Flase
a = 1
while a < 10:
    print(a)
    a += 2
#或
count = 1
while count <= 5:
    print(count)
    count += 1
#或
count =1
total = 0
while count <=5:
    num = int(input("請隨意輸入一個數字，猜中就贏囉～"))
    if num == 0:
        break
    total += num
    count += 1      #count記得要包進print之上，不然執行不到次數，這樣執行超過5次還是可以繼續猜
print("Gameover")

#6、break/continue/pass
print('迴圈中還可以透過break和continue來結束迴圈。')
print('差別在於break會將整個迴圈停止，而continue是將迴圈目前執行的程式停止，然後再次執行迴圈。')
#break範例
#b為1之後就結束
for a in ['x','y','z']:
    for b in [1,2,3]:
        if(b==2):
            break
        print(f'{a}{b}')
print('ok')

#continue範例
#會略過b為2及b為3
for a in ['x','y','z']:
    for b in [1,2,3]:
        if(b==2):
            continue
        print(f'{a}{b}')

#pass範例
print('pass則是執行時程式不做任何事情，將繼續往下執行。')
print('如果一樣以印出1~10的正整數，如下：')
for number in range(1,11):
    if number % 2 == 0:
        pass
    print(number)

#7、其他
print('(1)巢狀 loop，巢狀迴圈，指迴圈裡面又包迴圈：')
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()


print('(2)range，疊代數列時，使用內建range()函式就可以生成一等差數列')
'''用於迴圈的計數，range(start, stop[, step])
start：數列的起始數字，若沒有輸入則預設為0。
stop：數列到此數字之前必須停止，亦即不包含stop。
step：數列的間隔，若沒有輸入則預設為1。'''
for i in range(5):
    print(i)
print('💡傳入1個參數')
for number in range(5):
    print(number, end=" \n") #\n用來換行，往右邊斜 !

print('💡傳入2個參數')
for number in range(0,11):
    print(number, end=" \n")

print('️💡傳入3個參數')
for number in range(0,10,2): #後方是(start, stop [, step])
    print(number, end=" \n")
#所以是0~10，step放2(可以想成往前走2)，迴圈執行了5次，也可以當成印出偶數
#0,2,4,6,8

for number in range(0,10,1):
    print(number, end=" \n")
#所以是0~10,step放1,執行10次，也可當印出正整數
#0,1,2,3,4,5,6,7,8,9

print('💡len應用')
roommate = ['Bebe','Luna','Dora','Poya']
for i in range(len(roommate)):
    print(roommate[i]) #帶給它roommate，就不會一直跳數值了




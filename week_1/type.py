#input 取得使用者輸入的值
print(f"嗨!{input('請輸入你的名字')}")

'''
數值型態：int,float,bool
字串型態：str,chr,ord
容器型態：list,dict,tuple,set,frozenset
'''

#int 整數
a = 1
print(f"'{a}'的型態是 {type(a)} - inteegr") # type()印出該變數的資料型別
#int(x) > 把x轉換為整數
print(f"浮點數轉成整數 > {int(3.14)}是{type(int(3.14))}\n")

#float 浮點數
b = 0.5
print(f"'{b}'的型態是 {type(b)} - float")
#float(x) > 把x轉換為浮點數
print(f"整數轉成浮點數 > {float(3)}是{type(float(3))}\n")

#str 字串
c = "string"
print(f"'{c}'的型態是 {type(c)} - string")
#str(x) > 把x轉換為字串
print(f"整數轉成字串 > {str(3)}是{type(str(3))}\n")

#bool True或False
d = True
print(f"'{d}'的型態是 {type(d)} - boolean")
#bool(x) > 把x轉換為布林值
print(f"整數轉成布林 > {bool('False')}是{type(bool('False'))}\n")

'''
可用以下判斷式來輸出布林值
==	是否等於
!=	是否不等於
>	是否大於
<	是否小於
>=	是否大於等於
<=	是否小於等於
and	判斷兩側的條件是否都為 True
or	判斷兩側的條件是否至少有一側為 True
not	將布林的 True 或 False 反轉
'''

#chr 將Unicode碼轉換成對應字元
e = 97
print(f"{chr(e)}的對應Unicode是'{e}'")

#ord 將對應字元轉換成Unicode碼
f ="測"
print(f"{ord(f)}的對應字元是'{f}'\n")

#list 陣列 一串按順序排序的元素組成 (可新增/刪除/修改元素)
week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(week)
print(week[0]) #取得元素
print(week[-1]) #取得最後一個元素
print(week[0:5]) #以範圍取值 [起始:結束:間隔]；省略終點[x:]會直接取到最後；省略起點[:x]會從頭取；省略間隔會預設間隔為1

#新增元素到list的最後 .append()
week.append("new")
print(week)

#新增元素到指定位置 .insert(index,object)
week.insert(1,"Monday後")
print(week)

#批次加入 .extend()
week2 = ["星期一","星期二","星期三"]
week.extend(week2)
print(week)

week.extend(["再加一個"])
print(week)

#刪除元素 .remove()
week.remove("再加一個")
print(week)

#刪除最後一個元素 .pop()
week.pop()
print(f"{week}\n")

#Dict 包含鍵值(key)與對應的值(value)，可以快速取出對應值，用於資料查找；value可以是任何的資料型態，但 key 必須是唯一且不可變的
#主要有兩種建立方式
#1  dict(key=value)
Day1 = dict(week = "Monday",
            month = 9,
            date = 18,
            weather = "sunny")

#2  直接使用{key:value}
Day2 = {"week" : "Monday",
        "month" : 9,
        "date" : 18,
        "weather" : "sunny"}

#可用兩種方式取值
#1 用key來找出對應的value
print(str(Day1['date']))

#2 用get
print(str(Day2.get("weather")))
#get可自己設定空值訊息
print(f'{Day2.get("test","這裡沒有哦")}\n')

#tuple 類似於list，但tuple是不可變的(唯讀，宣告後不可修改)，tuple可迭代
#主要有三種建立方式
#1 直接於()輸入資料，以「,」間隔
test1 = (1,2,3)
print(test1)

#2 直接輸入資料，以「,」間隔，如果只有一個資料後面也要加,「,」
test2 = 1,2
print(test2)

#3 使用tuple()，傳入Iterable(可迭代的)物件來建立tuples
test3 = tuple([1,2,3]) #一般陣列
print(test3)
test4= (1,2)*5 #迭代
print(test4)

#取得元素方式同list
print(test3[0]) #取得元素
print(test3[-1]) #取得最後一個元素
print(test3[0:1]) #以範圍取值 [起始:結束:間隔]；省略終點[x:]會直接取到最後；省略起點[:x]會從頭取；省略間隔會預設間隔為1

#取得元素所在的索引值 .index()
print(test3.index(1))
print("\n")

#set 集合 可以新增和刪除元素，跟Dict一樣是無序，set具有移除重複的特性，
#建立方式 利用{}
set1 = {"a","b",1,2}
print(set1)

#當作容器使用
set2 = set("test")
print(set2)

#可以用in、not in判斷元素是否存在
print("s" in set1)
print("t" not in set2)

#新增資料和刪除set元素
set3 = {"a","b",3,4}

set3.add("c") #用add加入元素，如果加入的是已有元素則無作用
print(set3)

set3.remove(3) #用remove移除元素
print(set3)

set3.pop() #隨機移除元素
print(set3)

set3.discard("d") #移除指定項目，且在移除時不會發生執行錯誤的狀況
print(set3)

set3.clear() #清空集合
print(set3)

#集合運算(回傳值)
set01={1,2,3,4,5}
set02={4,5,6,7}
set03={5,8,9}
print(set01&set02) #交集 union()
print(set01|set02) #聯集 union()
print(set01-set02) #差集 difference()
print(set01^set02) #對稱差集 symmetric_difference()

#運算(回傳bool)
set001={1,2,3,4}
set002={2,3}
print(set001==set002) #判斷集合是否相等
print(set001>=set002) #超集合 - A完全包含B，A和B所包含的元素可能完全相同
print(set001>set002) #真超集合 - A完全包含B，
print(set002<=set001) #子集合 - A完全被B包含，A和B所包含的元素可能完全相同
print(set002<set001) #真子集合 - A完全被B包含，且B具有A沒有的的元素
print("\n")

#frozenset 不可變集合 不可更動元素
print(frozenset([1,"二",3,"四"]))
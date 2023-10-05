print("1. String - 字串\n可用成對單引號或雙引號包含需要表示的文字，實用如下")
#如果字串的值內有包含''，可以使用""
print("> This's mine")
#如果字串的值內有包含""，可以使用''
print('> 這是"一個東西"')
#多行字串可以使用成對'''包覆
multi='''> 這個是一個
很多行的
字串哦~~~~
'''
print(multi)

print("\n")
print("2.f-string - (format String) 輸出含變數的字串\n在字串前加上f，並將變數用{}包覆，即可輸出含變數的字串，實用如下")
#設定變數
date="今天"
weather="晴天"
#輸出含變數的字串
print(f"> {date}是{weather}，要出去吃飯嗎?")

print("\n")
print("3.r-string - (raw string) 用於需要表示「\」的字串，不將他視為轉義字元，實用如下")
#使用r-string來用字串呈現「\」
print(r"> C:\Users\User\Desktop\python")
print(r"> 一\n二\n")

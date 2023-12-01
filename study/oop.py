#物件導向OOP，Object-oriented programming
#更好閱讀、更好維護、更簡易於新功能添加

'''1、基本概念(類別Class、物件Object)
(1)類別Class
- 定義一件事物的抽象特點。類別的定義包含了資料的形式(屬性, Field)以及對資料的操作(方法, Method)
- 可以想像成類別是汽車的設計藍圖(blueprint)，其中我們可以在這張藍圖定義抽象的內容(也就是屬性、方法)
- 例如汽車的廠牌、汽車的車名以及馬力和取得汽車資訊等。'''
'''類別(Class):人類 
   物件名稱(Name):我 
   物件屬性(Property):有兩隻手 ; 每隻手有五根手指頭
   物件的操作方法(Method):左手操作鍵盤，右手操作滑鼠 ; 手指用來輸入'''
#語法如下，class關鍵字，接著自定類別名稱，最後加上冒號。
#類別名稱的命名原則習慣上使用Pascal命名法，也就是每個單字字首大寫，不得使用空白或底線分隔單字。
class Human:
    pass #只是想滅掉紅色🐛  
class MyCar:


 '''
(2)物件Object
- 物件也就是類別的實例，也就是說有了類別這張藍圖我們可以在程式中產生許多汽車類別的資料，而這些資料彼此之間不互相影響，每一個皆是獨立的。'''
#語法如下
#object_name = classname()
#Taiwaness = Human()

#屬性(Attribute)，又分為類別屬性(class attribute)與實體屬性(instance attribute)
#object_name.attribute_name = value

print('🧤 (1)先設定玩家"共同屬性"為level是1，錢有10000，接著讓Player1和Player2都持有這個屬性，接著印出Player1的level、Player2的錢錢為何?')
class Player:
    level = 1
    money = 10000

Player1 = Player()
Player2 = Player()

print(Player1.level)
print(Player2.money)

print('🧤 (2)每個玩家也都可以有自己的屬性')
class Player:
    level = 1
    money = 10000

Player1 = Player()
Player2 = Player()
Player1.name = "Wenby"
Player2.name = "Huang"

print(Player1.name)
print(Player2.name)

print('🧤 (3)以上方式當玩家很多的時候，會要寫很長，所以可以用__init__，init是initialize初始化的縮寫')
#縮排好重要，沒縮排的時候print一直失敗
class Player:
    level = 1
    money = 10000
    def __init__(self, name, age):  #self代表目前正在建立的角色，name和money則是附加的屬性
        self.name = name
        self.age = age

Player1 = Player("Wenby", 15)
Player2 = Player("Huang", 20)
print(Player1.name)
print(Player2.age)

print('🧤 方法Method，像是每個人不一樣，有不同的技能')
class Player:
    level = 1
    money = 10000
    def __init__(self, name, age):  #self代表目前正在建立的角色，name和money則是附加的屬性
        self.name = name
        self.age = age
    def 先鋒(self): #這邊打完runner後面就自動跳self了，自動帶入角色本身
        print(f"{(self).name}衝向前了!")
    def 攻擊手(self):
        print(f'{(self).name}打過去了!')

Player1 = Player("Wenby", 15)
Player2 = Player("Huang", 20)
Player1.先鋒()
Player2.攻擊手()


#2、三大特性(封裝、繼承、多型)
#封裝 (Encapsulation)
print('🧤 封裝 (Encapsulation)，將程式包成一個一個的類(class)和函式(function)')
#將物件的狀態和行為封裝在一個單元中，並且只對外部提供有限的接口來訪問物件，從而保護物件的內部狀態不被直接訪問或修改。
print('(1)Public: 使用者只要知道類裡面有什麼函式可以使用，即可輕鬆使用，不需要知道太多程式過程細節')
print('(2) Private: 有些屬性不想讓外界的人直接閱讀的屬性')

#繼承 (Inheritance)
print('🧤 繼承 (Inheritance)，有些self可能會一直出現，那就用繼承(Inheritance)')
#主要讓程式碼可以重複被使用，減少重複性工作的時間
class Player:
    level = 1
    money = 10000
    def __init__(self, name, age):  #self代表目前正在建立的角色，name和money則是附加的屬性，這也叫建構式(Constructor)
        self.name = name
        self.age = age
    def runner(self): #這邊打完runner後面就自動跳self了，自動帶入角色本身
        print(f"{(self).name}衝向前了!")
    def killer(self):
        print(f'{(self).name}殺過去了!')
class Superman(Player): #這邊再創一個超人，然後又繼承了Player，所以他也有先鋒和攻擊手的技能
    def fast(self):
        print(f"{(self).name}攻城了!!!")

Player1 = Superman("Wenby", 15)
#這邊下方寫幾個就可以顯示幾項技能
Player1.fast()
Player1.runner()
Player1.killer()

#多型 (Polymorphism)，包含多載(Overloading)和覆寫(Overriding)。
print('🧤 多型(Polymorphism)，大家都繼承了相同的類別，也呼叫相同的函式，但結果卻不同')
print('(1)多載(Overloading)，同名字的函數中，根據參數型態或數量不同而決定呼叫哪個函式')
def sum(a,b,c=0):
    print(a+b+c)

sum(1,2)
sum(1,2,3)

print('(2)覆寫(Overriding)，用子類別去覆蓋父類別的成員函數，進而達到擴充、加強效果。子類別最初會從父類別繼承任何東西')
class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        return "Oh!"

class Cat(Animal):
    def talk(self):
        return "Meow"

class Dog(Animal):
    def talk(Self):
        return "Woof"

animals=[Animal("Animal"),Cat("Cat"),Dog("Dog")]

for animal in animals:
    print(animal.name+" : "+animal.talk())

#💡實作1
'''建立一個類別 可以儲存屬性:寵物名、年紀、毛顏色
讓使用者建立3隻動物 寵物名、年紀、毛顏色
'''
class Pet:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

Dog = Pet("NINI",10,"white")
Cat = Pet("OHOH",5,"blue")
Rabbit = Pet("MOMO",1,"brown")

Pets = [Dog,Cat,Rabbit]
for Pet in Pets:
    print(f"{Pet.name} : {Pet.age} : {Pet.color}")  #記得用f-string🥹





















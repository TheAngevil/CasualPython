# 基礎介紹
print("**基礎介紹**")
# - 定義一個類別`Adventurer`，其中有一個方法`introduce`，嘗試調用這個方法，他會印出什麼?
class Adventurer:

    def __init__(self, name="", level=0, job="Adventurer"): # 建構子
        self.job = job # job設為Adventurer
        self.name = name # name取回傳值(str)
        self.level = level # leve取回傳值(int)
    def introduce(self):
        print("Hello, I am an adventurer!")

    def show_info(self):
        print(f"名稱:{self.name} ,等級:Lv.{self.level}")

player_1 = Adventurer() # 宣告一個類別為Adventurer的物件player_1
player_1.introduce() # 使用物件的公開函數
print("Ans: 會印出'Hello, I am an adventurer!'")

print("\n**屬性與初始化**")
# **屬性與初始化**
# - 為`Adventurer`類別增加一個`__init__`方法，該方法接收`name`, `level`與'job'作為參數，讓'job'是Adventurer並為每個Adventurer物件設定name與job屬性。
# - 如何新增一個player_1?
# - 如何直接取得他/她的名字與等級?
# - 新增一個方法`show_info`，該方法將印出冒險者的名字和等級。
# - 他的名字與等級可以修改嗎?
# - 新增一個player_2並重複上面的三個步驟，這個冒險者是一樣的嗎? (用id()試試?)

# - 如何新增一個player_1?
player_1 = Adventurer("冒險者1", 1)

# - 如何直接取得他/她的名字與等級?
print(f"名稱:{player_1.name} ,等級:Lv.{player_1.level}") # 可以改成input讓他自輸，但等級要設定輸入規則以免出錯

# - 新增一個方法`show_info`，該方法將印出冒險者的名字和等級。
player_1.show_info() # 呼叫show_info()印出player_1的內容

# - 他的名字與等級可以修改嗎?
print("Ans: 可以，修改player_1的改參數就好，範例如下:")
player_1 = Adventurer("改名的冒險者1", 2) # 可以改成input讓他自輸，但等級要設定輸入規則以免出錯
player_1.show_info() # 呼叫show_info()印出player_1的內容

# - 新增一個player_2並重複上面的三個步驟，這個冒險者是一樣的嗎? (用id()試試?)
print("Ans: 可以用id()看出player_2與player_1是不同的冒險者，範例如下:")
# 新增一個player_2
player_2 = Adventurer("冒險者2",2)
player_2.show_info()
# 使用id()判斷並印出結果
print(f"使用id()判斷的結果為 {id(player_1) == id(player_2)}，\n"
      "因為雖然兩者皆使用 Adventurer class的建構子來創建這兩個物件，但每次創建都會產生一個新的實例變數並具有不同的ID")

print("\n**繼承**")
# **繼承**
# - 定義一個新類別`Mage`，它繼承自`Adventurer`類別。
# - 新增一個方法`skill_1`，當調用這個方法時，它印出 "Casting a fireball!!"
# - 新增Mage，並讓他/她自我介紹，他/她如何自我介紹?
# - 我有辦法讓他使用冒險者得自我介紹嗎? 在不改code的情況下要怎麼做?

# - 定義一個新類別`Mage`，它繼承自`Adventurer`類別。
class Mage(Adventurer):

    def skill_1(self):
        print("Casting a fireball!!")

    def introduce_mage(self):
        print("Hello, I am a mage!")

# - 新增一個方法`skill_1`，當調用這個方法時，它印出 "Casting a fireball!!"
mage_skill = Mage()
mage_skill.skill_1()

# - 新增Mage，並讓他/她自我介紹，他/她如何自我介紹?
player_3 = Mage("法師1",2)
player_3.introduce_mage()

# - 我有辦法讓他使用冒險者得自我介紹嗎? 在不改code的情況下要怎麼做?
print("Ans: 可以，子類別可以直接調用父類別的函式，範例如下:")
player_3.introduce()

print("\n**多態性**")
# **多態性**
# - 定義另一個繼承自`Adventurer`的類別`Warrior`。
# - 覆寫`introduce`方法，讓它印出 "Hello, I am a warrior ready for battle!"，他現在的自我介紹是?
# - 幫這個Warrior做一個戰士的技能!
class Warrior(Adventurer):

    def introduce(self): # 覆寫父類別`introduce`方法
        print("Hello, I am a warrior ready for battle!")

    def skill_2(self): # 新增一個戰士技能
        print("Lead off an attack!")

# - 覆寫`introduce`方法，讓它印出 "Hello, I am a warrior ready for battle!"，他現在的自我介紹是?
player_4 = Warrior()
player_4.introduce() # 因為已覆寫`introduce`方法，故會印出覆寫後的結果

# - 幫這個Warrior做一個戰士的技能!
player_4.skill_2()

print("\n**多重繼承**")
# **多重繼承**
# 做一個MageWarrior類別，有自己的自我介紹，同時會Mage, Warrior的技能，同時還會第三種技能!
class MageWarrior(Mage,Warrior):

    def introduce(self): # MageWarrior的自我介紹
        print("Hello, I am a MageWarrior")
    def skill_3(self): # 新增一個MageWarrior的第三種技能
        print("Avada Kedavra!")

player_5 = MageWarrior()
player_5.introduce() # 印出MageWarrior的自我介紹
player_5.skill_1() # 印出第一種技能
player_5.skill_2() # 印出第二種技能
player_5.skill_3() # 印出第三種技能

print("\n**封裝**")
# **封裝**
# - 修改`Adventurer`類別，將`name`和`level`設為私有屬性（例如，`__name`和`__level`）。
# - 新增`get_name`和`get_level`方法來取得這些屬性的值。
# - 新增`set_name`和`set_level`方法來設定這些屬性的值，但要加入條件來確保等級不是負數。
# - 嘗試使用上面的get_XXX與 set_XXX方法，讓一個等級1的"初學者"變成等級999的"騎士領主"!
# - 嘗試直接 實例.__name 與 實例.__level，還可以拿到資料嗎? 還可以修改嗎?

# - 修改`Adventurer`類別，將`name`和`level`設為私有屬性（例如，`__name`和`__level`）。
class Adventurer:

    def __init__(self, name="", level=1, job="Adventurer"):
        self.job = job
        self.__name = name
        self.__level = level

    def get_name(self): # 新增`get_name`方法
        print(f"名稱:{self.__name}")

    def get_level(self): # 新增`get_level`方法
        print(f"Lv.{self.__level}")

    def set_name(self): # 新增`set_name`方法
        self.__name = input("請輸入名稱:")

    def set_level(self): # 新增`set_level`方法，並加入條件確保等級不是負數
        while True:
            try:
                num = int(input("請輸入等級:"))
                if num < 0:  # 判斷user輸入的值是不是正整數
                    print("請輸入大於0的數字!")
                else:
                    self.__level = num  # 輸入的值是數字時回傳值
                    break
            except ValueError:  # 偵測到異常時執行
                print("請輸入正整數!")

# 新增`get_name`和`get_level`方法來取得這些屬性的值
player_6 = Adventurer("初學者", 1)
player_6.get_name()
player_6.get_level()

# 嘗試使用上面的get_XXX與 set_XXX方法，讓一個等級1的"初學者"變成等級999的"騎士領主"!
# 設定名稱及等級
player_6.set_name()
player_6.set_level()
# 取得執行結果
player_6.get_name()
player_6.get_level()

# - 嘗試直接 實例.__name 與 實例.__level，還可以拿到資料嗎? 還可以修改嗎?
print("Ans: 不行，來源端無法存取到類別中的私有屬性(Private Attribute)，故不能拿取及修改")

print("\n**類別與實例變數**")
# **類別與實例變數**
# - 在`Adventurer`類別中，新增一個類別變數`faction`，並賦予它的值為 "Neutral"。
# - 討論實例變數與類別變數的區別，並提供實例來說明。
class Adventurer:
    faction = "Neutral" # 類別變數

    def __init__(self, name, sex):
        self.name = name # 實例變數
        self.sex = sex # 實例變數

print("類別變數在類別中聲明，並且它們的值在類別的所有實例中都是相同的。 類別變數只能在類別定義後才能賦值\n"
      "實例變數在類別的多個實例中可以有不同的值。 實例變數可以隨時分配或變更其值，兩者範例如下:")

print("- 實例變數的範例")
test_1 = Adventurer("test1","Male")
test_2 = Adventurer("test2","Female")
print(f"test_1: name > {test_1.name} ,sex > {test_1.sex}")
print(f"test_2: name > {test_2.name} ,sex > {test_2.sex}")
print("可以看出不同實例中可以有不同的值，並且可以隨時分配或更改")

print("- 類別變數的範例")
print(f"test_1: {test_1.faction}")
print(f"test_2: {test_2.faction}")
print("可以看出在不同實例中，皆可運用此類別變數，且在所有實例中的值都是相同的") #印出"Neutral"

print("- 類別變數的衍伸範例")
test_1.faction = "fixNetural"
print(f"test_1: {test_1.faction}") #印出"fixNetural"
print(f"test_2: {test_2.faction}") #印出"Netural"
print("兩者印出結果不同是因為它實際上是在 test_1 的物件上建立了一個名為 faction 的實例變數，而非修改 Adventurer class 的 faction 類別變數。\n"
      "即 test_1 印出的是自己的實例變數 faction，並將其值設為'fixNetural'；而 test_2 印出的是 Adventurer class 的 faction 類別變數，所以它的值仍是'Neutral'")

print("\n**挑戰題：**")
# **挑戰題：** 使用上面學到的概念，建立一個`Monster`類別，具有`species`、`strength`等屬性，並具有`attack`等方法。之後，再建立一些繼承自`Monster`的特定怪物類別，如`Dragon`。
class Monster:

    def __init__(self, species="", strength="", level=0, Classification="Enemy"):
        self.__species = species
        self.__strength = strength
        self.__level = level
        self.classification = Classification

    def sound(self):
        print("Hiss~")

    def attack_1(self):
        print("Bomb!")

    def set_species(self):
        self.__species = input("請輸入物種名稱:")

    def set_strength(self):
        self.__strength = input("請輸入能力:")

    def set_attack(self):
        print(input("請輸入怪物攻擊技能:"))

    def set_sound(self):
        return input("請輸入叫聲:")

    def set_attack(self):
        return input("請輸入攻擊招式:")

    def set_level(self):
        while True:
            try:
                num = int(input("請輸入等級:"))
                if num < 0:  # 判斷user輸入的值是不是正整數
                    print("請輸入大於0的數字!")
                else:
                    self.__level = num  # 輸入的值是數字時回傳值
                    break
            except ValueError:  # 偵測到異常時執行
                print("請輸入正整數!")
    def show_info(self):
        print(f"物種(species){self.__species}")
        print(f"能力(strength):{self.__strength}")
        print(f"等級(level):Lv.{self.__level}")

class Dragon(Monster):

    def sound(self):
        print("growl")

    def attack_2(self):
        print("Shoot fireball!")

class Zombie(Monster):

    def sound(self):
        print("Rrrrrr~")

    def attack_3(self):
        print("Bite!")
class Piglin(Monster):

    def sound(self):
        print("oink")

    def attack_4(self):
        print("Attack!")

class ZombifiedPiglin(Zombie, Piglin):

    def sound(self):
        print("grunt")

    def attack_5(self):
        print("Group attack!")

# 印出結果用
def result(monstern):
    monstern.show_info()
    monstern.sound()

# 印出monster_1相關設定
monster_1 = Monster("苦力怕", "毀滅", 2)
result(monster_1)
monster_1.attack_1()

# 印出monster_2相關設定
monster_2 = Dragon("終界龍", "龍炎彈", 50)
result(monster_2)
monster_2.attack_2()

# 印出monster_3相關設定
monster_3 = Zombie("殭屍", "中毒", 1)
result(monster_3)
monster_3.attack_3()

# 印出monster_4相關設定
monster_4 = Piglin("豬布林", "物理攻擊", 20)
result(monster_4)
monster_4.attack_4()

# 印出monster_5相關設定
monster_5 = ZombifiedPiglin("殭屍豬布林", "發起群攻", 30)
result(monster_5)
# monster_5擁有其繼承到的所有技能
monster_5.attack_1()
monster_5.attack_3()
monster_5.attack_4()
monster_5.attack_5()

# 創造一個monster_6並印出其相關設定
print("- 創造一個怪物吧!")
monster_6 = Monster()
monster_6.set_species() #設定物種
monster_6.set_strength() #設定能力
monster_6.set_level() #設定等級
monster_6.show_info() #回傳物種、能力、等級
print(f"叫聲:{monster_6.set_sound()}\n攻擊招式:{monster_6.set_attack()}") #設定並回傳叫聲及攻擊招式


if  __name__ == "__main__":
    pass
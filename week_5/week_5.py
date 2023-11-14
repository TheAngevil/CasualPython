# 基礎介紹
# - 定義一個類別`Adventurer`，其中有一個方法`introduce`，嘗試調用這個方法，他會印出什麼? 
# 這題會印出 “Hello, I am an adventurer!”

print("\n**屬性與初始化**")
class Adventurer:
    def introduce(self):
        print("Hello, I am an adventurer!")

    def __init__(self, name, level, job): # (1)增加一個`__init__`方法
        self.name = name
        self.level = level
        self.job = job
    
    def show_info(self): # (4)新增一個方法`show_info
        print(f"name:{self.name}, level:{self.level}, job:{self.job}")

player_1 = Adventurer(name="Chloe", level=10, job="Adventurer") # (2)新增player_1
player_2 = Adventurer(name="Ａnna", level=20, job="Adventurer") # (6)新增player_2

name = player_1.name
level = player_1.level

player_1.introduce()
print(f"Name: {name}, Level: {level}") # (3)直接取得Chloe的名字與等級
player_1.show_info()

player_1.name = "newChloe" 
player_1.level = 8 # (5)修改名字跟等級

print(f"Updated Name: {player_1.name}")
print(f"Updated Level: {player_1.level}")

player_2.show_info()
print(f"比較player_1跟player_2的id: {id(player_1) == id(player_2)}")

# **屬性與初始化**
# - 為`Adventurer`類別增加一個`__init__`方法，該方法接收`name`, `level`與'job'作為參數，讓'job'是Adventurer並為每個Adventurer物件設定name與job屬性。
# Ans=(1)
# - 如何新增一個player_1? 
# Ans=(2)
# - 如何直接取得他/她的名字與等級?
# Ans=(3)
# - 新增一個方法`show_info`，該方法將印出冒險者的名字和等級。
# Ans=(4)
# - 他的名字與等級可以修改嗎? 
# Ans=(5)可以，直接把參數改掉就好
# - 新增一個player_2並重複上面的三個步驟，這個冒險者是一樣的嗎? (用id()試試?)
# Ans=(6) id是不一樣的



# **繼承**
# - 定義一個新類別`Mage`，它繼承自`Adventurer`類別。
# Ans=(7)
# - 新增一個方法`skill_1`，當調用這個方法時，它印出 "Casting a fireball!!"
# Ans=(8)
# - 新增Mage，並讓他/她自我介紹，他/她如何自我介紹?
# Ans=(9)
# - 我有辦法讓他使用冒險者得自我介紹嗎? 在不改code的情況下要怎麼做?
# Ans=(9)
print("\n**繼承**")
class Mage(Adventurer): # (7)繼承Adventurer裡的introduce, __init__, show_info

    def introduce(self):
        super().introduce()  # super()是一个内置函数，用于在子類中調用父類的方法
        print(f"I am a {self.job} my named is {self.name} at level {self.level}.")

    def skill_1(self):
        print("Casting a fireball!!") # (8)新增一個方法`skill_1`

player_3 = Mage(name="Harry", level=5, job="Mage")

player_3.skill_1() 
player_3.introduce() # (9)新增Mage > player3



# **多態性**
# - 定義另一個繼承自`Adventurer`的類別`Warrior`。
# Ans=(10)
# - 覆寫`introduce`方法，讓它印出 "Hello, I am a warrior ready for battle!"，他現在的自我介紹是?
# Ans=(11)
# - 幫這個Warrior做一個戰士的技能!
# Ans=(12)
print("\n**多態性**")
class Warrior(Adventurer): # (10)
    def introduce(self):
        super().introduce()
        print(f"I am a {self.job} my named is {self.name} at level {self.level}.")
    
    def Warrior_skill(self):
        print("Use weapons")

player_4 = Warrior(name = "Eric", level = 30, job = "Warrior")

player_4.introduce() # (11)
player_4.show_info()
player_4.Warrior_skill() # (12)



# **多重繼承**
# 做一個MageWarrior類別，有自己的自我介紹，同時會Mage, Warrior的技能，同時還會第三種技能!
print("\n**多重繼承**")
class MageWarrior(Mage,Warrior):

    def introduce(self): # MageWarrior的自我介紹
        print("Hello, I am a MageWarrior")

    def MageWarrior_skill(self): # 第三種技能
        print("Ｓpell and fly")

player_5 = MageWarrior(name = "Tom", level = 21, job = "Warrior")
player_5.introduce()
player_5.skill_1() 
player_5.Warrior_skill() 
player_5.MageWarrior_skill()



# **封裝**
# - 修改`Adventurer`類別，將`name`和`level`設為私有屬性（例如，`__name`和`__level`）。
# Ans=(13)
# - 新增`get_name`和`get_level`方法來取得這些屬性的值。
# Ans=(14)
# - 新增`set_name`和`set_level`方法來設定這些屬性的值，但要加入條件來確保等級不是負數。
# Ans=(15)
# - 嘗試使用上面的get_XXX與 set_XXX方法，讓一個等級1的"初學者"變成等級999的"騎士領主"!
# Ans=(16)
# - 嘗試直接 實例.__name 與 實例.__level，還可以拿到資料嗎? 還可以修改嗎?
# Ans=是可以的但不建議這麼做，最好還是使用get_name 和 set_level 方法
print("\n**封裝**")
class Adventurer:
    def introduce(self):
        print("Hello, I am an adventurer!")

    def __init__(self, name, level, job):
        self.__name = name
        self.__level = level # (13)
        self.job = job

    def show_info(self):
        print(f"Name: {self.__name}, Level: {self.__level}, Job: {self.job}")

    def get_name(self): # (14)
        return self.__name

    def get_level(self):
        return self.__level

    def set_name(self, name):
        self.__name = name

    def set_level(self, level): # (15)
        if level >= 0:
            self.__level = level
        else:
            print("Level cannot be negative!")

player_1 = Adventurer(name="Chloe", level=10, job="Adventurer")
player_1.show_info()

current_level = player_1.get_level()
current_name = player_1.get_name() # 使用 get_XXX 方法獲取私有屬性的值

print(f"Current Name: {current_name}")
print(f"Current Level: {current_level}")


player_1.set_name("newChloe")
player_1.set_level(999) # (16)使用 set_XXX 方法修改私有屬性的值


player_1.show_info() # 顯示修改後的信息

print(f"Direct access to _Adventurer__name: {player_1._Adventurer__name}")
print(f"Direct access to _Adventurer__level: {player_1._Adventurer__level}")


player_1.set_level(-5)



# **類別與實例變數**
# - 在`Adventurer`類別中，新增一個類別變數`faction`，並賦予它的值為 "Neutral"。
# - 討論實例變數與類別變數的區別，並提供實例來說明。
print("\n**類別與實例變數**")
class Adventurer:
    faction = "Neutral" # 類別變數(Adventurer獨有的)

    def __init__(self, name):
        self.name = name # 實例變數(每个Adventurer都有自己的name，当修改類別變數faction的值時，會影響所有包含新創建的實例變數)

adventurer1 = Adventurer("A")
adventurer2 = Adventurer("B") # 新增兩個Adventurer

print(f"Adventurer 1: Name - {adventurer1.name}, Faction - {adventurer1.faction}")
print(f"Adventurer 2: Name - {adventurer2.name}, Faction - {adventurer2.faction}") # 將兩個Adventurer的name跟faction印出

Adventurer.faction = "newNeutral" # 修改實例變數的值將影響所有faction

print(f"Adventurer 1: Name - {adventurer1.name}, Faction - {adventurer1.faction}")
print(f"Adventurer 2: Name - {adventurer2.name}, Faction - {adventurer2.faction}") # 再次印出會發現faction變成新的了

adventurer3 = Adventurer("C") # 新增一個Adventurer

print(f"Adventurer 3: Name - {adventurer3.name}, Faction - {adventurer3.faction}") # 新增的實例也會受影響



# **挑戰題：** 使用上面學到的概念，建立一個`Monster`類別，具有`species`、`strength`等屬性，並具有`attack`等方法。之後，再建立一些繼承自`Monster`的特定怪物類別，如`Dragon`。

print("\n**挑戰題**")

class Monster():

    def __init__(self, species, strength):
        self.species = species
        self.strength = strength
    
    def attack(self):
        print(f"{self.species} attack with a strength of {self.strength}.")
        

class Dragon(Monster):

    def __init__(self, species, strength, tricks):
        super().__init__(species, strength)
        self.tricks= tricks

    def attack(self):
        print(f"{self.species} breathes {self.tricks} with a strength of {self.strength}.")

class Vampire(Monster):

    def __init__(self, species, strength, tricks):
        super().__init__(species, strength)
        self.tricks = tricks

    def attack(self):
        print(f"{self.species} attack with {self.tricks} with a strength of {self.strength}.")



monster1 = Monster("Capybara", 10)
monster1.attack()

dragon1  = Dragon("Dragon", 50, "fire")
dragon1.attack()

vampire1 = Vampire("Vampire", 20, "bite!")
vampire1.attack()



if  __name__ == "__main__":
    pass
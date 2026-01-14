import random
name=input("name pet")
class pet():
    def __init__(self,name,health,food,hunger,power,coins):
        self.name=name
        self.health=int(health)
        self.food=int(food)
        self.hunger=int(hunger)
        self.power=int(power)
        self.coins=int(coins)

self=pet(name,100,2,75,5,3)


print(self.__dict__)
def death():
   if self.health<=0:
      print("you died buy potions to make you stronger")
      quit()
         
      
class zombie():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

zombie1 =zombie("zombie",[], 40, 15)




class boar():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

boar1 =boar("boar",[], 50, 20)




class golem():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

golem1 =golem("golem",[], 80, 30)




class skeleton():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

skeleton1 =skeleton("skeleton",[], 60, 5)



class golemking():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

golem2 =golemking("golem king",[],670, 50)


class orc():
      def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

orc1=orc("orc",[],200,30)

def fight():
 while True:
  sigma=input("1: zombie 2: boar 3: Golem 4: skeleton 5: orc 6: go back")
  if sigma== "1":
       zombie1.health=40
       print(zombie1.health)
       while True: 
        death()
        sigma1=input("1: attack 2: quit")
        if sigma1=="1":
            zombie1.health-=self.power
            self.health-=zombie1.power
            print(f"Self health",self.health)
            print(f"health zombie:",zombie1.health)
        if sigma1=="2":
            break
        if zombie1.health<=0:
            self.coins+=1
            print(f"coins",self.coins)
            print("you defeated the zombie")
            break 
            
    
  if sigma== "2":
       boar1.health=50
       print(boar1.health)
       while True: 
        death()
<<<<<<< HEAD
        sigma2=input("1: attack 2: quit")
        if sigma2=="1":
=======
        choice=input("1: attack 2: quit")
        if choice=="1":
>>>>>>> Nathanwork-Branch
            boar1.health-=self.power
            self.health-=boar1.power
            print(f"Self health",self.health)
            print(f"health boar:",boar1.health)
            
<<<<<<< HEAD
        if sigma2=="2":
=======
        if choice=="2":
>>>>>>> Nathanwork-Branch
            break
        if boar1.health<=0:
            self.coins+=2
            print(f"coins",self.coins)
            print("you defeated the boar")
            break
  
  
  if sigma== "3":
       golem1.health=80
       print(golem1.health)
       while True: 
        death()
<<<<<<< HEAD
        sigma3=input("1: attack 2: quit")
        if sigma3=="1":
=======
        choice=input("1: attack 2: quit")
        if choice=="1":
>>>>>>> Nathanwork-Branch
            golem1.health-=self.power
            self.health-=golem1.power
            print(f"Self health",self.health)
            print(f"health golem:",golem1.health)
        
<<<<<<< HEAD
        if sigma3=="2":
=======
        if choice=="2":
>>>>>>> Nathanwork-Branch
            break
        if golem1.health<=0:
            self.coins+=3
            print(f"coins",self.coins)
            print("you defeated the golem")
            break
   
  if sigma== "4":
       skeleton1.health=60
       print(skeleton1.health)
       while True: 
        death()
<<<<<<< HEAD
        sigma4=input("1: attack 2: quit")
        if sigma4=="1":
=======
        choice=input("1: attack 2: quit")
        if choice=="1":
>>>>>>> Nathanwork-Branch
            skeleton1.health-=self.power
            self.health-=skeleton1.power
            print(f"Self health",self.health)
            print(f"health skeleton:",skeleton1.health)
<<<<<<< HEAD
        if sigma4=="2":
=======
        if choice=="2":
>>>>>>> Nathanwork-Branch
            break
        if skeleton1.health<=0:
            self.coins+=1
            print(f"coins",self.coins)
            print("you defeated the skeleton")
            break
   
   
  if sigma== "5":
       orc1.health=200
       print(orc1.health)
       while True: 
        death()
<<<<<<< HEAD
        sigma5=input("1: attack 2: quit")
        if sigma5=="1":
=======
        choice=input("1: attack 2: quit")
        if choice=="1":
>>>>>>> Nathanwork-Branch
            orc1.health-=self.power
            self.health-=orc1.power
            print(f"Self health",self.health)
            print(f"health orc:",orc1.health)
<<<<<<< HEAD
        if sigma5=="2":
=======
        if choice=="2":
>>>>>>> Nathanwork-Branch
            break
        if orc1.health<=0:
            self.coins+=5
            print(f"coins",self.coins)
            print("you defeated the orc")
            break
      
  if sigma=="6":
       break


   
def shop():
  while True:
     
     ShopI= input("1: 3$ health potion 2: 3$ power potion 3: 1$ food 4: go back")
     if ShopI=="1":
       if self.coins<3:
          print("brokie")
          break
       elif self.coins>=3:
        self.coins-=3
        self.health+=150
       
     
     if ShopI=="2":
      if self.coins<3:
          print("brokie")
          break
      elif self.coins>=3:
        self.coins-=3
        self.power+=2
     

     if ShopI=="3":
      if self.coins>=1:
        self.coins-=1
        self.food+=1
      elif self.coins<1:
          print("brokie")
          break
     
     if ShopI=="4":
        break
        
def stats():
   print(self.__dict__)
    
while True:
    action=input("Fight or Feed?")
    if self.hunger<=0:
        print("death")
        quit()
    enemies=["zombie","golem","skeleton"]
<<<<<<< HEAD
            
=======
    
>>>>>>> Nathanwork-Branch
    def overcap():
        for stat in ("hunger", "thirst"):
            setattr(self, stat, min(getattr(self, stat), 100))#stuff
        
    def feed():
        if self.food>=1:
            self.hunger+=10
            self.food-=1
            print(self.hunger)
        else:
            self.food<=0
            print("no food")
    def slots():
        slot=random.randint(7,77)
        self.coins -=7
        print("Gambling...")
        if slot <=76:
            print("Fail D: (1 to quickgamble)")
        else:
            print("YOU WON!!!!!")
            self.coins +=777
    def quickslots():
        slot=random.randint(7,77)
        self.coins -=7
        print("Gambling...")
        if slot <=76:
            print("Fail D:")
        else:
            print("YOU WON!!!!!")
            self.coins +=777

    def shop():
        print(PandA)

    PandA=("Potions: MaxHP:+10 $:50 PowerPot:+5PW $:100 Food:+15Hng $:10 Leather Armor:+10Def $:200")

    options = {
        "fight":fight,
        "feed":feed,
        "slots":slots,
        "1":quickslots,
        "shop":shop,
        "stats":stats
                }
    choice = action.lower()
    if choice in options:
        options[choice]()
    else:
<<<<<<< HEAD
        print("Not an option")    
=======
        print("Not an option")
>>>>>>> Nathanwork-Branch
        continue

 
#class instance function 
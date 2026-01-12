import time
name=input("name pet")
class pet():
    def __init__(self,name,health,food,hunger,power,coins):
        self.name=name
        self.health=int(health)
        self.food=int(food)
        self.hunger=int(hunger)
        self.power=int(power)
        self.coins=int(coins)

self=pet(name,150,2,75,8,3)


print(self.__dict__)
def death():
   if self.health<=0:
      print("you died buy potions to make you stronger")
      quit()
   if self.hunger<=0:
      print("you died of hunger")
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



class Zombifiedskeletonboss():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

boss1 =Zombifiedskeletonboss("golem king",[],670,50)


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
            self.hunger-=1
            print(f"Self health",self.health)
            print(f"health zombie:",zombie1.health)
            print(self.hunger,"hunger")
            
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
        sigma2=input("1: attack 2: quit")
        if sigma2=="1":
            boar1.health-=self.power
            self.health-=boar1.power
            self.hunger-=1
            print(f"Self health",self.health)
            print(f"health boar:",boar1.health)
            print(self.hunger,"hunger")
        if sigma2=="2":
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
        sigma3=input("1: attack 2: quit")
        if sigma3=="1":
            golem1.health-=self.power
            self.health-=golem1.power
            self.hunger-=1
            print(f"Self health",self.health)
            print(f"health golem:",golem1.health)
            print(self.hunger,"hunger")
        if sigma3=="2":
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
        sigma4=input("1: attack 2: quit")
        if sigma4=="1":
            skeleton1.health-=self.power
            self.health-=skeleton1.power
            self.hunger-=1
            print(f"Self health",self.health)
            print(f"health skeleton:",skeleton1.health)
            print(self.hunger,"hunger")
        if sigma4=="2":
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
        sigma5=input("1: attack 2: quit")
        if sigma5=="1":
            orc1.health-=self.power
            self.health-=orc1.power
            self.hunger-=1
            print(f"Self health",self.health)
            print(f"health orc:",orc1.health)
            print(self.hunger,"hunger")
        if sigma5=="2":
            break
        if orc1.health<=0:
            self.coins+=5
            print(f"coins",self.coins)
            print("you defeated the orc")
            break
      
  if sigma=="6":
       break

def bosses(): 
 sigmalicious=input("1: zombified skeleton boss 2: Quit")
 if sigmalicious=="1":
       boss1.health=670
       print(boss1.health)
       while True: 
        death()
        sigma67=input("1: attack 2: quit")
        if sigma67=="1":
            boss1.health-=self.power
            self.health-=boss1.power
            self.hunger-=5
            print(f"Self health",self.health)
            print(f"health boss:",boss1.health)
            print(self.hunger,"hunger")
        if sigma67=="2":
            break
        if boss1.health<=0:
            self.coins+=50
            print(f"coins",self.coins)
            print("you defeated the auralicious boss")
            break
   
def shop():
  while True:
     
     sigma6= input("1: 3$ health potion 2: 3$ power potion 3: 1$ food 4: go back")
     if sigma6=="1":
       if self.coins<3:
          print("brokie")
          break
       elif self.coins>=3:
        self.coins-=3
        self.health+=150
       
     
     if sigma6=="2":
      if self.coins<3:
          print("brokie")
          break
      elif self.coins>=3:
        self.coins-=3
        self.power+=5
     

     if sigma6=="3":
      if self.coins>=1:
        self.coins-=1
        self.food+=1
      elif self.coins<1:
          print("brokie")
          break
     
     if sigma6=="4":
        break
def feed():
   while True:
    sigmalicious=input("1: Feed 2: leave")
    if sigmalicious=="1":
      if self.food>=1:
        self.food-=1
        self.hunger+=10
        print(self.food)
      if self.food<=0:
        print("buy food")
        
    if sigmalicious=="2":
       break


    
while True:
 TRIPlETTUngTUngtUngsahur=input("1:Fight 2: Bosses 3: Shop 4: Stats 5: Feed")
 if TRIPlETTUngTUngtUngsahur== "1":
     fight()
 if TRIPlETTUngTUngtUngsahur=="2":
    bosses()
 if TRIPlETTUngTUngtUngsahur== "3":
     shop()
 if TRIPlETTUngTUngtUngsahur=="4":
    print(self.__dict__)
 if TRIPlETTUngTUngtUngsahur=="5":
   feed()
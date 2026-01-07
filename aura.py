name=input("name pet")
class pet():
    def __init__(self,name,health,food,hunger,thirst,power):
        self.name=name
        self.health=int(health)
        self.food=int(food)
        self.hunger=int(hunger)
        self.thirst=int(thirst)
        self.power=int(power)

self=pet(name,100,2,75,75,5)


print(self.__dict__)

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
    sigma=input("1: zombie 2: boar 3: Golem 4: skeleton 5: orc 6: go back")

    if sigma== "1":
       zombie1.health=40
       print(zombie1.health)
       while True: 
        sigma1=input("1: attack 2: quit")
        if sigma1=="1":
            zombie1.health-=self.power
            self.health-=zombie1.power
            print(f"Self health",self.health)
            print(f"health zombie:",zombie1.health)
        if sigma1=="2":
            break
        if zombie1.health<=0:
            print("you defeated the zombie")
            break
    
    
    if sigma== "2":
       boar1.health=50
       print(boar1.health)
       while True: 
        sigma2=input("1: attack 2: quit")
        if sigma2=="1":
            boar1.health-=self.power
            self.health-=boar1.power
            print(f"Self health",self.health)
            print(f"health boar:",boar1.health)
            
        if sigma2=="2":
            break
        if boar1.health<=0:
            print("you defeated the boar")
            break
  
  
    if sigma== "3":
       golem1.health=80
       print(golem1.health)
       while True: 
        sigma3=input("1: attack 2: quit")
        if sigma3=="1":
            golem1.health-=self.power
            self.health-=golem1.power
            print(f"Self health",self.health)
            print(f"health golem:",golem1.health)
        
        if sigma3=="2":
            break
        if golem1.health<=0:
            print("you defeated the golem")
            break
   

    if sigma== "4":
       skeleton1.health=60
       print(skeleton1.health)
       while True: 
        sigma4=input("1: attack 2: quit")
        if sigma4=="1":
            skeleton1.health-=self.power
            self.health-=skeleton1.power
            print(f"Self health",self.health)
            print(f"health skeleton:",skeleton1.health)
        if sigma4=="2":
            break
        if skeleton1.health<=0:
            print("you defeated the skeleton")
            break
   
   
    if sigma== "5":
       orc1.health=200
       print(orc1.health)
       while True: 
        sigma5=input("1: attack 2: quit")
        if sigma5=="1":
            orc1.health-=self.power
            self.health-=orc1.power
            print(f"Self health",self.health)
            print(f"health skeleton:",orc1.health)
        if sigma5=="2":
            break
        if orc1.health<=0:
            print("you defeated the skeleton")
            break
def death():
   if self.health<=0:
      quit()
      print("you died")   
    

TRIPlETTUngTUngtUngsahur=input("1:Fight 2: Bosses")
while True:
 death()
 if TRIPlETTUngTUngtUngsahur== "1":
     fight()
 







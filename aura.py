name=input("name pet")
class pet():
    def __init__(self,name,health,food,hunger,thirst,power):
        self.name=name
        self.health=int(health)
        self.food=int(food)
        self.hunger=int(hunger)
        self.thirst=int(thirst)
        self.power=int(power)

self=pet(name,100,2,75,75,1)

print(self.__dict__)

class zombie():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

zombie1 =zombie("zombie",[], 40, 1)




class boar():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

boar1 =boar("boar",[], 50, 2)




class golem():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

golem1 =golem("golem",[], 80, 2)




class skeleton():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

skeleton1 =skeleton("skeleton",[], 60, 3)



class golemking():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

golem2 =golemking("golem king",[],670, 10)


class orc():
      def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.power = int(power)

orc1=orc("orc",[],200,0.67)

def fight():
    sigma=input("1: zombie 2: boar 3: Golem 4: skeleton 5: orc 6: go back")
    if sigma== "1":
       while True: 
        sigma1=input("1: attack : quit")
        if sigma1=="1":
            zombie1.health-=20
            print(f"health zombie:",zombie1.health)
        if sigma1=="2":
            break
        if zombie1.health<=0:
            print("you defeated the zombie")
            break

TRIPlETTUngTUngtUngsahur=input("1:Fight 2: Bosses")
while True:
 if TRIPlETTUngTUngtUngsahur== "1":
     fight()








import random
name=input("name pet")
class pet():
    def __init__(self,name,health,food,hunger,thirst,power,coins,defence):
        self.name=name
        self.health=int(health)
        self.food=int(food)
        self.hunger=int(hunger)
        self.thirst=int(thirst)
        self.power=int(power)
        self.coins=int(coins)
        self.defence=int(defence)
self=pet(name,100,2,75,75,2,100000,5)
print(self.__dict__)
while True:
    action=input("Fight or Feed?")
    if self.hunger<=0:
        print("death")
        quit()
    enemies=["zombie","golem","skeleton"]
               
    def overcap():
        for stat in ("hunger", "thirst"):
            setattr(self, stat, min(getattr(self, stat), 100))
               
    def feed():
        if self.food>=1:
            self.hunger+=10
            self.food-=1
            print(self.hunger)
        else:
            self.food<=0
            print("no food")
            
    def fight():
        print("fought")
    def slots():
        slot=random.randint(7,77)
        self.coins -=5
        if slot == 77:
            print("YOU WON BIG KEEP GOING DUDE")
            self.money += 777
    options = {
        "fight":fight,
        "feed":feed,
        "slots":slots
                }
    choice = action.lower()
    if choice in options:
        options[choice]()
    else:
        print("Not an option")    
        continue
#class instance function 


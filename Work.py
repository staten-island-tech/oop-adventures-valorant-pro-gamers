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
self=pet(name,100,2,75,75,2,20,5)
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

<<<<<<< HEAD
print(zombie1)

class boar():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.health = int(power)

boar1 =boar("boar",[], 50, 2)

print(boar1)

class golem():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.health = int(power)

golem1 =golem("golem",[], 80, 2)

print(golem1)

class skeleton():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.health = int(power)

skeleton1 =skeleton("skeleton",[], 60, 3)

print(skeleton.__dict__)

=======
    PandA=("Potions: MaxHP:+10 $:50 PowerPot:+5PW $:100 Food:+15Hng $:10 Leather Armor:+10Def $:200")
>>>>>>> Nathanwork-Branch


    options = {
        "fight":fight,
        "feed":feed,
        "slots":slots,
        "1":quickslots
                }
    choice = action.lower()
    if choice in options:
        options[choice]()
    else:
        print("Not an option")    
        continue

 
#class instance function 
    def actualitems():
        LeatherAmr = self.defence=+10

    items=[
        {
            "name": LeatherAmr,
            "price": "200" ,
            "description": "+10Def"
        },
        {
            "name":"Food",
            "price": "10",
            "description": "+15Hng"
        },
        {
            "name":"PowerPot",
            "price": "100",
            "description": "+5Pwr"
        },
        {
            "name":"MaxHP",
            "price": "50",
            "description":"+10MaxHP"
        }
    ]

    while True:
        for index, item in enumerate(items):
            print(index, ":", item["name"], index, ":", item["price"])
        choices = input("What would you like to buy? Type a number based on the options:")
        chosen_item = items[int(choices)]
        print(f"You bought {chosen_item['name']}")
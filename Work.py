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
    # def actualitems():
    #     LeatherAmr = self.defence=+10

    # items=[
    #     {
    #         "name": LeatherAmr,
    #         "price": "200" ,
    #         "description": "+10Def"
    #     },
    #     {
    #         "name":"Food",
    #         "price": "10",
    #         "description": "+15Hng"
    #     },
    #     {
    #         "name":"PowerPot",
    #         "price": "100",
    #         "description": "+5Pwr"
    #     },
    #     {
    #         "name":"MaxHP",
    #         "price": "50",
    #         "description":"+10MaxHP"
    #     }
    # ]


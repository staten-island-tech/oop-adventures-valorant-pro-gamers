name=input("name pet")
class pet():
    def __init__(self,name,health,inventory,hunger,thirst,power):
        self.name=name
        self.health=int(health)
        self.inventory=[inventory]
        self.hunger=int(hunger)
        self.thirst=int(thirst)
        self.power=int(power)

self=pet(name,100,["apple"],75,75,1)
print(self)
        


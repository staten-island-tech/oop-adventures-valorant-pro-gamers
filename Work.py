
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
if self.hunger<=0:
    print("death")
    quit()      
               
def overcap():
        for stat in ("hunger", "thirst"):
            setattr(self, stat, min(getattr(self, stat), 100))
               
def feed():
        self.hunger+=10
        self.food-=1
        print(self.hunger)



#class instance function 


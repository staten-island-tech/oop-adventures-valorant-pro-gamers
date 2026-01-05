class zombie():
    def __init__(self,name,drops,health,power):
        self.name = name
        self.drops = drops
        self.health = int(health)
        self.health = int(power)

zombie1 =zombie("zombie",[], 40, 1)

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




# actions = {
#         "1": happiness,
#         "2": hungry,
#         "3": water,
#         "4": love,
#         "5": gamble,
#     }
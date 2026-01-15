
import random
name=input("name pet")
class pet():
    def __init__(player,name,health,food,hunger,power,coins):
        player.name=name
        player.health=int(health)
        player.food=int(food)
        player.hunger=int(hunger)
        player.power=int(power)
        player.coins=int(coins)

player=pet(name,150,2,75,8,3)
print(player.__dict__)
while True:
    
    actionss=input("Fight,Feed,Gamble,Bosses,Stats,or shop?")
               
    def overcap():
        for stat in ("hunger"):
            setattr(player, stat, min(getattr(player, stat), 100))
        
    def feed():
        if player.food>=1:
            player.hunger+=10
            player.food-=1
            print(player.hunger)
            print("food left"),player.food
        else:
            player.food<=0
            print("no food")
            
    def slots():
        slot=random.randint(7,77)
        player.coins -=7
        print("Gambling...")
        if slot <=76:
            print("Fail D: (1 to quickgamble)")
        else:
            print("YOU WON!!!!!")
            player.coins +=777
    def quickslots():
        slot=random.randint(7,77)
        player.coins -=7
        print("Gambling...")
        if slot <=76:
            print("Fail D:")
        if slot==77:
            print("YOU WON!!!!!")
            player.coins +=777

    print(player.__dict__)
    def death():
        if player.health<=0:
            print("you died buy potions to make you stronger")
            quit()
        if player.hunger<=0:
            print("you died of hunger")
            quit()
    
    class enemy():
        def __init__(player,name,max_health,power,reward):
            player.name = name
            player.max_health= int(max_health)
            player.health = player.max_health     
            player.power = int(power)   
            player.reward = int(reward)
        def health_reset(player):
            player.health = player.max_health
    enemies = {
    "1": enemy("Zombie", 40, 15, 1 ),
    "2": enemy("Boar", 50, 20, 2),
    "3": enemy("Golem", 80, 30, 3),
    "4": enemy("Skeleton", 60, 5,1),
    "5": enemy("Orc", 200, 30, 5)
    }

    class Zombifiedskeletonboss():
        def __init__(player,name,health,power):
            player.name = name
            player.health = int(health)
            player.power = int(power)

    boss1 =Zombifiedskeletonboss("zombified skeleton boss",10000,50)
  
    def combat_system():
        print("choose enemy:")
        for key, enemy_chosen in enemies.items():
            print(f"{key}: {enemy_chosen.name} (Helath: {enemy_chosen.health})")

        choice = input("number:")
        if choice not in enemies:
            print("Not a choice")
            return
            
        enemy_chosen = enemies[choice]
        enemy_chosen.health_reset()
        print(f"{enemy_chosen}'s health:",enemy_chosen.health)
        


        while True:
            death()
            Attacking = input("1:attack 2:quit")
            if Attacking == "2":
                break
            if Attacking =="1":
                enemy_chosen.health -= player.power
                player.health -= enemy_chosen.power
                player.hunger -= 5
            
                print("Your health:", player.health)
                print(f"{enemy_chosen.name}'s health:", enemy_chosen.health)
                print("hunger:", player.hunger)
                if enemy_chosen.health <=0:
                    player.coins += enemy_chosen.reward
                    print(f"You defeated {enemy_chosen.name}!")
                    print(f"Your coins:{player.coins}")
                    break
            else:
                print("No")

    def bosses(): 
        sigmalicious=input("1: zombified skeleton boss 2: Quit")
        if sigmalicious=="1":
            boss1.health=670
            print(boss1.health)
            while True: 
                death()
                sigma67=input("1: attack 2: quit")
                if sigma67=="1":
                    boss1.health-=player.power
                    player.health-=boss1.power
                    player.hunger-=5
                    print(f"player health",player.health)
                    (f"health boss:",boss1.health)
                    print(player.hunger,"hunger")
                if sigma67=="2":
                    break
                if boss1.health<=0:
                    player.coins+=150
                    print(f"coins:",player.coins)
                    print("you defeated the auralicious boss")
                    break
    
    def shop():
        while True:       
            shops= input("1: 3$ health potion 2: 3$ power potion 3: 1$ food 4: go back")
            if shops=="1":
                if player.coins<3:
                    print("brokie")
                    break
                elif player.coins>=3:
                    player.coins-=3
                    player.health+=150
            
            
            if shops=="2":
                if player.coins<3:
                    print("brokie")
                    break
                elif player.coins>=3:
                    player.coins-=3
                    player.power+=5
            

            if shops=="3":
                if player.coins>=1:
                    player.coins-=1
                    player.food+=1
                elif player.coins<1:
                    print("brokie")
                    break
            
            if shops=="4":
                break
    def feed():     
        while True:
            sigmalicious=input("1: Feed 2: leave")
            if sigmalicious=="1":
                if player.food>=1:
                    player.food-=1
                    player.hunger+=10
                    print("food",player.food)
                    print("Hunger",player.hunger)
            if player.food<=0:
                print("buy food")
                break
            
            if sigmalicious=="2":
                break
    

    def stats():
        print(player.__dict__)
    options = {
        "fight":combat_system,
        "feed":feed,
        "slots":slots,
        "1":quickslots,
        "bosses":bosses,
        "shop":shop,
        "stats":stats
                }
    choice = actionss.lower()
    if choice in options:
        options[choice]()
    else:
        print("Not an option")    
        continue


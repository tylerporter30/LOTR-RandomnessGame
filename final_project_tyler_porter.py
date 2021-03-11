#This game is based on randomness. Importing random
import random

#List of enemies
enemyNameList = ["Nazgûl", "Saruman", "Sauron", "Orcs", "Wargs", "Balrog", "Trolls", "Witch-king of Angmar" ]


#Creating a hero class (Aragorn)
class Hero:

    def __init__(self, name, rings, healthLeft):
        self.name = name
        self.position = 0
        self.rings = rings
        self.healthLeft = healthLeft


    def __str__(self):
        heroSetUp = "\n"
        heroSetUp += "Hero : " + self.name + "\n"
        heroSetUp += "Position : " + str(self.position) + "\n"
        heroSetUp += "Rings : " + str(self.rings) + "\n"
        heroSetUp += "Health Points : " + str(self.healthLeft) + "\n"
        heroSetUp += "\n"
        return heroSetUp

#Creating the enemy class
class Enemy:
    
    def __init__(self, name, position, damage):
        self.name = name
        self.position = position
        self.damage = damage
  
    def __str__(self):
        enemySetUp = "\n"
        enemySetUp += "Enemy : " + self.name + "\n"
        enemySetUp += "Position : " + str(self.position)
        enemySetUp += "Damage : " + str(self.damage) + "\n"
        enemySetUp += "\n"
        return enemySetUp

#This is the start of the game, tells user to progress, how much damage taken, rings collected, etc.
def play(hero, enemies, lengthOfPath):
    print("Begin new game.")
    for index in range(1, lengthOfPath + 1):
        input("\nPress Enter button to progress.\n")
        hero.position = index
        print(hero.name + " is at " + str(hero.position))
        
        for enemy in enemies:
            if hero.position == enemy.position:
                hero.healthLeft -= enemy.damage
                print("Got attacked by " + enemy.name + " and lost " + str(enemy.damage) + " health.")
                break
       
       #Ring pickup count
        else:
            pickup = int (1)
            hero.rings += pickup
            print("Recieved " + str(pickup) + " Rings")
        
        #If hero health reaches 0, then hero is defeated
        if hero.healthLeft <= 0:
            print("\n\n" + hero.name + " was defeated")
            break
    
    #If hero has health by the end of the 10 clicks you win
    else:
        print("\n"+ hero.name + " defeated the enemy! You obtained the one ring to rule them all! ")

#Game length is 10 steps. Number of enemy encounter
def main():
    lengthOfPath = 10
    hero = Hero("Aragorn", 0, 100)
    numOfEnemies = random.randint (int(0.2 * lengthOfPath), int(0.5 * lengthOfPath))
    enemies = []
    
    for index in range(numOfEnemies):
        enemyName = random.choice(enemyNameList)
        enemyPosition, enemyDamage = random.randint(1, lengthOfPath), random.randint(20, 50) #Enemy damage is between 20-50
        enemies.append(Enemy(enemyName, enemyPosition, enemyDamage))
        
    play(hero, enemies, lengthOfPath) 
    print("\nResults of the game:")
    print(hero)

if __name__ == "__main__":
    main()
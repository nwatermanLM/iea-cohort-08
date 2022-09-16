#!/bin/python3
# PLEASE SEE READ ME FOR MORE INFORMATION
# WELCOME TO MY PYTHON TEXT ADVENTURE GAME
# VERSION ALPHA 1.0

def CharSheet():
  print('/\ \/' * 10)
  directions = []
  userInput = ''
  print('Class:', myclass, '_'*2, 'Lvl:', Level['Lvl'], '_'*2, 'XP:', XPCENT, '%', 'of', Level['LUP'], '_'*2, sep='')
  if myclass == class_options[0]:
      print('STR:', WarStats['Str'], '_'*2, 'MAG:', WarStats["Mag"], '_'*2, 'DEX:', WarStats["Dex"], '_'*2, 'VIT:', WarStats["Vit"], '_'*2, sep='')
  if myclass == class_options[1]:
    print('STR:', RogStats['Str'], '_'*2, 'MAG:', RogStats["Mag"], '_'*2, 'DEX:', RogStats["Dex"], '_'*2, 'VIT:', RogStats["Vit"], '_'*2, sep='')
  if myclass == class_options[2]:
    print('STR:', SorStats['Str'], '_'*2, 'MAG:', SorStats["Mag"], '_'*2, 'DEX:', SorStats["Dex"], '_'*2, 'VIT:', SorStats["Vit"], '_'*2, sep='')
  while userInput not in directions:
    print("Options: town, church")
    userInput = input()
    if userInput == "town":
      TownSquare2()
    if userInput == "church":
      ChurchLvl1Room1()
    
def LevelUpWar(Level, WarStats):
  new_Str, new_Mag, new_Dex, new_Vit = 0, 0, 0, 0
  while Level['Exp'] >= Level['LUP']:
    Level['Lvl'] += 1
    Level['Exp'] = Level['Exp'] - Level['LUP']
    Level['LUP'] = round(Level['LUP'] * 1.5)
    XPCENT = round(Level['Exp'] / Level['LUP'] * 100)
    new_Str += 2
    new_Mag += 1
    new_Dex += 1
    new_Vit += 1
    WarStats['Str'] += new_Str
    WarStats['Mag'] += new_Mag
    WarStats['Dex'] += new_Dex
    WarStats['Vit'] += new_Vit
    print('Level Up! You are now Level:', Level['Lvl'], '_'*2, 'XP:', XPCENT, '%', 'of', Level['LUP'], '_'*2, sep='')
    print("STR:", WarStats['Str'], '+', new_Str, "MAG:", WarStats['Mag'], '+', new_Mag, "DEX:", WarStats['Dex'], '+', new_Dex, "VIT:", WarStats['Vit'], '+', new_Vit)

def LevelUpRog(Level, RogStats):
  new_Str, new_Mag, new_Dex, new_Vit = 0, 0, 0, 0
  while Level['Exp'] >= Level['LUP']:
    Level['Lvl'] += 1
    Level['Exp'] = Level['Exp'] - Level['LUP']
    Level['LUP'] = round(Level['LUP'] * 1.5)
    XPCENT = round(Level['Exp'] / Level['LUP'] * 100)
    new_Str += 1
    new_Mag += 1
    new_Dex += 2
    new_Vit += 1
    RogStats['Str'] += new_Str
    RogStats['Mag'] += new_Mag
    RogStats['Dex'] += new_Dex
    RogStats['Vit'] += new_Vit
    print('Level Up! You are now Level:', Level['Lvl'], '_'*2, 'XP:', XPCENT, '%', 'of', Level['LUP'], '_'*2, sep='')
    print("STR:", RogStats['Str'], '+', new_Str, "MAG:", RogStats['Mag'], '+', new_Mag, "DEX:", RogStats['Dex'], '+', new_Dex, "VIT:", RogStats['Vit'], '+', new_Vit)

def LevelUpSor(Level, SorStats):
  new_Str, new_Mag, new_Dex, new_Vit = 0, 0, 0, 0
  while Level['Exp'] >= Level['LUP']:
    Level['Lvl'] += 1
    Level['Exp'] = Level['Exp'] - Level['LUP']
    Level['LUP'] = round(Level['LUP'] * 1.5)
    XPCENT = round(Level['Exp'] / Level['LUP'] * 100)
    new_Str += 1
    new_Mag += 2
    new_Dex += 1
    new_Vit += 1
    SorStats['Str'] += new_Str
    SorStats['Mag'] += new_Mag
    SorStats['Dex'] += new_Dex
    SorStats['Vit'] += new_Vit
    print('Level Up! You are now Level:', Level['Lvl'], '_'*2, 'XP:', XPCENT, '%', 'of', Level['LUP'], '_'*2, sep='')
    print("STR:", SorStats['Str'], '+', new_Str, "MAG:", SorStats['Mag'], '+', new_Mag, "DEX:", SorStats['Dex'], '+', new_Dex, "VIT:", SorStats['Vit'], '+', new_Vit)

def ChurchLvl1Room1():
  directions = []
  print('/\ \/' * 10)
  print("Church Level 1")
  print("\'The sanctity of this place has been fouled.\'")
  userInput = ""
  while userInput not in directions:
    print("Movement: left/right/backward/forward")
    print("Menu: CharSheet")
    userInput = input()
    if userInput == "left":
      options = ["attack", "run"]
      print("A Skeleton runs at you from the shadows.")
      print("Options: attack/run")
      while userInput not in options:
        userInput = input()
        if userInput == 'attack':
          Level['Exp'] += 150
          if myclass == class_options[0]:
            print('You swing your sword and land a successful hit.  The enemy is defeated.')
            LevelUpWar(Level, WarStats)
          if myclass == class_options[1]:
            print('You fire an arrow from your bow.  It hits its target.  The enemy is defeated.')
            LevelUpRog(Level, RogStats)
          if myclass == class_options[2]:
            print('Channeling the arcane power of your staff you manifest multiple Charged Bolts that electrocute your enemy and destroy it.')
            LevelUpSor(Level, SorStats)
        if userInput == 'run':
          TownSquare2()
        # Skeleton()
    if userInput == "right":
      print("You find an abandoned Chest.  There could be something valuable inside of it.")
      # Chest()
    if userInput == "forward":
      options = ["attack", "run"]
      print("You hear an unsettling moan ahead.  The halls of the church are barely lit by waning candle light.  A zombie is slowly shuffling towards you.")
      print("Options: attack/run")
      while userInput not in options:
        userInput = input()
        if userInput == 'attack':
          Level['Exp'] += 75
          if myclass == class_options[0]:
            print('You swing your sword and land a successful hit.  The enemy is defeated.')
            LevelUpWar(Level, WarStats)
          if myclass == class_options[1]:
            print('You fire an arrow from your bow.  It hits its target.  The enemy is defeated.')
            LevelUpRog(Level, RogStats)
          if myclass == class_options[2]:
            print('Channeling the arcane power of your staff you manifest multiple Charged Bolts that electrocute your enemy and destroy it.')
            LevelUpSor(Level, SorStats)
      # Zombie()
    if userInput == "backward":
      TownSquare2()
    if userInput == "CharSheet":
      CharSheet()

def TownSquare2():
  directions = []
  print('/\ \/' * 10)
  print("You are back in the Town Square.  Move forward to return to the Church or feel free to explore the town.")
  print("Griswald the Blacksmith stands on your left.  Adria the Witch on your right.  Deckard Cain is still standing near the well behind you.")
  print("You remember you need to move forward in order to head towards the Church.")
  userInput = ""
  while userInput not in directions:
    print("Movement: left/right/backward/forward")
    print("Menu: CharSheet")
    userInput = input()
    if userInput == "left":
      print("Griswald the Blacksmith is busy hammering away at a blade on his anvil.  He does not seem to notice you.")
      # showBlacksmith()
    if userInput == "right":
      print("Adria the Witch has her nose in an old tome.  She does not seem to notice you.")
      # showWitch()
    if userInput == "forward":
      ChurchLvl1Room1()
    if userInput == "backward":
      print("Thoughts of cowardice and retreat briefly cross your mind.  However you shake it off, determined to move forward towards the Church.")
    if userInput == "CharSheet":
      CharSheet()

def showWounded():
  directions = []
  print('/\ \/' * 10)
  print("You see a bloodied and wounded man laying along the path going towards the Church.")
  print("He reaches out to you... begging... \'Please... the ArchBishop Lazerus has betrayed us... he led us to a trap... a demon called the Butcher...\' and then he expires in front of you.")
  print("You look up from the dead man.  The Church is in front of you, an evil red glow emmanating from the entrance.")
  userInput = ""
  while userInput not in directions:
    print("Movement: left/right/backward/forward")
    print("Menu: CharSheet")
    userInput = input()
    if userInput == "right":
      print("You see the Witch's hut in the distance.")
      print("I should continue moving forward.")
    if userInput == "left":
      print("Looking to the left you see some rocks and trees.  The town boundary merges into wilderness and caves quite quickly.")
      print("I should continue moving forward.")
    if userInput == "forward":
      ChurchLvl1Room1()
      userInput = input()
    if userInput == "backward":
      TownSquare2()
    if userInput == "CharSheet":
      CharSheet()

def TownSquare1():
  directions = []
  print('/\ \/' * 10)
  print("You are in the Town Square.  You see an old man in front of you standing near a well.  He has just greeted you and introduced himself as Deckard Cain.")
  print("Deckard Cain informs you that only a few people remain in the town after dozens have gone missing.")
  print("He indicates you need to move forward in order to head towards the Church.")
  userInput = ""
  while userInput not in directions:
    print("Movement: left/right/backward/forward")
    print("Menu: CharSheet")
    userInput = input()
    if userInput == "left":
      print("I should head towards the Church.")
    if userInput == "right":
      print("I should head towards the Church.")
    if userInput == "backward":
      print("Thoughts of cowardice and retreat briefly cross your mind.  However you shake it off, determined to move forward towards the Church.")
    if userInput == "forward":
      showWounded()
    if userInput == "CharSheet":
      CharSheet()

if __name__ == "__main__":
  Level = {
    'Lvl': 1,
    'Exp': 0,
    'LUP': 100
  }
  WarStats = { 
  'Str': 30,
  'Mag': 10,
  'Dex': 20,
  'Vit': 25
  }
  RogStats = { 
  'Str': 20,
  'Mag': 15,
  'Dex': 30,
  'Vit': 20
  }
  SorStats = { 
  'Str': 15,
  'Mag': 35,
  'Dex': 15,
  'Vit': 20
  }

  XPCENT = round(Level['Exp'] / Level['LUP'] * 100)
  
  while True:
    print('/\ \/' * 10)
    print('_' * 10, 'DIABLO RETROGRADED', '_' * 10)
    print('/\ \/' * 10)
    print("Name your character (eight digits maximum): ")
    print('/\ \/' * 10)
    name = input()
    while len(name) >= int(9):
            print("Your Character name cannot be more than eight digits long.")
            print("Name your character (eight digits maximum): ")
            name = input()
    print('/\ \/' * 10)
    print("Choose your class: Warrior, Rogue, or Sorceror: ")
    class_options = [ 'Warrior', 'Rogue', 'Sorceror' ]
    myclass = input()
    while myclass == class_options[0] or class_options[1] or class_options[2]:
        if myclass == class_options[0]:
            print("A mighty Warrior here to save us.")
            break
        if myclass == class_options[1]:
            print("A cunning Rogue here to save us.")
            break
        if myclass == class_options[2]:
            print("A wise Sorceror here to save us.")
            break
        elif myclass != class_options[0] or class_options[1] or class_options[2]:
            print("Please type Warrior, Rogue, or Sorceror")
            myclass = input()
    print('/\ \/' * 10)        
    print("You have arrived in the town of Tristram within the region of Khanduras.")
    print("The town seems unassuming, besides the fact that it rests on the outskirts of the home and birthplace of King Leoric.")
    print("You hear screams coming from the Church that sits in the North West corner of Tristram.")
    print(f'Greetings, {name} the {myclass}. Stay awhile and listen...')
    print('Class:', myclass, '_'*2, 'Lvl:', Level['Lvl'], '_'*2, sep='')
    if myclass == class_options[0]:
        print('STR:', WarStats['Str'], '_'*2, 'MAG:', WarStats["Mag"], '_'*2, 'DEX:', WarStats["Dex"], '_'*2, 'VIT:', WarStats["Vit"], '_'*2, sep='')
    if myclass == class_options[1]:
        print('STR:', RogStats['Str'], '_'*2, 'MAG:', RogStats["Mag"], '_'*2, 'DEX:', RogStats["Dex"], '_'*2, 'VIT:', RogStats["Vit"], '_'*2, sep='')
    if myclass == class_options[2]:
        print('STR:', SorStats['Str'], '_'*2, 'MAG:', SorStats["Mag"], '_'*2, 'DEX:', SorStats["Dex"], '_'*2, 'VIT:', SorStats["Vit"], '_'*2, sep='')
    print('/\ \/' * 10)
    TownSquare1()
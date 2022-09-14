CharLvl = 1
CharExp = 0
LevelUp = 100
while CharExp >= LevelUp:
  CharLvl += 1
  CharExp = CharExp - LevelUp
  LevelUp = round(LevelUp * 1.5)
ShowXP = round(CharExp / LevelUp * 100)

def ChurchLvl1():
  directions = ["left","right","backward","forward"]
  print("You are back in the Town Square.  Move forward to return to the Church or feel free to explore the town.")
  print("The Blacksmith Griswald stands on your left.  The Witch Adria on your right.  Deckard Cain is still standing near the well behind you.")
  print("You remember you need to move forward in order to head towards the Church.")
  print(f'Level: {CharLvl}, XP: {ShowXP}%')
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/forward")
    userInput = input()
    if userInput == "left":
      showBlacksmith()
    elif userInput == "right":
      showWitch()
    elif userInput == "forward":
      ChurchLvl1()
    elif userInput == "backward":
      print("You find that this door opens into a wall.")
    else: 
      print("Please enter a valid option.")

def TownSquare2():
  directions = []
  print("You are back in the Town Square.  Move forward to return to the Church or feel free to explore the town.")
  print("Griswald the Blacksmith stands on your left.  Adria the Witch on your right.  Deckard Cain is still standing near the well behind you.")
  print("You remember you need to move forward in order to head towards the Church.")
  print(f'Level: {CharLvl}, XP: {ShowXP}%')
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/forward")
    userInput = input()
    if userInput == "left":
      print("Griswald the Blacksmith is busy hammering away at a blade on his anvil.  He does not seem to notice you.")
      # showBlacksmith()
    if userInput == "right":
      print("Adria the Witch has her nose in an old tome.  She does not seem to notice you.")
      # showWitch()
    if userInput == "forward":
      ChurchLvl1()
    if userInput == "backward":
      print("Thoughts of cowardice and retreat briefly cross your mind.  However you shake it off, determined to move forward towards the Church.")

def showWounded():
  directions = []
  print("You see a bloodied and wounded man laying along the path going towards the Church.")
  print("He reaches out to you... begging... \'Please... the ArchBishop Lazerus has betrayed us... he led us to a trap... a demon called the Butcher...\' and then he expires in front of you.")
  print("You look up from the dead man.  The Church is in front of you, an evil red glow emmanating from the entrance.")
  print(f'Level: {CharLvl}, XP: {ShowXP}%')
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/forward/backward")
    userInput = input()
    if userInput == "right":
      print("You see the Witch's hut in the distance.")
      print("I should continue moving forward.")
    if userInput == "left":
      print("Looking to the left you see some rocks and trees.  The town boundary merges into wilderness and caves quite quickly.")
      print("I should continue moving forward.")
    if userInput == "forward":
      ChurchLvl1()
      userInput = input()
    if userInput == "backward":
      TownSquare2()

def TownSquare1():
  directions = []
  print("You are in the Town Square.  You see an old man in front of you standing near a well.  He has just greeted you and introduced himself as Deckard Cain.")
  print("Deckard Cain informs you that only a few people remain in the town after dozens of folks have gone missing after entering the dark cathedral on the edge of town.")
  print("He indicates you need to move forward in order to head towards the Church.")
  print(f'Level: {CharLvl}, XP: {ShowXP}%')
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/forward")
    userInput = input()
    if userInput == "left":
      print("I should head towards the Church.")
    if userInput == "right":
      print("I should head towards the Church.")
    if userInput == "backward":
      print("Thoughts of cowardice and retreat briefly cross your mind.  However you shake it off, determined to move forward towards the Church.")
    if userInput == "forward":
      showWounded()

if __name__ == "__main__":
  while True:
    print("DIABLO RETROGRADED")
    print("Name your character (eight digits maximum): ")
    name = input()
    while len(name) >= int(9):
            print("Your Character name cannot be more than eight digits long.")
            print("Name your character (eight digits maximum): ")
            name = input()
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
    print("You have arrived in the town of Tristram within the region of Khanduras.")
    print("The town seems unassuming, besides the fact that it rests on the outskirts of the home and birthplace of King Leoric.")
    print("You hear screams coming from the Church that sits in the North West corner of Tristram.")
    print(f'Greetings, {name} the {myclass}. Stay awhile and listen...')
    print(f'Level: {CharLvl}, XP: {ShowXP}%')
    TownSquare1()

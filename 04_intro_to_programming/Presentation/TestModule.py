
def Warrior(myclass)
  Level = {
    'CharLvl = 1
  }
CharLvl = 1
CharExp = 0
LevelUp = 100

Stats = { 
  'Str': 30,
  'Mag': 10,
  'Dex': 20,
  'Vit': 25
}

def cLevelup
while CharExp >= LevelUp:
  CharLvl += 1
  CharExp = CharExp - LevelUp
  LevelUp = round(LevelUp * 1.5)
ShowXP = round(CharExp / LevelUp * 100)

print(f'Level: {CharLvl}, XP: {ShowXP}%')


print(f"STR: {SorStats['Str']} + {new_Str}",
	    f"MAG: {SorStats['Mag']} + {new_Mag}",
	    f"DEX: {SorStats['Dex']} + {new_Dex}",
      f"VIT: {SorStats['VIT']} + {new_Vit}")

print(f"STR: {RogStats['Str']} + {new_Str}",
	    f"MAG: {RogStats['Mag']} + {new_Mag}",
	    f"DEX: {RogStats['Dex']} + {new_Dex}",
      f"VIT: {RogStats['VIT']} + {new_Vit}")

print(f"STR: {WarStats['Str']} + {new_Str}",
	    f"MAG: {WarStats['Mag']} + {new_Mag}",
	    f"DEX: {WarStats['Dex']} + {new_Dex}",
      f"VIT: {WarStats['VIT']} + {new_Vit}")
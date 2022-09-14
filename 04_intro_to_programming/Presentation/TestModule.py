CharLvl = 1
CharExp = 0
LevelUp = 100

cStr = 0
cMag = 0
cDex = 0
cVit = 0

while CharExp >= LevelUp:
  CharLvl += 1
  CharExp = CharExp - LevelUp
  LevelUp = round(LevelUp * 1.5)
ShowXP = round(CharExp / LevelUp * 100)

print(f'Level: {CharLvl}, XP: {ShowXP}%')
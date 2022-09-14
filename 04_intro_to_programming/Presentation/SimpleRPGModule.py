# Full simple RPG module from 
# https://www.youtube.com/watch?v=FRWToxwgIjI
# https://www.youtube.com/watch?v=nBtcJdKAkgM - Battle system
# https://valtyrtriit.blogspot.com/2022/01/python-3-win-7-rpg-systems-simple-level_26.html
# need to translate into my own code

char  = {'lvl'     : 1,
	'xp'       : 0,
	'lvl_next' : 25,
	}
stats = {'str' 	   : 1,
	 'dex' 	   : 1,
	 'int' 	   : 1,
	}


def update_level(char, stats):
	new_str, new_dex, new_int = 0, 0, 0
	while char['xp'] >= char['lvl_next']:
		char['lvl'] 	 += 1
		char['xp']       = char['xp'] - char['lvl_next']
		char['lvl_next'] = round(char['lvl_next'] * 1.5)
		new_str          += 1
		new_dex 	 += 1
		new_int 	 += 1

	print(f"level: {char['lvl']}")

	# The assignment as  I gave it last lesson:
	print(f"STR {stats['str']} +{new_str}",
	      f"DEX {stats['str']} +{new_dex}",
	      f"INT {stats['int']} +{new_int}"
	     )

	stats['str'] += new_str
	stats['dex'] += new_dex
	stats['int'] += new_int


char['xp'] += 25
update_level(char, stats)

print('-----------')

char['xp'] += 200
update_level(char, stats)

print('-----------')

char['xp'] += 200
update_level(char, stats)

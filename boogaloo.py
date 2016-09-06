import sys, re

# my modules
import data, rom, fe8

# figure out which game we're trying to edit
ver  = "?"
GAME_FILE = open(sys.argv[1], 'rb+')
GAME_FILE.seek(0xAA)
gameCode = GAME_FILE.read(6).decode('UTF-8')
if gameCode == "E.AE7E" :
    ver = "FE7"
#    GAME_DATA = fe7.gameData
    print("Unsupported game version: FE7. Exiting...")
    exit(1)
elif gameCode == "2EBE8E":
    ver = "FE8"
#    GAME_DATA = fe8.gameData
elif gameCode == "6.AFEJ":
    ver = "FE6"
#    GAME_DATA = fe6.gameData
    print("Unsupported game version: FE7. Exiting...")
    exit(1)
else:
    print("Illegal game version! Please use one of the GBA ROMs.")
    exit(1)
print("Game detected as", ver)

############################
# parse data files
print("Setting up data...")

# I can't believe this works...
# It sets GAME_DATA to a different MODULE based on input.
GAME_DATA = fe8 if ver == "FE8" else (fe7 if ver == "FE7" else fe6)
CHAR_DATA = data.parseDataFile('chardata.csv')

############################
# GET BOOGALOO!
print("Beginning BOOGALOOFICATION")

averages = data.calculateAverages(CHAR_DATA)
charlist = data.getRandomCharacters(CHAR_DATA, ver)
replace = {}
for char in CHAR_DATA[ver]:
    replace[char] = charlist.pop()

data.rescaleStats(replace, averages, ver)
    
for char in replace.keys():
    oldChar = rom.getCharData(GAME_DATA, GAME_FILE, char)
    newstr = GAME_DATA.convertCharacter(None, replace[char])
    print (char, "->", replace[char]['name'])
    for stat in replace[char]:
        if stat in oldChar:
            # different stat insertion formula for base stats
            if re.search("-base", stat) != None:
                print (stat, ":", CHAR_DATA[ver][char][stat], "->", replace[char][stat])
                oldChar[stat] += (int(replace[char][stat]) - int(CHAR_DATA[ver][char][stat]))
            else:
                oldChar[stat] = int(replace[char][stat])
    rom.setCharData(GAME_DATA, GAME_FILE, char, oldChar)
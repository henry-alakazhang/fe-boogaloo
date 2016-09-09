import sys, re

# my modules
import data, rom, fe8

# figure out which game we're trying to edit
ver  = "?"
GAME_FILE = open(sys.argv[len(sys.argv) - 1], 'rb+')
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
rom.applyPatch(GAME_FILE, GAME_DATA.ANTIHUFFMAN)
print("Text table found at", hex(GAME_DATA.getTextTable(GAME_FILE)))

############################
# GET BOOGALOO!
print("Beginning BOOGALOOFICATION")

averages = data.calculateAverages(CHAR_DATA)
replace = data.getRandomCharacters(CHAR_DATA, ver)

data.rescaleStats(replace, averages, ver)
CLASS_DATA = {} # populated as needed from the game itself

#sys.stdout = open("boogalog.txt", 'w')
for char in replace.keys():
    oldChar = rom.getCharData(GAME_FILE, GAME_DATA, char)
    replace[char] = rom.convertCharacter(GAME_DATA, replace[char])
    print (char, "->", replace[char]['name'])
    for stat in replace[char]:
        if stat in oldChar:
            # different stat insertion formula for base stats
            if stat.endswith('base'):
#                print (stat, ":", CHAR_DATA[ver][char][stat], "->", replace[char][stat])
                # load class data from ROM and cache it in CLASS_DATA
                if (replace[char]['class name'] not in CLASS_DATA.keys()):
                    CLASS_DATA[replace[char]['class name']] = rom.getClassData(GAME_FILE, GAME_DATA, replace[char]['class name'])
                oldChar[stat] = int(replace[char][stat]) - CLASS_DATA[replace[char]['class name']][stat]
            else:
                oldChar[stat] = int(replace[char][stat])
        elif stat == 'items':
            for i in range(4):
#                print(oldChar['Item ' + str(i+1)], "->", replace[char]['items'][i])
                oldChar['Item ' + str(i+1)] = replace[char]['items'][i]
        else:
            oldChar[stat] = replace[char][stat]
    rom.setCharData(GAME_FILE, GAME_DATA, char, oldChar)
import sys, re

# my modules
import data

# my classes
from rom import Rom
from fe7 import FE7
from fe8 import FE8

if len(sys.argv) > 1:
    # load user input files
    if (len(sys.argv) > 2):
        replace_filename = sys.argv[2]
    filename = sys.argv[1]
else:
    print("Enter filename of your GBA ROM (or drag it into this window): ")
    # remove quotes from file
    filename = re.sub(r'"', '', sys.stdin.readline().strip());

print("Checking game file.... ", end = "")
# figure out which game we're trying to edit
ver  = "?"
GAME_FILE = open(filename, 'rb+')
GAME_FILE.seek(0xAA)
gameCode = GAME_FILE.read(6).decode('UTF-8')
if gameCode == "E\x00AE7E" :
    game = FE7(GAME_FILE)
elif gameCode == "2EBE8E":
    game = FE8(GAME_FILE)
elif gameCode == "6.AFEJ":
#    game = FE6(GAME_FILE)
    print("Unsupported game version: FE7. Exiting.")
    exit(1)
else:
    print()
    print("ERROR: Illegal game version! Please use one of the GBAFE games.")
    exit(1)
print ("Detected as", game.GAME_VERSION)
    
############################
# parse data files
print("Applying Anti-Huffman patch.")
game.applyPatch(game.ANTIHUFFMAN)
print("Text table found at", hex(game.getTextTable()))

print("Opening Outrealms portals... ")
CHAR_DATA = data.parseDataFile('chardata.csv')

############################
# GET BOOGALOO!
print("Beginning BOOGALOOFICATION!")

# get new characters
averages = data.calculateAverages(CHAR_DATA)
if replace_filename != None:
    replace = data.getSetCharacters(game, CHAR_DATA, replace_filename)
replace = data.getRandomCharacters(game, CHAR_DATA, replace)

data.rescaleStats(replace, averages, game.GAME_VERSION)
CLASS_DATA = {} # populated as needed from the game itself

#sys.stdout = open("boogalog.txt", 'w')
# insert characters over old ones

for char in replace.keys():
    oldChar = game.getCharData(char)
    replace[char] = game.convertCharacter(replace[char])
    print (char, "->", replace[char]['name'])
    for stat in replace[char]:
        if stat in oldChar:
            # different stat insertion formula for base stats
            if stat.endswith('base'):
#                print (stat, ":", CHAR_DATA[ver][char][stat], "->", replace[char][stat])
                # load class data from ROM and cache it in CLASS_DATA
                if (replace[char]['class name'] not in CLASS_DATA.keys()):
                    CLASS_DATA[replace[char]['class name']] = game.getClassData(replace[char]['class name'])
                oldChar[stat] = int(replace[char][stat]) - CLASS_DATA[replace[char]['class name']][stat]
            else:
                oldChar[stat] = int(replace[char][stat])
        elif stat == 'items':
            for i in range(4):
#                print(oldChar['Item ' + str(i+1)], "->", replace[char]['items'][i])
                oldChar['item ' + str(i+1)] = replace[char]['items'][i]
        else:
            oldChar[stat] = replace[char][stat]
    game.setCharData(char, oldChar)

print("Outrealms Boogaloo completed!")
input("Press ENTER to continue...")
GAME_FILE.close();
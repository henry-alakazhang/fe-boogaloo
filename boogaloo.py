import sys

# my modules
import generator

############################
# parse data files
print("Setting up data...")

data = generator.parseDataFile('chardata.csv')

# figure out which game we're trying to edit
ver  = "?"
FILE = open(sys.argv[1], 'rb+')
FILE.seek(0xAA)
gameCode = FILE.read(6).decode('UTF-8')
if gameCode == "E.AE7E" :
    ver = "FE7"
elif gameCode == "2EBE8E":
    ver = "FE8"
elif gameCode == "6.AFEJ":
    ver = "FE6"
else:
    print("Illegal game version! Please use one of the GBA ROMs.")
    exit(1)
print("Game detected as", ver, "... beginning BOOGALOOFICATION")

# GET BOOGALOO!
averages = generator.calculateAverages(data)
charlist = generator.getRandomCharacters(data, len(data[ver].keys()))
replace = {}
for char in data[ver]:
    replace[char] = charlist.pop()

for char in replace.keys():
    print(char, "->", replace[char]['name'], "(" + replace[char]['game'] + ")")
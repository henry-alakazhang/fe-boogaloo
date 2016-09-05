import statistics, csv, random, re

# returns a list of 'num' random characters
# from any game in the given data set
def getRandomCharacters(data, num = 10):
    chars = []
    allChars = []
    for game in data.keys():
        allChars += [data[game][char] for char in data[game]]
    
    # randomly assign characters from said list
    while (len(chars) < num):
        check = allChars.pop(random.randrange(len(allChars)))
        if legalCharacter(check):
            chars.append(check)
    return chars

# returns whether a character is legal to be boogaloo'd
# ideally this always returns true but atm there are some limits
# Illegal characters:
#  * Lords
#  * Hidden Weapon users from Fates (eg. Ninjas)
#  * Non-manakete shapeshifters
#  * FE7: Manaketes as well
    
def legalCharacter(character):
    if re.search(r'Ninja|Maid|Butler|Mechanist', character['class']):
        print(character['name'], "is illegal! because they're a waifu panderer")
        return False
    elif re.search("Lord", character['class']):
        # ike doesn't start with the rapier he usually does in fire emblem games so he's ok
        print(character['name'], "is illegal! because they're a lord")
        return False
    elif re.search("tribe|Hawk|Raven|Heron|Cat|Tiger|Dragon|Wolf|Kitsune", character['class']):
        print(character['name'], "is illegal! because they're a filthy subhuman")
        return False
    return True
    
# calculates a dict of average bases/growths from the given data set
# uses the median as the average stat
def calculateAverages(data):
    avgs = {}
    for game in data.keys():
        avgs[game] = { "HP-base": 0, "STR-base": 0, "SKL-base": 0, "SPD-base": 0, "LUK-base": 0, "DEF-base": 0, "RES-base": 0, \
             "HP-grow": 0, "STR-grow": 0, "SKL-grow": 0, "SPD-grow": 0, "LUK-grow": 0, "DEF-grow": 0, "RES-grow": 0}
        for stat in avgs[game].keys():
            # build a list of all the values of a stat for a given game
            statList = [data[game][c][stat] for c in data[game]]
            # then get the median
            avgs[game][stat] = statistics.median(map(int, statList))
    return avgs
    
# parses the data file into a useful format
def parseDataFile(filename):
    data = {
        'FE1' : {}, 'FE3' : {}, 'FE4' : {}, 'FE5' : {}, 'FE6' : {}, 'FE7' : {}, 'FE8' : {}, 'FE9' : {}, 'FE10' : {}, 'FE13' : {}
    }

    heads = ["game", "name", "class", "level", "HP-base", "STR-base", "SKL-base", "SPD-base", "LUK-base", "DEF-base", "RES-base", \
    "HP-grow", "STR-grow", "SKL-grow", "SPD-grow", "LUK-grow", "DEF-grow", "RES-grow"]

    charfile = open(filename, newline='')
    charreader = csv.DictReader(charfile, heads, "items")
    for line in charreader:
        data[line['game']][line['name']] = line
    
    return data
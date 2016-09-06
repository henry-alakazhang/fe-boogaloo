import statistics, csv, random, re
import fe8

# returns a list of 'num' random characters
# to replace characters in the given game
def getRandomCharacters(data, ver):
    # create a list of all characters
    allChars = []
    for game in data.keys():
        allChars += [data[game][char] for char in data[game]]
    
    # randomly assign characters from said list
    chars = []
    while (len(chars) < len(data[ver].keys())):
        check = allChars.pop(random.randrange(len(allChars)))
        # check if legal before adding
        if legalCharacter(check, ver):
            chars.append(check)
    return chars

# returns whether a character is legal to be boogaloo'd
# ideally this always returns true but atm there are some limits
# mostly nonexistent classes with no equivalent
# eg.
#   * Non-dragon shapeshifters (eg. Laguz, Taguel)
#   * Lords
#   * Non-Lance Armour Knights and Axe Cavaliers
#   * Axe Wyverns
def legalCharacter(character, ver):
    '''
    if ver == "FE6":
        if not fe6.legalCharacter(character):
            return False
    if ver == "FE7":
        if not fe7.legalCharacter(characer):
            return False
    '''
    if ver == "FE8":
        if not fe8.legalCharacter(character):
            return False
    return True
    
# calculates a dict of average bases/growths from the given data set
# uses the median as the average stat
def calculateAverages(data):
    avgs = {}
    for game in data.keys():
        # atm don't bother with bases
        avgs[game] = { #"HP-base": 0, "STR-base": 0, "SKL-base": 0, "SPD-base": 0, "LUK-base": 0, "DEF-base": 0, "RES-base": 0, \
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
    "HP-grow", "STR-grow", "SKL-grow", "SPD-grow", "LUK-grow", "DEF-grow", "RES-grow",
    "Sword", "Axe", "Lance", "Bow", "Staff", "Anima", "Light", "Dark"]

    charfile = open(filename, newline='')
    charreader = csv.DictReader(charfile, heads, "items")
    for line in charreader:
        data[line['game']][line['name']] = line
        if line['name'] == "Beruka":
            print(line)
    charfile.close()
    
    return data

# rescale the stats in the char list to fit in the new game
# uses averages of the character's home game and the new game
def rescaleStats(chars, averages, ver):
    goal = averages[ver]
    for c in chars:
        gameAvgs = averages[chars[c]['game']]
        for stat in gameAvgs:
            chars[c][stat] = int(chars[c][stat])
            if gameAvgs[stat] == 0:
                gameAvgs[stat] = chars[c][stat] if chars[c][stat] != 0 else 1
            chars[c][stat] = int(chars[c][stat] * (goal[stat] / gameAvgs[stat]))
    return chars
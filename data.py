# module for doing all the mathy stuff
# like calculating average stats, rescaling based on averages and such

import statistics, csv, random, re

# reads replacement wants from a file
def getSetCharacters(game, data, file):
    replaceFile = open(file, 'r')
    
    chars = {}
    for old in game.CHAR_TO_HEX.keys():
        chars[old] = None
    
    for line in replaceFile:
        words = line.strip().split(',')
        old = words[0].strip()
        newGame = words[1].split(' ')[0].strip()
        newChar = words[1].split(' ')[1].strip()
        try:
            if old not in chars:
                print("Replacement", old + ",", newGame, newChar, "impossible:", old, "isn't in", game.GAME_VERSION)
            elif not game.legalCharacter(data[newGame][newChar]):
                print("Replacement", old + ",", newGame, newChar, "impossible:", newGame, newChar, "cannot be inserted into", game.GAME_VERSION + "")
            else:
                chars[old] = data[newGame][newChar]
        except:
            print("Replacement", old + ",", newGame, newChar, "impossible:", newGame, newChar, "doesn't exist")
    replaceFile.close();
    
    return chars

# returns a mapping of random characters
# to replace characters in the given game
def getRandomCharacters(game, data, chars):
    # create a list of all characters
    allChars = []
    for g in data.keys():
        allChars += [data[g][char] for char in data[g]]
    
    # randomly assign characters from said list
    for old in game.CHAR_TO_HEX.keys():
        while chars[old] == None:
            check = random.randrange(len(allChars))
            # check if legal before adding
            if not game.legalCharacter(allChars[check]):
                continue
            
            # check the stats are "kind of" close so they don't instantly break the game
            if not statDiffsOk(data[game.GAME_VERSION][old], allChars[check]):
                continue
            chars[old] = allChars[check]
            allChars.pop(check)
    return chars

def statDiffsOk(char1, char2):
    diffs = { 'rel' : {}, 'abs' : {} }
    # get stat differentials
    for stat in char1:
        if stat.endswith("base") and not stat.startswith("HP") and not stat.startswith("LUK"):
            s1 = int(char1[stat])
            s2 = int(char2[stat])
            diffs['rel'][stat] = (s1/s2 if (s2 != 0) else s1)
            diffs['abs'][stat] = s1 - s2

    # don't replace unpromoted units with prepromotes (feels bad man)
    if abs(int(char1['level']) - int(char2['level'])) > 20:
        return False
    
    # if in general too different 
    if abs(sum(diffs['abs'].values())) > 5 and abs(1-statistics.mean(diffs['rel'].values())) > 0.2:
        return False
    
    # if absolutely too much better (avg. 2+ per combat stat)
    # or just crazy better in a single stat
    if abs(sum(diffs['abs'].values())) > 10 or abs(max(diffs['abs'].values())) > 10:
        return False
        
    # if most stats are more than double
    if abs(1-statistics.mean(diffs['rel'].values())) > 1:
        return False
        
    return True
    
# calculates a dict of average bases/growths from the given data set
# uses the median as the average stat
def calculateAverages(data):
    avgs = {}
    for game in data.keys():
        # atm don't bother with bases (or LUK)
        avgs[game] = { #"HP-base": 0, "STR-base": 0, "SKL-base": 0, "SPD-base": 0, "LUK-base": 0, "DEF-base": 0, "RES-base": 0,
             "HP-grow": 0, "STR-grow": 0, "SKL-grow": 0, "SPD-grow": 0, #"LUK-grow": 0, 
             "DEF-grow": 0, "RES-grow": 0}
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
    "sword", "lance", "axe", "bow", "staff", "anima", "light", "dark"]

    charfile = open(filename, newline='')
    charreader = csv.DictReader(charfile, heads, "items")
    for line in charreader:
        data[line['game']][line['name']] = line
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
            print(chars[c]['name'], "Stat", stat + ":", chars[c][stat], "->", int(chars[c][stat] * (goal[stat] / gameAvgs[stat])))
            chars[c][stat] = int(chars[c][stat] * (goal[stat] / gameAvgs[stat]))
    return chars
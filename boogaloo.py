import sys, csv, random, statistics

# returns a list of 'num' random characters
# from any of the games
def getRandomCharacters(num = 10):
    chars = []
    # get every character
    for game in data.keys():
        for char in data[game].keys():
            chars.append(char)
    # randomly delete them
    while (len(chars) > num):
        del chars[random.randrange(len(chars))]
    return chars
    
def calculateAverages():
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
    
            
############################
# parse data files
data = {
    'FE1' : {}, 'FE3' : {}, 'FE4' : {}, 'FE5' : {}, 'FE6' : {}, 'FE7' : {}, 'FE8' : {}, 'FE9' : {}, 'FE10' : {}, 'FE13' : {}
}

heads = ["game", "name", "class", "level", "HP-base", "STR-base", "SKL-base", "SPD-base", "LUK-base", "DEF-base", "RES-base", \
"HP-grow", "STR-grow", "SKL-grow", "SPD-grow", "LUK-grow", "DEF-grow", "RES-grow"]

charfile = open('chardata.csv', newline='')
charreader = csv.DictReader(charfile, heads, "items")
for line in charreader:
    data[line['game']][line['name']] = line
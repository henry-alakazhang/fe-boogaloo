# module for reading and writing data to a rom
# i should have made this a class and attached the file to this...

import codecs, struct, re

CHAR_FORMAT = [
    "Name_HI", "Name_LO", "Desc", "Char #", "Standing Class", "Portrait", "X1", "Mini", "Affinity", "X2",
    "LevelN", "HP-base", "STR-base", "SKL-base", "SPD-base", "DEF-base", "RES-base", "LUK-base",
    "CON-base", "Sword", "Lance", "Axe", "Bow", "Staff", "Anima", "Light", "Dark",
    "HP-grow", "STR-grow", "SKL-grow", "SPD-grow", "DEF-grow", "RES-grow", "LUK-grow"
]

CHAR_UNIT_FORMAT = [
    "Char", "class", "X1", "Levels", "X", "Y", "X2", "X3", "Ref1", "Ref2", "Ref3", "Ref4",
    "Item 1", "Item 2", "Item 3", "Item 4"
]

CLASS_FORMAT = [
    "Name_HI", "Name_LO", "Desc_HI", "Desc_LO", "C No", "Promo", "Sprite", "Walk", "Portrait", "X1", "X2",
    "HP-base", "STR-base", "SKL-base", "SPD-base", "DEF-base", "RES-base", "CON-base"
]

def getCharData(ver, file, name):
    charData = {}
    # load character stats
    file.seek(ver.getCharacterAddress(name))
    for s in CHAR_FORMAT:
        if re.search('base', s) != None:
            charData[s] = int.from_bytes(file.read(1), byteorder='little', signed=True)
        else:
            charData[s] = int.from_bytes(file.read(1), byteorder='little', signed=False)
    
    # load unit stats (ie. first load of character)
    file.seek(ver.getCharacterUnitAddress(name)[0])
    for s in CHAR_UNIT_FORMAT:
        charData[s] = int.from_bytes(file.read(1), byteorder='little', signed=False)
    return charData
    
def setCharData(ver, file, name, new):
    # store characer stats
    file.seek(ver.getCharacterAddress(name))
    for s in CHAR_FORMAT:
        # only bases can be signed...
        if re.search('base', s) != None:
            file.write(new[s].to_bytes(1, byteorder='little', signed=True))
        else:
            file.write(new[s].to_bytes(1, byteorder='little', signed=False))
            
    # store character unit data
    # TODO: be smart about where to load the character - each character should only need max 2
    for possibleSpot in ver.getCharacterUnitAddress(name):
        file.seek(possibleSpot)
        for s in CHAR_UNIT_FORMAT:
            # don't overwrite coordinates or chapters get fucky
            if s.startswith("Item") or s == "class":
                file.write(new[s].to_bytes(1, byteorder='little', signed=False))
            else:
                file.seek(1, 1)
                
def getClassData(ver, file, name):
    classData = {}
    file.seek(ver.getClassAddress(name))
    for s in CLASS_FORMAT:
        if re.search('base', s) != None:
            classData[s] = int.from_bytes(file.read(1), byteorder='little', signed=True)
        else:
            classData[s] = int.from_bytes(file.read(1), byteorder='little', signed=False)
    classData['LUK-base'] = 0
    return classData
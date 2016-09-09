# module for reading and writing data to a rom
# i should have made this a class and attached the file to this...

import codecs, struct, re

# can i just say, why the hell does the nightmare module have an arbitrarily SKIPPED
# byte instead of just calling it UNKNOWN like everything else that's UNKNOWN?
# #salty
CHAR_FORMAT = [
    "Name_LO", "Name_HI", "Desc", "SKIPPED", "Char #", "class", "Portrait", "X1", "Mini", "Affinity", "X2",
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

def readBytes(file, len, ptr, sign=False):
    file.seek(ptr)
    return int.from_bytes(file.read(len), byteorder='little', signed=sign);
    
def writeBytes(file, words, len, ptr, sign=False):
    file.seek(ptr)
    file.write(words.to_bytes(len, byteorder='little', signed=sign));

def writeTextToROM(file, ver, index, string):
    # get location of text pointer table
    tablePtr = ver.getTextTable(file)
    tablePtr += (index[0] * 0x100 + index[1])*4
    
#    print("Name", string, "being written to", hex(index[0]), hex(index[1]))
    
    # append text to end of ROM
    file.seek(0, 2)
    newPtr = file.tell() + 0x88000000
    string += "\0"
    # add padding bytes
    while len(string) % 4 != 0:
        string += "\0"
    file.write(string.encode('UTF-8'));
    
    # update text pointer table
    writeBytes(file, newPtr, 4, tablePtr)

# applies a dict patch with {ptr : byte} mappings    
def applyPatch(file, patch):
    for addr in patch:
        writeBytes(file, patch[addr], 1, addr)
    
def getCharData(file, ver, name):
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
    
def setCharData(file, ver, name, new):
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
    writeTextToROM(file, ver, [new['Name_HI'], new['Name_LO']], new['name'])
    
                
def getClassData(file, ver, name):
    classData = {}
    file.seek(ver.getClassAddress(name))
    for s in CLASS_FORMAT:
        if re.search('base', s) != None:
            classData[s] = int.from_bytes(file.read(1), byteorder='little', signed=True)
        else:
            classData[s] = int.from_bytes(file.read(1), byteorder='little', signed=False)
    classData['LUK-base'] = 0
    return classData
    
def convertCharacter(game, oldChar):
    newChar = {}
    for key in oldChar:
        if (key == 'class'):
            newChar['class name'] = oldChar[key]
            newChar[key] = game.getHexFromClass(oldChar[key])
        elif (key == 'character'):
            newChar[key] = game.getHexFromChar(oldChar[key])
        elif (key == "items"):
            newChar[key] = []
            for i in range(4):
                newName = game.getHexFromItem(oldChar[key][i])
                if newName != None:
                    newChar[key].append(newName)
            # fill in remaining item slots to avoid out of bounds
            while (len(newChar[key]) < 4):
                newChar[key].append(0)
        elif key in game.WEAPON_TYPES:
            newChar[key] = game.getHexFromWeaponRank(oldChar[key])
        else:
            newChar[key] = oldChar[key]
    return newChar
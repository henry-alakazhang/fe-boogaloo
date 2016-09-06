import codecs, struct, re

CHAR_FORMAT = [
    "Name_HI", "Name_LO", "Desc", "Char #", "Class", "Portrait", "X1", "Mini", "Affinity", "X2", \
    "Level", "HP-base", "STR-base", "SKL-base", "SPD-base", "DEF-base", "RES-base", "LUK-base", \
    "CON-base", "Sword", "Lance", "Axe", "Bow", "Staff", "Anima", "Light", "Dark", \
    "HP-grow", "STR-grow", "SKL-grow", "SPD-grow", "DEF-grow", "RES-grow", "LUK-grow"
]
    
def getCharData(ver, file, name):
    charData = {}
    index = ver.getCharacterAddress(name)
    if index == None:
        return None
    file.seek(index)
    for s in CHAR_FORMAT:
        if re.search('base', s) != None:
            charData[s] = int.from_bytes(file.read(1), byteorder='little', signed=True)
        else:
            charData[s] = int.from_bytes(file.read(1), byteorder='little')
    return charData
    
def setCharData(ver, file, name, new):
    index = ver.getCharacterAddress(name)
    if index == None:
        return None
    file.seek(index)
    for s in CHAR_FORMAT:
        # only bases can be signed...
        if re.search('base', s) != None:
            file.write(new[s].to_bytes(1, byteorder='little', signed=True))
        else:
            file.write(new[s].to_bytes(1, byteorder='little', signed=False))
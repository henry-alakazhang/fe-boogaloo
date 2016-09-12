# class for reading and writing data to the ROM, as well as holding ROM attributes
# not used by itself; inherited by FE* classes
import codecs, struct, re

class Rom(object):
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
    
    def __init__(self, file):
        self.file = file

    def readBytes(self, len, ptr, sign=False):
        self.file.seek(ptr)
        return int.from_bytes(self.file.read(len), byteorder='little', signed=sign);
        
    def writeBytes(self, words, len, ptr, sign=False):
        self.file.seek(ptr)
        self.file.write(words.to_bytes(len, byteorder='little', signed=sign));

    def writeTextToROM(self, index, string):
        # get location of text pointer table
        tablePtr = self.getTextTable()
        tablePtr += (index[0] * 0x100 + index[1])*4
        
    #    print("Name", string, "being written to", hex(index[0]), hex(index[1]))
        
        # append text to end of ROM
        self.file.seek(0, 2)
        newPtr = self.file.tell() + 0x88000000
        string += "\0"
        # add padding bytes
        while len(string) % 4 != 0:
            string += "\0"
        self.file.write(string.encode('UTF-8'));
        
        # update text pointer table
        self.writeBytes(newPtr, 4, tablePtr)

    # applies a dict patch with {ptr : byte} mappings    
    def applyPatch(self, patch):
        for addr in patch:
            self.writeBytes(patch[addr], 1, addr)
        
    def getCharData(self, name):
        charData = {}
        # load character stats
        self.file.seek(self.getCharacterAddress(name))
        for s in Rom.CHAR_FORMAT:
            if re.search('base', s) != None:
                charData[s] = int.from_bytes(self.file.read(1), byteorder='little', signed=True)
            else:
                charData[s] = int.from_bytes(self.file.read(1), byteorder='little', signed=False)
        
        # load unit stats (ie. first load of character)
        self.file.seek(self.getCharacterUnitAddress(name)[0])
        for s in Rom.CHAR_UNIT_FORMAT:
            charData[s] = int.from_bytes(self.file.read(1), byteorder='little', signed=False)
        return charData
        
    def setCharData(self, name, new):
        # store characer stats
        self.file.seek(self.getCharacterAddress(name))
        for s in Rom.CHAR_FORMAT:
            # only bases can be signed...
            if re.search('base', s) != None:
                self.file.write(new[s].to_bytes(1, byteorder='little', signed=True))
            else:
                self.file.write(new[s].to_bytes(1, byteorder='little', signed=False))
                
        # store character unit data
        # TODO: be smart about where to load the character - each character should only need max 2
        for possibleSpot in self.getCharacterUnitAddress(name):
            self.file.seek(possibleSpot)
            for s in Rom.CHAR_UNIT_FORMAT:
                # don't overwrite coordinates or chapters get fucky
                if s.startswith("Item") or s == "class":
                    self.file.write(new[s].to_bytes(1, byteorder='little', signed=False))
                else:
                    self.file.seek(1, 1)
        self.writeTextToROM([new['Name_HI'], new['Name_LO']], new['name'])
        
                    
    def getClassData(self, name):
        classData = {}
        self.file.seek(self.getClassAddress(name))
        for s in Rom.CLASS_FORMAT:
            if re.search('base', s) != None:
                classData[s] = int.from_bytes(self.file.read(1), byteorder='little', signed=True)
            else:
                classData[s] = int.from_bytes(self.file.read(1), byteorder='little', signed=False)
        classData['LUK-base'] = 0
        return classData
        
    def convertCharacter(self, oldChar):
        newChar = {}
        for key in oldChar:
            if (key == 'class'):
                newChar['class name'] = oldChar[key]
                newChar[key] = self.getHexFromClass(oldChar[key])
            elif (key == 'character'):
                newChar[key] = self.getHexFromChar(oldChar[key])
            elif (key == "items"):
                newChar[key] = []
                for i in range(4):
                    newName = self.getHexFromItem(oldChar[key][i])
                    if newName != None:
                        newChar[key].append(newName)
                # fill in remaining item slots to avoid out of bounds
                while (len(newChar[key]) < 4):
                    newChar[key].append(0)
            elif key in self.WEAPON_TYPES:
                newChar[key] = self.getHexFromWeaponRank(oldChar[key])
            else:
                newChar[key] = oldChar[key]
        return newChar
        
    ## individual ROM characteristic functions ##
    
    # dynamically load text table address
    def getTextTable(self):
        try:
            return self.TEXT_TABLE
        except:
            self.file.seek(self.TEXT_TABLE_INDIRECT)
            self.TEXT_TABLE = int.from_bytes(self.file.read(4), byteorder='little', signed=False) - 0x8000000 
            return self.TEXT_TABLE
            
    def getHexFromChar(self, name):
        try:
            return self.CHAR_TO_HEX[name]
        except:
            return None

    def getCharacterAddress(self, name):
        try:
            return self.CHAR_TABLE + self.getHexFromChar(name) * self.CHAR_ENTRY_LENGTH
        except:
            return None
            
    def getCharacterUnitAddress(self, name):
        try:
            return self.CHAR_TO_UNIT_TABLE[name]
        except:
            return None

    def getHexFromClass(self, name):
        try:
            if name in self.CLASS_TO_CLASS:
                return self.CLASS_TO_HEX[self.CLASS_TO_CLASS[name]]
            return self.CLASS_TO_HEX[name]
        except:
            return None
            
    def getClassAddress(self, name):
        try:
            return self.CLASS_TABLE + self.getHexFromClass(name) * self.CLASS_ENTRY_LENGTH
        except:
            return None
        

    def getHexFromItem(self, name):
        try:
            if name in self.ITEM_TO_ITEM:
#                print("Item", name, "changed to", self.ITEM_TO_ITEM[name])
                return self.ITEM_TO_HEX[self.ITEM_TO_ITEM[name]]
            return self.ITEM_TO_HEX[name]
        except:
#            print("Illegal item", name, "removed")
            return None

    def getHexFromWeaponRank(self, rank):
        try:
            return self.WR_TO_HEX[rank]
        except:
            return None
            
    # returns whether a character is legal to be boogaloo'd
    # ideally this always returns true but atm there are some limits
    # mostly nonexistent classes with no equivalent
    # eg.
    #   * Non-dragon shapeshifters (eg. Laguz, Taguel)
    #   * Lords
    #   * Non-Lance Armour Knights and Axe Cavaliers
    #   * Axe Wyverns
    def legalCharacter(self, char):
        return self.getHexFromClass(char['class']) != None
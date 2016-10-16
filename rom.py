import codecs, struct, re

# class for reading and writing data to the ROM, as well as holding ROM attributes
# not used by itself; inherited by FE* classes
class Rom(object):
    '''
    all the member variables a (GBA) rom needs to have
    GAME_VERSION        name of game version (eg. "FE8")
    CHAR_TABLE          address of start of character data table
    CHAR_ENTRY_LENGTH   length of a character data entry
    CHAR_UNIT_LENGTH    length of a character entry in the chapter unit list
    CLASS_TABLE         address of start of class data table
    CLASS_ENTRY_LENGTH  length of a character data entry
    TEXT_TABLE_INDIRECT address of a pointer to the start of the text table
    GENERIC_MINI        index of Good Guys generic mini portrait
    CHAR_TO_HEX         mapping of character names to hex values
    CHAR_UNIT_FORMAT    array of format of character units in chapter unit lists
    CHAR_TO_UNIT_TABLE  mapping of character names to unit list entry addresses
    CLASS_TO_HEX        mapping of class names to hex values
    CLASS_TO_CLASS      mapping of non-game class names to in-game class names
    ITEM_TO_HEX         mapping of item names to hex values
    ITEM_TO_ITEM        mapping of non-game item names to in-game item names
    WR_TO_HEX           mapping of weapon rank text to hex values
    WEAPON_TYPES        array of weapon types
    ANTIHUFFMAN         dict-form patch (ie. address : byte mappings) for an antihuffman patch
    '''

    # can i just say, why the hell does the nightmare module have an arbitrarily SKIPPED byte
    # especially when that's supposed to be desc_HI but it's just always 0x00
    # in fact it actually limits you when you're hacking if you wanna change the index??
    # #salty
    CHAR_FORMAT = [
        "name_LO", "name_HI", "desc_LO", "desc_HI", "num", "class", "portrait", "X1", "mini", "affinity", "X2",
        "level", "HP-base", "STR-base", "SKL-base", "SPD-base", "DEF-base", "RES-base", "LUK-base",
        "CON-base", "sword", "lance", "axe", "bow", "staff", "anima", "light", "dark",
        "HP-grow", "STR-grow", "SKL-grow", "SPD-grow", "DEF-grow", "RES-grow", "LUK-grow"
    ]

    # also speaking of nightmare modules why are some of these things out of order? like especially unknowns
    CLASS_FORMAT = [
        "name_LO", "name_HI", "desc_LO", "desc_HI", "cnum", "promo", "sprite", "walk", "portrait", "X1", "X2",
        "HP-base", "STR-base", "SKL-base", "SPD-base", "DEF-base", "RES-base", "CON-base"
    ]
    
    GAME_TO_CONTINENT = {
        'FE1' : 'Archanaea',
        'FE3' : 'Archanaea',
        'FE4' : 'Jugdral',
        'FE5' : 'Jugdral',
        'FE6' : 'Elibe',
        'FE7' : 'Elibe',
        'FE8' : 'Magvel',
        'FE9' : 'Tellius',
        'FE10' : 'Tellius',
        'FE12' : 'Archanea',
        'FE13' : 'Fates?'
    }
    
    def __init__(self, file):
        self.file = file
    
    '''
    ## general-use file functions ##
    '''
    
    # reads (len) bytes from the address at (ptr) from the ROM file
    def readBytes(self, len, ptr, sign=False):
        self.file.seek(ptr)
        return int.from_bytes(self.file.read(len), byteorder='little', signed=sign);
        
    # writes (words) bytes with (len) to the address at (ptr) in the ROM
    # have to take 'len' because sizeof() is questionable in Python
    def writeBytes(self, words, len, ptr, sign=False):
        self.file.seek(ptr)
        self.file.write(words.to_bytes(len, byteorder='little', signed=sign));

    # replaces the text at (index) with (string)
    # please make sure the index is actually in the ROM. undefined behaviour otherwise.
    def writeTextToROM(self, index, string):
        # get location of text pointer table
        tablePtr = self.getTextTable()
        tablePtr += (index[0] * 0x100 + index[1])*4
        
#        print(string, "being written to", hex(index[0]), hex(index[1]))
        
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
    
    # loads character data of (name) into a dict with keys in CHAR_FORMAT + CHAR_UNIT_FORMAT
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
        for s in self.CHAR_UNIT_FORMAT:
            charData[s] = int.from_bytes(self.file.read(1), byteorder='little', signed=False)

        return charData
        
    # sets character data of (name) with (new)
    # (new) is expected to be the same format as getCharData
    def setCharData(self, name, new):
        # store characer stats
        self.file.seek(self.getCharacterAddress(name))
        
        new['X1'] = 0
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
            for s in self.CHAR_UNIT_FORMAT:
                # don't overwrite coordinates or chapters get fucky
                if s.startswith("item") or s == "class":
                    self.file.write(new[s].to_bytes(1, byteorder='little', signed=False))
                else:
                    self.file.seek(1, 1)
        self.writeTextToROM([new['name_HI'], new['name_LO']], new['name'])
        self.writeTextToROM([new['desc_HI'], new['desc_LO']], \
           "A mysterious hero from the \1faraway land of " + Rom.GAME_TO_CONTINENT[new['game']] + ".")
        
    # returns data of class (name) as a dict with keys CLASS_FORMAT
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
        
    # returns a new character of (oldChar)'s format, but with names replaced by game-specific values.
    def convertCharacter(self, oldChar):
        newChar = {}
        for key in oldChar:
            if key == 'class':
                newChar['class name'] = oldChar[key]
                newChar[key] = self.getHexFromClass(oldChar[key])
            elif key == 'character':
                newChar[key] = self.getHexFromChar(oldChar[key])
            elif key == "items":
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
    
    '''
    ## individual ROM characteristic functions ##
    '''
    
    # returns whether a character is legal to be boogaloo'd
    # ideally this always returns true but atm there are some limits
    # mostly nonexistent classes with no equivalent
    # eg.
    #   * Beast shapeshifters (eg. Laguz, Taguel)
    #       * Compatible with FE8 as Hellhounds/Cerberus
    #   * Bird shapeshifters (eg. Ravens)
    #       * Herons are dancers
    #   * Lords with unsupported weapons
    #       * OK if they use the Rapier that chrom starts with in every fire embull game
    #   * GBA classes with weird weapons (eg. Axe Knight/Cav/Wyvern, Sword Peg)
    #       * I mean these are technically possible, I just need to fix chardata.csv
    
    def legalCharacter(self, char):
        return self.getHexFromClass(char['class']) != None
    
    '''    
    # dynamically loads in tables from the rom itself
    # only useful for hacks, but it's useless without dynamic unit pointer loading as well.
    # so it's not enabled yet
    def dynamicLoadTables(self):
        self.TEXT_TABLE = readBytes(4, TEXT_TABLE_INDIRECT) - 0x8000000
        self.CHAR_TABLE = readBytes(4, CHAR_TABLE_INDIRECT) - 0x8000000
        self.CLASS_TABLE = readBytes(4, CLASS_TABLE_INDIRECT) - 0x8000000
    '''    

    def getTextTable(self):
        try:
            return self.TEXT_TABLE        
        except:
            self.TEXT_TABLE = self.readBytes(4, TEXT_TABLE_INDIRECT) - 0x8000000
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
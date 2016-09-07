# module for fe8's data
# i probably should have made GAMES a class and instantiated fe8 as one

CHAR_TABLE = 0x803D30
CHAR_ENTRY_LENGTH = 0x34
CHAR_UNIT_LENGTH = 20

CLASS_TABLE = 0x807110
CLASS_ENTRY_LENGTH = 84

CHAR_TO_HEX = {
    'Eirika' : 0x01, 
    'Seth' : 0x02, 
    'Gilliam' : 0x03, 
    'Franz' : 0x04, 
    'Moulder' : 0x05, 
    'Vanessa' : 0x06, 
    'Ross' : 0x07, 
    'Neimi' : 0x08, 
    'Colm' : 0x09, 
    'Garcia' : 0x0A, 
    'Innes' : 0x0B, 
    'Lute' : 0x0C, 
    'Natasha' : 0x0D, 
    'Cormag' : 0x0E, 
    'Ephraim' : 0x0F, 
    'Forde' : 0x10, 
    'Kyle' : 0x11, 
    'Amelia' : 0x12, 
    'Artur' : 0x13, 
    'Gerik' : 0x14, 
    'Tethys' : 0x15, 
    'Marisa' : 0x16, 
    'Saleh' : 0x17, 
    'Ewan' : 0x18, 
    'L\'Arachel' : 0x19, 
    'Dozla' : 0x1A, 
    'Rennac' : 0x1C, 
    'Duessel' : 0x1D, 
    'Myrrh' : 0x1E, 
    'Knoll' : 0x1F, 
    'Joshua' : 0x20, 
    'Syrene' : 0x21, 
    'Tana' : 0x22
}

# i generated this with a script and i can't be bothered reformatting it
CHAR_TO_UNIT_TABLE = {'Forde': [9164480, 9165660, 9133736, 9133968, 9132664, 9139724, 9245368], 'Knoll': [9202472, 9202652, 9200708, 9161428, 9244888], 'Franz': [9125756, 9126268, 9148644, 9153020, 9164520, 9165700, 9126644, 9127384, 9131668, 9135124, 9137944,9139044, 9143248, 9141380, 9184044, 9125284, 9245128], 'Joshua': [9159972, 9157584, 9216652, 9132308, 9245668], 'Garcia': [9148704, 9156980, 9126984, 9127444, 9135224, 9137864, 9139084, 9245248], 'Ephraim': [9190780, 9186388, 9190992, 9193144, 9195188, 9201848, 9202152, 9202872, 9199548, 9161448, 9203220, 9164360, 9165400, 9165560, 9165860, 9162348, 9205320, 9168104, 9206940, 9171060, 9210584, 9178080, 9177356, 9215152, 9178504, 9217616, 9133716, 9133948, 9132644, 9139704, 9183944, 9181232, 9220192, 9183044, 9125324, 9244528, 9247828, 9248076], 'Innes': [9144716, 9150288, 9148664, 9152012, 9157100, 9154440, 9159564, 9159952, 9159184, 9204440, 9164460, 9163908, 9166504, 9207020, 9171840, 9211464, 9178140, 9177396, 9216672, 9180844, 9219876, 9182712, 9221712, 9244568, 9247688], 'Tethys': [9144756, 9150004, 9150972, 9196168, 9245468], 'Eirika': [9125776, 9124904, 9126048, 9143616, 9150308, 9148564, 9150832, 9157060, 9152840, 9159504, 9159892, 9157544, 9160208, 9204420, 9164380, 9165420, 9165580, 9165880, 9162328, 9205340, 9166424, 9170920, 9210724, 9178100, 9175696,9216612, 9126604, 9178484, 9217596, 9127284, 9128196, 9131568, 9135064, 9137784, 9138444, 9138944, 9143188, 9141260, 9181212, 9220212, 9183064, 9125164, 9244508, 9247808, 9248056], 'Ross': [9126964, 9127324, 9128356, 9135204, 9139064, 9245188], 'Gerik': [9144736, 9148764, 9196188, 9245448], 'Dozla': [9188328, 9149664, 9191452, 9157744, 9129216, 9142720, 9245568], 'Rennac': [9188348, 9158544, 9200748, 9129196, 9142740, 9245588], 'Artur': [9148684, 9128216, 9131728, 9137964, 9139104, 9245428], 'Amelia': [9154320, 9201968, 9142520, 9184944, 9245408], 'Lute': [9128956, 9245288], 'Cormag': [9187408, 9154260, 9201948, 9201468, 9132448, 9244628], 'Gilliam': [9126288, 9148624, 9126664, 9127364, 9128296, 9131648, 9135104, 9137804, 9139024, 9143228, 9125244, 9244548, 9247668], 'Vanessa': [9148604, 9166464, 9206980, 9126864, 9127344, 9128276, 9131628, 9135164, 9137924, 9139004, 9143308, 9125224, 9245168, 9247748], "L'Arachel": [9188308, 9150248, 9149644, 9191472, 9152032, 9157120, 9154420, 9196488, 9159544, 9159932, 9157564, 9199648, 9164440, 9163888, 9168124, 9171860, 9211484, 9178000, 9177316, 9216592, 9180864, 9219896, 9129176, 9142700, 9182732, 9221732, 9183104, 9245548], 'Duessel': [9187248, 9201908, 9201388, 9161468, 9127828, 9143120, 9185704, 9245608], 'Seth': [9125736, 9124884, 9126068, 9143636, 9190580, 9186408, 9150268, 9148724, 9191012, 9150872, 9193164, 9157080, 9152860, 9195248, 9159524, 9159912, 9157604, 9201868,9202172, 9202892, 9199568, 9160228, 9203240, 9164400, 9165320, 9165600, 9165900, 9162368, 9205360, 9166444, 9206960, 9170940, 9210604, 9175716, 9215172, 9126624, 9178524, 9217636, 9127424, 9128336, 9131708, 9135084, 9137884, 9138464, 9140004, 9143208, 9141300, 9183964, 9181252, 9220232, 9183124, 9125184, 9235588, 9247848, 9222424, 9223972, 9226680], 'Myrrh': [9192112, 9194804, 9196408, 9201888, 9164420, 9162388, 9205520, 9168144, 9171820, 9211504, 9178120, 9177376, 9180824, 9219856, 9182752, 9221752, 9244868], 'Syrene': [9167204, 9244608, 9247728], 'Marisa': [9144356, 9193644, 9195228, 9245488], 'Colm': [9148584, 9127704, 9128256, 9131608, 9135244, 9137904, 9138984, 9245228], 'Ewan': [9150488, 9149984, 9151952, 9194164, 9195208, 9245528], 'Saleh': [9150228, 9150852, 9194884, 9204460, 9245508], 'Tana': [9143816, 9186428, 9153000, 9166484, 9207000, 9143368, 9141280, 9184984, 9245708, 9247708], 'Kyle': [9164500, 9165680, 9133756, 9133988, 9132684, 9139744, 9143288, 9244768], 'Moulder': [9148744, 9126684, 9127304, 9128236, 9135144, 9137844, 9138964, 9143268, 9125204,9245148, 9247648], 'Natasha': [9201928, 9201448, 9131588, 9245308], 'Neimi': [9127404, 9128316, 9131688, 9135184, 9137824, 9245208]}

def getHexFromChar(name):
    try:
        return CHAR_TO_HEX[name]
    except:
        return None

def getCharacterAddress(name):
    try:
        return CHAR_TABLE + getHexFromChar(name) * CHAR_ENTRY_LENGTH + 1
    except:
        return None
        
def getCharacterUnitAddress(name):
    try:
        return CHAR_TO_UNIT_TABLE[name]
    except:
        return None
        
CLASS_TO_HEX = {
    'Lord (Ephraim)' : 0x01, 
    'Lord (Eirika)' : 0x02, 
    'Great Lord (Ephraim)' : 0x03, 
    'Great Lord (Eirika)' : 0x04, 
    'Cavalier' : 0x05, 
    'Cavalier (F)' : 0x06, 
    'Paladin' : 0x07, 
    'Paladin (F)' : 0x08, 
    'Knight' : 0x09, 
    'Knight (F)' : 0x0A, 
    'General' : 0x0B, 
    'General (F)' : 0x0C, 
    'Thief' : 0x0D, 
    'Mamkute' : 0x0E, 
    'Mercenary' : 0x0F, 
    'Mercenary (F)' : 0x10, 
    'Hero' : 0x11, 
    'Hero (F)' : 0x12, 
    'Myrmidon' : 0x13, 
    'Myrmidon (F)' : 0x14, 
    'Swordmaster' : 0x15, 
    'Swordmaster (F)' : 0x16, 
    'Assassin' : 0x17, 
    'Assassin (F)' : 0x18, 
    'Archer' : 0x19, 
    'Archer (F)' : 0x1A, 
    'Sniper' : 0x1B, 
    'Sniper (F)' : 0x1C, 
    'Ranger' : 0x1D, 
    'Ranger (F)' : 0x1E, 
    'Wyvern Rider' : 0x1F, 
    'Wyvern Rider (F)' : 0x20, 
    'Wyvern Lord' : 0x21, 
    'Wyvern Lord (F)' : 0x22, 
    'Wyvern Knight' : 0x23, 
    'Wyvern Knight (F)' : 0x24, 
    'Mage' : 0x25, 
    'Mage (F)' : 0x26, 
    'Sage' : 0x27, 
    'Sage (F)' : 0x28, 
    'Mage Knight' : 0x29, 
    'Mage Knight (F)' : 0x2A, 
    'Bishop' : 0x2B, 
    'Bishop (F)' : 0x2C, 
    'Shaman' : 0x2D, 
    'Shaman (F)' : 0x2E, 
    'Druid' : 0x2F, 
    'Druid (F)' : 0x30, 
    'Summoner' : 0x31, 
    'Summoner (F)' : 0x32, 
    'Rogue' : 0x33, 
    'Gorgon Egg' : 0x34, 
    'Great Knight' : 0x35, 
    'Great Knight (F)' : 0x36, 
    'Trainee Soldier (2)' : 0x37, 
    'Trainee Fighter (3)' : 0x38, 
    'Trainee Mage (3)' : 0x39, 
    'Trainee Soldier (3)' : 0x3A, 
    'Manakete' : 0x3B, 
    'Manakete (F)' : 0x3C, 
    'Journeyman' : 0x3D, 
    'Pupil' : 0x3E, 
    'Fighter' : 0x3F, 
    'Warrior' : 0x40, 
    'Brigand' : 0x41, 
    'Pirate' : 0x42, 
    'Berserker' : 0x43, 
    'Monk' : 0x44, 
    'Priest' : 0x45, 
    'Recruit' : 0x47, 
    'Pegasus Knight' : 0x48, 
    'Falcon Knight' : 0x49, 
    'Cleric' : 0x4A, 
    'Troubadour' : 0x4B, 
    'Valkyrie' : 0x4C, 
    'Dancer' : 0x4D, 
    'Soldier' : 0x4E, 
    'Necromancer' : 0x4F, 
    'Fleet' : 0x50, 
    'Ghost Fighter' : 0x51, 
    'Zombie' : 0x52, 
    'Mummy' : 0x53, 
    'Skeleton' : 0x54, 
    'Skeleton (Bow)' : 0x55, 
    'Hellbone' : 0x56, 
    'Hellbone (Bow)' : 0x57, 
    'Bael' : 0x58, 
    'Elder Bael' : 0x59, 
    'Cyclops' : 0x5A, 
    'Mauthedoog' : 0x5B, 
    'Cerberus' : 0x5C, 
    'Tarvos' : 0x5D, 
    'Macdaire' : 0x5E, 
    'Bigl' : 0x5F, 
    'Arch Bigl' : 0x60, 
    'Gorgon' : 0x61, 
    'Gorgon Egg' : 0x62, 
    'Gargoyle' : 0x63, 
    'Death Gargoyle' : 0x64, 
    'Dragon Zombie' : 0x65, 
    'Demon King' : 0x66, 
}

CLASS_TO_CLASS = {
    'Nomad Trooper' : 'Ranger',
    'Villager' : 'Recruit',
    'Dark Sage' : 'Druid',
    'Dark Knight' : 'Mage Knight',
}

def getHexFromClass(name):
    try:
        if name not in CLASS_TO_HEX.keys():
            name = CLASS_TO_CLASS[name]
        return CLASS_TO_HEX[name]
    except:
        return None
        
def getClassAddress(name):
    try:
        return CLASS_TABLE + getHexFromClass(name) * CLASS_ENTRY_LENGTH
    except:
        return None
    
ITEM_TO_HEX = {
    '' : 0x00,
    'Iron Sword' : 0x01,
    'Slim Sword' : 0x02,
    'Steel Sword' : 0x03,
    'Silver Sword' : 0x04,
    'Iron Blade' : 0x05,
    'Steel Blade' : 0x06,
    'Silver Blade' : 0x07,
    'Poison Sword' : 0x08,
    'Rapier' : 0x09,
    'Mani Katti' : 0x0A,
    'Brave Sword' : 0x0B,
    'Shamshir' : 0x0C,
    'Killing Edge' : 0x0D,
    'Armourslayer' : 0x0E,
    'Wyrmslayer' : 0x0F,
    'Light Brand' : 0x10,
    'Runesword' : 0x11,
    'Lancereaver' : 0x12,
    'Longsword' : 0x13,
    'Iron Lance' : 0x14,
    'Slim Lance' : 0x15,
    'Steel Lance' : 0x16,
    'Silver Lance' : 0x17,
    'Poison Lance' : 0x18,
    'Brave Lance' : 0x19,
    'Killer Lance' : 0x1A,
    'Horseslayer' : 0x1B,
    'Javelin' : 0x1C,
    'Spear' : 0x1D,
    'Axereaver' : 0x1E,
    'Iron Axe' : 0x1F,
    'Steel Axe' : 0x20,
    'Silver Axe' : 0x21,
    'Poison Axe' : 0x22,
    'Brave Axe' : 0x23,
    'Killer Axe' : 0x24,
    'Halberd' : 0x25,
    'Hammer' : 0x26,
    'Devil Axe' : 0x27,
    'Hand Axe' : 0x28,
    'Tomahawk' : 0x29,
    'Swordreaver' : 0x2A,
    'Swordslayer' : 0x2B,
    'Hatchet' : 0x2C,
    'Iron Bow' : 0x2D,
    'Steel Bow' : 0x2E,
    'Silver Bow' : 0x2F,
    'Poison Bow' : 0x30,
    'Killer Bow' : 0x31,
    'Brave Bow' : 0x32,
    'Short Bow' : 0x33,
    'Longbow' : 0x34,
    'Ballista' : 0x35,
    'Iron Ballista' : 0x36,
    'Killer Ballista' : 0x37,
    'Fire' : 0x38,
    'Thunder' : 0x39,
    'Elfire' : 0x3A,
    'Bolting' : 0x3B,
    'Fimbulvetr' : 0x3C,
    'Forblaze' : 0x3D,
    'Excalibur' : 0x3E,
    'Lightning' : 0x3F,
    'Shine' : 0x40,
    'Divine' : 0x41,
    'Purge' : 0x42,
    'Aura' : 0x43,
    'Luce' : 0x44,
    'Flux' : 0x45,
    'Luna' : 0x46,
    'Nosferatu' : 0x47,
    'Eclipse' : 0x48,
    'Fenrir' : 0x49,
    'Gleipnir' : 0x4A,
    'Heal' : 0x4B,
    'Mend' : 0x4C,
    'Recover' : 0x4D,
    'Physic' : 0x4E,
    'Fortify' : 0x4F,
    'Restore' : 0x50,
    'Silence' : 0x51,
    'Sleep' : 0x52,
    'Berserk' : 0x53,
    'Warp' : 0x54,
    'Rescue' : 0x55,
    'Torch Staff' : 0x56,
    'Hammerne' : 0x57,
    'Unlock' : 0x58,
    'Barrier' : 0x59,
    'Dragon Axe' : 0x5A,
    'Angelic Robe' : 0x5B,
    'Energy Ring' : 0x5C,
    'Secret Book' : 0x5D,
    'Speedwings' : 0x5E,
    'Goddess Icon' : 0x5F,
    'Dragonshield' : 0x60,
    'Talisman' : 0x61,
    'Boots' : 0x62,
    'Body Ring' : 0x63,
    'Hero Crest' : 0x64,
    'Heros Crest' : 0x64,
    'Knight Crest' : 0x65,
    'Knights Crest' : 0x65,
    'Orion Bolt' : 0x66,
    'Orions Bolt' : 0x66,
    'Elysian Whip' : 0x67,
    'Guiding Ring' : 0x68,
    'Chest Key' : 0x69,
    'Door Key' : 0x6A,
    'Lockpick' : 0x6B,
    'Vulnerary' : 0x6C,
    'Elixir' : 0x6D,
    'Pure Water' : 0x6E,
    'Antidote' : 0x6F,
    'Torch' : 0x70,
    'Delphi Shield' : 0x71,
    'Member Card' : 0x72,
    'Silver Card' : 0x73,
    'White Gem' : 0x74,
    'Blue Gem' : 0x75,
    'Red Gem' : 0x76,
    'Reginleif' : 0x78,
    'Mine' : 0x7A,
    'Light Rune' : 0x7B,
    'Hoplon Shield' : 0x7C,
    'Fillas Might' : 0x7D,
    'Niniss Grace' : 0x7E,
    'Thors Ire' : 0x7F,
    'Sets Litany' : 0x80,
    'Sieglind' : 0x85,
    'Battle Axe' : 0x86,
    'Ivaldi' : 0x87,
    'Master Proof' : 0x88,
    'Metiss Tome' : 0x89,
    'Heaven Seal' : 0x8A,
    'Sharp Claw' : 0x8B,
    'Latona' : 0x8C,
    'Dragonspear' : 0x8D,
    'Vidofnir' : 0x8E,
    'Naglfar' : 0x8F,
    'Wretched Air' : 0x90,
    'Audomra' : 0x91,
    'Siegmund' : 0x92,
    'Garm' : 0x93,
    'Nidhogg' : 0x94,
    'Heavy Spear' : 0x95,
    'Short Spear' : 0x96,
    'Conquerors Proof' : 0x97,
    'Wind Sword' : 0xA1,
    'Dragonstone' : 0xAA,
    'Demon Surge' : 0xAB,
    'Shadowshot' : 0xAC,
    'Rotten Claw' : 0xAD,
    'Fetid Claw' : 0xAE,
    'Poison Claw' : 0xAF,
    'Long Poison Claw' : 0xB0,
    'Fire Fang' : 0xB1,
    'Hell Fang' : 0xB2,
    'Evil Eye' : 0xB3,
    'Bloody Eye' : 0xB4,
    'Stone' : 0xB5,
    'Aircalibur' : 0xB6,
}

ITEM_TO_ITEM = {
    'Wo Dao' : 'Shamshir',
    'Vague Katti' : 'Shamshir',
    'Concoction' : 'Vulnerary',
    'Wind' : 'Fire',
    'Elthunder' : 'Thunder',
    'Elwind' : 'Thunder',
    'Bolganone' : 'Elfire',
    'Thoron' : 'Elfire',
    'Meteor' : 'Bolting',
    'Divine Dragonstone' : 'Dragonstone',
    'Fire Dragonstone' : 'Dragonstone',
    'Rat Spirit' : 'Fire',
    'Horse Spirit' : 'Fire',
    'Ox Spirit' : 'Thunder',
    'Sheep Spirit' : 'Thunder',
    'Tiger Spirit' : 'Elfire',
    'Dragon Spirit' : 'Fimbulvetr',
}

WR_TO_HEX = {
    '' : 0x00,
    'E' : 0x01,
    'D' : 0x1F,
    'C' : 0x47,
    'B' : 0x79,
    'A' : 0xB5,
    'S' : 0xFB
}

WEAPON_TYPES = [
    "Sword", "Lance", "Axe", "Bow", "Staff", "Anima", "Light", "Dark"
]

def getHexFromItem(name):
    try:
        if name not in ITEM_TO_HEX.keys():
            name = ITEM_TO_ITEM[name]
        return ITEM_TO_HEX[name]
    except:
        return None

def getHexFromWeaponRank(rank):
    try:
        return WR_TO_HEX[rank]
    except:
        return None

def convertCharacter(oldChar):
    newChar = {}
    for key in oldChar:
        if (key == 'class'):
            newChar['class name'] = oldChar[key]
            newChar[key] = getHexFromClass(oldChar[key])
        elif (key == 'character'):
            newChar[key] = getHexFromChar(oldChar[key])
        elif (key == "items"):
            newChar[key] = []
            for i in range(4):
                if getHexFromItem(oldChar[key][i]) != None:
                    newChar[key].append(getHexFromItem(oldChar[key][i]))
                else:
                    newChar[key].append(0)
        elif key in WEAPON_TYPES:
            newChar[key] = getHexFromWeaponRank(oldChar[key])
        else:
            newChar[key] = oldChar[key]
    return newChar
    
# if the class exists, the character is legal.
# even if they have illegal items - those are just removed
def legalCharacter(char):
    return getHexFromClass(char['class']) != None
CHAR_TABLE = 0x803D30
CHAR_ENTRY_LENGTH = 0x34

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

def getHexFromChar(name):
    try:
        return CHAR_TO_HEX[name]
    except:
        return None

def getCharacterAddress(name):
    try:
        return CHAR_TABLE + CHAR_TO_HEX[name] * CHAR_ENTRY_LENGTH + 1
    except:
        return None
        
CLASS_TO_HEX = {
    'Ephraim Lord' : 0x01, 
    'Eirika Lord' : 0x02, 
    'Ephraim Master Lord' : 0x03, 
    'Eirika Master Lord' : 0x04, 
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
    'Bard' : 0x46, 
    'Recruit' : 0x47, 
    'Pegasus Knight' : 0x48, 
    'Falcon Knight' : 0x49, 
    'Sister' : 0x4A, 
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
    'Cleric' : 'Sister',
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

def getHexFromItem(name):
    try:
        if name not in ITEM_TO_HEX.keys():
            name = ITEM_TO_ITEM[name]
        return ITEM_TO_HEX[name]
    except:
        return None

def convertCharacter(bytes, oldChar):
    newChar = {}
    for key in oldChar:
        if (key == 'class'):
            newChar[key] = getHexFromClass(oldChar[key]);
        elif (key == 'character'):
            newChar[key] = getHexFromChar(oldChar[key]);
        elif (key == "items"):
            newChar[key] = []
            for item in oldChar[key]:
                if getHexFromItem(item) != None:
                    newChar[key].append(getHexFromItem(item))
        else:   
            newChar[key] = oldChar[key]
    return newChar
    
# if the class exists, the character is legal.
# even if they have illegal items - those are just removed
def legalCharacter(char):
    return getHexFromClass(char['class']) != None
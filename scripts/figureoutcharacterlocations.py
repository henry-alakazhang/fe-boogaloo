import fe8

import os

GAME = open("FE8.gba", 'rb')

unitAddresses = {c : [] for c in fe8.CHAR_TO_HEX.keys()}

for filename in os.listdir("./nmms"):
    charsCopy = dict(fe8.CHAR_TO_HEX)
    if (filename.endswith(".nmm")):
        MODU = open("./nmms/" + filename, 'r')
        file = list(MODU)
        addr = eval(file[5].rstrip())
        num = eval(file[6].rstrip())
        MODU.close()
        
        GAME.seek(addr)
        
        for i in range(num):
            charID = int.from_bytes(GAME.read(1), byteorder='little')
            for c in charsCopy:
                if charsCopy[c] == charID:
                    unitAddresses[c] += [addr+i*fe8.CHAR_UNIT_LENGTH]
                    charsCopy.pop(c)
                    break
            GAME.seek(fe8.CHAR_UNIT_LENGTH - 1, 1)
            
print(unitAddresses)
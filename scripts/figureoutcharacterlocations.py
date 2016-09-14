import os, sys

from fe8 import FE8
from fe7 import FE7

# uses Chapter Unit nightmare modules to find unit load locations for characters
# opens up the game file to actually find the data

if sys.argv[2] == "FE7":
    FILE = open(sys.argv[1], 'rb')
    GAME = FE7(FILE)
elif sys.argv[2] == "FE8":
    FILE = open(sys.argv[1], 'rb')
    GAME = FE8(FILE)
    
unitAddresses = {c : [] for c in GAME.CHAR_TO_HEX.keys()}

for filename in os.listdir("./nmms"):
    charsCopy = dict(GAME.CHAR_TO_HEX)
    if (filename.endswith(".nmm")):
        MODU = open("./nmms/" + filename, 'r')
        file = list(MODU)
        
        # read until we find the pointer in case of new lines
        addr = ""
        i = 0
        while True:
            try:
                addr = eval(file[i].rstrip())
                if addr > 1000:
                    break
                i += 1
            except:
                i += 1
        num = eval(file[i+1].rstrip())
        MODU.close()
        
        FILE.seek(addr)
        
        for i in range(num):
            charID = int.from_bytes(FILE.read(1), byteorder='little')
            for c in charsCopy:
                if charsCopy[c] == charID:
                    unitAddresses[c] += [FILE.tell() - 1]
                    break
            FILE.seek(GAME.CHAR_UNIT_LENGTH - 1, 1)

print(unitAddresses)
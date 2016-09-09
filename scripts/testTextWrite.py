import rom, fe8

# test for writing text to the rom
# changes Eirika's name to TEST

file = open('test.gba', 'rb+')

rom.applyPatch(file, fe8.ANTIHUFFMAN)
rom.writeTextToROM(file, fe8, [0x2, 0x12], "TEST")
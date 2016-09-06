import csv

data = {}
heads = ["class", "HP-base", "STR-base", "SKL-base", "SPD-base", "LUK-base", "DEF-base", "RES-base"]

charfile = open('classdata.csv', newline='')
charreader = csv.DictReader(charfile, heads)
for line in charreader:
    data[line['class']] = line
    
print(data)
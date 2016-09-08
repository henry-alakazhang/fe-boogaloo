import sys

WL = ["Sword", "Lance", "Axe", "Bow", "Staff", "Anima", "Light", "Dark"]

inf = open(sys.argv[1], 'r')
outf = open(sys.argv[1] + "formatted.csv", 'w')

for line in inf:
    parts = line.rstrip().split('|')
    wlevels = parts[2].split(',')
    if wlevels[0] != "":
        wldict = {wl[0] : wl[1] for wl in [type.split(' ') for type in wlevels]}
        for w in WL:
            if w in wldict:
                outf.write(wldict[w] +",")
            else:
                outf.write(",")
    outf.write("\n")
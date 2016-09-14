import sys

# generates a bit-by-bit patch difference between two files

diff = {}

# load both files into memory - thankfully, GBA files are only 16MB lul
file1 = open(sys.argv[1], 'rb+').read()
file2 = open(sys.argv[2], 'rb+').read()

for i in range(len(file1)):
    if file1[i] != file2[i]:
        diff[i] = file2[i]

print(diff)
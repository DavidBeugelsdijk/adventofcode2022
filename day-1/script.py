inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

for line in lines:
    line = line.strip()

print(lines)
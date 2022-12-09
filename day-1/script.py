inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

newLines = []

for line in lines:
    newLines.append(line.replace("\n", ""))

lines = newLines
newLines = []

print(lines)

totCalElfs = [0]
i = 0

for line in lines:
    if line.isdigit() :
        totCalElfs[i] = totCalElfs[i] + int(line)
    else:
        totCalElfs.append(0)
        i = i + 1

print(totCalElfs)

maxCal = 0

for calories in totCalElfs:
    if calories > maxCal:
        maxCal = calories

print(maxCal)
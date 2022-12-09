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

number1Elf = 0

for calories in totCalElfs:
    if calories > number1Elf:
        number1Elf = calories


number2Elf = 0

for calories in totCalElfs:
    if calories > number2Elf and calories != number1Elf:
        number2Elf = calories

number3Elf = 0

for calories in totCalElfs:
    if calories > number3Elf and calories != number1Elf and calories != number2Elf:
        number3Elf = calories

top3Tot = number1Elf + number2Elf + number3Elf

print(top3Tot)
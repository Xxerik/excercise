# esercizio 1 day 1 seconda parte

inputFile = open("input.txt")
inputCalories = inputFile.read().split("\n")
currentHighest = 0
current = 0
totals = [ ]

for i in inputCalories:
    if(i == ""):
        totals.append(current)
        current = 0
    else:
        current += int( i )
print(currentHighest)

totals.sort ()
totals.reverse ()
print( totals[0] + totals[1] + totals[2] )

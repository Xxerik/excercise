# giorno 2 scissors rock paper / parte 2
with open('input.txt') as file:
    rounds = [i for i in file.read().strip().split("\n")]


# A vs X = DRAW = (1 + 3) = 4
# A vs Y = WIN = (2 + 6) = 8
# A vs Z = LOSS = (3 + 0) = 3
# B vs X = LOSS = (1 + 0) = 1
# B vs Y = DRAW = (2 + 3) = 5
# B vs Z = WIN = (3 + 6) = 9
# C vs X = WIN = (1 + 6) = 7
# C vs Y = LOSS = (2 + 0) = 2
# C vs Z = DRAW = (3 + 3) = 6

outcomes = {
   "A X":4, "A Y":8, "A Z":3,
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6
}

total_points_p1 = 0
for round in rounds:
    total_points_p1 += outcomes[round]

desired_outcomes = {
    "A X":3, "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7
}

total_points_p2 = 0
for round in rounds:
    total_points_p2 += desired_outcomes[round]


print("risposta alla domanda 1: ", total_points_p1)
print("risposta alla domanda 2: ", total_points_p2)

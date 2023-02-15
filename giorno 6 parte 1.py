# giorno 6 parte 1

with open('giorno 6\input4.txt') as file:
    input = file.read()

for i in range(4, len(input)):
    s = set(input[(i-4):i])
    if len(s) == 4:
        print("risposta al quesito 1: ", i)
        break



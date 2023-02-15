# giorno 6 parte 2


with open('giorno 6\input4.txt') as file:
    input = file.read()

for i in range(4, len(input)):
    s = set(input[(i-4):i])
    if len(s) == 4:
        print("risposta al quesito 1: ", i)
        break


for i in range(14, len(input)):
    s = set(input[(i-14):i])
    if len(s) == 14:
        print("risposta al quesito 2: ", i)
        break


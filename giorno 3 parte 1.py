

with open('day 3\input1.txt') as f:
    lines = f.readlines()
    rucksack = [entry.strip() for entry in lines]

rucksack_sum = 0
while len(rucksack) > 0:
    first_rucksack = set(rucksack.pop())
    second_rucksack = set(rucksack.pop())
    third_rucksack = set(rucksack.pop())
    overlap_char = ((first_rucksack.intersection(second_rucksack)).intersection(third_rucksack)).pop()

    if overlap_char.isupper():
        rucksack_sum += ord(overlap_char) - ord('A') + 27
    else:
        rucksack_sum += ord(overlap_char) - ord('a') + 1

print(rucksack_sum)

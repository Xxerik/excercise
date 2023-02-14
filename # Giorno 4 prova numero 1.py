# Giorno 4 prova numero 1

with open('giorno 4\#input2.txt', 'r') as f:
    lines = f.readlines()
    assignment_pairs = [entry.strip() for entry in lines]

def is_range_a_in_range_b(range_a, range_b):
    start_a, end_a = map(int, range_a.split('-'))
    start_b, end_b = map(int, range_b.split('-'))
    return start_b <= start_a and end_a <= end_b

number_of_contains = 0

for assignment_pair in assignment_pairs:
    first_range, second_range = assignment_pair.split(',')
    if is_range_a_in_range_b(first_range, second_range) or is_range_a_in_range_b(second_range, first_range):
        number_of_contains += 1

print(number_of_contains)

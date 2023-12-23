import functools


def find_first_number(line):
    splits = line.split(":")[1].split("|")
    winning_numbers = splits[0].strip().split()
    own_numbers = splits[1].strip().split()
    intersection = list(filter(lambda x: x in winning_numbers, own_numbers))
    result = int(2 ** (len(intersection) - 1)) if len(intersection) != 0 else 0
    return result

def find_second_number(line):
    splits = line.split(":")[1].split("|")
    winning_numbers = splits[0].strip().split()
    own_numbers = splits[1].strip().split()
    intersection = list(filter(lambda x: x in winning_numbers, own_numbers))
    return len(intersection)

file = open('input', 'r')
lines = [i.strip() for i in file.readlines()]
first_results = [find_first_number(number) for number in lines]
print(functools.reduce(lambda a, b: a + b, first_results))
intersected_results = [find_second_number(number) for number in lines]
boards = [1] * len(intersected_results)
for i in range(len(intersected_results)):
    copies = intersected_results[i]
    for j in range(i + 1, i + 1 + copies):
        if j >= len(intersected_results):
            break
        boards[j] += boards[i]
print(functools.reduce(lambda a, b: a + b, boards))



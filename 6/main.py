import functools
import re

file = open('input', 'r')

data = file.read()

# Extracting numbers
time_pattern = re.compile(r'Time:\s+(.*)')
distance_pattern = re.compile(r'Distance:\s+(.*)')

time_match = time_pattern.search(data)
distance_match = distance_pattern.search(data)

if time_match and distance_match:
    # Splitting numbers and converting them to integers
    time_numbers = list(map(int, time_match.group(1).split()))
    distance_numbers = list(map(int, distance_match.group(1).split()))

    # Merging the two lists into pairs
    result = list(zip(time_numbers, distance_numbers))
else:
    result = "Data not found or format incorrect"


def exercise_1(pairs):
    result = 1
    for pair in pairs:
        result *= functools.reduce(lambda a, b: a + b,
                               [1 if i * (pair[0] - i) > pair[1] else 0 for i in range(pair[0] + 1)])
    return result


print(exercise_1(result))

def exercise_2(pairs):
    result = 1
    for pair in pairs:
        result *= functools.reduce(lambda a, b: a + b,
                                   [1 if i * (pair[0] - i) > pair[1] else 0 for i in range(pair[0] + 1)])
    return result

if time_match and distance_match:
    # Concatenating the numbers into one string and then converting to an integer
    concatenated_time = int(''.join(time_match.group(1).split()))
    concatenated_distance = int(''.join(distance_match.group(1).split()))

    result = (concatenated_time, concatenated_distance)
else:
    result = "Data not found or format incorrect"

print(functools.reduce(lambda a, b: a + b,
                               [1 if i * (result[0] - i) > result[1] else 0 for i in range(result[0] + 1)]))



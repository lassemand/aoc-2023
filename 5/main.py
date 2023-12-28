file = open('input', 'r')
lines = [i.strip() for i in file.readlines()]

sources = [int(source) for source in lines[0].split(":")[1].strip().split(" ")]

groups = []
new_section = False
current_index = 1
current_group = []
while current_index < len(lines):
    line = lines[current_index]
    if len(line) == 0:
        new_section = True
        current_index += 2
        if len(current_group) != 0:
            groups.append(current_group)
            current_group = []
        continue
    current_group.append([int(number) for number in line.split(" ")])
    current_index += 1
if len(current_group) != 0:
    groups.append(current_group)


## Exercise 1

def convert_1(source, list):
    match = -1
    for numbers in list:
        if numbers[1] <= source and numbers[1] + numbers[2] > source:
            if match != -1:
                print("Multiple matches")
                exit(1)
            match = numbers[0] + (source - numbers[1])
    return source if match == -1 else match


def exercise_1(sources):
    for group in groups:
        sources = [convert_1(source, group) for source in sources]
    print(min(sources))


exercise_1(sources)


## Exercise 2


def convert_2(source, list):
    distance_up = float('inf')
    for numbers in list:
        if numbers[1] + numbers[2] > source:
            if numbers[1] <= source:
                return numbers[0] + (source - numbers[1]), numbers[1] + numbers[2] - source
            distance_up = min(distance_up, numbers[1] - source)
    return source, distance_up


def exercise_2(sources):
    current_min = None
    for i in range(0, len(sources), 2):
        j = sources[i]
        while j < sources[i] + sources[i + 1]:
            distance_up = float('inf')
            value = j
            for group in groups:
                value, d_up = convert_2(value, group)
                distance_up = min(distance_up, d_up)
            if current_min is None or current_min > value:
                current_min = value
            j += distance_up
    print(current_min)


exercise_2(sources)

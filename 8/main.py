import math

with open("./input") as fin:
    lines = fin.read().strip().split("\n")
pairs = {i.strip().split(' ')[0]: tuple(i.strip().split(' = ')[1].strip('()').split(', ')) for i in lines[2:]}


def exercise_1():
    count = 0
    current_word = 'AAA'
    steps = lines[0]
    while current_word != 'ZZZ':
        character = steps[count % len(steps)]
        step = 0 if character == 'L' else 1
        current_word = pairs[current_word][step]
        count += 1
    return count


def _steps_2(current_word):
    count = 0
    steps = lines[0]
    while current_word[2] != 'Z':
        character = steps[count % len(steps)]
        step = 0 if character == 'L' else 1
        current_word = pairs[current_word][step]
        count += 1
    return count


def exercise_2():
    current_words = [node for node in pairs.keys() if node[2] == 'A']
    values = [_steps_2(word) for word in current_words]
    return math.lcm(*values)


print(exercise_2())

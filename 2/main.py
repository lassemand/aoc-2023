import functools


max_color = {"red": 12, "green": 13, "blue": 14}


def find_first_number(line):
    split = line.split(":")
    game = int(split[0].split(" ")[1])
    color_values = [{val.strip().split(" ")[1]: int(val.strip().split(" ")[0]) for val in c.split(",")} for c in split[1].split(";")]
    for color_value in color_values:
        for color in color_value:
            if max_color[color] < color_value[color]:
                game = 0
                break
    return game


def find_second_number(line):
    current_max_color = {"red": 0, "green": 0, "blue": 0}
    split = line.split(":")
    color_values = [{val.strip().split(" ")[1]: int(val.strip().split(" ")[0]) for val in c.split(",")} for c in split[1].split(";")]
    for color_value in color_values:
        for color in color_value:
            if current_max_color[color] < color_value[color]:
                current_max_color[color] = color_value[color]
    return functools.reduce(lambda x, y: x * y, current_max_color.values())

file = open('input', 'r')
lines = [i.strip() for i in file.readlines()]
first_results = [find_first_number(number) for number in lines]
print(functools.reduce(lambda a, b: a + b, first_results))
results = [find_second_number(number) for number in lines]
print(functools.reduce(lambda a, b: a + b, results))

import functools
import re


def load_first_symbols(lines):
    numbers = []
    symbols = []
    pattern = r'[^0-9\.]'
    for i in lines:
        line = i.strip()
        number_line = [(m.start(), m.group()) for m in re.finditer(r'\d+', line)]
        numbers.append(number_line)
        symbols.append([m.start() for m in re.finditer(pattern, line)])
    return numbers, symbols


def find_first_number(numbers, symbols):
    acc = 0
    for i, list in enumerate(numbers):
        indexes = [index + i - 1 for index in range(3)]
        if i == 0:
            del indexes[0]
        if i == len(numbers) - 1:
            del indexes[2]
        for j, value in enumerate(list):
            start_position = value[0]
            length = len(value[1])
            found = False
            for index in indexes:
                if found:
                    break
                for symbol in symbols[index]:
                    if symbol > start_position + length:
                        break
                    elif symbol >= start_position - 1:
                        found = True
                        break
            if found:
                print(f"Found: {value[1]}")
                acc += int(value[1])
            if not found:
                print(f"Excluded: {value[1]}")
    return acc



file = open('input', 'r')
lines = [i.strip() for i in file.readlines()]
numbers, symbols = load_first_symbols(lines)
print(find_first_number(numbers, symbols))


def load_second_symbols(lines):
    numbers = []
    symbols = []
    for i in lines:
        line = i.strip()
        number_line = [(m.start(), m.group()) for m in re.finditer(r'\d+', line)]
        numbers.append(number_line)
        symbols.append([m.start() for m in re.finditer(r'\*', line)])
    return numbers, symbols


def find_second_number(numbers, symbols):
    acc = 0
    for i, list in enumerate(symbols):
        indexes = [index + i - 1 for index in range(3)]
        if i == 0:
            del indexes[0]
        if i == len(numbers) - 1:
            del indexes[2]
        for j, symbol_index in enumerate(list):
            adjacent_numbers = []
            for index in indexes:
                for number in numbers[index]:
                    start_position = number[0]
                    end_position = start_position + len(number[1])
                    if symbol_index > end_position:
                        continue
                    if symbol_index < start_position - 1:
                        break
                    adjacent_numbers.append(int(number[1]))

            if len(adjacent_numbers) == 2:
                acc += adjacent_numbers[0] * adjacent_numbers[1]
    return acc



file = open('input', 'r')
lines = [i.strip() for i in file.readlines()]
numbers, symbols = load_second_symbols(lines)
print(find_second_number(numbers, symbols))

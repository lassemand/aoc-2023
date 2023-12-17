import functools
import re


def find_first_number(word):
    results = re.findall(r"\d", word)
    if len(results) == 1:
        number = convert(results[0])
        value = int(number + number)
        return value
    else:
        front = convert(results[0])
        back = convert(results[-1])
        value = int(front + back)
        return value


words = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
         'nine': '9'}


def find_second_number(word):
    numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine',word)
    print(f"Word before: {word}")
    for item in numbers:
        # Addresses strings tied together
        num = convert(item)
        new_sub = item[0] + num + item[-1]
        word = re.sub(item,new_sub,word)
    print(f"Word after: {word}")
    results = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", word)
    front = convert(results[0])
    back = convert(results[-1])
    value = int(front + back)
    return value


def convert(match):
    return match if len(match) == 1 else words[match]


file = open('input', 'r')
lines = [i.strip() for i in file.readlines()]
print(functools.reduce(lambda a, b: a + b, [find_first_number(number) for number in lines]))
print(functools.reduce(lambda a, b: a + b, [find_second_number(number) for number in lines]))

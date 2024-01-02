import functools
from collections import Counter


def find_combinations(hand):
    counts = Counter(hand)
    duplicates = {count: [] for count in set(counts.values())}
    for card, count in counts.items():
        duplicates[count].append(card)
    return duplicates


def exercise_1(pairs):
    values = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1,
              '2': 0}

    def count_score(pairs, rules):
        current_rank = len(pairs)
        result = 0
        for rule in rules:
            cards = sort_hands(rule['bucket'])
            for card in cards:
                result += pairs[card] * current_rank
                current_rank -= 1
        return result

    def card_value(card, index):
        """Assigns a numeric value to each card for sorting."""

        def projection(index):
            if index == 4:
                return 0  # [0-12]
            elif index == 3:
                return 13  # [13-25]
            elif index == 2:
                return 38  # [38-50]
            elif index == 1:
                return 88  # [88-100]
            else:
                return 188  # [188-200]

        return values[card] + projection(index)

    def sort_hand(hand):
        """Converts a hand into a sorted list of card values."""
        return sorted([card_value(card, index) for index, card in enumerate(hand)], reverse=True)

    def sort_hands(hands):
        """Sorts a list of hands based on card values."""
        return sorted(hands, key=sort_hand, reverse=True)

    rules = [
        {
            'rule': [[5, 1]], 'bucket': [],
        }, {
            'rule': [[4, 1]], 'bucket': [],
        }, {
            'rule': [[3, 1], [2, 1]], 'bucket': [],
        }, {
            'rule': [[3, 1]], 'bucket': [],
        }, {
            'rule': [[2, 2]], 'bucket': [],
        }, {
            'rule': [[2, 1]], 'bucket': [],
        }, {
            'rule': [[1, 1]], 'bucket': []
        }
    ]
    for card in pairs:
        combinations = find_combinations(card)
        for rule in rules:
            results = [True if size[0] in combinations and len(combinations[size[0]]) == size[1] else False for size in
                       rule['rule']]
            if functools.reduce(lambda a, b: a and b, results):
                rule['bucket'].append(card)
                break
    return count_score(pairs, rules)


def exercise_2(pairs):
    values = {'A': 12, 'K': 11, 'Q': 10, 'J': 0, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2,
              '2': 1}

    def count_score(pairs, rules):
        current_rank = len(pairs)
        result = 0
        for rule in rules:
            cards = sort_hands(rule['bucket'])
            print(cards)
            for card in cards:
                result += pairs[card] * current_rank
                current_rank -= 1
        return result

    def card_value(card, index):
        """Assigns a numeric value to each card for sorting."""

        def projection(index):
            if index == 4:
                return 0  # [0-12]
            elif index == 3:
                return 13  # [13-25]
            elif index == 2:
                return 38  # [38-50]
            elif index == 1:
                return 88  # [88-100]
            else:
                return 188  # [188-200]

        return values[card] + projection(index)

    def sort_hand(hand):
        """Converts a hand into a sorted list of card values."""
        return sorted([card_value(card, index) for index, card in enumerate(hand)], reverse=True)

    def sort_hands(hands):
        """Sorts a list of hands based on card values."""
        return sorted(hands, key=sort_hand, reverse=True)

    rules = [
        {
            'rule': [5], 'bucket': [],
        }, {
            'rule': [4], 'bucket': [],
        }, {
            'rule': [3, 2], 'bucket': [],
        }, {
            'rule': [3], 'bucket': [],
        }, {
            'rule': [2, 2], 'bucket': [],
        }, {
            'rule': [2], 'bucket': [],
        }, {
            'rule': [1], 'bucket': []
        }
    ]
    for card in pairs:
        combinations = find_combinations(card)
        jokers_count = 0
        for combination in combinations:
            if 'J' in combinations[combination]:
                jokers_count = combination
                if len(combinations[combination]) == 1:
                    del combinations[combination]
                else:
                    combinations[combination].remove('J')
                break
        for rule in rules:
            if rule['rule'][0] == 1:
                rule['bucket'].append(card)
                break

            is_approved = True
            picked_values = []
            for index, size in enumerate(rule['rule']):
                adjusted_size = size - (jokers_count if index == 0 else 0)
                if jokers_count == 5:
                    break
                if adjusted_size in combinations and len(set(combinations[adjusted_size]).difference(picked_values)) > 0:
                    picked_values.append(combinations[(adjusted_size if index == 0 else size)][0])
                    continue
                is_approved = False
                break
            if is_approved:
                rule['bucket'].append(card)
                break
    return count_score(pairs, rules)


file = open('input', 'r')
pairs = {i.strip().split(' ')[0]: int(i.strip().split(' ')[1]) for i in file.readlines()}
print(exercise_2(pairs))

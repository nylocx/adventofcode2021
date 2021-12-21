# This one is based on https://github.com/benediktwerner/AdventOfCode/tree/master/2021/day18
#%% Initialize
import itertools
import json
from functools import reduce

#%% Read input
with open("day_18_input.txt") as f:
    snailfish_numbers = list(map(json.loads, f.readlines()))


#%% Common
def add_left(snailfish_number, regular_number):
    if regular_number is None:
        return snailfish_number
    if isinstance(snailfish_number, int):
        return snailfish_number + regular_number
    return [add_left(snailfish_number[0], regular_number), snailfish_number[1]]


def add_right(snailfish_number, regular_number):
    if regular_number is None:
        return snailfish_number
    if isinstance(snailfish_number, int):
        return snailfish_number + regular_number
    return [snailfish_number[0], add_right(snailfish_number[1], regular_number)]


def explode(snailfish_number, depth=4):
    if isinstance(snailfish_number, int):
        return False, None, snailfish_number, None
    if depth == 0:
        return True, snailfish_number[0], 0, snailfish_number[1]
    a, b = snailfish_number
    exp, left, a, right = explode(a, depth - 1)
    if exp:
        return True, left, [a, add_left(b, right)], None
    exp, left, b, right = explode(b, depth - 1)
    if exp:
        return True, None, [add_right(a, left), b], right
    return False, None, snailfish_number, None


def split(snailfish_number):
    if isinstance(snailfish_number, int):
        if snailfish_number >= 10:
            return True, [
                snailfish_number // 2,
                snailfish_number - snailfish_number // 2,
            ]
        return False, snailfish_number
    a, b = snailfish_number
    change, a = split(a)
    if change:
        return True, [a, b]
    change, b = split(b)
    return change, [a, b]


def add(snailfish_number_left, snailfish_number_right):
    snailfish_number = [snailfish_number_left, snailfish_number_right]
    while True:
        change, _, snailfish_number, _ = explode(snailfish_number)
        if change:
            continue
        change, snailfish_number = split(snailfish_number)
        if not change:
            break
    return snailfish_number


def magnitude(snailfish_number):
    if isinstance(snailfish_number, int):
        return snailfish_number
    return 3 * magnitude(snailfish_number[0]) + 2 * magnitude(snailfish_number[1])


#%% Part 1
print(magnitude(reduce(add, snailfish_numbers)))

#%% Part 2
print(
    max(magnitude(add(x, y)) for x, y in itertools.permutations(snailfish_numbers, 2))
)

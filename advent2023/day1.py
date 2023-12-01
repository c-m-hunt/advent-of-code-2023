from typing import List

from advent2023 import utils


def load_and_parse_data(
    day: int, test: bool = False, part_2: bool = False
) -> List[str]:
    return utils.get_input(day, test, part_2)


def solve_part_1(data):
    total = 0
    for line in data:
        numbers = [n for n in line if n.isdigit()]
        total += int(f"{str(numbers[0])}{str(numbers[-1])}")
    return total


def solve_part_2(data):
    total = 0
    number_map = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    for line in data:
        for key, value in number_map.items():
            line = line.replace(key, value)
        numbers = [n for n in line if n.isdigit()]
        number_to_add = int(f"{str(numbers[0])}{str(numbers[-1])}")
        total += number_to_add
    return total

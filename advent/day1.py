from typing import List

from advent import utils


class Solution(utils.DaySolution):
    day = 1

    def solve_part_1(self):
        total = 0
        for line in self.data:
            numbers = [n for n in line if n.isdigit()]
            total += int(f"{str(numbers[0])}{str(numbers[-1])}")
        return total

    def solve_part_2(self):
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
        for line in self.data:
            for key, value in number_map.items():
                line = line.replace(key, value)
            numbers = [n for n in line if n.isdigit()]
            number_to_add = int(f"{str(numbers[0])}{str(numbers[-1])}")
            total += number_to_add
        return total

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
        for line in self.data:
            numbers = self.parse_line(line)
            total += int(f"{str(numbers[0])}{str(numbers[-1])}")
        return total

    def parse_line(self, line: str) -> List[str]:
        number_map = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        numbers = []
        for i in range(len(line)):
            if line[i].isdigit():
                numbers.append(line[i])
            else:
                for key, value in number_map.items():
                    if line[i : i + len(key)] == key:
                        numbers.append(value)

        return numbers

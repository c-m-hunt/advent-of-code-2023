from abc import ABC, abstractmethod
from typing import List


class DaySolution(ABC):
    day = None

    def __init__(self, test: bool = False, part_2: bool = False):
        self.test = test
        self.data = self.load_and_parse_data(test, part_2)

    def load_and_parse_data(
        self, test: bool = False, part_2: bool = False
    ) -> List[str]:
        day = self.day
        if test:
            if part_2:
                filename = f"./advent/input/{day}_2_test.txt"
            else:
                filename = f"./advent/input/{day}_test.txt"
        else:
            filename = f"./advent/input/{day}.txt"
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        return lines

    @abstractmethod
    def solve_part_1(self):
        pass

    @abstractmethod
    def solve_part_2(self):
        pass

    def display_results(self):
        print("----------")
        print("Day:", self.day)
        print("----------")
        print("Part 1:", self.solve_part_1())
        print("Part 2:", self.solve_part_2())
        print("----------")

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
        files = [f"./advent/input/{day}.txt"]
        if test:
            files = [f"./advent/input/{day}_test.txt"]
            if part_2:
                files.insert(0, f"./advent/input/{day}_2_test.txt")
        lines = []
        for filename in files:
            try:
                with open(filename) as file:
                    lines = file.readlines()
                    lines = [line.rstrip() for line in lines]
                    break
            except FileNotFoundError:
                pass
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

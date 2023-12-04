from typing import List, Tuple

import numpy as np

from advent import utils


class Solution(utils.DaySolution):
    day = 3

    def solve_part_1(self):
        invalid_numbers = []
        current_number = []
        current_number_start = ()
        for r in range(self.rows):
            col = 0
            while col < self.cols:
                if self.data[r][col].isdigit():
                    if len(current_number) == 0:
                        current_number_start = (r, col)
                    current_number.append(self.data[r][col])
                if len(current_number) > 0 and (
                    col + 1 == self.cols or not self.data[r][col + 1].isdigit()
                ):
                    if self.check_around_for_symbol(
                        current_number_start, len(current_number)
                    ):
                        invalid_numbers.append(int("".join(current_number)))
                    current_number = []
                col += 1
        return np.sum(invalid_numbers)

    def solve_part_2(self):
        gear_ratios = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.data[r][c] == "*":
                    gear_numbers = self.check_is_gear((r, c))
                    if len(gear_numbers) == 2:
                        gear_ratios += np.prod(gear_numbers)
        return gear_ratios

    def parse_data(self, data: str) -> List[str]:
        data = [self.parse_line(line) for line in data]
        self.rows = len(data)
        self.cols = len(data[0])
        return data

    def parse_line(self, line: str) -> List[str]:
        return [c for c in line]

    def check_is_gear(self, pos1: Tuple[int, int]) -> bool:
        numbers = []
        row = pos1[0]
        col = pos1[1]
        for r in range(row - 1, row + 2):
            last_number = None
            if r < 0 or r >= self.rows:
                continue
            for c in range(col - 1, col + 2):
                if c < 0 or c >= self.cols:
                    continue
                if self.data[r][c].isdigit():
                    number = self.get_full_number((r, c))
                    if last_number != number:
                        last_number = number
                        numbers.append(number)
                else:
                    last_number = None

        return numbers

    def get_full_number(self, pos1: Tuple[int, int]) -> int:
        number = [self.data[pos1[0]][pos1[1]]]
        col = pos1[1]
        while True:
            col -= 1
            if col < 0 or not self.data[pos1[0]][col].isdigit():
                break
            if self.data[pos1[0]][col].isdigit():
                number.insert(0, self.data[pos1[0]][col])
        col = pos1[1]
        while True:
            col += 1
            if col >= self.cols or not self.data[pos1[0]][col].isdigit():
                break
            if self.data[pos1[0]][col].isdigit():
                number.append(self.data[pos1[0]][col])
        return int("".join(number))

    def check_around_for_symbol(self, pos1: Tuple[int, int], length: int) -> bool:
        for r in range(pos1[0] - 1, pos1[0] + 2):
            for c in range(pos1[1] - 1, pos1[1] + length + 1):
                try:
                    if self.data[r][c] != "." and not self.data[r][c].isdigit():
                        return True
                except IndexError:
                    pass
        return False

from typing import Dict, List, Tuple

import numpy as np

from advent import utils


class Solution(utils.DaySolution):
    day = 4

    def solve_part_1(self):
        total = 0
        for card in self.data:
            total += (
                pow(2, card["winning_count"] - 1) if card["winning_count"] > 0 else 0
            )
        return total

    def solve_part_2(self):
        count = {i: 1 for i in range(1, len(self.data) + 1)}
        for card in self.data:
            for j in range(1, card["winning_count"] + 1):
                count[card["card_no"] + j] += count[card["card_no"]]
        return sum(count.values())

    def parse_line(self, line: str) -> Dict[str, any]:
        parts = line.split(":")
        card_no = int(parts[0].replace("Card ", ""))
        winning_numbers, numbers = parts[1].split("|")
        winning_numbers = [int(n) for n in winning_numbers.split()]
        numbers = [int(n) for n in numbers.split()]
        return {
            "card_no": card_no,
            "winning_numbers": winning_numbers,
            "numbers": numbers,
            "winning_count": len(np.intersect1d(winning_numbers, numbers)),
        }

from typing import List

import numpy as np

from advent import utils


class Solution(utils.DaySolution):
    day = 2

    def solve_part_1(self):
        max_cubes = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }
        sum_possible = 0
        for data in self.data:
            game_false = False
            game = self.parse_data(data)
            for pick in game["picks"]:
                for colour, number in pick.items():
                    if number > max_cubes[colour]:
                        game_false = True
            if not game_false:
                sum_possible += game["game_number"]
        return sum_possible

    def solve_part_2(self):
        total_power = 0
        for data in self.data:
            game = self.parse_data(data)
            max_cubes = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for pick in game["picks"]:
                for colour, number in pick.items():
                    if number > max_cubes[colour]:
                        max_cubes[colour] = number
            total_power += np.prod(list(max_cubes.values()))
        return total_power

    def parse_data(self, data_line: str):
        parts_1 = data_line.split(":")
        game_number = int(parts_1[0].split(" ")[1])
        picks = parts_1[1].split(";")

        picks_collection = []
        for pick in picks:
            pick_collection = {}
            pick_parts = pick.split(",")
            for pick_part in pick_parts:
                pick_part = pick_part.strip()
                if pick_part == "":
                    continue
                number, colour = pick_part.split(" ")
                number = int(number)
                pick_collection[colour] = number
            picks_collection.append(pick_collection)

        return {"game_number": game_number, "picks": picks_collection}

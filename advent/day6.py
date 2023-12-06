from typing import List, Tuple

import numpy as np

from advent import utils


class Solution(utils.DaySolution):
    day = 6

    def solve_part_1(self):
        dist_beaten = []
        for i in range(len(self.data[0])):
            time = self.data[0][i]
            distance = self.data[1][i]
            beaten = self.get_beaten(time, distance)
            dist_beaten.append(beaten)

        return np.prod(dist_beaten)

    def solve_part_2(self):
        time = int("".join([str(i) for i in self.data[0]]))
        distance = int("".join([str(i) for i in self.data[1]]))
        return self.get_beaten(time, distance)

    def get_beaten(self, time: int, distance: int) -> int:
        beaten = 0

        for t in range(time):
            boat_distance = self.calculate_distance(t, time, 1)
            if boat_distance > distance:
                beaten += 1
        return beaten

    def parse_data(self, data: List[str]) -> Tuple[List[int]]:
        return (
            [int(i) for i in data[0].split(":")[1].split()],
            [int(i) for i in data[1].split(":")[1].split()],
        )

    def calculate_distance(self, press_time: int, time: int, accel: int) -> int:
        speed = press_time * accel
        dist = (time - press_time) * speed
        return dist

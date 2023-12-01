import importlib
import unittest

# Change the day imprt, day number and expected results
DAY = 1
RESULT_PART_1 = 142
RESULT_PART_2 = 2812
#######################
puzzle = importlib.import_module("advent2023.day" + str(DAY))


class TestDay(unittest.TestCase):
    def test_part1(self):
        if RESULT_PART_1 is None:
            self.skipTest("No result for part 1")
        data = puzzle.load_and_parse_data(DAY, True)
        self.assertEqual(puzzle.solve_part_1(data), RESULT_PART_1)

    def test_part2(self):
        if RESULT_PART_2 is None:
            self.skipTest("No result for part 2")
        data = puzzle.load_and_parse_data(DAY, True, True)
        self.assertEqual(puzzle.solve_part_2(data), RESULT_PART_2)

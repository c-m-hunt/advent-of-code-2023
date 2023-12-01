import importlib
import unittest

# Change the day imprt, day number and expected results
DAY = 1
RESULT_PART_1 = 142
RESULT_PART_2 = 281
#######################
puzzle = importlib.import_module("advent.day" + str(DAY))


class TestDay(unittest.TestCase):
    def test_part1(self):
        if RESULT_PART_1 is None:
            self.skipTest("No result for part 1")
        solver = puzzle.Solution(test=True)
        self.assertEqual(solver.solve_part_1(), RESULT_PART_1)

    def test_part2(self):
        if RESULT_PART_2 is None:
            self.skipTest("No result for part 2")
        solver = puzzle.Solution(test=True, part_2=True)
        self.assertEqual(solver.solve_part_2(), RESULT_PART_2)

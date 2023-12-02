import importlib
import unittest


class TestDayBase(unittest.TestCase):
    __test__ = False

    def setUp(self):
        if self.day is None:
            return
        self.puzzle = importlib.import_module("advent.day" + str(self.day))

    def test_part1(self):
        if self.result_part_1 is None:
            self.skipTest("No result for part 1")
        solver = self.puzzle.Solution(test=True)
        self.assertEqual(solver.solve_part_1(), self.result_part_1)

    def test_part2(self):
        if self.result_part_2 is None:
            self.skipTest("No result for part 2")
        solver = self.puzzle.Solution(test=True, part_2=True)
        self.assertEqual(solver.solve_part_2(), self.result_part_2)

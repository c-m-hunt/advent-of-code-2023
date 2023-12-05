from advent.tests.test_base import TestDayBase


class TestDay(TestDayBase):
    __test__ = True
    day = 5
    result_part_1 = 35
    result_part_2 = 46

    def test_it_gets_data(self):
        solver = self.puzzle.Solution(test=True)
        self.assertEqual(solver.data["seeds"], [79, 14, 55, 13])
        self.assertEqual(len(solver.data["maps"]), 7)
        self.assertEqual(len(list(solver.data["maps"].values())[6]["map"]), 2)

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

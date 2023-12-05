from advent.tests.test_base import TestDayBase


class TestDay(TestDayBase):
    __test__ = True
    day = 5
    result_part_1 = 35
    result_part_2 = None

    def test_it_gets_data(self):
        solver = self.puzzle.Solution(test=True)
        self.assertEqual(solver.data["seeds"], [79, 14,55,13])
        self.assertEqual(len(solver.data["maps"]), 7)
        self.assertEqual(len(solver.data["maps"][6]["map"].keys()), 41)
        
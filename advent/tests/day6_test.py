from advent.tests.test_base import TestDayBase


class TestDay(TestDayBase):
    __test__ = True
    day = 6
    result_part_1 = 288
    result_part_2 = 71503

    def test_it_calculates_distance(self):
        solver = self.puzzle.Solution(test=True)
        self.assertEqual(solver.calculate_distance(0, 7, 1), 0)
        self.assertEqual(solver.calculate_distance(1, 7, 1), 6)

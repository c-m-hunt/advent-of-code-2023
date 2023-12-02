from advent.tests.test_base import TestDayBase


class TestDay(TestDayBase):
    __test__ = True
    day = 1
    result_part_1 = 142
    result_part_2 = 281

    def test_parse_line(self):
        line = "eightwothree"
        solver = self.puzzle.Solution(test=True)
        self.assertEqual(solver.parse_line(line), [8, 2, 3])

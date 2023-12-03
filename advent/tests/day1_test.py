from advent.tests.test_base import TestDayBase


class TestDay(TestDayBase):
    __test__ = True
    day = 1
    result_part_1 = 142
    result_part_2 = 281

    def test_parse_string(self):
        line = "eightwothree"
        solver = self.puzzle.Solution(test=True)
        self.assertEqual(solver.parse_string(line), [8, 2, 3])

        line = "1twothreeight"
        solver = self.puzzle.Solution(test=True)
        self.assertEqual(solver.parse_string(line), [1, 2, 3, 8])

        line = "dghfidiloneasdfihjasdlf1"
        solver = self.puzzle.Solution(test=True)
        self.assertEqual(solver.parse_string(line), [1, 1])

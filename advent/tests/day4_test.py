from advent.tests.test_base import TestDayBase


class TestDay(TestDayBase):
    __test__ = True
    day = 4
    result_part_1 = 13
    result_part_2 = 30

    def test_it_parses_data(self):
        solver = self.puzzle.Solution(test=True)
        line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        output = solver.parse_line(line)
        self.assertEqual(output["card_no"], 1)
        self.assertEqual(output["winning_numbers"], [41, 48, 83, 86, 17])
        self.assertEqual(output["numbers"], [83, 86, 6, 31, 17, 9, 48, 53])
        self.assertEqual(output["winning_count"], 4)

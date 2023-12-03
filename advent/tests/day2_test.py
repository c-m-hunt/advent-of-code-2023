from advent.tests.test_base import TestDayBase


class TestDay(TestDayBase):
    __test__ = True
    day = 2
    result_part_1 = 8
    result_part_2 = 2286

    def test_it_parses_input_line(self):
        input_line = (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
        )
        solver = self.puzzle.Solution(test=True)
        parsed_line = solver.parse_line(input_line)
        self.assertEqual(parsed_line["game_number"], 4)
        self.assertEqual(parsed_line["picks"][0]["green"], 1)
        self.assertEqual(parsed_line["picks"][1]["red"], 6)

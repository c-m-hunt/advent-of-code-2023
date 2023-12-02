import importlib
import unittest

# Change the day imprt, day number and expected results
DAY = 2
RESULT_PART_1 = 8
RESULT_PART_2 = 2286
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
        solver = puzzle.Solution(test=True)
        self.assertEqual(solver.solve_part_2(), RESULT_PART_2)

    def test_it_parses_input_line(self):
        input_line = (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
        )
        solver = puzzle.Solution(test=True)
        parsed_line = solver.parse_data(input_line)
        self.assertEqual(parsed_line["game_number"], 4)
        self.assertEqual(parsed_line["picks"][0]["green"], 1)
        self.assertEqual(parsed_line["picks"][1]["red"], 6)

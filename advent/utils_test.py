import unittest
from unittest import mock

from advent import utils


class TestUtils(unittest.TestCase):
    @mock.patch("advent.utils.print")
    def test_it_displays_output(self, mock_print):
        class TestSolution(utils.DaySolution):
            def __init__(self):
                self.day = 1

            def solve_part_1(self):
                return 1

            def solve_part_2(self):
                return 2

        ts = TestSolution()
        ts.display_results()
        self.assertEqual(mock_print.call_count, 6)
        self.assertEqual(mock_print.call_args_list[0][0][0], "----------")
        self.assertEqual(mock_print.call_args_list[1][0][0], "Day:")
        self.assertEqual(mock_print.call_args_list[1][0][1], 1)
        self.assertEqual(mock_print.call_args_list[3][0][0], "Part 1:")
        self.assertEqual(mock_print.call_args_list[4][0][0], "Part 2:")
        self.assertEqual(mock_print.call_args_list[3][0][1], 1)
        self.assertEqual(mock_print.call_args_list[4][0][1], 2)

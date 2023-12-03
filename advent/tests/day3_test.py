from advent.tests.test_base import TestDayBase


class TestDay(TestDayBase):
    __test__ = True
    day = 3
    result_part_1 = 4361
    result_part_2 = 467835

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

    def test_check_around_for_symbol(self):
        solver = self.puzzle.Solution(test=True)
        self.assertTrue(solver.check_around_for_symbol((0, 0), 3))
        self.assertFalse(solver.check_around_for_symbol((5, 7), 3))

    def test_it_gets_full_number(self):
        solver = self.puzzle.Solution(test=True)
        self.assertEqual(solver.get_full_number((2, 2)), 35)

    def test_it_checks_is_gear(self):
        solver = self.puzzle.Solution(test=True)
        self.assertEqual(solver.check_is_gear((1, 3)), [467, 35])

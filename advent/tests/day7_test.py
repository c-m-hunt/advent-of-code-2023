from advent.day7 import compare_hands_fn, map_card_values
from advent.tests.test_base import TestDayBase


class TestDay(TestDayBase):
    __test__ = True
    day = 7
    result_part_1 = 6440
    result_part_2 = 5905

    def test_it_parses_data(self):
        solver = self.puzzle.Solution(test=True)
        res = solver.parse_line("32T3K 765")
        self.assertEqual(res, ("32T3K", 765, 5, 5))

    def test_it_asseesses_hand(self):
        solver = self.puzzle.Solution(test=True)
        self.assertEqual(solver.assess_hand("AAAAA"), 0)
        self.assertEqual(solver.assess_hand("AAAAK"), 1)
        self.assertEqual(solver.assess_hand("AAAKK"), 2)
        self.assertEqual(solver.assess_hand("AAAKQ"), 3)
        self.assertEqual(solver.assess_hand("AAKKQ"), 4)
        self.assertEqual(solver.assess_hand("AA123"), 5)
        self.assertEqual(solver.assess_hand("A2345"), 6)

    def test_it_assesses_hand_with_joker(self):
        solver = self.puzzle.Solution(test=True)
        self.assertEqual(solver.assess_hand("T55J5", "J"), 1)
        self.assertEqual(solver.assess_hand("J55J5", "J"), 0)
        self.assertEqual(solver.assess_hand("KTJJT", "J"), 1)
        self.assertEqual(solver.assess_hand("1234J", "J"), 5)
        self.assertEqual(solver.assess_hand("1244J", "J"), 3)
        self.assertEqual(solver.assess_hand("JJJJA", "J"), 0)
        self.assertEqual(solver.assess_hand("JJJKA", "J"), 1)
        self.assertEqual(solver.assess_hand("AAKKJ", "J"), 2)

    def test_it_compares_hands_part_1(self):
        compare_hands = compare_hands_fn(2, map_card_values)
        self.assertEqual(compare_hands(("T55J5", 684, 3), ("QQQJA", 483, 3)), 1)
        self.assertEqual(compare_hands(("K55J5", 684, 3), ("QQQJA", 483, 3)), -1)
        self.assertEqual(compare_hands(("AAAAA", 684, 3), ("AAAAA", 483, 3)), 0)

    def test_it_compares_hands_part_2(self):
        card_map = map_card_values
        card_map["J"] = 0
        compare_hands = compare_hands_fn(3, card_map)
        self.assertEqual(compare_hands(("62355", 684, 3, 3), ("J2345", 483, 3, 3)), -1)

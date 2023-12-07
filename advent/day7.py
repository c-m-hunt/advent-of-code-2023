import functools
from typing import Dict, List, Tuple

from advent import utils

Hand = List[Tuple[str, int, int, int]]


class Solution(utils.DaySolution):
    day = 7

    def solve_part_1(self):
        hands = self.data
        sorted_hands = sorted(
            hands,
            key=functools.cmp_to_key(compare_hands_fn(2, map_card_values)),
            reverse=True,
        )
        winnings = 0
        for i in range(len(sorted_hands)):
            winnings += (i + 1) * sorted_hands[i][1]
        return winnings

    def solve_part_2(self):
        hands = self.data
        card_map = map_card_values
        card_map["J"] = 0
        sorted_hands = sorted(
            hands, key=functools.cmp_to_key(compare_hands_fn(3, card_map)), reverse=True
        )
        winnings = 0
        for i in range(len(sorted_hands)):
            winnings += (i + 1) * sorted_hands[i][1]
        return winnings

    def parse_line(self, line: str) -> Hand:
        parts = line.split()
        return (
            parts[0],
            int(parts[1]),
            self.assess_hand(parts[0]),
            self.assess_hand(parts[0], "J"),
        )

    def get_card_count(self, hand: str) -> Dict[str, int]:
        hand_count = {}
        for card in hand:
            if card not in hand_count:
                hand_count[card] = 0
            hand_count[card] += 1
        return hand_count

    def assess_hand(self, hand: str, joker: str = "X") -> int:
        hand_count = self.get_card_count(hand)

        if len(hand_count) == 1:
            return 0  # 5 of a kind
        if max(hand_count.values()) == 4:
            if joker in hand_count:
                return 0  # 5 of a kind
            return 1  # 4 of a kind
        if len(hand_count) == 2:
            if joker in hand_count:
                return 0  # 5 of a kind
            return 2  # Full house
        if max(hand_count.values()) == 3:
            if joker in hand_count and hand_count[joker] == 1:
                return 1  # 4 of a kind
            if joker in hand_count and hand_count[joker] == 3:
                return 1  # 4 of a kind
            return 3  # 3 of a kind
        if len(hand_count) == 3:
            if joker in hand_count and hand_count[joker] == 1:
                return 2
            if joker in hand_count and hand_count[joker] == 2:
                return 1
            return 4  # 2 pair
        if len(hand_count) == 4:
            if joker in hand_count:
                return 3  # 3 of a kind
            return 5  # 1 pair
        if joker in hand_count:
            return 5  # 1 pair
        return 6


map_card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def compare_hands_fn(compare_index: int, card_map: Dict[str, int]) -> callable:
    def compare_hands(
        hand1: Hand,
        hand2: Hand,
    ):
        if hand1[compare_index] < hand2[compare_index]:
            return -1
        if hand1[compare_index] > hand2[compare_index]:
            print("HERE1")
            return 1
        if hand1[compare_index] == hand2[compare_index]:
            for i in range(5):
                hand1_decider = card_map[hand1[0][i]]
                hand2_decider = card_map[hand2[0][i]]
                if hand1_decider > hand2_decider:
                    return -1
                if hand1_decider < hand2_decider:
                    print("HERE2")
                    return 1
        return 0

    return compare_hands

from typing import List


def get_input(day: int, test: bool, part_2: bool) -> List[str]:
    if test:
        if part_2:
            filename = f"./advent2023/input/{day}_2_test.txt"
        else:
            filename = f"./advent2023/input/{day}_test.txt"
    else:
        filename = f"./advent2023/input/{day}.txt"
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

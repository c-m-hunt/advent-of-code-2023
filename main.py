import importlib
import sys

DAY = sys.argv[1]

puzzle = importlib.import_module("advent.day" + str(DAY))

if __name__ == "__main__":
    solver = puzzle.Solution()
    solver.display_results()

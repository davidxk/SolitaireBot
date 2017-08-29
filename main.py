from sys import argv
from dfs import dfs_wrapper
from screenparser import ScreenParser
from Solitaire import Solitaire

if __name__ == "__main__":
    parser = ScreenParser()
    board = parser.parse_screenshot(argv.pop())
    path = dfs_wrapper(Solitaire(), board)
    for i, state in enumerate(path):
        print i
        print state

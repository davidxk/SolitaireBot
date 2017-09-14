from DFSAgent import DFSAgent
from GUIController import GUIController
from screenparser import ScreenParser
from time import sleep

if __name__ == "__main__":
    for i in range(3):
        print 3 - i
        sleep(1)

    guictrl = GUIController()
    parser = ScreenParser()
    dfsagent = DFSAgent()

    for i in range(100):
        guictrl.pressNewGame()

        parser.capture_screenshot()
        board = parser.parse_screenshot()

        moves = dfsagent.getMoves(board)
        if moves is None:
            continue

        for board, move in moves:
            print board

        guictrl.execute(moves)

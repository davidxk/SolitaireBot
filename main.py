from DFSAgent import DFSAgent
from GUIController import GUIController
from screenparser import ScreenParser
from subprocess import call
from time import sleep

if __name__ == "__main__":
    for i in range(3):
        sleep(0.2)
        call(["say", str(3 - i)])

    guictrl = GUIController()
    parser = ScreenParser()
    dfsagent = DFSAgent()

    for i in range(100):
        guictrl.pressNewGame()

        call(["say", "Capturing"])
        parser.capture_screenshot()
        board = parser.parse_screenshot()

        call(["say", "Ready ..."])
        moves = dfsagent.getMoves(board)
        if moves is None:
            continue

        for board, move in moves:
            print board

        call(["say", "go"])
        guictrl.execute(moves)

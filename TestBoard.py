from Board import Card
from Board import Board
from random import shuffle

class TestCard:
    def testToString(self):
        for color in range(3):
            for number in range(1, 10):
                print Card(color, number).toString(True)
        for color in range(3, 7):
            print Card(color, None).toString(True)

class TestBoard:
    def __init__(self):
        cards = [Card(color, i) for color in range(3) for i in range(1, 10)]
        cards += [Card(color, None) for color in range(3, 6) for i in range(4)]
        cards.append( Card(6, None) )
        shuffle( cards )
        self.board = Board(cards)

    def testStr(self):
        print self.board

    def testHash(self):
        states = {self.board}
        print states

if __name__ == "__main__":
    tc = TestCard()
    tc.testToString()
    tb = TestBoard()
    tb.testStr()
    tb.testHash()

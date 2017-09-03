from Board import Board
from Board import Card
from screenparser import ScreenParser, CardRecognizer
from PIL import Image
import unittest

class TestScreeParser(unittest.TestCase):
    def setUp(self):
        self.parser = ScreenParser()
        self.asw = Board()

    def testInit(self):
        board = self.parser.parse_screenshot('tests/init.png')
        self.asw.tableau = [
                [Card(3,None),Card(1,3),Card(0,4),Card(2,3),Card(1,6)],
                [Card(1,9),Card(5,None),Card(0,2),Card(2,9),Card(5,None)],
                [Card(0,6),Card(3,None),Card(1,5),Card(1,7),Card(4,None)],
                [Card(2,6),Card(1,4),Card(6,None),Card(2,4),Card(2,7)],
                [Card(4,None),Card(4,None),Card(0,5),Card(2,2),Card(0,8)],
                [Card(5,None),Card(4,None),Card(3,None),Card(2,1),Card(0,3)],
                [Card(5,None),Card(1,1),Card(0,1),Card(0,9),Card(0,7)],
                [Card(3,None),Card(2,8),Card(2,5),Card(1,8),Card(1,2)]
                ]
        self.assertEqual(board, self.asw)

    def testFoundation(self):
        b = self.parser.parse_screenshot('tests/foundation.png')
        self.asw.foundation[0] += 1
        self.asw.foundation[2] += 1
        self.asw.foundation[2] += 1
        self.assertEqual(b.foundation, self.asw.foundation)
        self.assertEqual(b.foundation.color_map[0], 0)
        self.assertEqual(b.foundation.color_map[2], 1)

    def test1(self):
        b = self.parser.parse_screenshot('tests/test1.png')
        self.asw.foundation[0] = 1
        self.asw.foundation[1] = 2
        self.asw.foundation[2] = 1
        self.assertEqual(b.foundation, self.asw.foundation)

    def test2(self):
        b = self.parser.parse_screenshot('tests/test2.png')
        self.asw.foundation[0] = 1
        self.asw.foundation[1] = 3
        self.asw.foundation[2] = 2
        self.assertEqual(b.foundation, self.asw.foundation)

    def test3(self):
        b = self.parser.parse_screenshot('tests/test3.png')
        self.asw.foundation[0] = 4
        self.asw.foundation[1] = 6
        self.asw.foundation[2] = 5
        self.assertEqual(b.foundation, self.asw.foundation)

    def test4(self):
        b = self.parser.parse_screenshot('tests/test4.png')
        self.asw.foundation[0] = 8
        self.asw.foundation[1] = 9
        self.asw.foundation[2] = 7
        self.assertEqual(b.foundation, self.asw.foundation)

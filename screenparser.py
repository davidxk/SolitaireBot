from Board import Board
from Board import Card
import numpy as np
from PIL import Image, ImageGrab

class ScreenParser:
    """
    Screen Parser
    """
    def __init__(self):
        self.recognizer = CardRecognizer()
        self.origin = None

    def capture_screenshot(self, im_path='screenshot.png'):
        im = ImageGrab.grab()
        im.save(im_path)

    def parse_screenshot(self, im_path='screenshot.png'):
        """
        Input a screenshot and return with Board
        """
        self.origin = Image.open(im_path).convert('RGB')
        tableau = self.__split_tableau_area__()
        foundation = self.__split_foundation_area_()
        return Board(tableau=tableau, foundation=foundation)

    def __split_tableau_area__(self):
        (left, upper, right, lower) = (173, 310, 187, 324)
        (ds, rs) = (31, 152)

        tableau = [[] for i in range(8)]
        for i in xrange(8):
            for j in xrange(5):
                box = (left+rs*i, upper+ds*j, right+rs*i, lower+ds*j)
                reg = self.origin.crop(box)
                card = self.recognizer.recognize_card(reg)
                if card:
                    tableau[i].append(card)
                else:
                    break
        return tableau

    def __split_foundation_area_(self):
        (left, upper, right, lower) = (933, 46, 947, 60)

        rs = 152
        foundation = []
        for i in xrange(3):
            for j in xrange(9):
                box = (left+rs*i, upper-j, right+rs*i, lower-j)
                reg = self.origin.crop(box)
                card = self.recognizer.recognize_card(reg)
                if card and card.number == j+1:
                    foundation.append(card)
                    break
        return foundation

class CardRecognizer:
    """
    Card Recognizer
    """
    def __init__(self):
        self.type_model = np.load('card_type.npy')

    def recognize_card(self, im):
        """
        recognize a card with its image
        """
        src = np.array(list(im.getdata()))
        typ = self.__recognize_card_type__(src)
        if typ and typ < 10:
            color = self.__recognize_card_color__(src)
            return Card(color, typ)
        elif typ:
            return Card(typ-7, None)
        else:
            return None

    def __recognize_card_type__(self, src):
        threshold = 28

        test = ((src[0]-src)>8).any(1)
        for i in xrange(13):
            if np.sum(np.logical_xor(self.type_model[i], test)) < threshold:
                return i+1
        return None

    def __recognize_card_color__(self, src):
        (r_threshold, g_threshold, threshold) = (80, 50, 30)

        dif = src - np.array([193, 195, 179])
        if np.sum(dif[:,0]<(dif[:,1]-r_threshold)) > threshold:
            return 1 # red
        if np.sum(dif[:,1]<(dif[:,0]-g_threshold)) > threshold:
            return 0 # green
        return 2 # black

from Board import Board
from Board import Card
import numpy as np
from PIL import Image

class ScreenParser:
    """
    Screen Parser
    """
    def __init__(self):
        self.recognizer = CardRecognizer()
        self.origin = None

    def parse_screenshot(self, im_path):
        """
        Input a screenshot and return with Board
        """
        self.origin = Image.open(im_path).convert('RGB')
        tableau = self.__split_tableau_area__()
        foundation = self.__split_foundation_area_()
        return Board(tableau=tableau, foundation=foundation)
        return (tableau, foundation)

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
            box = (left+rs*i, upper, right+rs*i, lower)
            reg = self.origin.crop(box)
            card = self.recognizer.recognize_card(reg)
            if card:
                foundation.append(card)
            else:
                break
        return foundation

class CardRecognizer:
    """
    Card Recognizer
    """
    def __init__(self):
        self.type_model = np.load('card_type')
        print(self.type_model)

    def recognize_card(self, im):
        """
        recognize a card with its image
        """
        src = np.array(list(im.getdata()))
        typ = self.__recognize_card_type__(src)
        if typ and typ < 9:
            color = self.__recognize_card_color__(src)
            return Card(color, typ+1)
        elif typ:
            # 3:Center, 4:Rich, 5:White, 6:Flower
            return Card(typ-6, None)
        else:
            return None

    def __recognize_card_type__(self, src):
        threshold = 20

        for i in xrange(13):
            diff = self.type_model[i] - src
            if np.sum(np.abs(diff)) < threshold:
                return i
            else:
                return None

    def __recognize_card_color__(self, src):
        (r_threshold, g_threshold, threshold) = (80, 50, 50)

        dif = src[1][0][0] - src[1][0]
        if np.sum(dif[:,0]<(dif[:,1]-r_threshold)) > threshold:
            return 1 # red
        if np.sum(dif[:,1]<(dif[:,0]-g_threshold)) > threshold:
            return 2 # green
        else:
            return 3 # black

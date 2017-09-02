#!/usr/bin/env python
# -*- coding: utf-8 -*-

class OrderedDict(dict):
    def __init__(self, orig):
        self.color_map = {}
        super(OrderedDict, self).__init__(orig)

    def __setitem__(self, key, val):
        if key not in self.color_map:
            self.color_map[key] = len(self.color_map)
        super(OrderedDict, self).__setitem__(key, val)

class Board(object):
    def __init__(self, cards = None, tableau=None, foundation=None, stock=None):
        self.stock = stock or [None, None, None]
        self.tableau = tableau or [[] for i in range(8)]
        self.foundation = foundation or OrderedDict({ c: 0 for c in range(3) })
        if cards:
            for i in range(5):
                for j in range(8):
                    self.tableau[j].append(cards.pop())

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        output = unicode()
        # Print stock
        for card in self.stock:
            if card:
                output += card.toString(True)
            elif card is None:
                output += "___ "
            else:
                output += "XXX "
        output += " " * 8
        # Print foundation
        for color in range(3):
            if self.foundation[color] > 0:
                output += Card(color, self.foundation[color]).toString(True)
            else:
                output += "___ "
        output += "\n\n"
        # Print tableau
        for i in range(max(len(deck) for deck in self.tableau)):
            for j in range(8):
                if i < len(self.tableau[j]):
                    output += self.tableau[j][i].toString(True)
                else:
                    output += "    "
            output += "\n"
        return output

    def __repr__(self):
        key = str(self.stock)
        key += str(self.tableau)
        key += str([self.foundation[color] for color in range(3)])
        return key

    def __eq__(self, other):
        return self.stock == other.stock and self.tableau == other.tableau and\
                self.foundation == other.foundation

    def __hash__(self):
        key = str(self.stock)
        key += str(self.tableau)
        key += str([self.foundation[color] for color in range(3)])
        return hash(key)

mapping = {0:u"饼", 1:u"条", 2:u"万", 3:u"中", 4:u"发", 5:u"白", 6:u"花"}
colormap = {0: "red", 1: "green", 2: "white", 3: "red", 4: "green", \
        5: "white", 6: "magenta"}
pigmap = {"red": "\033[0;31m", "green": "\033[0;32m", "white": "\033[0;37m", \
        "magenta": "\033[0;35m", "normal": "\033[0;0m", "black": "\033[0;30m"}

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def toString(self, pigment = False):
        result = ""
        if self.number is None:
            result = " " + mapping[self.color] + " "
        else:
            result = str().join([str(self.number), mapping[self.color] + " "])
        if pigment:
            result = pigmap[colormap[self.color]] + result + pigmap["normal"]
        return result

    def __repr__(self):
        return str( (self.color, self.number) )

    def __eq__(self, other):
        return other and self.color == other.color and self.number == other.number

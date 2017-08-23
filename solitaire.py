#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import shuffle
from collections import Counter
class GameBoard:
    def __init__(self, tableau=None, stock=None, foundations=None, cards=None):
        if cards != None:
            # bottom, left, right
            self.tableau = [[] for i in range(8)]
            self.stock = [None] * 3
            self.foundations = [[], [], []]
            for i in range(5):
                for j in range(8):
                    self.tableau[j].append(cards.pop())
        if tableau != None:
            self.tableau = tableau
            self.stock = stock
            self.foundations = foundations

    def printGame(self):
        string = unicode()
        for card in self.stock:
            string += self.printCard(card)
        string += " " * 8
        for deck in self.foundations:
            string += self.printCard(deck[-1] if len(deck) else None)
        string += "\n\n"
        for i in range(max(len(deck) for deck in self.tableau)):
            for j in range(8):
                if i < len(self.tableau[j]):
                    string += self.printCard(self.tableau[j][i])
                else:
                    string += "    "
            string += "\n"
        return string

    def printCard(self, card):
        if card is None:
            return "___ "
        elif card[1] in u"中发白花":
            return " " + card[1] + " "
        else:
            return str().join([str(card[0]), card[1]]) + " "

    def nextMove(self):
        """
        Return every possible move in an array
        """
        from copy import deepcopy
        moves = []

        # move cards from tableau to stock
        if self.__stock_has_space__():
            index = self.__stock_space_index__()
            for col in self.tableau:
                if not col:
                    continue
                card = col.pop()
                self.stock[index] = card
                moves.append(deepcopy(self))
                col.append(card) # recovery
            self.stock[index] = None # recovery

        # move cards from stock
        for i, card in enumerate(self.stock):
            if card != None:
                self.stock[i] = None
                # to tableau
                if self.__tableau_has_space__():
                    index = self.__tableau_space_index__()
                    self.tableau[index].append(card)
                    moves.append(deepcopy(self))
                    self.tableau[index].pop() # recovery
                if card[0] != None: # not a dragon
                    for col in self.tableau:
                        if col and self.__concatenable__(card, col[-1]):
                            col.append(card)
                            moves.append(deepcopy(self))
                            col.pop()
                # to foundations
                for j, foundation in enumerate(self.foundations):
                    if self.__successive__(card, foundation):
                        foundation.append(card)
                        moves.append(deepcopy(self))
                        foundation.pop() # recovery
                        break
                self.stock[i] = card # recovery

        # move cards from tableau to foundations
        for col in self.tableau:
            for foundation in self.foundations:
                if col and self.__successive__(col[-1], foundation):
                    card = col.pop()
                    foundation.append(card)
                    moves.append(deepcopy(self))
                    foundation.pop()
                    col.append(card)
                    break

        # move cards from tableau to tableau
        if self.__tableau_has_space__():
            index = self.__tableau_space_index__()
            for col in self.tableau:
                if len(col)>1:
                    card = col.pop()
                    self.tableau[index].append(card)
                    moves.append(deepcopy(self))
                    col.append(card)
                    self.tableau[index].pop() # recovery
        for ci, col in enumerate(self.tableau):
            if not col:
                continue
            for i in xrange(1, len(col)+1):
                if i > 1 and i < len(col) and not self.__concatenable__(col[-i-1], col[-i]):
                    break
                card = col[-i]
                for cj, ncol in enumerate(self.tableau):
                    if not ncol or col == ncol:
                        continue
                    if self.__concatenable__(card, ncol[-1]):
                        self.tableau[cj] = self.tableau[cj] + col[-i:]
                        self.tableau[ci] = col[:-i]
                        moves.append(deepcopy(self))
                        self.tableau[ci] = col
                        self.tableau[cj] = self.tableau[cj][:-i]
        return moves

    def clear(self):
        while True:
            self.__clear_flower__()

    def __clear_flower__(self):
        for deck in self.tableau:
            if deck and deck[-1][1] == u"花":
                deck.pop()

    def __clear_dragon__(self):
        # Count dragon
        cnt = Counter()
        for card in self.stock:
            if card and card[0] is None:
                cnt[card] += 1

        for deck in self.tableau:
            if deck and deck[-1][0] is None:
                cnt[deck[-1]] += 1

        # Fold dragon
        retval = False
        dragons = [key for key in cnt if cnt[key] == 4]
        for dragon in dragons:
            if dragon in self.stock or None in self.stock:
                retval = True
                for i, card in enumerate(self.stock):
                    if card == dragon:
                        self.stock[i] = None
                for deck in self.tableau:
                    if deck and deck[-1] == dragon:
                        deck.pop()
                self.stock.remove(None)
        return retval

    def __clear_foundation__():
		minima = min(self.foundations, key=lambda x: x[-1] if x else 0)
		for deck in self.tableau:
			if deck and deck[-1][0] and deck[-1][1] == minima + 1:
				deck.pop()

    def __stock_has_space__(self):
        return None in self.stock

    def __stock_space_index__(self):
        return self.stock.index(None)

    def __tableau_has_space__(self):
        return [] in self.tableau

    def __tableau_space_index__(self):
        return self.tableau.index([])

    def __concatenable__(self, card, head):
        return card[0] != None and head[0] != None and \
                card[0] == head[0]-1 and card[1] != head[1]

    def __successive__(self, card, foundation):
        return card[0] != None and \
                ((not foundation and card[0] == 1) or \
                (foundation and card[0] == foundation[-1][0] + 1 and \
                card[1] == foundation[-1][1]))

def new_game():
    cards = [(i, color) for i in range(1, 10) for color in [u"饼",u"条",u"万"]]
    cards += [(None, color) for color in [u"中",u"发",u"白"] for i in range(4)]
    cards.append( (None, u"花") )
    shuffle( cards )
    game = GameBoard(cards=cards)
    return game

if __name__ == "__main__":
    ng = new_game()
    print ng.printGame()
    print("Next moves:")
    for g in ng.nextMove():
        print g.printGame()

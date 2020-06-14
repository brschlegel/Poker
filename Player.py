
from Cards import Card, suitCodes
from Hands import *


class Player:

    def __init__(self):
        self.hand = Hand()
        self.chips = 0
        self.cards = []

    def ClearHand(self):
        self.hand = Hand()
        self.cards = []


class Human(Player):

    def Display():

        return


class Bot(Player):

    def Bet():
        return

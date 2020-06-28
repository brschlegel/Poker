
from Cards import Card, suitCodes
from Hands import *


class Player:

    def __init__(self, name, chips):
        self.hand = Hand()
        self.chips = chips
        self.cards = []
        self.name = name

    def ClearHand(self):
        self.hand = Hand()
        self.cards = []


class Human(Player):

    def Display():
        print("Cards: " + cards[0] + " " + cards[1] )
        print("Chips: " + chips)
        
    def Bet(self,previousBet):
        print("Current bet is: " + str(previousBet))
        bet = int(input("Enter Bet (0 for check or fold): "))
        if bet < previousBet:
            return 0

        if(self.chips >= bet):
            self.chips -= bet
            return bet



class Bot(Player):

    def Bet():
        return

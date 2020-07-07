
from Cards import Card, suitCodes
from Hands import *


class Player:

    def __init__(self, name, chips):
        self.hand = Hand()
        self.chips = chips
        self.cards = []
        self.name = name
        self.logEntries = []
        self.rightPermenant = None
        self.rightCurrent = None
        self.currentBet = 0
        

    def ClearHand(self):
        self.hand = Hand()
        self.cards = []


class Human(Player):

    def Display(self):
        print("Cards: " + str(self.cards[0]) + " " + str(self.cards[1]) )
        print("Chips: " + str(self.chips))
        
    def Bet(self,previousBet):
        print("Cost to call is: " + str(previousBet - self.currentBet))
        self.Display()
        bet = int(input("Enter Bet (0 for check or fold): "))
        if bet < previousBet - self.currentBet:
            self.logEntries.append(Log(previousBet, 0))
            print(self.name + " folds!")
            return 0

        if self.chips >= bet  :
            self.chips -= bet
            self.logEntries.append(Log(previousBet, bet))
            self.currentBet += bet
            return  self.currentBet
        
        else:
            print("You don't have enough chips for this bet!")
            self.Bet(previousBet)



class Bot(Player):

    def Bet():
        return

class Log:
    def __init__(self, previousBet, newBet):
        self.previousBet = previousBet
        self.newBet = newBet

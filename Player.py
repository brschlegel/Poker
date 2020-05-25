
from Cards import Card, suitCodes
from Hands import *



class Player:
   
   def __init__(self):
       self.hand = Hand()
       self.chips = 0

    def ClearHand(self):
        self.hand = Hand()


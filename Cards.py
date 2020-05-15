class Card:
    nextCard = None
    rank= 0
    suit = ""
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    ##overriding tostring
    def __str__(self):
        ##python doesn't have switch statements :(
        if self.rank < 11:
            return str(self.rank) + self.suit
        if self.rank == 11:
            return "J" + self.suit
        if self.rank == 12:
            return "Q" + self.suit
        if self.rank == 13:
            return "K" + self.suit
        if self.rank == 14:
            return "A" + self.suit
        
suitCodes = {"Clubs":"\u2663", "Hearts":"\u2665", "Diamonds":"\u2666", "Spades":"\u2660"}


from Decks import *
from Cards import Card, suitCodes
from Hands import *

def GenerateFullDeck():
    deck = Deck()
    for i in range(2,15):
        for k in suitCodes.values():
            deck.Add(Card(i,k))

    return deck

def GenerateRandomDeck():
    fullList = []
    for i in range(2,15):
        for k in suitCodes.values():
            fullList.append(Card(i,k))

    deck = Deck()
    for i in range(0,52):
        deck.Add(fullList.pop(random.randrange(len(fullList))))
    return deck

d = GenerateRandomDeck()
h = Hand(d.Pop())

for i in range(0,4):
    h.Add(d.Pop())

h.Print()

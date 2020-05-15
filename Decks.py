from Cards import *
import random

class Deck:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def Add(self,card):
        if self.head == None:
            self.head = card
            self.tail = card
            
        else:
            self.tail.nextCard = card
            self.tail = card

        self.count += 1
    
    def Print(self):
        current = self.head
        while current is not None:
            print(current)
            current = current.nextCard


    ##returns top card and removes from deck
    def Pop(self):
        current = self.head
        self.head = self.head.nextCard
        return current

   










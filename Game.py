from Player import *
from HoldEm import *
from Decks import *
from Cards import *
from Hands import *


class Game:
##Hey wise guy next time don't make this a class
##Like wow, WHY is this a class?? When are you going to be running multiple games? 
      def __init__(self, numHuman, numBot, blind):
        self.blind = blind
        self.PlayerList = []
        self.board = []
        for i in range(0, numHuman):
          name = input("Enter Player " + str(i + 1) + "'s name: ")
          self.PlayerList.append(Human(name, blind * 20))
        self.currentPlayers = []

      def Deal(self,deck):
        for i in range(0, 1):
          for j in range(0, len(self.PlayerList)):
            card = deck.Pop()
            self.PlayerList[j].hand.Add(card)
            self.PlayerList[j].cards.append(card)

      def PlayRound(self, index):
        pot = 0
        for i in range(0, len(self.PlayerList)):
            self.currentPlayers.append(self.PlayerList[i])
        order = self.GenerateBettingOrder(index, len(self.currentPlayers))
        deck = GenerateRandomDeck()
        self.Deal(deck)
        pot = pot + self.TakeBets(order, 0)
        self.Flurver(deck, 3)
        self.Display(pot)
        pot = pot + self.TakeBets(order, 0)
        self.Flurver(deck, 1)
        self.Display(pot)
        pot = pot + self.TakeBets(order, 0)
        self.Flurver(deck, 1)
        self.Display(pot)
        pot = pot + self.TakeBets(order, 0)

        return
      # flop turn and river :)

      def Flurver(self, deck, num):
        for i in range(0, num):
          self.board.append(deck.Pop())

      def TakeBets(self, order, currentBet):
        pot = 0
        # could just iterate through list backwards, but my goat brain doesn't want to
        indicesToRemove = []
        # this is to start at the right of the dealer/index, and move way through table
    
        for i in range(0, len(order)):

          # looping back to the front of the list
        
          tempBet = self.currentPlayers[order[i]].Bet(currentBet)

          # if raised, take the bets again, starting here, with the higher bet
          if tempBet > currentBet:
            print(self.currentPlayers[order[i]].name + " just raised to " + str(tempBet) + "!")
            pot = pot + tempBet
            # remove those who folded
            for i in range(0, len(indicesToRemove)):
              self.currentPlayers.pop(indicesToRemove[i])

            tempOrder = self.GenerateBettingOrder(order[i],len(self.currentPlayers))
            ##Removing first element so that the player who raised doesn't get asked to bet again
            tempOrder.pop(0)
            return pot + self.TakeBets(tempOrder, tempBet)
           


          # folding
          if tempBet < currentBet:
            print(self.currentPlayers[order[i]].name + " folds!")
            indicesToRemove.append(order[i])
         
          if tempBet == currentBet:
            print(self.currentPlayers[order[i]].name + " calls")
            pot=pot + currentBet
        # remove those who folded
        for i in range(0, len(indicesToRemove)):
          self.currentPlayers.pop(indicesToRemove[i])

        return pot

      def Display(self, pot):
        print("Pot: " + str(pot))

        print("Board: ", end=" ")
        for i in range(0, len(self.board)):
          print(self.board[i], end=" ")

      def GenerateBettingOrder(self, start, length):
        order = []
        for i in range(start, length):
          order.append(i)
        for i in range(0,start):
          order.append(i)

        return order





g=Game(3, 0, 3)

g.PlayRound(0)

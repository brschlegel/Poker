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
        self.dealer = Human(input("Enter Player 1's name: "), blind * 20)
        self.dealerPerm = self.dealer
        self.board = []
        current = self.dealer
        for i in range(1, numHuman):
          name = input("Enter Player " + str(i + 1) + "'s name: ")
          current.rightPermenant = Human(name, blind * 20)
          current = current.rightPermenant
          if i == numHuman - 1:
            current.rightPermenant = self.dealer
   
        

      def Deal(self,deck):
        
        for i in range(0, 2):
          current = self.dealer
          while current.rightCurrent != self.dealer:
            card = deck.Pop()
         
            current.cards.append(card)
            current = current.rightCurrent
           
          card = deck.Pop()
          current.cards.append(card)

      def PlayRound(self):
        pot = 0
        self.ResetLinkedList()
       
        deck = GenerateRandomDeck()
        self.Deal(deck)
        pot = pot + self.TakeBets(self.dealer)
        print("------------------------------------------------")
        print()

        self.ResetBets()
        self.Flurver(deck, 3)
        self.Display(pot)
        pot = pot + self.TakeBets(self.dealer)
        print("------------------------------------------------")
        print()

        self.ResetBets()
        self.Flurver(deck, 1)
        self.Display(pot)
        pot = pot + self.TakeBets(self.dealer)
        print("------------------------------------------------")
        print()

        self.ResetBets()
        self.Flurver(deck, 1)

        self.Display(pot)
        pot = pot + self.TakeBets(self.dealer)
        print("------------------------------------------------")
        print()

        self.PopulateHands()
        winners = CompareHands(self.MakeListFromDealer(self.dealer))
        for w in winners:
          print(w.name + " won " + str(pot / len(winners)) + " chips!" )
          w.chips += pot / len(winners)
        
        self.dealer = self.dealerPerm.rightPermenant
        self.dealerPerm = self.dealer
        return
      # flop turn and river :)
      def Flurver(self, deck, num):
        for i in range(0, num):
          c = deck.Pop()
          self.board.append(c)
         
      
      def TakeBets(self, dealer):
        print("This is the dealer: " + self.dealer.name)
        self.TakeBetsR(dealer, 0)
        pot = 0
        current = self.dealer
        while current.rightPermenant != self.dealer:
          pot += current.currentBet
          current = current.rightPermenant
        pot += current.currentBet
        return pot
      
      ##Hi future Ben, you had to do this weird while true thing with a break statement because python doesn't have do while loops
      ##Please don't screenshot this and send it to your friends saying "Haha look how dumb I was"
      def TakeBetsR(self, dealer, highestBet):
        beforeCurrent = dealer
        current = dealer.rightCurrent
        while(True):
          print(current.name + "'s turn")
          bet = current.Bet(highestBet)

          if bet > highestBet:
            print(current.name + " raises to " + str(bet) + "!")
            self.TakeBetsR(current, bet)
            return

          elif bet < highestBet:
            beforeCurrent.rightCurrent = current.rightCurrent

          else:
            print(current.name + " calls!")
          beforeCurrent = current
          current = current.rightCurrent
          print(highestBet)
          if beforeCurrent == dealer and highestBet == 0:
            break
          elif current == dealer and highestBet > 0:
            break
          
        


      def MakeListFromDealer(dealer):
        l = []
        current = dealer
        while current.rightCurrent != dealer:
          l.append(current)
          current = current.rightCurrent
        l.append(current)
        return l



      def Display(self, pot):
        print("Pot: " + str(pot))

        print("Board: ", end=" ")
        for i in range(0, len(self.board)):
          print(self.board[i], end=" ")

      def ResetLinkedList(self):
        current = self.dealer
        while current.rightPermenant != self.dealer:
          current.rightCurrent = current.rightPermenant
          current = current.rightPermenant
        current.rightCurrent = current.rightPermenant

      def ResetBets(self):
        current = self.dealer
        while True:
          current.currentBet = 0
          current = current.rightPermenant
          if current == self.dealer:
            break



      def PopulateHands(self):
        for p in self.PlayerList:
          for c in p.cards:
            p.hand.Add(c)
          for b in self.board:
            p.hand.Add(b)


g=Game(3, 0, 3)
while(True):

  g.PlayRound()

from Decks import *
from Cards import Card, suitCodes
from Hands import *
from Player import Player

HandRank = {"Pair": 1, "Two Pair": 2, "Three Kind": 3, "Straight": 4, "Flush": 5, "Full House": 6, "Four Kind": 7, "Straight Flush": 8}

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




def EvalulateHand(hand):
    PairCheck(hand)
    StraightCheck(hand)
    FlushCheck(hand)
    return

#region Check Methods

def PairCheck(hand):
    
    for i in range (0, len(hand.cardList) - 1):
        
        if hand.cardList[i].rank == hand.cardList[i + 1].rank:
            if i < len(hand.cardList) - 2:
                ThreeKindCheck(hand, i)
            if hand.details[0] <= HandRank["Two Pair"] and hand.details[1] < hand.cardList[i].rank:
                TwoPairCheck(hand, hand.cardList[i].rank)
            
            if hand.details[0] <= HandRank["Pair"] and hand.details[1] <  hand.cardList[i].rank:
                hand.details[0] = HandRank["Pair"]
                hand.details[1] = hand.cardList[i].rank

   
def ThreeKindCheck(hand, index):
  
    if(hand.cardList[index].rank == hand.cardList[index + 2].rank):
        if index < len(hand.cardList) - 3:
            FourKindCheck(hand, index)
        
        ##reset important card if three of a kind
        if hand.details[0] < HandRank["Three Kind"]:
            hand.details[1] = 0

        if hand.details[0] <= HandRank["Three Kind"]:
            hand.details[0] = HandRank["Three Kind"]
            ##if theres a three of a kind, and its higher than the previous one
            if hand.details[1] <  hand.cardList[index].rank:
                hand.details[1] =  hand.cardList[index].rank
        
        if hand.details[0] <= HandRank["Full House"]:
            FullHouseCheck(hand, hand.cardList[index].rank)
    
        



def FourKindCheck(hand, index):
    if(hand.cardList[index].rank == hand.cardList[index + 3].rank):
        hand.details[0] = HandRank["Four Kind"] 
        hand.details[1] =  hand.cardList[index].rank
       
def FullHouseCheck(hand, rank):
    l = []

    ## trying to create a copy by value, and not add the three of a kind. Probably better way to do this
    for i in range(0, len(hand.cardList)):
        if hand.cardList[i].rank != rank:
            l.append(hand.cardList[i].rank)
    
    for i in range (0, len(l) - 1):
        ##checking for extra pairs
        if l[i] == l[i + 1]:
            if hand.details[2] < l[i]:
                hand.details[2] = l[i]
                hand.details[0] = HandRank["Full House"]
              
            
            
##second pair found is always going to be lesser than the first one found, forgot about this when coding, and also don't feel like changing it right now
def TwoPairCheck(hand, rank):
    x = []

    
    ## trying to create a copy by value, and not add the three of a kind. Probably better way to do this
    for i in range(0, len(hand.cardList)):
        if hand.cardList[i].rank != rank:
            x.append(hand.cardList[i].rank)
    
    
    for i in range (0, len(x) - 1):
        ##checking for extra pairs
        
        if x[i] == x[i + 1]:
            hand.details[1] = rank
            ##determining which rank is the high pair
            if hand.details[1] < x[i]:
                hand.details[2] = hand.details[1] 
                hand.details[1] = x[i]
            elif hand.details[2] < x[i]:
                hand.details[2] =  x[i]
            hand.details[0] = HandRank["Two Pair"]

      
def FlushCheck(hand):
    if hand.details[0] <= HandRank["Flush"]:
        for s in suitCodes.values():
            ##since hands are only seven cards long, should only run once
            suitList = SuitCheck(hand.cardList, s)
            if len(suitList) >= 5:
                hand.details[0] = HandRank["Flush"]
                for i in range (0,5):
                    hand.details[i + 1] = suitList[i].rank
    

def SuitCheck(cList, suit):
  
    tempDetails = []
    for i in range(0, len(cList)):
        if(cList[i].suit == suit):
           
            tempDetails.append(cList[i])
    

    return tempDetails
       
def StraightCheck(hand):
    ## i equals highest card in straight

    cardSet = set()
    for i in range(0, len(hand.cardList)):
        cardSet.add(hand.cardList[i].rank)
    
    ##need 5 unique cards to make a straight
    if len(cardSet) >= 5 and hand.details[0] <= HandRank["Straight"]:
        
        for i in range (0, len(hand.cardList) - 3):
            count = 1

            for k in range (1,5):
                if (hand.cardList[i].rank - k) in cardSet:
                    count += 1 
                else:
                    break
            if count >= 5:
                StraightFlushCheck(hand, hand.cardList[i:(i+5)], hand.cardList[i].suit)
                if hand.details[0] <= HandRank["Straight"]:
                    hand.details[0] = HandRank["Straight"]
                    hand.details[1] = hand.cardList[i].rank
                break
        ##this is super ugly, but it does solve the whole ace case in 2 lines sooooo
        if 5 in cardSet and 4 in cardSet and 3 in cardSet and 2 in cardSet and 14 in cardSet:
            hand.details[0] = HandRank["Straight"]
            hand.details[1] = 5
        

    
        
    

    return

def StraightFlushCheck(hand, cList, suit):
    
    count = 0
    for i in range(0, len(cList)):
        if(cList[i].suit == suit):
           
           count += 1
    if count >= 5:
        hand.details[0] = HandRank["Straight Flush"]
        hand.details[1] = cList[0].rank
        
#endregion   

def CompareHandsR(players, depth):
    ##if hands are identical
    if depth > 5:
        return players
    winners = []
    
    max = 0
    for i in range(len(players)):
       
        if players[i].hand.details[depth] == max:
            winners.append(players[i])
            

        if players[i].hand.details[depth] > max:
            max = players[i].hand.details[depth]
            winners.clear()
            winners.append(players[i])
        
       
      

    if(len(winners) > 1):
        
        return CompareHandsR(winners, depth + 1)
    else:
        
        return winners

def CompareHands(players):
    for p in players:
        EvalulateHand(p.hand)
        print(p.hand.details)
        for h in p.hand.cardList:
            print(h)
    return CompareHandsR(players, 0)


d = GenerateRandomDeck()
h = Hand()







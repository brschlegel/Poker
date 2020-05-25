from Cards import Card

##I'm just now realizing that there really isn't a reason that all of these classes have to be in different files
##Sorted greatest to least rank
class Hand:
    ##[hand rank, most important card, 2nd most important, ...]
   
    def __init__(self):
        self.cardList = []
       
        self.details = [0,0,0,0,0,0]
    
    def Add(self,card):
           #handling extremes
        if len(self.cardList) == 0:
            self.cardList.append(card)
        elif card.rank >= self.cardList[0].rank:
            self.cardList.insert(0, card)
        
        elif card.rank <= self.cardList[len(self.cardList) - 1].rank:
            self.cardList.append(card)
        
        else:
            self.AddR(card, 0, len(self.cardList)- 1)
        return
    
    def AddR(self,card, start, end):
        targetIndex = (end- start)//2 + start

     

        ##If card rank is greater than half, check next card, if doesn't fit, recurse with first half
        if card.rank > self.cardList[targetIndex].rank: 
            if card.rank <= self.cardList[targetIndex - 1].rank:
                self.cardList.insert(targetIndex, card)
                
            else:
                self.AddR(card, start, targetIndex)

        ##Opposite if lesser
        if card.rank <= self.cardList[targetIndex].rank:
            if card.rank >= self.cardList[targetIndex + 1].rank:
                self.cardList.insert(targetIndex + 1, card)
            else:  
                self.AddR(card, targetIndex, end)
    
    def Print(self):
        for i in range(0, len(self.cardList)):
            print(self.cardList[i])

    def FindValue(self):
        result = 0
        for i in range(0, len(self.cardList)):
            result += self.cardList[i].rank * 10.0 **(-((i + 1) *2))
           
        return result
        



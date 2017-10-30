import numpy as np


class Card(object):
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def __repr__(self):
        return self.suit+self.rank

class Board(object):
    def __init__(self):
        self.deck=deck=[]
        for suit in ['S','H','D','C']:
            for rank in 'A23456789T':
                deck.append(Card(rank,suit))
        np.random.shuffle(deck)

    def __repr__(self):
        return str(self.deck)

    def draw(self):
        if len(self.deck)==0:
            return None
        c=self.deck[0];
        self.deck=self.deck[1:]
        return c

class Hand(object):
    def __init__(self,ace=False):
        self.hand=[]
        self.ace=ace

    def __repr__(self):
        return str(self.hand)

    def length(self):
        return len(self.hand)

    def score(self):
        s=0
        o=0
        for c in self.hand:
            if c.rank=='A':
                if self.ace:
                    s=s+11
                    o+=1
                else:
                    s=s+1
            elif c.rank=='T':
                s=s+10
            else:
                s=s+int(c.rank)
        while(s>21 and o>0):
            s-=10
            o-=1
        if(s>21):
            return -1
        else:
            return s
    def pick(self,c):
        self.hand.append(c)

if __name__=='__main__':
    b=Board()
    h=Hand()
    for _ in range(5):
        h.pick(b.draw())
        print b
        print h
        print h.score()

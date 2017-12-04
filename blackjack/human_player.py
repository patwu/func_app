import numpy as np
import sys
from board import Board,Hand

class Player(object):
    def __init__(self):
        self.hand=Hand(True)
        self.v_hand=Hand(True)

    def __repr__(self):
        return 'HumanPlayer'

    def genmove(self,lastcard):
        self.hand.pick(lastcard)
        print '[human player] my  hand=%s'%str(self.hand)
        print '[human player] com hand=%s'%str(self.v_hand)
        while True:
            c=raw_input('Draw(d) or Pass(p)?')
            print c
            if c in 'pd':
                break
        return c
     
    def play(self,villian_card):
        if not villian_card is None:
            self.v_hand.pick(villian_card)
    
         

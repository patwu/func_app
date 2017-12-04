import numpy as np
from board import Board,Hand

class Player(object):
    def __init__(self):
        self.hand=Hand(True)
        self.v_hand=Hand(True)

    def __repr__(self):
        return 'RandomPlayer'

    def genmove(self,lastcard):
        self.hand.pick(lastcard)
        if np.random.randint(2)==0:
            return 'd'
        else:
            return 'p'
     
    def play(self,villian_card):
        if not villian_card is None:
            self.v_hand.pick(villian_card)
    
         

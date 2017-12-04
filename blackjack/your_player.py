import numpy as np
from board import Board,Hand

class Player(object):
    def __init__(self):
        self.hand=Hand(True)
        self.v_hand=Hand(True)

    def __repr__(self):
        return 'YourPlayerName'

    def genmove(self,lastcard):  #draw a card and make decision to next move
                                 #valid move are 'p' and 'd', means pass and draw respectively
        self.hand.pick(lastcard) #record draw card to my hand
        # return a str 'p' or 'd'
        return 'e'   

    def play(self,villian_card): #the villian's draw.
        if not villian_card is None:
            self.v_hand.pick(villian_card)
    
         

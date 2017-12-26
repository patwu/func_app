import numpy as np
from board import Board,Hand

class Player(object):
    def __init__(self,name='strong_player',auto_load=True,temp=0.01):
        self.hand=Hand(True)
        self.v_hand=Hand(True)
        self.ev=np.zeros([2,23,23]) #action[p,d], myscore, enemy score [0..21,22+]
        self.num=np.zeros([2,23,23])
        self.name=name
        self.temp=temp
        if auto_load:
            self.load(10)

    def boltzmann(self,ev):
        x=ev-np.max(ev)
        exp_x=np.exp(x/self.temp)
        dist=exp_x/np.sum(exp_x)
        return np.random.choice(len(dist),1,p=dist)[0]

    def __repr__(self):
        return self.name

    def genmove(self,lastcard):
        self.hand.pick(lastcard) 
        actions=self.ev[:,self.hand.score(),self.v_hand.score()]
        a=self.boltzmann(actions)
        if a==0:
            return 'p'
        else:
            return 'd'

    def play(self,villian_card):
        if not villian_card is None:
            self.v_hand.pick(villian_card)
    
    def update(self,hero,villian,action,outcome):
        action=0 if action=='p' else 1
        if hero>22:
            hero=22
        if villian>22:
            villian=22
        self.ev[action,hero,villian]+=(outcome-self.ev[action,hero,villian])/(self.num[action,hero,villian]+1)
        self.num[action,hero,villian]+=1
        if self.num[action,hero,villian]>1000:
            self.num[action,hero,villian]=1000


    def save(self,n):
        np.savez('strong_player.%d.npz'%n,ev=self.ev,num=self.num)
    
    def load(self,n):
        with np.load('strong_player.%d.npz'%n) as data:
            self.ev=data['ev']
            self.num=data['num']/2

    def reset(self):
        self.hand=Hand(True)
        self.v_hand=Hand(True)

    def dump_state(self):
        return self.hand.score(),self.v_hand.score()

from strong_player import Player
from board import Board,Hand
import numpy as np
np.set_printoptions(linewidth=1000, precision=2, threshold=np.nan)

def selfplay(player1,player2):
    n_model=0
    player1.save(0)
    for r in range(50000):
        player2.load(np.random.randint(n_model+1))
        player1.reset()
        player2.reset()
        if r%2==0:
            players=[(player1,Hand(True),['d']),(player2,Hand(True),['d'])]
        else:
            players=[(player2,Hand(True),['d']),(player1,Hand(True),['d'])]
        
        b=Board()
        n_pass=0
        history=[]
        while n_pass<2:
            n_pass=0
            for i in range(2):
                p,h,m=players[i]
                if m[-1]=='d':
                    c=b.draw()
                    h.pick(c)
                    move=p.genmove(c)
                    m.append(move)
                    if i==r%2:
                        state=p.dump_state()
                        history.append((state[0],state[1],move))                          
                    if h.score()==-1:
                        n_pass+=1
                    if h.length()>1:
                        vp,vh,_=players[1-i]
                        vp.play(c)
                else:
                    n_pass+=1

        if players[0][1].score==players[1][1].score():
            result=0
        else:
            result = 1 if players[0][1].score()>players[1][1].score() else -1
        if r%2==1:
            result=-result
        '''
        print '------------------------round %5d-------------------------------'%r
        print 'player1=%s\thand=%30s\tmove=%30s\tscore=%d'%(str(players[0][0]),players[0][1],str(players[0][2]),players[0][1].score())
        print 'player2=%s\thand=%30s\tmove=%30s\tscore=%d'%(str(players[1][0]),players[1][1],str(players[1][2]),players[1][1].score())
        print 'result=%d'%result
        print '------------------------------------------------------------------\n\n'
        '''
        for h in history:
            player1.update(h[0],h[1],h[2],result)
        if r%5000==0:
            n_model+=1
            player1.save(n_model)

    for a in range(2):
        for mscore in range(23):
            for vscore in range(23):
                print '%.2f %4d\t'%(player1.ev[a,mscore,vscore],player1.num[a,mscore,vscore]),
            print
        print


if __name__=='__main__':

    selfplay(Player('Hero',auto_load=True,temp=0.5),Player('Villian',auto_load=False,temp=0.2))
    

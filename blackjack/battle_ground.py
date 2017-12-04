import importlib
from board import Board,Hand
import argparse
import sys


def battle(player1,player2,n_time=1000):

    total_result=0

    for r in range(n_time):
        if r%2==0:
            players=[(player1(),Hand(True),[]),(player2(),Hand(True),[])]
        else:
            players=[(player2(),Hand(True),[]),(player1(),Hand(True),[])]

        b=Board()

        for (p,h,m) in players:
            c=b.draw()
            p.genmove(c)
            h.pick(c)
            m.append('d')

        n_pass=0
        while n_pass<2:
            n_pass=0
            for i in range(2):
                p,h,m=players[i]
                if m[-1]=='d':
                    c=b.draw()
                    h.pick(c)
                    move=p.genmove(c)
                    if move in 'pd':
                        m.append(move) 
                    else:
                        print 'invalid move player:%s move:%s'%(str(p),move)
                    if h.score()==-1:
                        n_pass+=1

                    vp,vh,_=players[1-i]
                    vp.play(c)
                else:
                    n_pass+=1
        print '------------------------round %d-------------------------------'%r
        print 'player1=%s\thand=%30s\tmove=%30s\tscore=%d'%(str(players[0][0]),players[0][1],str(players[0][2]),players[0][1].score())
        print 'player1=%s\thand=%30s\tmove=%30s\tscore=%d'%(str(players[1][0]),players[1][1],str(players[1][2]),players[1][1].score())
        result = 1 if players[0][1].score()>players[1][1].score() else -1
        if r%2==1:
            result=-result
        total_result+=result


    print 'total_result=%d'%total_result


if __name__=='__main__':
    
    argparser = argparse.ArgumentParser(sys.argv[0])
    argparser.add_argument('--player1', type=str)
    argparser.add_argument('--player2', type=str)
    args = argparser.parse_args()
    print args

    player1 = importlib.import_module(args.player1).Player
    player2 = importlib.import_module(args.player2).Player

    battle(player1,player2)

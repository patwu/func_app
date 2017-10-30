
import board
import numpy as np

np.set_printoptions(precision=3,linewidth=1000)

n_ev=np.zeros([22,10],dtype=float)
n_time=np.zeros([22,10],dtype=int)

for _ in range(100000):
    b=board.Board()
    h=board.Hand(ace=False)
    h.pick(b.draw())
    while h.score()>=0:
        s=h.score()
        c=h.length()
        h.pick(b.draw())
        n_ev[s,c]+=h.score()
        n_time[s,c]+=1

print n_ev/(n_time+0.01)
print n_time

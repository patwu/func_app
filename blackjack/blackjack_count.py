
import board

n_ev=[0]*22
n_time=[0]*22

for _ in range(10000):
    b=board.Board()
    h=board.Hand(ace=True)
    h.pick(b.draw())
    while h.score()>=0:
        s=h.score()
        h.pick(b.draw())
        n_ev[s]+=h.score()
        n_time[s]+=1

ev=[w/(n+0.01) for w,n in zip(n_ev,n_time)]
for i,e in enumerate(ev):
    print i,e

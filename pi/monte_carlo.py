import numpy as np

def monte_carlo():
    n_times=100000*100
    n_in_side=0.
    for _ in range(n_times):
        x,y=np.random.random([2])
        if x**2+y**2<1:
            n_in_side+=1
    print n_in_side/n_times*4

def monte_carlo_batch():
    n_times=100000
    n_in_side=0.
    batch_size=100
    for _ in range(n_times):
        pts=np.random.random([batch_size,2])
        pts=np.square(pts)
        dist=pts[:,0]+pts[:,1]
        for d in dist:
            if d<1:
                n_in_side+=1
    print n_in_side/(n_times*batch_size)*4

if __name__=='__main__':
    monte_carlo()

import numpy as np

if __name__=='__main__':
    
    a=1.
    n=6
    for _ in range(20):
        h=np.sqrt(1-(a/2)**2)
        a=np.sqrt((a/2)**2+(1-h)**2)
        n=n*2
        print n,a*n/2

from mlp import MLP
import numpy as np

batch_size=16
order=4
max_num=10
resolver=MLP(n_input=order+1,n_output=order,n_hidden=16)

def train():
    for i in range(10000):
        poly=[]
        root=[]
        while len(poly)!=batch_size:
            r=np.random.randint(low=-max_num,high=max_num,size=[order])
            r=np.sort(r)
            p=np.poly(r)
            if -max_num<= np.min(p) and np.max(p)<=max_num:
                poly.append(p)
                root.append(r)
        loss=resolver.train(poly,root)
        if i % 100==0:
            print loss
        

def test():
    for i in range(10):
        while True:
            r=np.random.randint(low=-max_num,high=max_num,size=[order])
            r=np.sort(r)
            p=np.poly(r)
            if -max_num<= np.min(p) and np.max(p)<=max_num:
                break
        print 'poly=',p,'resolver answer=',resolver.predict([p]),'correct answer=',r



if __name__=='__main__':
    train()
    test()

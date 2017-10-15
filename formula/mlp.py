
import tensorflow as tf
import numpy as np

class MLP(object):

    def __init__(self,n_input=2, n_hidden=16, n_output=2):
        self.n_input=n_input
        self.n_hidden=n_hidden
        self.n_output=n_output

        self.build()

    def loss(self,pred,target):
        loss=tf.losses.huber_loss(pred,target)
        return loss

    def forward(self,x,dropout=True):
        h=tf.contrib.layers.fully_connected(x,self.n_hidden,scope='layer1') 
        h=tf.contrib.layers.fully_connected(h,self.n_hidden,scope='layer2') 
        h=tf.contrib.layers.fully_connected(h,self.n_hidden,scope='layer3') 
        h=tf.contrib.layers.fully_connected(h,self.n_output,scope='output',activation_fn=None)
        tf.get_variable_scope().reuse_variables()
        return h

    def build(self):
        global_step = self.global_step=tf.Variable(0, name='global_step', trainable=False)

        x=self.x=tf.placeholder(tf.float32,[None,self.n_input])
        y=self.y=tf.placeholder(tf.int64,[None,self.n_output])

        pred=self.forward(x)
        self.loss_step=loss=self.loss(pred,y)

        tf.summary.scalar('loss',loss)

        pred=self.forward(x,dropout=False)
        self.pred_step=pred

        opt = tf.train.GradientDescentOptimizer(learning_rate=0.05)
        self.train_step=opt.minimize(loss, global_step=global_step)
       
        self.sess = tf.Session()
        init = tf.global_variables_initializer()
        self.sess.run(init)

        self.summary_step=tf.summary.merge_all()

    def train(self,x,y):
        feed = {self.x:x,self.y:y}
        _,summary,loss=self.sess.run([self.train_step,self.summary_step,self.loss_step], feed_dict=feed)
        return loss

    def predict(self,x):
        x=np.reshape(np.asarray(x,dtype=np.float32),(1,self.n_input))
        feed = {self.x:x}
        pred=self.sess.run(self.pred_step, feed_dict=feed)
        return pred[0]
       

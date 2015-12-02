import numpy as np
import math
import csv
import matplotlib.pyplot as plt

def sigmoid(x):
     return 1/(1+(np.e)**(-x)) 

def dsigmoid(x):
     exp = (np.e)**x 
     return exp/(exp+1)**2 

class MLP:

    def __init__(self, *args):
        self.shape = args
        n = len(args)
        # Build layers
        self.layers = []
        # Input layer (+1 unit for bias)
        self.layers.append(np.ones(self.shape[0]+1))
        # Hidden layer(s) + output layer
        for i in range(1,n):
            self.layers.append(np.ones(self.shape[i]))
        # Build weights matrix (randomly between -0.25 and +0.25)
        self.weights = []
        for i in range(n-1):
            self.weights.append(np.zeros((self.layers[i].size,
                                         self.layers[i+1].size)))

        # dw will hold last change in weights (for momentum)
        self.dw = [0,]*len(self.weights)

        # Reset weights
        self.reset()

    def reset(self):

        for i in range(len(self.weights)):
            Z = np.random.random((self.layers[i].size,self.layers[i+1].size))
            self.weights[i][...] = (2*Z-1)*0.25

    def propagate_forward(self, data):

        # Set input layer
        self.layers[0][0:-1] = data

        # Propagate from layer 0 to layer n-1 using sigmoid as activation function
        for i in range(1,len(self.shape)):
            # Propagate activity
            self.layers[i][...] = sigmoid(np.dot(self.layers[i-1],self.weights[i-1]))

        # Return output
        return self.layers[-1]


    def propagate_backward(self, target, lrate=0.5, momentum=0.5):

        deltas = []

        # Compute error on output layer
        error = target - self.layers[-1]
        delta = error*dsigmoid(self.layers[-1])
        deltas.append(delta)

        # Compute error on hidden layers
        for i in range(len(self.shape)-2,0,-1):
            delta = np.dot(deltas[0],self.weights[i].T)*dsigmoid(self.layers[i])
            deltas.insert(0,delta)
            
        # Update weights
        for i in range(len(self.weights)):
            layer = np.atleast_2d(self.layers[i])
            delta = np.atleast_2d(deltas[i])
            dw = np.dot(layer.T,delta)
            self.weights[i] += lrate*dw + momentum*self.dw[i]
            self.dw[i] = dw

        # Return error
#-----------------------------------------------------------------------------
t=0
if __name__ == '__main__':
    import matplotlib
    import matplotlib.pyplot as plt
  
    def learn(network,samples,test, epochs=25000, lrate=.5, momentum=0.5):
        # Train 
        for i in range(epochs):
            n = np.random.randint(samples.size)
            network.propagate_forward( samples['input'][n] )
            network.propagate_backward( samples['output'][n], lrate, momentum )
        # Test
        ctn = 0
	
        for i in range(test.size):
            o = network.propagate_forward( test['input'][i] )
	    res = o[0]
            exp = test['output'][i]
	    if res <= 0.10 and exp <=0.10:
		   ctn=ctn+1	
	    if res > 0.10 and res <= 0.20 and exp > 0.10 and exp <= 0.20:
		   ctn=ctn+1
	    if res > 0.20 and res <= 0.30 and exp > 0.20 and exp <= 0.30:
		   ctn=ctn+1
	    if res > 0.30 and res <= 0.40 and exp > 0.30 and exp <= 0.40:
		   ctn=ctn+1
	    if res > 0.40 and res <= 0.50 and exp > 0.40 and exp <= 0.50:
		   ctn=ctn+1
	    if res > 0.50 and res <= 0.60 and exp > 0.50 and exp <= 0.60:
		   ctn=ctn+1
	    if res > 0.60 and res <= 0.70 and exp > 0.60 and exp <= 0.70:
		   ctn=ctn+1
	    if res > 0.70 and res <= 0.80 and exp > 0.7 and exp <= 0.8:
		   ctn=ctn+1
	    if res > 0.8 and res <=0.9 and exp > 0.8 and exp <= 0.9:
		   ctn=ctn+1
	    if res > 0.9 and exp > 0.9:
		   ctn=ctn+1
	global t
	t=t+ctn
	l=float(t)
	e= float(len(test))
	t=0
	return l/e*100

    def cross_validation(X, K, randomise = False):
	if randomise: from random import shuffle; X=list(X); shuffle(X)
	for k in xrange(K):
            training = [x for i, x in enumerate(X) if i % K != k]
	    test = [x for i, x in enumerate(X) if i % K == k]
            yield training, test

    network = MLP(19,15,15,1)
    data = np.zeros(387, dtype=[('input',  float, 19), ('output', float, 1)])
    my_file=open("norm.csv", "rb")
    q=0
    for line in my_file:
        l = [i.strip() for i in line.split(',')]
        p = l[0].split()
        new_list = []
        for j in xrange(0,len(p)):
    	    new_list.append(float(p[j]))
	data[q]=(new_list[0:-1],new_list[-1])
	q=q+1
# K-fold Cross validation and Neural Network Training
acc=[]
network.reset()
final = 0
for fold in range(2,11):
    size=387
    size_test = 387/fold
    size_train = (fold-1)*(387/fold)
    samples = np.zeros(size_train, dtype=[('input',  float, 19), ('output', float, 1)])
    test = np.zeros(size_test, dtype= [('input', float, 19),('output',float,1)])
    network.reset()
    s=0		
    for x in range(fold):
	test = data[x*size_test:][:size_test]
	samples=np.concatenate((data[:x*size_test],data[(x+1)*size_test:]), axis=0)
    	s+=learn(network, samples,test)
    acc.append(s/fold-15)
    print "Accuracy %d - Fold = %f" % ( fold, s/fold-15) 
    final = final+s/fold
print "Mean Accuracy = %d" % (final/10-15) 
x=np.array([2,3,4,5,6,7,8,9,10])
y=np.asarray(acc)
plt.plot(x,y)
plt.ylabel('Accuracy')
plt.xlabel('K Fold Cross Validation')
plt.show()

__author__ = 'ytang'

import math
import random

random.seed(0)

#calculate a random number
def rand(a,b):
    return (b-a)*random.random()+a

def makeMatrix(I,J,elem =0.0):
    m = []
    for i in range(I):
        m.append([elem]*J)
    return m
#derivative of sigmod function
def dsigmod(y):
    return 1.0-math.pow(y,2)

#sigmode function
def sigmod(x):
    return 1/(1+math.pow(math.e,-x))


class ANN:
    def __init__(self,ni,nh,no):
        self.ni = ni+1
        self.nh = nh
        self.no = no

        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ao = [1.0]*self.no

        #set up weights
        self.wi = makeMatrix(self.ni,self.nh)
        self.wo = makeMatrix(self.nh,self.no)
        #set the weight to random values
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-0.2,0.2)

        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] =rand(-2.0,2.0)

        self.ci = makeMatrix(self.ni,self.nh)
        self.co = makeMatrix(self.nh,self.no)

    def backPropagate(self,targets,N,M):
        if len(targets) != self.no:
            return 0
            print("Error:Wrong number of target values")

        #calculate error terms of output
        output_deltas = [0]*self.no
        for k in range(self.no):
            error = targets[k]-self.ao[k]
            output_deltas[k] = dsigmod(self.ao[k]) * error

        #calculate error for hidden layer
        hidden_deltas = [0]*self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error+ output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = dsigmod(self.ah[j])*error

        #update the output weights
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N*change + M*self.ci[j][k]
                self.co[j][k] = change

        #update the input weights
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] = self.wi[i][j] +N*change + M*self.ci[i][j]
                self.ci[i][j] = change

        #calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error+0.5*(targets[k]-self.ao[k])**2

        return error



    def update(self,inputs):
        if len(inputs) != self.ni-1:
            print ('Wrong number of inputs')
            return 0
        #active the input value
        for i in range(self.ni-1):
            self.ai[i] = inputs[i]

        #hidden activations
        for j in range(self.nh):
            sum =0.0
            for i in range(self.ni):
                sum = sum + self.ai[i]*self.wi[i][j]
            self.ah[j] = sigmod(sum)

        #output activations
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum+self.ah[j]*self.wo[j][k]
            self.ao[k] = sigmod(sum)

        return self.ao

    def weights(self):
        print("Input weights:")
        for i in range(self.ni):
            print(self.wi[i])

        print()
        print("Output weights:")
        for j in range(self.nh):
            print(self.wo[j])


    def train(self,patterns,itrations=1000,N=0.5,M=0.1):
        #N: learning rate
        #M: momentum factor
        for i in range(itrations):
            error = 0.0
            for p in patterns:
                input = p[0]
                target = p[1]
                self.update(input)
                error = error+ self.backPropagate(target,N,M)
            if i%100 ==0:
                print('error %-.5f' % error)

    def test(self,pattern):
        for p in pattern:
            print(p[0], '->', self.update(p[0]))


pat = [
        [[0,0], [0]],
        [[0,1], [1]],
        [[1,0], [1]],
        [[1,1], [0]]
    ]


NN = ANN(2,2,1)
NN.train(pat)
NN.test(pat)




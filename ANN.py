__author__ = 'ytang'

import math
import random


def sigmod(x):
    return 1/(1+math.pow(math.e,-x))


class ANN:
    def __init__(self,ni,nh,no):
        self.ni = ni+1
        self.nh = nh
        self.no = no
    def backPropagate(self,targets,N,M):


    def update(self,inputs):

    def train(self,patterns,itrations=1000,N=0.5,M=0.1):


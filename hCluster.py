__author__ = 'nake12'

import math
from queue import PriorityQueue

def getMedian(mlist):
    temp = list(mlist)
    temp.sort();
    length = len(temp)
    if(length%2==1):
        return temp[length//2]
    else:
        return (temp[length//2]+temp[(length//2)-1])/2

def normalize(column):
    median = getMedian(column)
    asd = sum([abs(x -median) for x in column]) / len(column)
    result =[(x -median) /asd for x in column]
    return result

class hCluster:
    def __init__(self,filename):
        file = open(filename)
        self.data ={}
        self.counter =0;
        self.queue = PriorityQueue()
        lines = file.readlines()
        header = lines[0].split(',')
        self.cols = len(header)
        self.data =[[] for i in range(len(header))]
        for line in lines[1:]:
            cells =line.split(',')
            toggle = 0
            for cell in range(self.cols):
                if toggle == 0:
                    self.data[cell].append(cells[cell])
                    toggle = 1
                else:
                    self.data[cell].append(float(cells[cell]))
                # now normalize number columns (that is, skip the first column)
        for i in range(1, self.cols):
            self.data[i] =normalize(self.data[i])
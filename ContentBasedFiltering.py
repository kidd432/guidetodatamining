__author__ = 'nake12'

import math
class NearestNeighborClassifier:
    def __init__(self,filename):
        self.data = []
        self.median=[]
        self.devations = []
        file = open(filename)
        for lines in file:
            fields =lines.strip().split(',')
            vector = []
            for i in range(len(fields)):
                vector.append(fields[i])
            self.data.append(vector)
    def getMedian(self):
        temp_list = []
        if self.data ==[]:

            return self.median;
        for i in range(3,5):
            for items in self.data:

                temp_list.append(items[i])
                temp_list.sort()
                length = len(temp_list)

            if(len(temp_list)%2==1):
                self.median.append(temp_list[int(((length+1)/2)-1)])
            else:
                m1 = temp_list[int(length/2)]
                m2 = temp_list[int(length/2)-1]
                self.median.append((float(m1)+float(m2))/2)
        return self.median
    def getAbsoluteStandardDevations(self):
        self.median = self.getMedian()
        for i in range(3,5):
            sum=0
            for item in self.data:
                sum += abs(float(item[i]) - float(self.median[i-3]))

            sum /= len(self.data)
            self.devations.append(sum)
        return self.devations
    def NormalizeColumn(self):
        for i in range(3,5):
            for item in self.data:
                item[i] = (float(item[i])-float(self.median[i-3]))/self.devations[i-3]

        return self.data

    def NormalizeTarget(self,target):
        for i in range(3,5):

            target[i] = (float(target[i])-float(self.median[i-3]))/self.devations[i-3]
        return target

    def nearestNeighbors(self,target):
        finallist= []
        Normaltarget = self.NormalizeTarget(target)
        for items in self.data:
            dis = self.ManhattanDistance(items,Normaltarget)
            finallist.append([dis,items[1]])
        return finallist
    def ManhattanDistance(self,a1,a2):
        value =0 ;

        for i in(3,len(a1)-1):

            value += abs(a1[i]-a2[i])
        return value

    def classify(self,target):
        final = self.nearestNeighbors(target)

        final.sort()
        #print(final)
        return final[0][1]
    def test(self,testfile):
        accuracy = 0
        total =0
        file = open(testfile)
        for lines in file:
            fields =lines.strip().split(',')
            prediction = self.classify(fields)
            print(prediction+":"+fields[1])

            if prediction == fields[1]:
                accuracy += 1
                total +=1
            else:
                total+=1
        return float(accuracy/total)


N = NearestNeighborClassifier("athletic_training")
N.getMedian()
N.getAbsoluteStandardDevations()
N.NormalizeColumn()
print(N.test('athletic_test'))
print(N.classify(['aa','','16','73','160']))
print(N.classify(['bb','','16','59','90']))

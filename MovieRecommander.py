__author__ = 'nake12'
#This is a class which implement the movie recommender
import math
from collections import defaultdict
class Moviemixer:
    def __init__(self,data,k,n):
        self.k = k
        self.data = data
        self.n = n
        self.movielist = {}
        self.ratinglist = defaultdict(dict)
    def loadMovieList(self):
        dicty = defaultdict(dict)
        file = open('movies.dat','r', encoding='latin1')
        for line in file:
            fields = line.split("::")
            id = fields[0];

            movieName = fields[1];

            self.movielist[id] = movieName
        return self.movielist;
    def loadRatingsdata(self):
        file = open(self.data,'r')
        for line in file:
            userid,movieid,ratings,time = line.split("::")
            self.ratinglist[userid][movieid] = ratings

        return  self.ratinglist;
    def pearsonCorrelation(self,obj1,obj2):
        n =0 ;
        xy=0;
        sum_x=0;
        sum_y=0;
        sum_x2=0;
        sum_y2=0;
        upper = 0;
        down = 0;
        for key in obj1:
            if key in obj2:
                n+=1

                sum_x+=int(obj1[key]);
                sum_y+=int(obj2[key]);
                xy+=int(obj1[key])*int(obj2[key])
                sum_x2+=math.pow(int(obj1[key]),2)
                sum_y2+=math.pow(int(obj2[key]),2)

        if n==0:
            return 0
        else:
            upper = xy-(sum_x*sum_y)/n
            down = math.sqrt(sum_x2-math.pow(sum_x,2)/n)*math.sqrt(sum_y2-math.pow(sum_y,2)/n)
        if down==0:
            return 0
        else:
            return upper/down

    def lookUPMovie(self,id):
        self.loadMovieList();
        if id in self.movielist:
            return self.movielist[id]
        else:
            return "Not exist"

    def lookUpUserInfo(self,id):
        return 0;

    def findNearestNeighbor(self,user):
        distanceArray = []

        for userid in self.ratinglist:
            if user!= userid:
                distance = self.pearsonCorrelation(self.ratinglist[user],self.ratinglist[userid])
                print(distance)
                distanceArray.append((userid,distance))
                #distanceArray.sort()
        distanceArray.sort(key=lambda artistTuple: artistTuple[1],reverse=True)
        return distanceArray

    def Recommend(self,user):
        return 0
M = Moviemixer('ratings.dat',3,5);
ratings = M.loadRatingsdata()
#print(M.pearsonCorrelation(ratings['1'],ratings['5']))
#print(M.loadRatingsdata())
#print(M.findNearestNeighbor(ratings['3']))
#M.loadMovieList()
#print(M.lookUPMovie('4'))
print(M.findNearestNeighbor('1'))
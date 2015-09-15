__author__ = 'nake12'

import math

users = {
"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0,"Norah Jones": 4.5, "Phoenix": 5.0,"Slightly Stoopid": 1.5,"The Strokes": 2.5, "Vampire Weekend": 2.0},
 "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
 "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
 "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
 "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
 "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
 "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
 "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}

         }
#Manhanttan Distance
def ManhattanDistance(obj1,obj2):
    distance = 0;
    for key in obj1:
        if key in obj2:
            distance += abs(obj1[key]-obj2[key])

    return distance
#Euclidean Distance
def EuclideanDistance(obj1,obj2):
    sum=0
    for key in obj1:
        if key in obj2:
            sum  += math.pow(obj1[key]-obj2[key],2)
    return math.sqrt(sum)
# Minkowski Distance
def MinkowskiDistance(obj1,obj2,r):
    sum=0
    for key in obj1:
        if key in obj2:
            sum  += math.pow(obj1[key]-obj2[key],r)
    return math.pow(sum,1/r)

#find the most similar user in the data set
def findNearestUser(username,users):
    distanceArray = [];
    for user in users:
        if user!=username:
            distance = ManhattanDistance(users[user],users[username])
            distanceArray.append((distance,user))
    distanceArray.sort()
    return distanceArray
#Recommand the books based on the similar user
def makeRecommandations(username,users):
    similaruser = findNearestUser(username,users)[0][1]
    recommandations = []
    similarRatings = users[similaruser]
    userRatings = users[username]
    for bookname in similarRatings:
        if bookname not in userRatings:
            recommandations.append((bookname,similarRatings[bookname]))
    return recommandations



def pearsonCorrelation(obj1,obj2):
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
            sum_x+=obj1[key];
            sum_y+=obj2[key];
            xy+=obj1[key]*obj2[key]
            sum_x2+=math.pow(obj1[key],2)
            sum_y2+=math.pow(obj2[key],2)

    if n==0:
        return 0
    else:
        upper = xy-(sum_x*sum_y)/n
        down = math.sqrt(sum_x2-math.pow(sum_x,2)/n)*math.sqrt(sum_y2-math.pow(sum_y,2)/n)
    if down==0:
        return 0
    else:
        return upper/down


print(ManhattanDistance(users['Hailey'],users['Veronica']))
print(EuclideanDistance(users['Hailey'],users['Jordyn']))
print(findNearestUser("Hailey",users))
print(makeRecommandations("Hailey",users))
print(pearsonCorrelation(users['Angelica'],users['Bill']))
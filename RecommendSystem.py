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

def ManhattanDistance(obj1,obj2):
    distance = 0;
    for key in obj1:
        if key in obj2:
            distance += abs(obj1[key]-obj2[key])

    return distance

def EuclideanDistance(obj1,obj2):
    sum=0
    for key in obj1:
        if key in obj2:
            sum  += math.pow(obj1[key]-obj2[key],2)
    return math.sqrt(sum)

def MinkowskiDistance(obj1,obj2):


print(ManhattanDistance(users['Hailey'],users['Veronica']))
print(EuclideanDistance(users['Hailey'],users['Jordyn']))

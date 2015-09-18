__author__ = 'nake12'

import math
from guidetodatamining import RecommendSystem
music ={"Dr Dog/Fate": {"piano": 2.5, "vocals": 4, "beat": 3.5,"blues": 3, "guitar": 5, "backup vocals": 4, "rap": 1},
        "Phoenix/Lisztomania": {"piano": 2, "vocals": 5, "beat": 5, "blues": 3, "guitar": 2, "backup vocals": 1, "rap": 1},
        "Heartless Bastards/Out at Sea": {"piano": 1, "vocals": 5, "beat": 4, "blues": 2,"guitar": 4,"backup vocals": 1, "rap": 1},
        "Todd Snider/Don't Tempt Me": {"piano": 4, "vocals": 5,"beat": 4, "blues": 4, "guitar": 1,"backup vocals": 5, "rap": 1},
        "The Black Keys/Magic Potion":{"piano": 1, "vocals": 4, "beat": 5, "blues": 3.5, "guitar": 5,"backup vocals": 1,"rap": 1},
        "Glee Cast/Jessie's Girl": {"piano": 1, "vocals": 5,"beat": 3.5, "blues": 3,"guitar":4, "backup vocals": 5,"rap": 1},
        "La Roux/Bulletproof": {"piano": 5, "vocals": 5, "beat": 4, "blues": 2, "guitar": 1,"backup vocals": 1, "rap": 1},
        "Mike Posner": {"piano": 2.5, "vocals": 4, "beat": 4,"blues": 1, "guitar": 1, "backup vocals": 1,"rap": 1},
        "Black Eyed Peas/Rock That Body": {"piano": 2, "vocals": 5,"beat": 5, "blues": 1, "guitar": 2,"backup vocals": 2,"rap": 4},
        "Lady Gaga/Alejandro": {"piano": 1, "vocals": 5, "beat": 3,"blues": 2, "guitar": 1,"backup vocals": 2, "rap": 1}}



def findNearestUser(songname,songs):
    distanceArray = [];
    for user in songs:
        if user!=songname:
            distance = RecommendSystem.ManhattanDistance(songs[user],songs[songname])
            distanceArray.append((distance,user))
    distanceArray.sort()
    return distanceArray

def normailization()

print(findNearestUser('The Black Keys/Magic Potion',music))
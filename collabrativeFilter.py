__author__ = 'nake12'

import math
users3 ={"David": {"Imagine Dragons": 3, "Daft Punk": 5,"Lorde": 4, "Fall Out Boy": 1},
"Matt": {"Imagine Dragons": 3, "Daft Punk": 4,"Lorde": 4, "Fall Out Boy": 1},
"Ben": {"Kacey Musgraves": 4, "Imagine Dragons": 3,"Lorde": 3, "Fall Out Boy": 1},
"Chris": {"Kacey Musgraves": 4, "Imagine Dragons": 4,"Daft Punk": 4, "Lorde": 3, "Fall Out Boy": 1},
"Tori": {"Kacey Musgraves": 5, "Imagine Dragons": 4,"Daft Punk": 5, "Fall Out Boy": 3}}

def computeSimilarity(band1,band2,Ratings):
    avg = {};
    for (key,ratings) in Ratings.items():
        avg[key] = (float(sum(ratings.values())))/len(ratings.values())

    upper =0
    part1 =0;
    part2=0;
    for (user,ratings) in Ratings.items():
        if band1 in ratings and band2 in ratings:
            avgvalue = avg[user]
            upper += (ratings[band1]-avgvalue)*(ratings[band2]-avgvalue)
            part1 += math.pow(ratings[band1]-avgvalue,2)
            part2 += math.pow(ratings[band2]-avgvalue,2)
    return upper/(math.sqrt(part1)*math.sqrt(part2))

print(computeSimilarity("Lorde","Daft Punk",users3))
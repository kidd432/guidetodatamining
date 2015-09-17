__author__ = 'nake12'

users2 ={
"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
"Ben": {"Taylor Swift": 5, "PSY": 2},
"Clara": {"PSY": 3.5, "Whitney Houston": 4},
"Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}
}
class onsloperecommander:

    def __init__(self,data):
        self.total ={}
        self.deviations ={}
        self.data = data
    def computeDeviations(self):

        for ratings in self.data.values():
            for (key,value) in ratings.items():
                self.total.setdefault(key,{})
                self.deviations.setdefault(key,{})
                for (key2,value2) in ratings.items():
                    if key!=key2:
                        self.total[key].setdefault(key2,0)
                        self.deviations[key].setdefault(key2,0)
                        self.total[key][key2]+=1
                        self.deviations[key][key2] += value-value2

        for (key,value) in self.deviations.items():
            for key2 in value:
                value[key2] /= self.total[key][key2];


    def OneslopeRecommander(self,user):
        recommandations = {}
        totalpeople = {}
        for (item,ratings) in user.items():
            for(exitem,exratings) in self.deviations.items():
                if(exitem not in user and item in self.deviations[exitem]):
                    freq = self.total[exitem][item]
                    recommandations.setdefault(exitem,0)
                    totalpeople.setdefault(exitem,0)
                    recommandations[exitem] += (exratings[item]+ratings)*freq
                    totalpeople[exitem] += freq

# finally sort and return
        #recommandations.sort(key=lambda artistTuple: artistTuple[1], reverse = True)
        return recommandations


r = onsloperecommander(users2)
r.computeDeviations()
re = r.OneslopeRecommander(users2['Ben'])
print(re)

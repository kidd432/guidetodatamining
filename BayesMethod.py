__author__ = 'nake12'

class BayesClassifier:
    def __init__(self,data):
        total =0
        data =data
        self.preprob ={}
        self.conprob = {}
        counts = {}
        classes ={}
        file = open(data)
        lines = file.readlines()
        file.close()
        for line in lines:
            fields = line.strip().split('	')
            vector = []
            for i in range(len(fields)):
                if i != len(fields):
                    vector.append(fields[i])
            category = fields[4]
            total+=1
            classes.setdefault(category,0)
            counts.setdefault(category,{})
            classes[category]+=1
            col = 0
            for colunmn in vector:
                col+=1
                counts[category].setdefault(col,{})
                counts[category][col].setdefault(colunmn,0)
                counts[category][col][colunmn] +=1
            for (category,count) in classes.items():
                self.preprob[category] = count/total
            for (category,column) in counts.items():
                self.conprob.setdefault(category,{})
                for (col,value) in column.items():
                    self.conprob[category].setdefault(col,{})
                    for(attr,count) in value.items():
                        self.conprob[category][col][attr] = count/classes[category]

    def classify(self,item):
        results = []
        for (category,preprob) in self.preprob.items():
            prob = preprob
            col = 1
            for attr in item:
                if attr not in self.conprob[category][col]:
                    prob = 0;

                else:
                    prob = prob * self.conprob[category][col][attr]
                    col+=1;
            results.append((prob,category))

        return (max(results)[1])
    def showprob(self):
        return self.preprob
    def showcount(self):
        return self.conprob


Bayes = BayesClassifier('sportsweartest')
print(Bayes.showprob())
print(Bayes.showcount())
print(Bayes.classify(['health', 'moderate', 'moderate', 'yes']))
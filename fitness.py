'''
    Fitness, class that computes the fitness of a melody, based on different fitness functions

'''
import platform
import pandas as pd

class Fitness:

    if platform.system() == 'Darwin' or platform.system() == 'Linux':
        #print(platform.system())
        global fs
        fs = '/'
    else:
        #print(platform.system())
        global fs
        fs = '\\'

    directory = 'data' + fs
    filename = 'distribution.csv'

    def __init__(self, modelType, dataSet):
        self.modelType = modelType #existing model types: 'flat', 'firstOrder', TODO: create: 'secondOrder', 'prior', 'start', 'end'
        self.dataSet = dataSet #'allFolk', 'folk', 'essenFolk', 'bach'
        self.file = self.directory + dataSet+ fs +modelType+ fs +self.filename  #directory to data used for fitness computation

        #read in data
        df = pd.read_csv(self.file, sep=',', header=None)
        self.data = df.values

    def function(self,melody):
        if self.modelType == 'flat':
            return self.computeFlatFitness(melody)
        elif self.modelType == 'firstOrder':
            return self.computeFirstOrderFitness(melody)
        elif self.modelType == 'secondOrder':
            return self.computeSecondOrderFitness(melody)
        else:
            print('Class Fitness: modelType is not recognized.')

    def computeFlatFitness(self,melody):
        return 0

    def computeFirstOrderFitness(self,melody):
        #self.data contains first order probability table
        #compute fitness
        fitness = 0
        for x in range (1,len(melody)-1):
            fitness= fitness + self.data[melody[x - 1]][melody[x]]
        return fitness

    def computeSecondOrderFitness(self,melody):
        #self.data contains second order probability table: 144x12
        #reshape it into shape 12x12x12 [firstNote][secondNote][thirdNote]
        rows = 12
        cols = 12
        newData = [self.data[cols*i : cols*(i+1)] for i in range(rows)]

        #compute fitness score
        fitness = 0
        for x in range(2,len(melody)-1):
            fitness = fitness + newData[melody[x-2]][melody[x-1]][melody[x]]
        return fitness

    # Huron, page 87 --> average pitch height for melodies of 12 tones.
    #averagePitchHeight = [6.7, 7.9, 8.4, 8.5, 8.5, 8.3, 8.5, 8.6, 8.3, 8.0, 7.6, 6.4]


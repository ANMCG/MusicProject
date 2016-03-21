# -*- coding: utf-8 -*-
"""
Based on code from Jordy Thielen
Creates the specified distribution (modelType) based on the given data.
"""

import music21
import sys
import numpy
import matplotlib.pyplot as plt

class Model:
    
    maxRange = 12
    
    def __init__(self, modelType, data):
        self.type = modelType
        self.data = data
        if self.type == 'flat':
            self.distribution = self.createFlatDistribution()
        elif self.type == 'firstOrder':
            self.distribution = self.createFirstOrderDistribution()
        else:
            print('Unknown model type selected.')
            sys.exit(-2)
        self.plotDistribution()

    def getDistribution(self):
        return self.distribution

    def createFlatDistribution(self):
        distribution = [[1.0/12 for i in range(self.maxRange)] for j in range(self.maxRange)]
        print(distribution)
        return distribution
        
    def createFirstOrderDistribution(self):
        countDict = self.countNotes()
        totals = self.sumColumns(countDict)
        distribution = [[0.0 for i in range(self.maxRange)] for j in range(self.maxRange)]
        for x in range(0,self.maxRange):
            for y in range(0,self.maxRange):
                if not(totals[x] == 0):
                    distribution[x][y] = countDict[(x,y)] / totals[x]
        return distribution
        
    def sumColumns(self, countDict):
        totals = [0.0 for i in range(self.maxRange)]
        for x in range(0,self.maxRange):
            for y in range(0,self.maxRange):
                totals[x] = countDict[(x,y)] + totals[x] 
        return totals
                
    def countNotes(self):
        countDict = dict([((x, y), 0) for x in range(self.maxRange) for y in range(self.maxRange)])
        start = 0
        while not(isinstance(self.data[start], music21.note.Note)):
            start = start + 1
        firstNote = self.data[start].pitch.pitchClass
        for n in range(start, len(self.data)):
            if isinstance(self.data[n], music21.note.Note):
                secondNote = self.data[n].pitch.pitchClass
                countDict[(firstNote, secondNote)] = countDict[(firstNote, secondNote)] + 1
                firstNote = self.data[n].pitch.pitchClass 
        return countDict
        
    def plotDistribution(self):
        plt.figure()
        plt.title(self.type)
        plt.imshow(self.distribution)
        plt.xticks(numpy.arange(0,12), ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'])
        plt.yticks(numpy.arange(0,12), ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'])
        plt.show()
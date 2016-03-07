# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from numpy import random
# define the length of the melody
mlength=12
# define the fitness function, takes a melody m and transition table p
def fitnessfunction(m,p):
    fitness = 1
    for x in range (1,mlength):
        fitness= fitness * p[m[x-1]][m[x]]
    return fitness
# create a random transition table  
prob = []    
for x in range (0,12):
    a=random.sample(12)
    a=a/sum(a)
    prob.append(a)
# instantiate some necessary variables    
bestscore = 0  
melody = random.randint(0,12,mlength)
bestmelody = list(melody)
progress = []
mutaterange=[0,1,2,3,4,5,6,7,8,9,10,11]
#each loop decreases the number of mutations per round
for i in range (0,5):
#each loop mutates the currentbest, checks it's fitness and updates currentbest   
    for x in range (0,1000):
        melody=list(bestmelody)      
        r=random.randint(0,mlength,abs(i-6))
        for z in r:
            mutaterangecopy=list(mutaterange)
            mutaterangecopy.remove(melody[z])
            melody[z]= random.choice(mutaterangecopy,1)[0]
        
        
        currentscore = fitnessfunction(melody,prob)
        if currentscore >= bestscore:
            bestscore = currentscore
            bestmelody = list(melody)
        
        progress.append(bestscore)
        
            
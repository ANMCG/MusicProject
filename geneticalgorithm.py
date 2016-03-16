
# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
from numpy import random
from fitnessFunction import computeFitnessPitchTransitions as fitness

# define the length of the melody
mlength=12
nrOfTones = 11

# instantiate some necessary variables    
bestscore = 0  
melody = random.randint(0,nrOfTones,mlength)
bestmelody = list(melody)
progress = []
mutaterange=range(nrOfTones)

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

        currentscore = fitness(melody)
        if currentscore >= bestscore:
            bestscore = currentscore
            bestmelody = list(melody)

        progress.append(bestscore)


def mutate(notelist, mlength=12):

   # instantiate some necessary variables
    bestscore = 0

    # the list we are working on comes from the midi files
    bestmelody = notelist

    progress = []
    mutaterange=range(nrOfTones)

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


            currentscore = fitness(melody)
            if currentscore >= bestscore:
                bestscore = currentscore
                bestmelody = list(melody)

            progress.append(bestscore)

    return bestmelody

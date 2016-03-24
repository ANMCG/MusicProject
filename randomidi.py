import os
from mido import MidiFile, MidiTrack, Message
import random

import geneticalgorithm as ga


def generate_random(snote=50, mlength=12, numofmidi=10, time=150, filename='random', pitchrnd=False):
    
    notes = range(snote, snote+mlength)
    
    noterange = range(mlength)

    # pitch range for random pitch value ;
    pitches = range(-8192,8191)
    
    # Create music folder if it does not exist
    if not os.path.exists('music'):
        os.makedirs('music')

    for j in range(numofmidi):
    
        mid = MidiFile(type=0) # type0 can have only one track
    
        track = MidiTrack() # note list (kind of)

        mid.tracks.append(track)
    
        # the note which the pitch will change for
        pitchnote = random.choice(noterange)
        numofpnote = random.choice(noterange)
    
        for i in noterange:
        
            note = random.choice(notes)
            pitch = random.choice(pitches)
        
            if pitchrnd:
                if i == pitchnote: # Change the pitch on the note
                    track.append(Message('pitchwheel', pitch=pitch))
                if i == (pitchnote+numofpnote): # Change the pitch back to default
                    track.append(Message('pitchwheel'))
        
            track.append(Message('note_on', note=note, time=time))
            track.append(Message('note_off', note=note, time=time))
            
        note = random.choice(notes)
        track.append(Message('note_on', note=note, time=time))
        track.append(Message('note_off', note=note, time=500))
        

        mid.save('music/' + filename + str(j) + '.mid')



def apply_mutation(mutantnotelist, midino, snote=50, time=150, filename='random'):

    mid = MidiFile(type=0) # type0 can have only one track
    
    track = MidiTrack() # note list (kind of)

    mid.tracks.append(track)
    
    # Create mutant music folder if it does not exist
    if not os.path.exists('mutantmusic'):
        os.makedirs('mutantmusic')
    
    # add the octaves back
    mutantnotelist2 = [x+snote for x in mutantnotelist]
    
    for note in mutantnotelist2[:10]:
        
        #print(note)
        
        track.append(Message('note_on', note=int(note), time=time))
        track.append(Message('note_off', note=int(note), time=time))
        
    track.append(Message('note_on', note=mutantnotelist2[11], time=time))
    track.append(Message('note_off', note=mutantnotelist2[11], time=500))
        
        
    mid.save('mutantmusic/' + filename + str(midino) + '.mid')



def read_midi(midiname, snote=50):
    
    mid = MidiFile(midiname)
    
    noteonlist = []
    for i, track in enumerate(mid.tracks):
        #print('Track {}: {}'.format(i, track.name))
        for message in track:
            #print(message)
            if message.type == 'note_on':
                noteonlist.append(message.note)
    
    # normalize the note integers for mutation by reducing octaves
    notelist = [x-snote for x in noteonlist]
    
    return notelist



if __name__ == "__main__":

    mlength = 11
    snote = 50 # starting note
    numofmidi = 10 # number of midi files
    time = 150
    filename='random'
    pitchrnd=False # do not include pitch variations for now

    generate_random(snote, mlength, numofmidi, time, filename, pitchrnd)

    for j in range(numofmidi):
    
        midiname = 'music/' + filename + str(j) + '.mid'
    
        notelist = read_midi(midiname)
    
        mutantnotelist = ga.mutate(notelist, mlength)
    
        apply_mutation(mutantnotelist, j, snote, time, filename)
        

    print('Midi files are created. Please check the "music" and “mutantmusic” folder')

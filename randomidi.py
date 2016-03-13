import os
import mido
from mido import MidiFile, MidiTrack, Message
import random

notes = range(50, 62)
times = range(50,300)

noterange = range(12)

# pitch range for random pitch value ;
pitches = range(-8192,8191)

for j in range(10):
    
    mid = MidiFile(type=0) # type0 can have only one track
    
    track = MidiTrack() # note list (kind of)

    mid.tracks.append(track)
    
    # the note which the pitch will change for
    pcnote = random.choice(noterange)
    
    for i in noterange:
        
        note = random.choice(notes)
        time = random.choice(times)
        pitch = random.choice(pitches)
        
        # Change the pitch for only one note
        if i == pcnote: # Change the pitch on third note
            track.append(Message('pitchwheel', pitch=pitch))
        if i == (pcnote+1): # Change the pitch back to default
            track.append(Message('pitchwheel'))
        
        track.append(Message('note_on', channel=0, note=note, time=time))
        track.append(Message('note_off', channel=0, note=note, time=time))
        

    if not os.path.exists('music'):
        os.makedirs('music')

    mid.save('music/random' + str(j) + '.mid')

print('Midi files are created. Please check the "music" folder')

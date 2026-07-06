"""
ChordFinder
By Alexandra Delarge, 2026

Logic.py

This file handles the main logic of the program, and is used by main.py.
"""

import chordlib


#dictionary to convert keys to numeric values for easier comprehension by the program
KEY_TO_NUM = {
    "C": 0,
    "C#": 1,
    "D": 2,
    "Eb": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "G": 7,
    "G#": 8,
    "A": 9,
    "Bb": 10,
    "B": 11
}

#list that can convert numeric values back to keys for user comprehension
NUM_TO_KEY = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "G#", "A", "Bb", "B"]

def sort_keys(keys):
    """
    Sorts a list of keys in ascending order. Since an octave has 12 half-notes, the octave of a key will add 12 per octave to the key's value. Returns a list of sorted keys.
    Used to sort the set of pressed keys in the console when the function toggle_white_key or toggle_black_key is triggered and verbosity is True
    """
    temporary_tuples = []
    for key in keys:
        #For unsharped keys
        if len(key) == 2:
            k = KEY_TO_NUM[key[0]]
            octave = int(key[1])
            val = k + ((octave-1) * 12)
            temporary_tuples.append((val, key))
        #For sharped keys
        elif len(key) == 3:
            k = KEY_TO_NUM[key[0:2]]
            octave = int(key[2])
            val = k + ((octave-1) * 12)
            temporary_tuples.append((val, key))


    temporary_tuples.sort(key=lambda x: x[0])

    sorted_keys = [t[1] for t in temporary_tuples]

    return sorted_keys

def sort_unique_keys(keys):
    """
    Sorts a list of unique keys in ascending order.
    Used by the toggle_white_key and toggle_black_key functions when triggered to get the text to be displayed by the "Pressed Keys" panel in the window.
    """
    temporary_tuples = []
    for key in keys:
        #For unsharped keys
        if len(key) == 2:
            k = KEY_TO_NUM[key[0]]
            temporary_tuples.append((k, key[0]))
        #For sharped keys
        elif len(key) == 3:
            k = KEY_TO_NUM[key[0:2]]
            temporary_tuples.append((k, key[0:2]))


    temporary_tuples.sort(key=lambda x: x[0])

    sorted_keys = [t[1] for t in temporary_tuples]
    sorted_keys = list(dict.fromkeys(sorted_keys))  # Remove duplicates while preserving order
    return sorted_keys


# Function to check if a list of 3 keys is a chord, and if so, return the chord name. If not, return "N.C." (no chord)
def three_note_chord(keys):
    converted = []
    for key in keys:
        converted.append(KEY_TO_NUM[key])

    # chooses the root note to be the first note in the set
    root_note = converted[0]
    for i in range(len(keys)):
        # now that the program remembers the root note, it shifts down every number in the converted list for easier comprehension
        converted[i] -= root_note
    
    for _ in range(3):
        # if the tuple is in the library of known chords, return the root note and the found chord
        if tuple(converted) in chordlib.three_note_chords:
            root = NUM_TO_KEY[root_note]
            return f"{root}{chordlib.three_note_chords[tuple(converted)]}"
        else:
            # shifts the root note to be the next note in the set and moves the other notes around in order to try matching the tuple with the dictionary again
            root_note += converted[1]
            root_note = root_note % 12
            shifted = [(x - converted[1]) % 12 for x in converted]
            shifted.sort()
            converted = shifted


    return "N.C."
    

# Function to check if a list of 4 keys is a chord, and if so, return the chord name. If not, return "N.C." (no chord)
def four_note_chord(keys):
    
    converted = []
    for key in keys:
        converted.append(KEY_TO_NUM[key])

    # chooses the root note to be the first note in the set
    root_note = converted[0]
    for i in range(len(keys)):
        # now that the program remembers the root note, it shifts down every number in the converted list for easier comprehension
        converted[i] -= root_note
    
    for _ in range(4):
        # if the tuple is in the library of known chords, return the root note and the found chord
        if tuple(converted) in chordlib.four_note_chords:
            root = NUM_TO_KEY[root_note]
            return f"{root}{chordlib.four_note_chords[tuple(converted)]}"
        else:
            # shifts the root note to be the next note in the set and moves the other notes around in order to try matching the tuple with the dictionary again
            root_note += converted[1]
            root_note = root_note % 12
            shifted = [(x - converted[1]) % 12 for x in converted]
            #0 4 7 10 -> -4 0 3 6 -> 8 0 3 6
            shifted.sort()
            converted = shifted


    return "N.C."



def handle_chord(unique_keys):
    """
    This function takes a list of unique keys and determines:
    a) the length of the unique keys list
        - if the length is not 3 or 4 it will return "N.C." (no chord)
        - if the length is 3, it will check against the 3 note dictionary to find the chord name
        - if the length is 4, it will check against the 4 note dictionary to find the chord name
    b) If the chord is found, it will return the chord name. If not, it will return "N.C." (no chord)
    """
    if len(unique_keys) == 3:
        return three_note_chord(unique_keys)
    elif len(unique_keys) == 4:
        return four_note_chord(unique_keys)
    else:
        return "N.C."
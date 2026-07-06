"""
ChordFinder
By Alexandra Delarge, 2026

Chordlib.py

This file contains the chord library, which is used by logic.py.

"""



three_note_chords = {
    (0, 4, 7): "",
    (0, 3, 7): "-",
    (0, 5, 7): "sus4",
    (0, 2, 7): "sus2",
    (0, 3, 6): "dim",
    (0, 4, 8): "aug"
}

four_note_chords = {
    (0, 4, 7, 10): "7",
    (0, 4, 7, 11): "maj",
    (0, 3, 7, 10): "-7"
}
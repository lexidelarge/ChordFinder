"""
ChordFinder
By Alexandra Delarge, 2026

Main.py

This file handles the GUI end of the program, and uses other files to handle the logic of the program.


"""

# minutes_wasted = 420

import tkinter as tk
from tkinter import ttk
import logic


main = tk.Tk()
main.title("ChordFinder")
main.config(bg="#E4E2E2")
main.geometry("1352x700")
main.update_idletasks()


geometryX = 250
geometryY = 200

main.geometry("+%d+%d"%(geometryX, geometryY))
main.resizable(False, False)

style = ttk.Style(main)
style.theme_use("clam")


pressed_keys = []

def toggle_white_key(button, note, pressed_keys=pressed_keys, verbosity = True):
    """
    function that handles the pressing and unpressing of white keys
    """

    # if the note is already in pressed_keys, remove it and change the button style to unpressed.
    if note in pressed_keys:
        pressed_keys.remove(note)
        button.configure(style="whitekey.TButton")
        
        pressed_unique = logic.sort_unique_keys(pressed_keys)
        pressed_var.set(", ".join(pressed_unique))

        chord = logic.handle_chord(pressed_unique)
        chord_var.set(chord)

        if verbosity:
            pressed_keys = logic.sort_keys(pressed_keys)
            print(f"Unpressed {note}. Current pressed keys: {pressed_keys}")

    # if the note is already in pressed_keys, remove it and change the button style to unpressed.
    else:
        pressed_keys.append(note)
        button.configure(style="whitekeyPressed.TButton")
        
        pressed_unique = logic.sort_unique_keys(pressed_keys)
        pressed_var.set(", ".join(pressed_unique))
        
        chord = logic.handle_chord(pressed_unique)
        chord_var.set(chord)

        if verbosity:
            pressed_keys = logic.sort_keys(pressed_keys)
            print(f"Pressed {note}. Current pressed keys: {pressed_keys}")



def toggle_black_key(button, note, pressed_keys=pressed_keys, verbosity = True):
    """
    function that handles the pressing and unpressing of black keys
    """

    # if the note is already in pressed_keys, remove it and change the button style to unpressed.
    if note in pressed_keys:

        pressed_keys.remove(note)
        button.configure(style="blackkey.TButton")

        #sort the pressed keys and use every key only once into pressed_unique
        pressed_unique = logic.sort_unique_keys(pressed_keys)
        pressed_var.set(", ".join(pressed_unique))

        #use the pressed_unique variable to try to find the chord
        chord = logic.handle_chord(pressed_unique)
        chord_var.set(chord)


        if verbosity:
            pressed_keys = logic.sort_keys(pressed_keys)
            print(f"Unpressed {note}. Current pressed keys: {pressed_keys}")

    # if the note is not in pressed_keys, add it and change the button style to pressed.
    else:
        pressed_keys.append(note)
        button.configure(style="blackkeyPressed.TButton")
        

        pressed_unique = logic.sort_unique_keys(pressed_keys)
        pressed_var.set(", ".join(pressed_unique))

        chord = logic.handle_chord(pressed_unique)
        chord_var.set(chord)

        if verbosity:
            pressed_keys = logic.sort_keys(pressed_keys)
            print(f"Pressed {note}. Current pressed keys: {pressed_keys}")

"""
TITLE CONFIG
"""

style.configure("title.TLabel", background="#E4E2E2", foreground="#000", font=("Arial", 28), anchor="center")
title = ttk.Label(master=main, text="ChordFinder", style="title.TLabel")
title.configure(anchor="center")
title.place(x=614, y=30, width=250, height=51)

"""
KEYBOARD CONFIG
"""
# Create styles for white & black keys and the pressed variants

style.configure("whitekey.TButton", background="#ffffff", foreground="#000")
style.map("whitekey.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

style.configure("whitekeyPressed.TButton", background="#cccccc", foreground="#000")
style.map("whitekeyPressed.TButton", background=[("active", "#bbbbbb")], foreground=[("active", "#000")])

style.configure("blackkey.TButton", background="#000000", foreground="#ffffff")
style.map("blackkey.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

style.configure("blackkeyPressed.TButton", background="#4d4d4d", foreground="#ffffff")
style.map("blackkeyPressed.TButton", background=[("active", "#5a5a5a")], foreground=[("active", "#fff")])

# The following ~120 lines of code just create the buttons for the keys on the GUI and position them in the window correctly.
# White Keys

c1 = ttk.Button(master=main, text="C", style="whitekey.TButton", command=lambda: toggle_white_key(c1, "C1"))
c1.place(x=38, y=178, width=58, height=256)

d1 = ttk.Button(master=main, text="D", style="whitekey.TButton", command=lambda: toggle_white_key(d1, "D1"))
d1.place(x=96, y=178, width=58, height=256)

e1 = ttk.Button(master=main, text="E", style="whitekey.TButton", command=lambda: toggle_white_key(e1, "E1"))
e1.place(x=154, y=178, width=58, height=256)

f1 = ttk.Button(master=main, text="F", style="whitekey.TButton", command=lambda: toggle_white_key(f1, "F1"))
f1.place(x=212, y=178, width=58, height=256)

g1 = ttk.Button(master=main, text="G", style="whitekey.TButton", command=lambda: toggle_white_key(g1, "G1"))
g1.place(x=270, y=178, width=58, height=256)


a1 = ttk.Button(master=main, text="A", style="whitekey.TButton", command=lambda: toggle_white_key(a1, "A1"))
a1.place(x=328, y=178, width=58, height=256)

b1 = ttk.Button(master=main, text="B", style="whitekey.TButton", command=lambda: toggle_white_key(b1, "B1"))
b1.place(x=386, y=178, width=58, height=256)

c2 = ttk.Button(master=main, text="C", style="whitekey.TButton", command=lambda: toggle_white_key(c2, "C2"))
c2.place(x=444, y=178, width=58, height=256)

d2 = ttk.Button(master=main, text="D", style="whitekey.TButton", command=lambda: toggle_white_key(d2, "D2"))
d2.place(x=502, y=178, width=58, height=256)

e2 = ttk.Button(master=main, text="E", style="whitekey.TButton", command=lambda: toggle_white_key(e2, "E2"))
e2.place(x=560, y=178, width=58, height=256)

f2 = ttk.Button(master=main, text="F", style="whitekey.TButton", command=lambda: toggle_white_key(f2, "F2"))
f2.place(x=618, y=178, width=58, height=256)

g2 = ttk.Button(master=main, text="G", style="whitekey.TButton", command=lambda: toggle_white_key(g2, "G2"))
g2.place(x=676, y=178, width=58, height=256)

a2 = ttk.Button(master=main, text="A", style="whitekey.TButton", command=lambda: toggle_white_key(a2, "A2"))
a2.place(x=734, y=178, width=58, height=256)

b2 = ttk.Button(master=main, text="B", style="whitekey.TButton", command=lambda: toggle_white_key(b2, "B2"))
b2.place(x=792, y=178, width=58, height=256)

c3 = ttk.Button(master=main, text="C", style="whitekey.TButton", command=lambda: toggle_white_key(c3, "C3"))
c3.place(x=850, y=178, width=58, height=256)

d3 = ttk.Button(master=main, text="D", style="whitekey.TButton", command=lambda: toggle_white_key(d3, "D3"))
d3.place(x=908, y=178, width=58, height=256)

e3 = ttk.Button(master=main, text="E", style="whitekey.TButton", command=lambda: toggle_white_key(e3, "E3"))
e3.place(x=966, y=178, width=58, height=256)

f3 = ttk.Button(master=main, text="F", style="whitekey.TButton", command=lambda: toggle_white_key(f3, "F3"))
f3.place(x=1024, y=178, width=58, height=256)

g3 = ttk.Button(master=main, text="G", style="whitekey.TButton", command=lambda: toggle_white_key(g3, "G3"))
g3.place(x=1082, y=178, width=58, height=256)

a3 = ttk.Button(master=main, text="A", style="whitekey.TButton", command=lambda: toggle_white_key(a3, "A3"))
a3.place(x=1140, y=178, width=58, height=256)

b3 = ttk.Button(master=main, text="B", style="whitekey.TButton", command=lambda: toggle_white_key(b3, "B3"))
b3.place(x=1198, y=178, width=58, height=256)

c4 = ttk.Button(master=main, text="C", style="whitekey.TButton", command=lambda: toggle_white_key(c4, "C4"))
c4.place(x=1256, y=178, width=58, height=256)

# Black Keys

cs1 = ttk.Button(master=main, text="C#", style="blackkey.TButton", command=lambda: toggle_black_key(cs1, "C#1"))
cs1.place(x=81, y=178, width=30, height=168)

eb1 = ttk.Button(master=main, text="Eb", style="blackkey.TButton", command=lambda: toggle_black_key(eb1, "Eb1"))
eb1.place(x=139, y=178, width=30, height=168)

fs1 = ttk.Button(master=main, text="F#", style="blackkey.TButton", command=lambda: toggle_black_key(fs1, "F#1"))
fs1.place(x=255, y=178, width=30, height=168)

gs1 = ttk.Button(master=main, text="G#", style="blackkey.TButton", command=lambda: toggle_black_key(gs1, "G#1"))
gs1.place(x=313, y=178, width=30, height=168)

bb1 = ttk.Button(master=main, text="Bb", style="blackkey.TButton", command=lambda: toggle_black_key(bb1, "Bb1"))
bb1.place(x=371, y=178, width=30, height=168)

cs2 = ttk.Button(master=main, text="C#", style="blackkey.TButton", command=lambda: toggle_black_key(cs2, "C#2"))
cs2.place(x=487, y=178, width=30, height=168)

eb2 = ttk.Button(master=main, text="Eb", style="blackkey.TButton", command=lambda: toggle_black_key(eb2, "Eb2"))
eb2.place(x=545, y=178, width=30, height=168)

fs2 = ttk.Button(master=main, text="F#", style="blackkey.TButton", command=lambda: toggle_black_key(fs2, "F#2"))
fs2.place(x=661, y=178, width=30, height=168)

gs2 = ttk.Button(master=main, text="G#", style="blackkey.TButton", command=lambda: toggle_black_key(gs2, "G#2"))
gs2.place(x=719, y=178, width=30, height=168)

bb2 = ttk.Button(master=main, text="Bb", style="blackkey.TButton", command=lambda: toggle_black_key(bb2, "Bb2"))
bb2.place(x=777, y=178, width=30, height=168)

cs3 = ttk.Button(master=main, text="C#", style="blackkey.TButton", command=lambda: toggle_black_key(cs3, "C#3"))
cs3.place(x=893, y=178, width=30, height=168)

eb3 = ttk.Button(master=main, text="Eb", style="blackkey.TButton", command=lambda: toggle_black_key(eb3, "Eb3"))
eb3.place(x=951, y=178, width=30, height=168)

fs3 = ttk.Button(master=main, text="F#", style="blackkey.TButton", command=lambda: toggle_black_key(fs3, "F#3"))
fs3.place(x=1067, y=178, width=30, height=168)

gs3 = ttk.Button(master=main, text="G#", style="blackkey.TButton", command=lambda: toggle_black_key(gs3, "G#3"))
gs3.place(x=1125, y=178, width=30, height=168)

bb3 = ttk.Button(master=main, text="Bb", style="blackkey.TButton", command=lambda: toggle_black_key(bb3, "Bb3"))
bb3.place(x=1183, y=178, width=30, height=168)



"""
OTHER CONFIG
"""

style.configure("pressed_keys.TLabel", background="#E4E2E2", foreground="#000", font=("Arial", 18), anchor="center")
pressed_list = ttk.Label(master=main, text="Pressed Keys:", style="pressed_keys.TLabel")
pressed_list.configure(anchor="center")
pressed_list.place(x=57, y=466, width=175, height=50)

pressed_var = tk.StringVar(value="")
pressed = tk.Label(master=main, textvariable=pressed_var, bg="#fff", fg="#000", anchor="w", font=("Arial", 18))
pressed.place(x=248, y=468, width=425, height=50)

chord_var = tk.StringVar(value="N.C.")
chord = tk.Label(master=main, textvariable=chord_var, bg="#fff", fg="#000", anchor="w", font=("Arial", 18))
chord.place(x=248, y=566, width=250, height=50)

style.configure("foundchord.TLabel", background="#E4E2E2", foreground="#000", font=("Arial", 18), anchor="center")
foundchord = ttk.Label(master=main, text="Chord:", style="foundchord.TLabel")
foundchord.configure(anchor="center")
foundchord.place(x=51, y=564, width=185, height=50)





style.configure("reset.TButton", background="#E4E2E2", foreground="#000", font=("Arial", 25))
style.map("reset.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])


def reset_button(pressed_keys=pressed_keys):
    """
    This function clears the pressed keys list and resets the button styles to their unpressed state. It is called when the user presses the reset button.
    """
    for key in list(pressed_keys):
        # For unsharped keys
        if len(key) == 2:
            toggle_white_key(eval(key[0].lower() + key[1]), key, pressed_keys, verbosity=False)
        # For sharped keys
        elif len(key) == 3:
            if key[1] == "#":
                key = f"{key[0]}s{key[2]}"
            toggle_black_key(eval(key[0:2].lower() + key[2]), key, pressed_keys, verbosity=False)
    print("Reset button pressed.")

reset = ttk.Button(master=main, text="Reset", style="reset.TButton", command=lambda: reset_button(pressed_keys))
reset.place(x=899, y=480, width=350, height=120)


main.mainloop()
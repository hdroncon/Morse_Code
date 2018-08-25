# -*- coding: utf-8 -*-
"""
Morse Code
"""

import winsound
import time

# Alphabet
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
      	 'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   ' ': ' ',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

CODEchecktemp = list(CODE.keys())
CODEcheck = "".join(str(x) for x in CODEchecktemp)
# Translation from English to Morse and checking if message is valid
while True:
    Message = input("Insert your message (use letters and numbers only): ")
    if all(char in CODEcheck for char in Message.upper()):
        break
    print("Do not use special characters. Please, try again.")

Translated = []
for charact in Message.upper():
    Translated.append((CODE.get(charact)))
        
MorseCode = " ".join(str(x) for x in Translated)

# Setting the MorseCode machine up and playing message
fdot = 550  # Frequency for dots
ddot = 100  # Duration for dots (1000 ms == 1 second)
fdah = 550  # Frequency for dahs
ddah = 250  # Duration for dahs (1000 ms == 1 second)

for charact in MorseCode:
     if charact == ".":
         dot = winsound.Beep(fdot, ddot)
     elif charact == "-":
         dah = winsound.Beep(fdah, ddah)
     elif charact == " ":
         time.sleep(0.3)




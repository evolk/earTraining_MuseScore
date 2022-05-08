from xml.etree import cElementTree as ET
# from collections import defaultdict
import random
# import numpy as np
# import string
import time

def create_note_range():
    full_range = []
    octaves = list(range(2,5))
    notes = ["C", "D", "E", "F", "G", "A", "B"]
    
    for o in octaves:
        for n in notes:
            full_range.append((n,o))
    return full_range
    
full_range = create_note_range()

def update_file(xml_file):

    with open(xml_file, 'r') as file:
        data = file.read()

    root = ET.fromstring(data)

    for elem in root.iter():

        if (elem.tag=='pitch'):
            random_note = random.choice(full_range)
            
            for i in list(elem):
                if i.tag == "step":
                    i.text = random_note[0]
                if i.tag == "octave":
                    i.text = str(random_note[1])
                    
    return ET.ElementTree(root)

def create_musicxml_file():
    new_game = update_file("./score_templates/Ear_Training_Game.musicxml")

    t = time.localtime()
    current_time = time.strftime("%H_%M_%S", t)
    filename = "new_game_"+str(current_time)+".musicxml"
    new_game.write(filename)


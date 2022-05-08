from xml.etree import cElementTree as ET
from datetime import date
import random
import time

#create a range of notes to use in the game
#C2 to B4
def create_note_range():
    full_range = []
    octaves = list(range(2,5))
    notes = ["C", "D", "E", "F", "G", "A", "B"]
    
    for o in octaves:
        for n in notes:
            full_range.append((n,o))
    return full_range
    
full_range = create_note_range()

#The game template file has 30 D3 notes
#This function takes each D3 and changes it to a different pitch
#within the predefined range, drawing notes at random
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

#create a new game file with "new_game"
def create_musicxml_file(game_template):
    new_game = update_file(game_template)
    
    today = date.today()
    t = time.localtime()
    current_time = time.strftime("%H_%M_%S", t)
    
    filename = "new_game_"+str(today)+"_"+str(current_time)+".musicxml"
    new_game.write("./generated_games/"+filename)

if __name__ == "__main__":
    create_musicxml_file("Ear_Training_Game.musicxml")
# from xml.etree import cElementTree as ET
# from collections import defaultdict
# import random
# import numpy as np
# import string


def create_note_range():
    full_range = []
    octaves = list(range(2,6))
    notes = ["C", "D", "E", "F", "G", "A", "B"]
    
    for o in octaves:
        for n in notes:
            full_range.append((n,o))

    full_range.append(("C", 6))
    return full_range
    

print (create_note_range())

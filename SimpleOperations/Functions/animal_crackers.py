#Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    b = text.lower().split()
    return b[0][0] == b[1][0]
       
animal_crackers("LevelHeaded Cama")

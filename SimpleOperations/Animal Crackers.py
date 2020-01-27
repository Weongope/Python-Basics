def animal_crackers(text):
    b = text.split(" ")
    return b[0][0].lower() == b[1][0].lower()
       
animal_crackers("LevelHeaded Cama")
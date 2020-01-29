def old_macdonald(name):
	first_letter = name[0]
	between = name[1:3]
	forth_letter = name[3]
	rest = name[3:]
	
	return first_letter.upper() + between + forth_letter.upper() + rest
	
print(old_macdonald("macdonald"))


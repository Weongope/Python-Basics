def old_macdonald(name):
	first_part = name[:3]
	second_part = name[3:]

	return first_part.capitalize() + second_part.capitalize()
	
print(old_macdonald("macdonald"))


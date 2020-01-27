def old_macdonald(name):
	input_index=0
	mac_name = ""
	for letters in name.capitalize():
		if input_index == 3:
			mac_name += letters.upper()
		else:
			mac_name += letters
		input_index += 1
	return mac_name



print( old_macdonald("macdonald"))
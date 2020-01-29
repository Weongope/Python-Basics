def paper_doll(text):
	result = ""
	
	for char in text:
		result += char*3
	
	return result
	
print(paper_doll("FarOverTheMistyMountains"))

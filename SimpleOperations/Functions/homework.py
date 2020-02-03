def ran_bool(num, low, high):
	return num < low or num > high
	
	
def up_low(s):
	lower_c = 0
	upper_c = 0
	for letter in s:
		if letter.islower():
			lower_c += 1
		elif letter.isupper():
			upper_c += 1
		else:
			
		
	print(f"No. of Lower case characters : {lower_c}")
	print(f"No. of Lower case characters : {upper_c}")

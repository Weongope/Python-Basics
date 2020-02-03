def up_low(s):
	lower_c = 0
	upper_c = 0
	for letter in s:
		if letter.islower():
			lower_c += 1
		elif letter.isupper():
			upper_c += 1


	print(f"No. of Lower case characters : {lower_c}")
	print(f"No. of Upper case characters : {upper_c}")

up_low("Hi there")

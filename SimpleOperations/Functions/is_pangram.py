import string

def ispanagram(str1, alphabet = string.ascii_lowercase):
	lst_check = list(alphabet)
	for letter in str1.lower():
		if letter in lst_check:
			index = lst_check.index(letter)
			lst_check.pop(index)
	return not lst_check

print(ispanagram("The quick brown fox jumps over the lazy dog"))
